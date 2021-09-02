from pytube import YouTube
import glob
import sys
import pytube
sys.path.append("./")
from src.constexpr import *

def download(download_link, file_format):
    youtube = YouTube(download_link)
    if file_format is AUDIO_FORMAT:
        video = youtube.streams.get_audio_only()
        video.download('./Downloads/Audios', None, file_format)
    elif file_format is VIDEO_FORMAT:
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        video.download('./Downloads/Videos', None, file_format)