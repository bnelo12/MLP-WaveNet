import os

from pydub import AudioSegment
from pydub.utils import make_chunks

from xml.dom import minidom

directory = os.fsencode("chords")

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    # get frame number and chord label from XML file
    xmldoc = minidom.parse("chords/" + filename)
    timeList = xmldoc.getElementsByTagName('timestamp')
    labelList = xmldoc.getElementsByTagName('label')

    times = []
    labels = []

    for time in timeList:
        milli_time = float(time.childNodes[0].nodeValue[:-1]) * 1000
        times.append(milli_time)

    for label in labelList:
        # remove slashes from file name
        label_val = label.childNodes[0].nodeValue
        label_val = label_val.replace("/","_")
        labels.append(label_val)

        # make chord directory if it does not exist
        os.makedirs("split/" + label_val, exist_ok=True)

    # split clip on
    clip_number = os.path.splitext(filename)[0]
    audio_segment = AudioSegment.from_file("data/" + clip_number + ".wav")

    times.append(len(audio_segment))

    for i in range(len(labels)):
        chord_segment = audio_segment[times[i] : times[i+1]]

        chord_segment.export("split/{0}/{1}_{2}.wav".format(labels[i], clip_number, i), format="wav")
