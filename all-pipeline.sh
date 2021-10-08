### Run from synth-polyp container:

## Create unrealistic synthetic data using 3D
# docker exec synth-polyp python ./synth/src/generate.py --name synth_polyp_V10 --size 8000


### Run from cyclegan container:

## Clean cyclegan folders
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images /cyclegan/data/synth_polyp_V10/trainA /cyclegan/data/synth_polyp_V10/trainB /cyclegan/data/synth_polyp_V10/testA /cyclegan/data/synth_polyp_V10/testB

## Prepare folder structure to train Cyclegan
# docker exec cyclegan python /cyclegan/cyclegan/prepare_cyclegan.py --name synth_polyp_V10 --synth-dataset /cyclegan/data/synth_polyp_V10 --real-dataset /polyp-data/TestDataset/Kvasir/images --train-size-real 90 --train-size-synth 200 --test-size 10

## Train Cyclegan using real images and unrealistic synthetic images 
# docker exec cyclegan python /cyclegan/cyclegan/train.py --dataroot /cyclegan/data/synth_polyp_V10/ --name synth_polyp_V10 --model cycle_gan --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints

## Clean cyclegan images
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
# docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 200
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Train 
docker exec -it main python /main/Train.py --train_path /kvasir-train-10 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d10-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-20 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d20-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-30 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d30-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-40 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d40-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-50 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d50-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-60 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d60-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-70 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d70-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-80 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d80-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-90 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d90-kvasir.log
docker exec -it main python /main/Train.py --train_path /kvasir-train-100 --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d100-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-10/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d10-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-20/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d20-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-30/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d30-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-40/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d40-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-50/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d50-kvasir.log
# docker exec -it main python /main/Train.py --train_path /polyp-data-100/TrainDataset --test_path /polyp-data/TestDataset/Kvasir --train_save synth_polyp_V10 | tee logs/synth_polyp_V10-d100-kvasir.log


## Generate masks
# docker exec -it main python /main/Test.py --pth_path /main/data/synth_polyp_V10/snapshots/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset --save_path /main/data/synth_polyp_V10/results

## Evaluate masks
# cd eval
# octave
# pkg install image-2.12.0.tar.gz
# pkg load image
# main