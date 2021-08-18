import os
import random

places_base_path = '/datasets/places/train'

def get_random_image(categories):
    
    rand_category = random.choice(categories)
    images = os.listdir(os.path.join(places_base_path, rand_category))
    image_name = random.choice(images)

    image_path = os.path.join(places_base_path, rand_category, image_name)

    return image_path