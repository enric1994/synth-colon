# python Train.py --train_path /main/synth/data/out/synth-polyp-V3 --test_path /polyp-data/TestDataset/CVC-300 --train_save synth-polyp-V3 | tee logs/train-synth-polyp-V3.log
python Train.py --train_path /polyp-data/TrainDataset --test_path /polyp-data/TestDataset/CVC-300 --train_save real_data_test_V1 | tee logs/real_data_test_V1.log

# python Test.py --pth_path /main/snapshots/synth-polyp-V3/HarD-MSEG-best.pth --test_data /polyp-data/TestDataset --save_path /main/results/synth-polyp-V3