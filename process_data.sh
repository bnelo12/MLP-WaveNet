cd wavenet_vocoder
python mksubset.py --train-dev-test-split ../data ../data_split
python preprocess.py songs ../data_split/dev ../data_preprocessed/dev
python preprocess.py songs ../data_split/train_no_dev ../data_preprocessed/train_no_dev
python preprocess.py songs ../data_split/eval ../data_preprocessed/eval
