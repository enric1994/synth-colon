import bpy
import random
import blender_utils as utils
from dtd_utils import get_random_texture


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


TOTAL_IMAGES = 1000

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

    max_rand = 1
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
    bpy.ops.object.mode_set(mode='OBJECT')

    #Create material
    mat = bpy.data.materials.new(name="Material")

    tex = bpy.data.textures.new("SomeName", 'IMAGE')
    img = bpy.data.images.load(filepath=get_random_texture())

    tex.image = img
    # tex.texture_coords = 'WINDOW'

    slot = mat.texture_slots.add()
    slot.texture = tex
    # slot.texture_coords = 'OBJECT'
    slot.texture_coords='GLOBAL'
    # import pdb;pdb.set_trace()

    # Apply material
    bpy.data.objects['MyCurveObject'].data.materials.append(mat)


    num_polyps = 3

    # Make polyps
    for i in range(0,num_polyps):
        bpy.ops.object.mode_set(mode='OBJECT')
        if i > 0:
            object_name = 'Sphere.' + str(i).zfill(3)
        else:
            object_name = 'Sphere'
        bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))

        bpy.data.objects[object_name].scale[0] = random.uniform(0.1, 0.5)
        bpy.data.objects[object_name].scale[1] = random.uniform(0.1, 0.5)
        bpy.data.objects[object_name].scale[2] = random.uniform(0.1, 0.5)

        bpy.data.objects[object_name].location[0] = random.uniform(2, 2.3)
        bpy.data.objects[object_name].location[1] = random.uniform(-1, 1)
        bpy.data.objects[object_name].location[2] = random.uniform(-1, 1)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.transform.vertex_random(offset=random.uniform(0,0.45), uniform=0.0, normal=0.0, seed=0)
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.mesh.vertices_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')

        #Create material
        mat = bpy.data.materials.new(name="Material." + str(i))

        tex = bpy.data.textures.new("SomeName." + str(i), 'IMAGE')
        img = bpy.data.images.load(filepath=get_random_texture())

        tex.image = img
        # tex.texture_coords = 'WINDOW'

        slot = mat.texture_slots.add()
        slot.texture = tex
        slot.texture_coords = 'GLOBAL'


        # Apply material
        bpy.data.objects[object_name].data.materials.append(mat)



        utils.save_project('/synth-polyp/scene.blend')

    # Set lighting
    lighting_config = {'l0': {
            'light_type': 'SUN',
            'position': [0,0,10],
            'rotation': [
                random.uniform(0,4),
                random.uniform(0,4),
                random.uniform(0,4)
            ],
            'energy': random.uniform(0,2),
            'shadow': False,
            'color': [
                random.uniform(0,1),
                random.uniform(0,1),
                random.uniform(0,1)
            ]

        },
        'l1': {
            'light_type': 'SUN',
            'position': [0,0,10],
            'rotation': [
                random.uniform(0,4),
                random.uniform(0,4),
                random.uniform(0,4)
            ],
            'energy': random.uniform(0,2),
            'shadow': False,
            'color': [
                random.uniform(0,1),
                random.uniform(0,1),
                random.uniform(0,1)
            ]

        },
        'l2': {
            'light_type': 'SUN',
            'position': [0,0,10],
            'rotation': [
                random.uniform(0,4),
                random.uniform(0,4),
                random.uniform(0,4)
            ],
            'energy': random.uniform(0,2),
            'shadow': False,
            'color': [
                random.uniform(0,1),
                random.uniform(0,1),
                random.uniform(0,1)
            ]
        }


    }
    utils.set_lighting(lighting_config)

    # Render
    utils.render_keyframes('images', image_number, 'test_dataset')

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
    utils.render_keyframes('masks', image_number, 'test_dataset')

    # Reset
    bpy.ops.wm.read_factory_settings(use_empty=True)


# import bpy
# import math
# import sys
# import os
# import random

# from dtd_utils import get_random_texture
# from places_utils import get_random_image

