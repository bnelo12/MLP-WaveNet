# Data Folder
Here you can use rsync to sync data from Google cloud to the data directory.

# Prerequisites

Download and install Google Cloud SDK by running:

`curl https://sdk.cloud.google.com | bash`

After installation run `gsinit` to finish the setup.

Then you can use rsync to sync the data directory with this folder:

`gsutil rsync gs://ml_proj ./`


