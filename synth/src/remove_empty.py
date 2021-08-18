import os
import numpy as np
from PIL import Image
clean_dir = '/synth-polyp/synth/data/out/test_dataset/mask/'
images_dir = '/synth-polyp/synth/data/out/test_dataset/image/'

images = os.listdir(clean_dir)

for image in images:
    img = Image.open(clean_dir + image)

    im=np.asarray(img)
    if 255 not in im:
        os.remove(clean_dir + image)
        os.remove(images_dir + image)

        print(image)
        # import pdb;pdb.set_trace()
    
