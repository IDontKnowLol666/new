import requests
public_url = "https://storage.googleapis.com/objectron"
blob_path = public_url + "/v1/index/cup_annotations_test"
video_ids = requests.get(blob_path).text
video_ids = video_ids.split('\n')
# Download the first ten videos in cup test dataset
for i in range(1):
    video_filename = public_url + "/videos/" + video_ids[i] + "/video.MOV"
    metadata_filename = public_url + "/videos/" + video_ids[i] + "/geometry.pbdata"
    annotation_filename = public_url + "/annotations/" + video_ids[i] + ".pbdata"
    # video.content contains the video file.
    video = requests.get(video_filename)
    metadata = requests.get(metadata_filename)
    annotation = requests.get(annotation_filename)
    file = open("video1.MOV", "wb")
    file.write(video.content)
    file.close()
from IPython.display import HTML
from base64 import b64encode
mp4 = open('/content/video1.MOV','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=400 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)
objectron_buckett = 'gs://objectron'
# Importing the necessary modules. We will run this notebook locally.

import tensorflow as tf
import glob
from IPython.core.display import display, HTML
import matplotlib.pyplot as plt
import os
import numpy as np
import tensorflow as tf
import cv2
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from objectron.schema import features
from objectron.dataset import box
from objectron.dataset import graphics
