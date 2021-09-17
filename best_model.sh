docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 5
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e5.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 10
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e10.log

docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 15
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e15.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 20
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e20.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 25
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e25.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 30
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e30.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 35
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e35.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 40
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e40.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 45
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e45.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 50
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e50.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 55
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e55.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 60
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e60.log


docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images
docker exec cyclegan python /cyclegan/cyclegan/test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase train --epoch 100
docker exec -it main python /main/Train.py --train_path /main/data/synth_polyp_V9 --test_path /polyp-data/TestDataset/CVC-ColonDB --train_save synth_polyp_V9 | tee logs/synth_polyp_V9-d-e100.log

## Generate masks
# docker exec -it main python /main/Test.py --pth_path /main/data/synth_polyp_V9/snapshots/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset/CVC-ColonDB --save_path /main/data/synth_polyp_V9/results

## Evaluate masks
# cd eval
# octave
# pkg install -forge image
# pkg load image
# main