### Run from synth-polyp container:

## Create unrealistic synthetic data using 3D
# docker exec synth-polyp python ./synth/src/generate.py --name synth_polyp_V10 --size 8000


### Run from cyclegan container:

## Clean cyclegan folders
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images /cyclegan/data/synth_polyp_V10/trainA /cyclegan/data/synth_polyp_V10/trainB /cyclegan/data/synth_polyp_V10/testA /cyclegan/data/synth_polyp_V10/testB

## Prepare folder structure to train Cyclegan
# docker exec cyclegan python /cyclegan/cyclegan/prepare_cyclegan.py --name synth_polyp_V10 --synth-dataset /cyclegan/data/synth_polyp_V10 --real-dataset /polyp-data/TestDataset/CVC-300/images --train-size-real 100 --train-size-synth 400 --test-size 10

## Train Cyclegan using real images and unrealistic synthetic images 
# docker exec cyclegan python /cyclegan/cyclegan/train.py --dataroot /cyclegan/data/synth_polyp_V10/ --name synth_polyp_V10 --model cycle_gan --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints

## Clean cyclegan images
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
# docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 200
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Train 
# docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-e200-cvc300.log

## Generate masks
docker exec -it main python /main/Test.py --pth_path /main/data/synth_polyp_V10/snapshots/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset --save_path /main/data/synth_polyp_V10/results

## Evaluate masks
# cd eval
# octave
# pkg install -forge image
# pkg load image
# main