# dataset_name = 'V3'

# BACKGROUND_CLASSES = ['cliff', 'hotel-outdoor', 'hangar-outdoor', 'bridge', 'moat-water', 'pond', 'hospital_room', 'mezzanine', 'ocean', 'apartment_building-outdoor', 'shoe_shop', 'bow_window-indoor', 'raceway', 'arena-performance', 'forest_path', 'ski_slope', 'building_facade', 'boathouse', 'hardware_store', 'ice_skating_rink-indoor', 'barndoor', 'cafeteria', 'aqueduct', 'village', 'iceberg', 'lighthouse', 'discotheque', 'sky', 'alley', 'corral', 'tower', 'oast_house', 'amusement_park', 'balcony-exterior', 'slum', 'delicatessen', 'pasture', 'embassy', 'jacuzzi-indoor', 'shopping_mall-indoor', 'balcony-interior', 'office_cubicles', 'pub-indoor', 'flea_market-indoor', 'legislative_chamber', 'basketball_court-indoor', 'gymnasium-indoor', 'harbor', 'kitchen', 'chalet', 'watering_hole', 'shower', 'elevator_lobby', 'forest-broadleaf', 'beauty_salon', 'staircase', 'auditorium', 'train_interior', 'living_room', 'swimming_pool-outdoor', 'restaurant_kitchen', 'swamp', 'lecture_room', 'biology_laboratory', 'forest_road', 'heliport', 'gift_shop', 'bazaar-outdoor', 'ball_pit', 'hangar-indoor', 'canal-urban', 'bank_vault', 'hunting_lodge-outdoor', 'loading_dock', 'boxing_ring', 'entrance_hall', 'shed', 'mosque-outdoor', 'desert-vegetation', 'parking_lot', 'elevator_shaft', 'throne_room', 'kennel-outdoor', 'pantry', 'recreation_room', 'jail_cell', 'inn-outdoor', 'locker_room', 'lock_chamber', 'stadium-baseball', 'arcade', 'swimming_hole', 'cockpit', 'boat_deck', 'fire_station', 'mountain', 'chemistry_lab', 'stadium-football', 'rope_bridge', 'lagoon', 'airplane_cabin', 'downtown', 'tree_farm', 'islet', 'mountain_snowy', 'ruin', 'attic', 'ice_floe', 'car_interior', 'lake-natural', 'dorm_room', 'home_theater', 'market-outdoor', 'greenhouse-indoor', 'bar', 'fishpond', 'florist_shop-indoor', 'mansion', 'bus_interior', 'dam', 'patio', 'athletic_field-outdoor', 'grotto', 'basement', 'shopfront', 'arena-hockey', 'carrousel', 'archaelogical_excavation', 'gazebo-exterior', 'beer_hall', 'rainforest', 'windmill', 'kasbah', 'office', 'mountain_path', 'schoolhouse', 'palace', 'bedchamber', 'crevasse', 'canyon', 'plaza', 'archive', 'laundromat', 'diner-outdoor', 'booth-indoor', 'natural_history_museum', 'stage-indoor', 'stage-outdoor', 'pagoda', 'volleyball_court-outdoor', 'beer_garden', 'wheat_field', 'rice_paddy', 'art_studio', 'bedroom', 'banquet_hall', 'repair_shop', 'raft', 'glacier', 'army_base', 'ice_skating_rink-outdoor', 'playroom', 'football_field', 'subway_station-platform', 'waiting_room', 'field_road', 'waterfall', 'classroom', 'garage-outdoor', 'utility_room', 'dining_room', 'wave', 'youth_hostel', 'phone_booth', 'art_gallery', 'corridor', 'museum-outdoor', 'temple-asia', 'nursing_home', 'snowfield', 'bakery-shop', 'lobby', 'office_building', 'bamboo_forest', 'aquarium', 'galley', 'butte', 'bazaar-indoor', 'library-outdoor', 'field-wild', 'amusement_arcade', 'gas_station', 'wind_farm', 'beach', 'sauna', 'ballroom', 'stadium-soccer', 'wet_bar', 'food_court', 'greenhouse-outdoor', 'arena-rodeo', 'corn_field', 'courthouse', 'racecourse', 'cabin-outdoor', 'courtyard', 'hayfield', 'airport_terminal', 'farm', 'martial_arts_gym', 'excavation', 'cottage', 'medina', 'ticket_booth', 'childs_room', 'clothing_store', 'zen_garden', 'candy_store', 'fire_escape', 'doorway-outdoor', 'orchestra_pit', 'movie_theater-indoor', 'drugstore', 'mausoleum', 'market-indoor', 'general_store-outdoor', 'clean_room', 'campsite', 'landing_deck', 'manufactured_home', 'water_park', 'highway', 'playground', 'water_tower', 'orchard', 'underwater-ocean_deep', 'physics_laboratory', 'pavilion', 'art_school', 'tundra', 'river', 'beach_house', 'cemetery', 'baseball_field', 'church-outdoor', 'artists_loft', 'church-indoor', 'skyscraper', 'museum-indoor', 'ice_shelf', 'landfill', 'science_museum', 'picnic_area', 'soccer_field', 'volcano', 'auto_factory', 'alcove', 'library-indoor', 'hospital', 'junkyard', 'crosswalk', 'pier', 'vegetable_garden', 'closet', 'promenade', 'botanical_garden', 'marsh', 'train_station-platform', 'supermarket', 'bullring', 'desert_road', 'auto_showroom', 'trench', 'home_office', 'creek', 'department_store', 'conference_room', 'valley', 'pizzeria', 'oilrig', 'butchers_shop', 'hotel_room', 'igloo', 'yard', 'amphitheater', 'roof_garden', 'house', 'badlands', 'pet_shop', 'railroad_track', 'reception', 'japanese_garden', 'castle', 'campus', 'television_room', 'bathroom', 'field-cultivated', 'lawn', 'hot_spring', 'burial_chamber', 'ice_cream_parlor', 'berth', 'restaurant', 'engine_room', 'dressing_room', 'sushi_bar', 'fountain', 'runway', 'toyshop', 'catacomb', 'construction_site', 'bowling_alley', 'canal-natural', 'topiary_garden', 'formal_garden', 'fabric_store', 'storage_room', 'general_store-indoor', 'airfield', 'park', 'vineyard', 'bookstore', 'barn', 'ski_resort', 'porch', 'jewelry_shop', 'arch', 'golf_course', 'viaduct', 'boardwalk', 'garage-indoor', 'industrial_area', 'bus_station-indoor', 'motel', 'sandbox', 'music_studio', 'dining_hall', 'street', 'elevator-door', 'computer_room', 'kindergarden_classroom', 'coffee_shop', 'television_studio', 'swimming_pool-indoor', 'desert-sand', 'stable', 'assembly_line', 'synagogue-outdoor', 'server_room', 'fastfood_restaurant', 'atrium-public', 'veterinarians_office', 'residential_neighborhood', 'nursery', 'coast', 'driveway', 'operating_room', 'parking_garage-indoor', 'tree_house', 'escalator-indoor', 'pharmacy', 'rock_arch', 'parking_garage-outdoor', 'restaurant_patio', 'conference_center']


