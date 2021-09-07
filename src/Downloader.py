from pytube import YouTube
import glob
import sys
import pytube
sys.path.append("./")
from src.constexpr import *

class Downloader:
    def __init__(self):
        self.link_to_download_list = []
    
    def set_link_list(self, link_to_download_list):
        self.link_to_download_list = link_to_download_list

    def get_link_list(self):
        return self.link_to_download_list

    def download_single_audio(self, link):
        ytube = YouTube(link)
        audio = ytube.streams.get_audio_only()
        audio.download('./Downloads/Audios')
    
    def download_single_video(self, link):
        ytube = YouTube(link)
        video = ytube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        video.download('./Downloads/Videos')
    
    def download_all_audios(self):
        for link in self.link_to_download_list:
            self.download_single_audio(link)
            
    
    def download_all_videos(self):
        for link in self.link_to_download_list:
            self.download_single_video(link)
