## Clean cyclegan images
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
# docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 50
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Train 
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.01 | tee logs/synth_polyp_V10-e50-a-lr1.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.001 | tee logs/synth_polyp_V10-e50-a-lr2.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.005 | tee logs/synth_polyp_V10-e50-a-lr3.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0001 | tee logs/synth_polyp_V10-e50-a-lr4.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0005 | tee logs/synth_polyp_V10-e50-a-lr5.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00001 | tee logs/synth_polyp_V10-e50-a-lr6.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00005 | tee logs/synth_polyp_V10-e50-a-lr7.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000001 | tee logs/synth_polyp_V10-e50-a-lr8.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000005 | tee logs/synth_polyp_V10-e50-a-lr9.log

## Clean cyclegan images
docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 40
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images

docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.01 | tee logs/synth_polyp_V10-e40-a-lr1.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.001 | tee logs/synth_polyp_V10-e40-a-lr2.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.005 | tee logs/synth_polyp_V10-e40-a-lr3.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0001 | tee logs/synth_polyp_V10-e40-a-lr4.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0005 | tee logs/synth_polyp_V10-e40-a-lr5.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00001 | tee logs/synth_polyp_V10-e40-a-lr6.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00005 | tee logs/synth_polyp_V10-e40-a-lr7.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000001 | tee logs/synth_polyp_V10-e40-a-lr8.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000005 | tee logs/synth_polyp_V10-e40-a-lr9.log


## Clean cyclegan images
docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 30
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images

docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.01 | tee logs/synth_polyp_V10-e30-a-lr1.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.001 | tee logs/synth_polyp_V10-e30-a-lr2.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.005 | tee logs/synth_polyp_V10-e30-a-lr3.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0001 | tee logs/synth_polyp_V10-e30-a-lr4.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0005 | tee logs/synth_polyp_V10-e30-a-lr5.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00001 | tee logs/synth_polyp_V10-e30-a-lr6.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00005 | tee logs/synth_polyp_V10-e30-a-lr7.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000001 | tee logs/synth_polyp_V10-e30-a-lr8.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000005 | tee logs/synth_polyp_V10-e30-a-lr9.log


## Clean cyclegan images
docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V10/cyclegan_images
## Infer cyclegan to unrealistic images 
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V10/ --checkpoints_dir /cyclegan/data/synth_polyp_V10/checkpoints --name synth_polyp_V10 --model cycle_gan --phase train --epoch 10
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images

docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.01 | tee logs/synth_polyp_V10-e10-a-lr1.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.001 | tee logs/synth_polyp_V10-e10-a-lr2.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.005 | tee logs/synth_polyp_V10-e10-a-lr3.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0001 | tee logs/synth_polyp_V10-e10-a-lr4.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.0005 | tee logs/synth_polyp_V10-e10-a-lr5.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00001 | tee logs/synth_polyp_V10-e10-a-lr6.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.00005 | tee logs/synth_polyp_V10-e10-a-lr7.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000001 | tee logs/synth_polyp_V10-e10-a-lr8.log
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V10 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth_polyp_V10 --lr 0.000005 | tee logs/synth_polyp_V10-e10-a-lr9.log
