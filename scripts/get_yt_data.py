from pytube import YouTube

video = YouTube('https://www.youtube.com/watch?v=58A-TI3AsV8')
stream = video.streams.filter(only_audio=True).all()
stream[0].download("./")
