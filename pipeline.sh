### Run from synth-polyp container:

## Create unrealistic synthetic data using 3D
python ./synth/src/generate.py --name synth_polyp_V7 --size 2000


### Run from cyclegan container:

## Prepare folder structure to train Cyclegan
# python /cyclegan/cyclegan/prepare_cyclegan.py --name synth_polyp_V6 --synth-dataset /cyclegan/data/synth_polyp_V6 --real-dataset /polyp-data/TrainDataset/images --size 300

## Train Cyclegan using real images and unrealistic synthetic images 
# python /cyclegan/cyclegan/train.py --dataroot /cyclegan/data/synth_polyp_V6/ --name synth_polyp_V6 --model cycle_gan --checkpoints_dir /cyclegan/data/synth_polyp_V6/checkpoints

## Infer cyclegan to unrealistic images 
# python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V6/ --checkpoints_dir /cyclegan/data/synth_polyp_V6/checkpoints --name synth_polyp_V6 --model cycle_gan 
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Train 
# python Train.py --train_path /polyp-data/TrainDataset --test_path /polyp-data/TestDataset/CVC-300 --train_save real_data_test_V1 | tee logs/real_data_test_V1.log

## Generate masks
# python Test.py --pth_path /main/snapshots/synth-polyp-V3/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset --save_path /main/results/synth-polyp-V3

## Evaluate masks
# cd eval
# pkg install -forge image
# pkg load image
# main