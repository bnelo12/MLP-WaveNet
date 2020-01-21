source ~/miniconda3/etc/profile.d/conda.sh
conda activate mlp_proj
export GOOGLE_APPLICATION_CREDENTIALS=/afs/inf.ed.ac.uk/user/s16/s1623919/Documents/Inf4/ClaireNet/credentials.json
python scrape_data.py