# items = os.listdir('/hand-synth/data/svg')

# for item in items:
# 	item_path = '/hand-synth/data/svg/' + item

# 	for image in range(0,500):
# 		utils.load_project('/hand-synth/base.blend')

# 		camera_config = {'position': [5,0,0],
# 		'render_size_x': 512,
# 		'render_size_y': 512}
# 		utils.set_camera(camera_config, 1)

# 		########################################
# 		background_config = {'position': [-5, 0, 0],
# 		'ambient_color': [0.5,0.5,0.5],
# 		'path': get_random_image(BACKGROUND_CLASSES),
# 		'size_x': 10,
# 		'size_y': 10}

# 		utils.set_background(background_config)
# 		##################
# 		lighting_config = {'l0': {
# 				'light_type': 'SUN',
# 				'position': [0,0,10],
# 				'rotation': [
# 					random.uniform(0,4),
# 					random.uniform(0,4),
# 					random.uniform(0,4)
# 				],
# 				'energy': random.uniform(0,2),
# 				'shadow': False,
# 				'color': [
# 					random.uniform(0,1),
# 					random.uniform(0,1),
# 					random.uniform(0,1)
# 				]

# 			},
# 			'l1': {
# 				'light_type': 'SUN',
# 				'position': [0,0,10],
# 				'rotation': [
# 					random.uniform(0,4),
# 					random.uniform(0,4),
# 					random.uniform(0,4)
# 				],
# 				'energy': random.uniform(0,2),
# 				'shadow': False,
# 				'color': [
# 					random.uniform(0,1),
# 					random.uniform(0,1),
# 					random.uniform(0,1)
# 				]

