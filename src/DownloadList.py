from pytube import YouTube

class DownloadList:
    def __init__(self, link_list):
        self.link_list = link_list
        self.link_index = 0
        self.video_titles = []
   
    def add_to_list(self, link):
        append_item = str(self.link_index) + "." + link
        self.link_list.append(append_item)
        self.link_index += 1
        video_title = YouTube(link).title
        self.video_titles.append(video_title)
    
    def remove_index(self, index):
        self.link_list.pop(index)
    
    def show_list(self):
        print(self.video_titles)



    