import os
import re

PROJECT_PATH = os.environ['PROJECT_PATH']
DATASET_DIR = os.environ['DATASET_DIR']
MODEL_DIR = os.path.join(PROJECT_PATH, 'wavenet', 'logdir', 'train')

# logdir/train/2020-01-21T17-12-15/model.ckpt-33600

models = os.listdir(MODEL_DIR)
latest_model = max([os.path.join(MODEL_DIR, model) for model in models], key=os.path.getmtime)

checkpoints = os.listdir(latest_model)

for checkpoint in checkpoints:
    if checkpoint.endswith('.meta'):
        checkpoint_num = re.findall('-.*\.', checkpoint)[0][1:-1]
        checkpoint_name = checkpoint[:-5]
        os.system('cd wavenet && python generate.py  --samples 80000 ' + latest_model + '/' + checkpoint_name + ' --wav_out_path ' + '../output/' + checkpoint_num + '.wav')
