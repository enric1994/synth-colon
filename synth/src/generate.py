import argparse
import bpy
import random
import blender_utils as utils
from dtd_utils import get_random_texture, get_random_polyp, plain_color
import os
import numpy as np
from PIL import Image


def gen(dataset_version, TOTAL_IMAGES):
    # Make colon

    def pathPointLoc(cpath, points):

        if cpath.type in ['NURBS', 'POLY']:
            cpath.points.add(len(points)-1)
            for (index, point) in enumerate(points):
                cpath.points[index].co = point
                print(cpath.points[index].co)
            cpath.use_endpoint_u = True
        elif cpath.type in ['BEZIER']:
            cpath.bezier_points.add(len(points)-1)
            for (index, point) in enumerate(points):
                x, y, z, w = point
                cpath.bezier_points[index].co = x, y, z
                cpath.bezier_points[index].handle_left = x-1, y-1, z-1
                cpath.bezier_points[index].handle_right = x+1, y+1, z+1
                print(cpath.bezier_points[index].co)
        return



    for image_number in range(0,TOTAL_IMAGES):
        utils.load_project('/synth-polyp/synth/base.blend')
        bpy.ops.curve.primitive_bezier_circle_add()
        b = bpy.data.objects['BezierCircle']
        b.scale[0] = 4
        b.scale[1] = 4

        cu = bpy.data.curves.new("MyCurveData", "CURVE")
        ob = bpy.data.objects.new("MyCurveObject", cu)
        polyline = cu.splines.new('NURBS')  # 'POLY''BEZIER''BSPLINE''CARDINAL''NURBS'

        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob

        cu.dimensions = '3D'
        cu.bevel_object = bpy.data.objects["BezierCircle"]
        cu.taper_object = bpy.data.objects["BezierCircle"]

        max_rand = 0.4
        long_interval = .5

        pts = [(0, 0, 0, 1), (1 *  long_interval, random.uniform(-max_rand,max_rand),random.uniform(-max_rand, max_rand), 1), (2 * long_interval, random.uniform(-max_rand, max_rand),random.uniform(-max_rand, max_rand), 1), (3 * long_interval, random.uniform(-max_rand, max_rand),random.uniform(-max_rand, max_rand), 1), (4 * long_interval, random.uniform(-max_rand, max_rand),random.uniform(-max_rand, max_rand), 1), (5 * long_interval, random.uniform(-max_rand, max_rand),random.uniform(-max_rand, max_rand), 1), (6 * long_interval, 0, 0, 1), (7 * long_interval, 0, 0, 1)]
        pathPointLoc(polyline, pts)

        bpy.context.scene.objects.active = bpy.data.objects['MyCurveObject']
        bpy.data.objects['MyCurveObject'].select = True


        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action = 'SELECT')

        bpy.ops.transform.vertex_random(offset=random.uniform(0,0.15), uniform=0.0, normal=0.0, seed=0)
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')

        #Create material
        mat = bpy.data.materials.new(name="Material")
        random_shade_1 = random.uniform(0.6,1.2)
        random_shade_2 = random.uniform(0.6,1.2)
        random_shade_3 = random.uniform(0.6,1.2)
        mat.diffuse_color=[0.800000 * random_shade_1, 0.18 * random_shade_2, 0.13 * random_shade_3]

        # tex = bpy.data.textures.new("SomeName", 'IMAGE')
        # img = bpy.data.images.load(filepath=plain_color('colon'))

        # tex.image = img
        # # tex.texture_coords = 'WINDOW'

        # slot = mat.texture_slots.add()
        # slot.texture = tex
        # # slot.texture_coords = 'OBJECT'
        # slot.texture_coords='GLOBAL'
        # import pdb;pdb.set_trace()

        # Apply material
        bpy.data.objects['MyCurveObject'].data.materials.append(mat)


        num_polyps = 1

        # Make polyps
        for i in range(0,num_polyps):
            bpy.ops.object.mode_set(mode='OBJECT')
            if i > 0:
                object_name = 'Sphere.' + str(i).zfill(3)
            else:
                object_name = 'Sphere'
            bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=128, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))

            bpy.data.objects[object_name].scale[0] = random.uniform(0.1, 0.5)
            bpy.data.objects[object_name].scale[1] = random.uniform(0.1, 0.5)
            bpy.data.objects[object_name].scale[2] = random.uniform(0.1, 0.5)

            bpy.data.objects[object_name].location[0] = random.uniform(2, 2.3)
            bpy.data.objects[object_name].location[1] = random.uniform(-1, 1)
            bpy.data.objects[object_name].location[2] = random.uniform(-1, 1)
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.transform.vertex_random(offset=random.uniform(0,0.05), uniform=0.0, normal=0.0, seed=0)
            bpy.ops.mesh.vertices_smooth()
            bpy.ops.mesh.vertices_smooth()
            bpy.ops.mesh.vertices_smooth()
            bpy.ops.mesh.vertices_smooth()
            bpy.ops.object.mode_set(mode='OBJECT')

            #Create material
            mat = bpy.data.materials.new(name="Material." + str(i))
            random_shade_1 = random.uniform(0.6,1.2)
            random_shade_2 = random.uniform(0.6,1.2)
            random_shade_3 = random.uniform(0.6,1.2)
            mat.diffuse_color=[0.800000 * random_shade_1, 0.18 * random_shade_2, 0.13 * random_shade_3]

            # tex = bpy.data.textures.new("SomeName." + str(i), 'IMAGE')
            # img = bpy.data.images.load(filepath=plain_color('polyp'))

            # tex.image = img
            # # tex.texture_coords = 'WINDOW'

            # slot = mat.texture_slots.add()
            # slot.texture = tex
            # slot.texture_coords = 'GLOBAL'


            # Apply material
            bpy.data.objects[object_name].data.materials.append(mat)



            

        # Set lighting
        lighting_config = {'l2': {
                'light_type': 'SUN',
                'position': [0,0,10],
                'rotation': [
                    random.uniform(0,4),
                    random.uniform(0,4),
                    random.uniform(0,4)
                ],
                'energy': random.uniform(2,2),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            },
            'l3': {
                'light_type': 'POINT',
                'position': [2.5,0,0],
                'rotation': [
                    random.uniform(0,4),
                    random.uniform(0,4),
                    random.uniform(0,4)
                ],
                'energy': random.uniform(0,1),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            },
            'l4': {
                'light_type': 'POINT',
                'position': [3.5,0,0],
                'rotation': [
                    random.uniform(0,4),
                    random.uniform(0,4),
                    random.uniform(0,4)
                ],
                'energy': random.uniform(0,1),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            },
            'negative_1': {
                'light_type': 'POINT',
                'position': [1.5,0,0],
                'rotation': [
                    0,0,0
                ],
                'negative_light': True,
                'energy': random.uniform(0,1),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            },
            'negative_2': {
                'light_type': 'POINT',
                'position': [1.5,0.2,0],
                'rotation': [
                    0,0,0
                ],
                'negative_light': True,
                'energy': random.uniform(0,1),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            },
             'negative_3': {
                'light_type': 'POINT',
                'position': [1.5,-0.2,0],
                'rotation': [
                    0,0,0
                ],
                'negative_light': True,
                'energy': random.uniform(0,1),
                'shadow': False,
                'color': [
                    1,1,1
                ]
            }



        }
        utils.set_lighting(lighting_config)

        utils.save_project('/synth-polyp/scene.blend')

        # Render
        utils.render_keyframes('images', image_number, dataset_version)

        # Render mask
        bpy.data.worlds['World'].horizon_color=(0,0,0)
        for light_name in lighting_config.keys():
            bpy.data.objects[light_name].hide_render=True

        for i in range(0,num_polyps):
            if i > 0:
                object_name = 'Sphere.' + str(i).zfill(3)
            else:
                object_name = 'Sphere'
            for slot in bpy.data.objects[object_name].material_slots:
                new_mat = bpy.data.materials.new(name="Mask")
                new_mat.diffuse_color = (1,1,1)
                slot.material = new_mat
                slot.material.use_shadeless=True
                
        # Hide other objects
        # bpy.data.objects['MyCurveObject'].hide_render=True

        # Render
        utils.render_keyframes('masks', image_number, dataset_version)

        # Reset
        bpy.ops.wm.read_factory_settings(use_empty=True)



    def remove_empty_masks(dataset_name):

        print('Removing images with no polyps...')

        clean_dir = '/synth-polyp/data/{}/masks/'.format(dataset_name)
        images_dir = '/synth-polyp/data/{}/images/'.format(dataset_name)

        images = os.listdir(clean_dir)

        for image in images:
            img = Image.open(clean_dir + image)

            im=np.asarray(img)
            polyp_pixels = np.count_nonzero(im)

            if polyp_pixels < 20000:
                os.remove(clean_dir + image)
                os.remove(images_dir + image)

                # print(image)
                # import pdb;pdb.set_trace()
            

    remove_empty_masks(dataset_version)

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default="test", help='Dataset name')
parser.add_argument('--size', type=int, default=10, help='Dataset size')
args = parser.parse_args()

gen(args.name, args.size)