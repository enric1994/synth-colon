#!/usr/bin/env python3

import bpy
from bpy_extras.object_utils import world_to_camera_view
import os
import random
import sys
from mathutils import Euler
# import imageio
# from imgaug import augmenters as iaa
from dtd_utils import get_random_texture
import shutil
import math

def save_project(path):
	bpy.ops.wm.save_as_mainfile(filepath=path)

# Imports a 3D model with textures, join parts and assigns a name
def import_object(path, name):
	bpy.ops.import_scene.obj(filepath=path)
   
	sel_objs = [ o for o in bpy.context.scene.objects if o.select ]
	if sel_objs:
		obj1 = sel_objs.pop()
		obj1.select = True
		bpy.context.scene.objects.active = obj1
	while len(sel_objs) >= 1:
		obj2 = sel_objs.pop()
		obj2.select = True
		bpy.ops.object.join()
	for obj in bpy.context.selected_objects:
		obj.name = name

def mute():
	# Redirect output to log file
	logfile = '/tmp/blender_render.log'
	open(logfile, 'a').close()
	desc = os.dup(1)
	sys.stdout.flush()
	os.close(1)
	os.open(logfile, os.O_WRONLY)
	return desc

def unmute(desc):
	# Disable output redirection
	os.close(1)
	os.dup(desc)
	os.close(desc)

def set_camera(camera_info, total_frames):
	camera = bpy.data.objects['Camera']

	# Set location
	camera.location = camera_info['position']

	# Set render resolution
	bpy.data.scenes["Scene"].render.resolution_percentage=100
	bpy.data.scenes["Scene"].render.resolution_x = camera_info['render_size_x']
	bpy.data.scenes["Scene"].render.resolution_y = camera_info['render_size_y']
	bpy.data.scenes['Scene'].render.image_settings.color_mode='RGB'
	if 'blur_samples' in camera_info:
		bpy.data.scenes['Scene'].render.use_motion_blur = True
		bpy.data.scenes['Scene'].render.motion_blur_samples = camera_info['blur_samples']
	if 'blur_shutter' in camera_info:
		bpy.data.scenes['Scene'].render.use_motion_blur = True
		bpy.data.scenes['Scene'].render.motion_blur_shutter = camera_info['blur_shutter']

	# Motion
	if 'motion' in camera_info:
		motion_config = camera_info['motion']

		# Read motion frames
		frames = [int(x) for x in motion_config.keys()]

		# Assign default velocity and acceleration
		position = camera.location
		rotation = camera.rotation_euler
		velocity = (0,0,0)
		acceleration = (0,0,0)
		rotation_velocity = (0,0,0)
		rotation_acceleration = (0,0,0)

		for frame in range(0,total_frames):

			# Read new motion
			
			if frame in frames:
				frame_str = str(frame)
				velocity = motion_config[frame_str]['velocity']
				acceleration = motion_config[frame_str]['acceleration']
				rotation_velocity = motion_config[frame_str]['rotation_velocity']
				rotation_acceleration = motion_config[frame_str]['rotation_acceleration']

			# Update 3D object position
			position = tuple(sum(x) for x in zip(position, velocity))

			# Update 3D object rotation
			rotation = tuple(sum(x) for x in zip(rotation, rotation_velocity))

			# Update translation and rotation velocity
			velocity = tuple(sum(x) for x in zip(velocity, acceleration))
			rotation_velocity = tuple(sum(x) for x in zip(rotation_velocity, rotation_acceleration))

			# Set position
			camera.location = position
			# Set rotation
			camera.rotation_euler = Euler(rotation,'XYZ')

			# Set keyframe
			camera.keyframe_insert(data_path='location',index = -1, frame=frame)
			camera.keyframe_insert(data_path='rotation_euler',index = -1, frame=frame)