# 			},
# 			'l2': {
# 				'light_type': 'SUN',
# 				'position': [0,0,10],
# 				'rotation': [
# 					random.uniform(0,4),
# 					random.uniform(0,4),
# 					random.uniform(0,4)
# 				],
# 				'energy': random.uniform(0,2),
# 				'shadow': False,
# 				'color': [
# 					random.uniform(0,1),
# 					random.uniform(0,1),
# 					random.uniform(0,1)
# 				]
# 			}


# 		}
# 		utils.set_lighting(lighting_config)



# 		bpy.ops.import_curve.svg (filepath=item_path)
# 		objects = bpy.context.scene.objects

# 		for obj in objects:
# 			obj.select = obj.type == "CURVE"
# 		bpy.context.scene.objects.active = bpy.data.objects["Curve"]
# 		bpy.ops.object.join()



# 		context = bpy.context
# 		scene = context.scene

# 		mball = bpy.data.objects.get("Curve")

# 		if mball:
# 			me = mball.to_mesh(scene, False, 'PREVIEW')

# 			# add an object
# 			o = bpy.data.objects.new("MBallMesh", me)
# 			scene.objects.link(o)
# 			o.matrix_world = mball.matrix_world

# 			# not keep original
# 			scene.objects.unlink(mball)


# 		bpy.context.scene.objects.active = o
# 		bpy.ops.object.modifier_add(type='SOLIDIFY')
# 		bpy.context.object.modifiers["Solidify"].offset = 0.1
# 		bpy.context.object.modifiers["Solidify"].thickness = random.uniform(0.01,0.03)
# 		bpy.context.active_object.rotation_mode = 'XYZ'

# 		# random.uniform(0,360)
# 		bpy.context.active_object.rotation_euler = (math.radians(random.uniform(0,360)), random.uniform(0,360), math.radians(random.uniform(0,360)))
# 		bpy.context.scene.objects.active.scale = (random.uniform(15,20), random.uniform(15,20), random.uniform(15,20))
# 		bpy.context.active_object.location = [random.uniform(-0.5,0.5),random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]

# 		# Remove materials
# 		o.data.materials.clear()

# 		# Create material
# 		mat = bpy.data.materials.new(name="Material")

# 		tex = bpy.data.textures.new("SomeName", 'IMAGE')
# 		img = bpy.data.images.load(filepath=get_random_texture())

# 		tex.image = img
# 		# tex.texture_coords = 'WINDOW'

# 		slot = mat.texture_slots.add()
# 		slot.texture = tex
# 		slot.texture_coords = 'OBJECT'


# 		# Apply material
# 		o.data.materials.append(mat)

# 		utils.save_project('/hand-synth/scene.blend')



# 		# Render
# 		utils.render_keyframes(item.split('.')[0], image, dataset_name)

# 		# Reset
# 		bpy.ops.wm.read_factory_settings(use_empty=True)
