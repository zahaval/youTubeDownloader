import yt_dlp
from pytube import YouTube
from sys import argv
import requests
import json
import os


def is_creative_commons(video):
    video_id = video.video_id
    print(f"Checking license for video ID: {video_id}")
    api_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=status&key=YOUR_API_KEY"
    response = requests.get(api_url)
    data = response.json()
    if "items" in data and data["items"]:
            for item in data['items']:
                if item["status"]["license"] == "creativeCommon":
                    return True
    return False


def download_video(link):
    yt = YouTube(link)
    print("Checking video license...")
    if is_creative_commons(yt):
        print("Video is Creative Commons licensed. Proceeding with download...")
        ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s')
    }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print(f"Video downloaded!")
    else:
        print("This video is not under a Creative Commons license. Download aborted.")

if __name__ == "__main__":
    if len(argv) > 1:
        link = argv[1]
        download_video(link)
    else:
        print("Please provide a video link.")