def set_background(background_info):

	background = bpy.data.objects['Background']

	if 'hide' in background_info:
		if background_info['hide']:
			background.hide = True
			background.hide_render = True	
			return

	
	

	# Set background position
	background.location = background_info['position']

	# Set background ambient color
	bpy.data.worlds['World'].horizon_color=background_info['ambient_color']

	# Set background content
	if 'path' in background_info:
		bpy.data.images['background.mp4'].filepath = background_info['path']

	# Set background size
	bpy.data.objects['Background'].scale[0] = background_info['size_x']
	bpy.data.objects['Background'].scale[1] = background_info['size_y']
	
def set_lighting(lighting_info):
	for light_name, light_data in lighting_info.items():
		bpy.ops.object.lamp_add(type=light_data['light_type'], location=light_data['position'], rotation=light_data['rotation'])
		lamp = bpy.context.active_object.data
		lamp.energy = light_data['energy']
		if 'color' in light_data:
			lamp.color = light_data['color']
		if 'negative_light' in light_data:
			lamp.use_negative = light_data['negative_light']
		if light_data['shadow']:
			lamp.shadow_method = 'RAY_SHADOW'
		if 'specular' in light_data:
			lamp.use_specular = light_data['specular']
		bpy.context.selected_objects[0].name = light_name

def set_occlusion(occlusion_info):
	for ocl_name, ocl_data in occlusion_info.items():
		if ocl_data['type'] == 'cube':
			bpy.ops.mesh.primitive_cube_add(location=ocl_data['position'],rotation = ocl_data['rotation'], radius=ocl_data['size'])
		if ocl_data['type'] == 'sphere':
			bpy.ops.mesh.primitive_ico_sphere_add(location=ocl_data['position'], rotation = ocl_data['rotation'], size=ocl_data['size'])
		# Assign color
		bpy.context.selected_objects[0].name = ocl_name
		mat = bpy.data.materials.new(name=str(ocl_name) + '_mat')
		mat.diffuse_color = (ocl_data['color'][0], ocl_data['color'][1], ocl_data['color'][2])
		activeObject = bpy.context.active_object
		activeObject.data.materials.append(mat)

def translate_vertices(obj_name, num, dist):
	obj = bpy.data.objects[obj_name]
	mesh = obj.data
	total_vertices = len(mesh.vertices)
	for _ in range(0,num):
		random_vert = random.randint(0, total_vertices -1)
		random_trans_x = random.uniform(-dist, dist)
		random_trans_y = random.uniform(-dist, dist)
		random_trans_z = random.uniform(-dist, dist)
		
		vert = mesh.vertices[random_vert]
		mat_world = obj.matrix_world

		pos_world = mat_world * vert.co
		
		pos_world.x += random_trans_x
		pos_world.y += random_trans_y
		pos_world.z += random_trans_z
		
		vert.co=mat_world.inverted() * pos_world

