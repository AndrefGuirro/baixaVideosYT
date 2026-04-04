import sys

from pytubefix import YouTube
from pytubefix.cli import on_progress

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "https://www.youtube.com/watch?v=-UEE9h9QqjM&t=7s"

yt = YouTube(url, on_progress_callback=on_progress)

print (f"Title: {yt.title}")
print (f"author: {yt.author}")

ys = yt.streams.get_highest_resolution()
ys.download()
