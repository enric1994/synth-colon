import os
import shutil
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--synth-dataset', type=str, help='Synthetic dataset')
parser.add_argument('--real-dataset', type=str, help='Real dataset')
parser.add_argument('--name', type=str, help='Target name')
# parser.add_argument('--size', type=int, default=1400, help='Train size')
args = parser.parse_args()

def prepare(real_dataset, target_name):

    # synth_dataset = synth_dataset + '/images'

    os.makedirs('/cyclegan/data/{}/testA'.format(target_name), exist_ok=True)
    os.makedirs('/cyclegan/data/{}/testB'.format(target_name), exist_ok=True)



    real_images = os.listdir(real_dataset)

    for f in real_images:
        shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/testA'.format(target_name))
    for f in real_images:
        shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/testB'.format(target_name))


prepare(args.real_dataset, args.name)