def set_objects(objects_info, render_size_x, render_size_y, total_frames):

	all_vertexs = []
	rnd = lambda i: round(i)
	rnd3 = lambda i: round(i, 3)

	previous_object_path = ''
	previous_object_name = ''

	tex_count = 0
	previous_object_no_trans = False

	# scn = bpy.context.scene

	for object_name, object_data in objects_info.items():

		# Duplicate identic objects to save time
		if object_data['path'] == previous_object_path and previous_object_no_trans:
			bpy.data.objects[previous_object_name].select = True
			bpy.ops.object.duplicate()
			bpy.ops.object.make_single_user(material=True, texture=True)
			new_object = bpy.data.objects[previous_object_name + '.001']
			new_object.name = object_name

		else:
			# Import, join parts and assign name
			import_object('/datasets/' + object_data['path'], object_name)

		previous_object_path = object_data['path']
		previous_object_name = object_name

		object3d = bpy.data.objects[object_name]

		# Clear previous modifiers
		for m in object3d.modifiers:
			object3d.modifiers.remove(m)

		if 'transforms' in objects_info[object_name]:
			previous_object_no_trans = False
			for transform in objects_info[object_name]['transforms']:
				if transform['type'] == 'CAST':
					bpy.ops.object.modifier_add(type=transform['type'])
					object3d.modifiers["Cast"].factor = transform['factor']
					object3d.modifiers["Cast"].cast_type = transform['cast_type']
				if transform['type'] == 'SCREW':
					bpy.ops.object.modifier_add(type=transform['type'])
					object3d.modifiers["Screw"].angle = transform['angle']
					object3d.modifiers["Screw"].screw_offset = transform['screw_offset']
				if transform['type'] == 'SOLIDIFY':
					bpy.ops.object.modifier_add(type=transform['type'])
					object3d.modifiers["Solidify"].thickness = transform['thickness']
				if transform['type'] == 'SIMPLE_DEFORM':
					bpy.ops.object.modifier_add(type=transform['type'])
					object3d.modifiers["SimpleDeform"].angle = transform['angle']
				if transform['type'] == 'RANDOMIZE':
					bpy.ops.object.mode_set(mode='EDIT')
					bpy.ops.transform.vertex_random(offset=transform['amount'])
					bpy.ops.object.mode_set(mode='OBJECT')
				if transform['type'] == 'TRANS_VERT':
					translate_vertices(object_name, transform['num'], transform['dist'] )
		else:
			previous_object_no_trans = True
		# Read initial pose info
		position = objects_info[object_name]['initial_position']
		rotation = objects_info[object_name]['initial_rotation']
		scale = objects_info[object_name]['scale']

		# Set initial location
		object3d.location = position

		# Set intitial rotation
		object3d.rotation_euler = Euler(rotation,'XYZ')

		# Set initial scale
		object3d.scale = scale

		# Motion
		if 'motion' in objects_info[object_name]:
			motion_config = objects_info[object_name]['motion']

			# Read motion frames
			frames = [int(x) for x in objects_info[object_name]['motion'].keys()]

			# Assign default velocity and acceleration
			velocity = (0,0,0)
			acceleration = (0,0,0)
			rotation_velocity = (0,0,0)
			rotation_acceleration = (0,0,0)

			for frame in range(0,total_frames):

				# Read new motion
				
				if frame in frames:
					frame_str = str(frame)
					velocity = motion_config[frame_str]['velocity']
					acceleration = motion_config[frame_str]['acceleration']
					rotation_velocity = motion_config[frame_str]['rotation_velocity']
					rotation_acceleration = motion_config[frame_str]['rotation_acceleration']

				# Update 3D object position
				position = tuple(sum(x) for x in zip(position, velocity))

				# Update 3D object rotation
				rotation = tuple(sum(x) for x in zip(rotation, rotation_velocity))

				# Update translation and rotation velocity
				velocity = tuple(sum(x) for x in zip(velocity, acceleration))
				rotation_velocity = tuple(sum(x) for x in zip(rotation_velocity, rotation_acceleration))

				# Set position
				object3d.location = position
				# Set rotation
				object3d.rotation_euler = Euler(rotation,'XYZ')

				# Set keyframe
				object3d.keyframe_insert(data_path='location',index = -1, frame=frame)
				object3d.keyframe_insert(data_path='rotation_euler',index = -1, frame=frame)


		if 'textures' in objects_info[object_name]:
			for material in bpy.data.objects[object_name].data.materials:
				for tex in material.texture_slots:
					if tex:
						bpy.data.images.new(str(tex_count), 0, 0)
						texture=tex.texture
						texture.image=bpy.data.images[str(tex_count)]
						bpy.data.images[str(tex_count)].source = 'FILE'
						texture.image.filepath='/datasets/' + objects_info[object_name]['textures'][material.name.split('.')[0]]
						tex_count += 1
		
		vertexs = []
		if '2d_vertex' in object_data:
			
			for vertex in object_data['2d_vertex']:
				scene = bpy.context.scene
				render = scene.render
				res_x = render_size_x
				res_y = render_size_y
				cam = bpy.data.objects['Camera']
				index = vertex
				scene.update()
				coords_2d = world_to_camera_view(scene, cam, object3d.matrix_world * object3d.data.vertices[index].co)
				
				x, y, d = coords_2d
			
				vertexs.append([rnd(res_x*x), res_y - rnd(res_y*y), rnd3(d)])
			all_vertexs.append(vertexs)
	return all_vertexs

