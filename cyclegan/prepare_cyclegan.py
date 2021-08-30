import os
import random
import shutil

synth_dataset = '/cyclegan/synth/data/out/synth-polyp-V4/images'
real_dataset = '/polyp-data/TrainDataset/images'
target_name = 'cyclegan_V4'
train_size = 1000

os.makedirs('/cyclegan/data/{}/trainA'.format(target_name), exist_ok=True)
os.makedirs('/cyclegan/data/{}/trainB'.format(target_name), exist_ok=True)
os.makedirs('/cyclegan/data/{}/testA'.format(target_name), exist_ok=True)
os.makedirs('/cyclegan/data/{}/testB'.format(target_name), exist_ok=True)

synth_images = os.listdir(synth_dataset)
trainA_images = random.sample(synth_images, train_size)
testA_images = [x for x in synth_images if x not in trainA_images]


real_images = os.listdir(real_dataset)

trainB_images = random.sample(real_images, train_size)
testB_images = [x for x in real_images if x not in trainB_images]

for f in trainA_images:
    shutil.copy(synth_dataset + '/' + f,'/cyclegan/data/{}/trainA'.format(target_name))
for f in testA_images:
    shutil.copy(synth_dataset + '/' + f,'/cyclegan/data/{}/testA'.format(target_name))
for f in trainB_images:
    shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/trainB'.format(target_name))
for f in testB_images:
    shutil.copy(real_dataset + '/' + f,'/cyclegan/data/{}/testB'.format(target_name))


