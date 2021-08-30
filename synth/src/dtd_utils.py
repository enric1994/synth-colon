import os
import random

base_path = '/datasets/dtd/images/'

def get_random_texture():
    
    categories = os.listdir(base_path)
    rand_category = random.choice(categories)
    images = os.listdir(os.path.join(base_path, rand_category))
    image_name = random.choice(images)

    image_path = os.path.join(base_path, rand_category, image_name)

    return image_path


def get_random_polyp():
    polyps_path = '/polyp-data/TrainDataset/images'
    
    # categories = os.listdir(base_path)
    # rand_category = random.choice(categories)
    images = os.listdir(polyps_path)
    image_name = random.choice(images)

    image_path = os.path.join(polyps_path, image_name)

    return image_path

def plain_color(name):
    if name == 'colon':
        return '/synth-polyp/synth/plain_colors/skin.png'
    elif name == 'polyp':
        return '/synth-polyp/synth/plain_colors/apple.png'