from __future__ import unicode_literals
from main import *
from PIL import Image
from urllib.request import urlretrieve
import pytube
from pytube import YouTube as yt
import youtube_dl
import requests
from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool
from pprint import pprint
import os
import json
try:

    from StringIO import StringIO

except ImportError:

    from io import StringIO


class VideoDownloader(QObject):

    def __init__(self, parent=None):
        self.progressChanged = pyqtSignal(int)
        super(VideoDownloader,self).__init__(parent)

   
    def my_hook(self, d):
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Done downloading {}".format(file_tuple[1]))
        if d['status'] == 'downloading':
            p = d['_percent_str'][:3]
            self.progressChanged.emit(int(p))

    def download(self, vid):
        ydl_opts = {
            'format': '136',
            'progress_hooks': [self.my_hook],
        }

        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download([vid])

class postProcessor(QObject):
    
    def __init__(self, url, parent=None):
        self.Time = pyqtSignal(str)
        self.Title = pyqtSignal(str)
        self.Size = pyqtSignal(str)
        self.choice = '136'
        self.ydl_opts = {'format': self.choice}
        self.url = url
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            meta = ydl.extract_info(
                self.url, download=False)
        self.thumbnail_url = meta['thumbnail']
        self.length = meta['duration']
        self.size = meta['filesize']
        self.title = meta['title']
        super(postProcessor,self).__init__(parent)


    def video_title(self):
        Title.emit(self.title)

    def video_time(self):
        seconds = self.length % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        time = "%d:%02d:%02d" % (hour, minutes, seconds)
        Time.emit(time)

    def formated_size(self):

        try:
            size = self.size
            power = 2**10
            n = 0
            power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
            while size > power:
                size /= power
                n += 1
            size = f"{round(size,2)}{power_labels[n]}B"
            Size.emit(size)
        except TypeError:
            return "0"

    def image_display(self):
        image = self.thumbnail_url
        image_name = image.split("/")
        image_name = image_name[4]
        image_name = f"video_thumbnails/{image_name}"
        im = Image.open(requests.get(image, stream=True).raw)
        size = 500, 300
        im.thumbnail(size)
        im.save(image_name + ".jpg")
        print(image_name)
        return image_name
