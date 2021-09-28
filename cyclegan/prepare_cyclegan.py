import os
import random
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--synth-dataset', type=str, help='Synthetic dataset')
parser.add_argument('--real-dataset', type=str, help='Real dataset')
parser.add_argument('--name', type=str, help='Target name')
parser.add_argument('--train-size-real', type=int, default=10, help='Train size real')
parser.add_argument('--train-size-synth', type=int, default=10, help='Train size synth')
parser.add_argument('--test-size', type=int, default=10, help='Test size')
args = parser.parse_args()

def prepare(synth_dataset, real_dataset, target_name, train_size_real, train_size_synth, test_size):

    synth_dataset = synth_dataset + '/images'

    os.makedirs('/cyclegan/data/{}/trainA'.format(target_name), exist_ok=True)
    os.makedirs('/cyclegan/data/{}/trainB'.format(target_name), exist_ok=True)
    os.makedirs('/cyclegan/data/{}/testA'.format(target_name), exist_ok=True)
    os.makedirs('/cyclegan/data/{}/testB'.format(target_name), exist_ok=True)

    synth_images = os.listdir(synth_dataset)
    random.shuffle(synth_images)
    synth_images = synth_images[:train_size_synth]
    
    trainA_images = random.sample(synth_images, len(synth_images)-test_size)
    testA_images = [x for x in synth_images if x not in trainA_images]


    real_images = os.listdir(real_dataset)
    random.shuffle(real_images)
    real_images = real_images[:train_size_real]

    trainB_images = random.sample(real_images, len(real_images)-test_size)
    testB_images = [x for x in real_images if x not in trainB_images]
    for f in trainA_images:
        shutil.copy(synth_dataset + '/' + f,'/cyclegan/data/{}/trainA'.format(target_name))
    for f in testA_images:
        shutil.copy(synth_dataset + '/' + f,'/cyclegan/data/{}/testA'.format(target_name))
    for f in trainB_images:
        shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/trainB'.format(target_name))
    for f in testB_images:
        shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/testB'.format(target_name))


prepare(args.synth_dataset, args.real_dataset, args.name, args.train_size_real, args.train_size_synth, args.test_size)