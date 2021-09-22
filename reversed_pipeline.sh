## Remove folders
# docker exec cyclegan rm -rf /cyclegan/data/synth_polyp_V9/cyclegan_images /cyclegan/data/synth_polyp_V9/trainA /cyclegan/data/synth_polyp_V9/trainB /cyclegan/data/synth_polyp_V9/testA /cyclegan/data/synth_polyp_V9/testB /cyclegan/data/synth_polyp_V9/results

## Prepare test dataset
# docker exec -it cyclegan python /cyclegan/cyclegan/prepare_infer_test.py --real-dataset /polyp-data/TestDataset/CVC-ColonDB/images --name synth_polyp_V9


## Infer cyclegan to TEST real images -> synth images
# docker exec cyclegan python /cyclegan/cyclegan/reversed_test.py --dataroot /cyclegan/data/synth_polyp_V9/ --checkpoints_dir /cyclegan/data/synth_polyp_V9/checkpoints --name synth_polyp_V9 --model cycle_gan --phase test --epoch 50 --direction BtoA
# --results_dir /cyclegan/data/synth_polyp_V6/cyclegan_images


### Run from main container:

## Remap folders
# docker exec -it main mkdir -p /main/data/synth_polyp_V9/cyclegan_images/CVC-ColonDB/images /main/data/synth_polyp_V9/cyclegan_images/CVC-ColonDB/masks
# docker exec -it main mv /main/data/synth_polyp_V9/cyclegan_images/* /main/data/synth_polyp_V9/cyclegan_images/CVC-ColonDB/images

## Generate masks
docker exec -it main python /main/Reversed_test.py --pth_path /main/data/synth_polyp_V9/snapshots/HarD-MSEG-best.pth --test_data /main/data/synth_polyp_V9/cyclegan_images --save_path /main/data/synth_polyp_V9/results

## Evaluate masks
# cd eval
# octave
# pkg install -forge image
# pkg load image
# main