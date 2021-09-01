from pytube import YouTube

def download(download_link, file_format):
    YouTube(download_link).streams.first().download()
    yt_downloader = YouTube(download_link)
    yt_downloader.streams.filter(progressive=True, file_extension=file_format).order_by('resolution').asc().first().download()
    