def render_keyframes(output_folder, image_id, dataset_name):
	os.makedirs('/synth-polyp/synth/data/out/{}/{}'.format(dataset_name, output_folder), exist_ok=True)
	image_paths = []
	# for i in range(0,total_frames):
	bpy.context.scene.frame_current = 0
	bpy.context.scene.render.image_settings.file_format = 'PNG'
	bpy.context.scene.render.filepath = '/synth-polyp/synth/data/out/{}/{}/{}.png'.format(dataset_name, output_folder, str(image_id).zfill(8))
	bpy.ops.render.render(write_still=True)

	image_paths.append('{}/{}.png'.format(output_folder, str(image_id).zfill(8)))

def hide_masked_objects(objects_info):
	for object_name, object_data in objects_info.items():
		if 'mask' in object_data:
			if object_data['mask']:
				bpy.data.objects[object_name].hide_render=True

def remove_lighting(lighting_info):
	for light_name in lighting_info.keys():
		bpy.data.objects[light_name].hide_render=True

def hide_background():
	
	# Hide screen
	bpy.data.materials['background'].use_shadeless = False
	
	# Set background color to black
	bpy.data.worlds['World'].horizon_color=(0,0,0)

def set_masks(objects_info):
	for object_name, object_data in objects_info.items():
		if 'mask' in object_data:
			if object_data['mask']:

				# Stop hidding mask object
				bpy.data.objects[object_name].hide_render=False

				for slot in bpy.data.objects[object_name].material_slots:
					new_mat = bpy.data.materials.new(name="Mask")
					new_mat.diffuse_color = (1,1,1)
					slot.material = new_mat
					slot.material.use_shadeless=True
			
			# Hide other objects
			else:
				bpy.data.objects[object_name].hide_render=True

def set_flow():
	bpy.data.scenes['Scene'].render.layers['RenderLayer'].use_pass_vector=True
	bpy.data.scenes['Scene'].use_nodes=True

	bpy.context.scene.use_nodes = True
	nodes = bpy.context.scene.node_tree.nodes
	output_file = nodes.new("CompositorNodeOutputFile")
	output_file.file_slots.new("Speed")

	os.makedirs('/exr', exist_ok=True)
	output_file.base_path = '/exr/'
	output_file.format.file_format = 'OPEN_EXR'

	tree = bpy.context.scene.node_tree
	links = tree.links

	links.new(tree.nodes[2].inputs[0], tree.nodes[1].outputs[0])
	links.new(tree.nodes[2].inputs[1], tree.nodes[1].outputs[5])



def process_flow(total_frames):
	os.makedirs('/output/flow', exist_ok=True)
	image_paths=[]
	
	# Ignore first frame
	for i in range(1,total_frames):
		bpy.context.scene.frame_current = i
		bpy.ops.render.render(write_still=True)


	flows = os.listdir('/exr')
	exrs = [x for x in flows if 'Speed' in x]
	exrs.sort()
	for i, exr in enumerate(exrs):
		os.system('/flowcode/FlowCode/my_build/exr2flo /exr/{} /output/flow/{}.flo'.format(
			exr, str(i).zfill(8)
		))
		image_paths.append('flow/{}.flo'.format(str(i).zfill(8)))
	
	return image_paths

def clean_data():
	shutil.rmtree('/exr', ignore_errors=True)
	shutil.rmtree('/output', ignore_errors=True)


def load_project(path):
	bpy.ops.wm.open_mainfile(filepath=path)
	# bpy.data.scenes['Scene'].render.use_raytrace = False
	# bpy.data.scenes['Scene'].render.use_simplify = True
	# bpy.data.scenes['Scene'].render.simplify_subdivision_render = 1
	# bpy.data.scenes['Scene'].render.simplify_subdivision = 1
	# bpy.data.scenes['Scene'].render.use_shadows = False
	# bpy.data.scenes['Scene'].render.use_sss = False
	# bpy.data.scenes['Scene'].render.threads_mode = 'FIXED'
	# bpy.data.scenes['Scene'].render.threads = 8
	# bpy.data.scenes['Scene'].render.use_free_image_textures= True

def exit_blender():
	bpy.ops.wm.quit_blender()