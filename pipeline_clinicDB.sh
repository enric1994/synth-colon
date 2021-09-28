### Run from synth-polyp container:

## Create unrealistic synthetic data using 3D
# docker exec synth-polyp python ./synth/src/generate.py --name synth_polyp_V9 --size 8000


### Run from cyclegan container:

## Prepare folder structure to train Cyclegan
# docker exec cyclegan python /cyclegan/cyclegan/prepare_cyclegan.py --name synth_polyp_V9.2 --synth-dataset /cyclegan/data/synth_polyp_V9.2 --real-dataset /polyp-data/TestDataset/CVC-ClinicDB/images --size 10

## Train Cyclegan using real images and unrealistic synthetic images 
docker exec cyclegan python /cyclegan/cyclegan/train.py --dataroot /cyclegan/data/synth_polyp_V9.2/ --name synth_polyp_V9.2 --model cycle_gan --checkpoints_dir /cyclegan/data/synth_polyp_V9.2/checkpoints

## Clean cyclegan images
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
## Infer cyclegan to unrealistic images 
# docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 15
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Train 
# docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-e-e15-colondb.log

## Generate masks
# docker exec -it main python /main/Test.py --pth_path /main/data/synth_polyp_V9/snapshots/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset --save_path /main/data/synth_polyp_V9/results

## Evaluate masks
# cd eval
# octave
# pkg install -forge image
# pkg load image
# main