from pytube import YouTube
from sys import argv

link = argv(range(1))
yt = YouTube(link)

print("Title",yt.title)
print("View:",yt.views)

yd = yt.streams.get_highest_resolution()

# yd.download('https://www.youtube.com/watch?v=HRnX0iljCBU')
yd.download('D:\youtube downloader')