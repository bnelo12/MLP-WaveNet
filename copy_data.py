import os
import shutil

PROJECT_PATH = os.environ['PROJECT_PATH']
DATASET_DIR = os.environ['DATASET_DIR']

source_files = os.listdir(os.path.join(PROJECT_PATH, 'data/'))

for file in source_files:
    if file.endswith('.wav'):
        shutil.copy(os.path.join(PROJECT_PATH, 'data/', file), DATASET_DIR)
