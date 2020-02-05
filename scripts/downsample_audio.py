import os
from librosa.core import load
from librosa.output import write_wav

DATA_DIR = '../data'
source_files = os.listdir(os.path.join(DATA_DIR))

print("Downsampling Audio Files in Data Directory...")

for idx, file in enumerate(source_files):
    if file.endswith('.wav'):
        print(f"Downsampling file {idx+1}/{len(source_files)}")
        y, _ = load(os.path.join(DATA_DIR, file), sr=16000)
        write_wav(os.path.join(DATA_DIR, file), y, 16000)