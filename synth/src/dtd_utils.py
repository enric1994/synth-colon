import os
import random

base_path = '/datasets/dtd/images/'

def get_random_texture():
    
    categories = os.listdir(base_path)
    rand_category = 'fibrous' #random.choice(categories)
    images = os.listdir(os.path.join(base_path, rand_category))
    image_name = random.choice(images)

    image_path = os.path.join(base_path, rand_category, image_name)

    return image_path