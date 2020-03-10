import os

from pytube import YouTube
from pytube import Playlist

from pydub import AudioSegment
from pydub.utils import make_chunks

from google.cloud import storage

CHUNK_LENGTH = 30000
START_AT = 1

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )



chunk_counter = 1
song_counter = 1

print("Downloading Playlist URLS...")
playlist = Playlist('https://www.youtube.com/playlist?list=PLBLYNxXZgsSOrrEOvajd9JdpJELCIo7R2')
playlist.populate_video_urls()
print("Download Complete.")
print("Downloading Videos")

print(playlist.video_urls)

for i, video_url in enumerate(playlist.video_urls):
    if i < START_AT - 1:
        continue
    print(f"Downloading {i+1}/{len(playlist.video_urls)}...")
    video = YouTube(video_url)
    print(video)
    stream = video.streams.filter(only_audio=True).all()
    print(stream[0])
    stream[0].download("./", filename='temp')
    print("Download complete.")

    audo_segment = AudioSegment.from_file("temp.mp4")
    chunks = make_chunks(audo_segment, CHUNK_LENGTH)

    print("Uploading clips to Google Cloud")
    for chunk in list(chunks)[:-1]:
        chunk_name = f"{chunk_counter}.wav"
        print(f"exporting  {chunk_name}")
        chunk.export('../data/' + chunk_name, format="wav")
        chunk_counter += 1
