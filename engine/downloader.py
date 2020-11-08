from __future__ import unicode_literals
import pytube
from pytube import YouTube as yt
from main import *
from PIL import Image
from urllib.request import urlretrieve
import youtube_dl
import requests
try:

   from StringIO import StringIO

except ImportError:

   from io import StringIO






def File_name(url):
    link = yt(url)
    title, thumbnail_url, length = link.title, link.thumbnail_url, link.length
    return  link, title, thumbnail_url, length

def convert(seconds): 
    seconds = File_name(seconds)[3] % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    time  = "%d:%02d:%02d" % (hour, minutes, seconds)
    return str(time) 

def image_display(image):
    image = File_name(image)[2]
    image_name = image.split("/")
    image_name = image_name[4]
    image_name = f"video_thumbnails/{image_name}"
    im = Image.open(requests.get(image, stream=True).raw)
    size = 500, 300
    im.thumbnail(size)
    im.save(image_name + ".jpg")
    print(image_name)
    return image_name

def Filesize(size):
    link = File_name(size)[0]
    filtered_link = link.streams.filter(progressive = True).first()
    filtered_link = filtered_link.filesize
    return filtered_link

def format_bytes(size):
    size = Filesize(size)
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    size = f"{round(size,2)}{power_labels[n]}B"
    return str(size)

def File_quality(url):
    video_format = []
    link = File_name(url)[0]
    filtered_link = link.streams.filter(progressive = True)
    for arrt in filtered_link:
        res = str(getattr(arrt,'resolution')) 
        mime_type = str(getattr(arrt,'mime_type'))
        mime_type = mime_type.split("/")
        mime_type = mime_type[1]
        v_formart = mime_type.upper() + "  " + res
        video_format.append(v_formart)
    print(video_format)
    return video_format


def File_nam(url):
    try:
        link = yt(url)
        title, thumbnail_url, video_length = link.title, link.thumbnail_url, link.length
        filtered_link = link.streams.filter(progressive = True)
        for arrt in filtered_link:
            res = getattr(arrt,'resolution') 
            mime_type = getattr(arrt,'mime_type')
            print(res,mime_type)
        print(title,thumbnail_url,video_length)
    except TypeError:
        link = yt(url)
        title, thumbnail_url, video_length = link.title, link.thumbnail_url, link.length
        filtered_link = link.streams.filter(progressive = True)
        resolution, video_format = getattr(filtered_link,'resolution'),getattr(filtered_link,'mime_type')
        print(title,thumbnail_url,video_length,video_format,resolution)



def Engine(url,quality):
    stream = Quality_select(url,quality)
    downloader = stream.download()
    return downloader


def my_hook(d):
    if d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        print("Done downloading {}".format(file_tuple[1]))
    if d['status'] == 'downloading':
        num = d['_percent_str'][:4]
        return num
def download_clip(url):
    ydl_opts = {
        'format': '136',
        'noplaylist': True,
        'continue_dl': True,
        'progress_hooks': [my_hook],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            ydl.prepare_filename(info_dict)
            ydl.download([url])
            return int(my_hook())
    except Exception:
        return False 
#File_quality("https://www.youtube.com/watch?v=wJHY-xkURvg")

#print(format_bytes("https://www.youtube.com/watch?v=u1BvQylSIo8"))

#print(convert("https://www.youtube.com/watch?v=u1BvQylSIo8"))

#File_name("https://www.youtube.com/watch?v=D0iCHFXHb_g&t=256s")[2]
#format_bytes("https://www.youtube.com/watch?v=dRRpbDFnMHI")
#image_display("https://www.youtube.com/watch?v=dRRpbDFnMHI")


