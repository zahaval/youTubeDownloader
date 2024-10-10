# YouTube Video Downloader (Creative Commons Checker)

This Python project allows you to download YouTube videos that are licensed under Creative Commons. 
It uses the YouTube Data API to check if a video has a Creative Commons license, and if so, it downloads the video using `yt-dlp`. 
If the video is not under a Creative Commons license, the download is aborted to comply with YouTube's copyright policies.


## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.x**: This project requires Python 3.x.
- **yt-dlp**: For downloading the videos. Install via pip:

    ```bash
    pip install yt-dlp
    ```

- **pytube**: Used to extract video ID from a YouTube link. Install via pip:

    ```bash
    pip install pytube
    ```

- **YouTube Data API v3 Key**: You'll need a valid YouTube Data API key to check video licenses. You can get this by creating a project on Google Cloud and enabling the YouTube Data API v3.

## Setup

1. Clone the repository or copy the Python script into your environment.
   
2. Install the required packages:

    ```bash
    pip install yt-dlp pytube requests
    ```

3. Get a YouTube Data API Key:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the YouTube Data API v3.
   - Generate an API key and replace `YOUR_API_KEY` in the script with your actual key.

4. Set Output Directory: The downloaded videos will be saved to the directory specified in the `ydl_opts` in the script. You can modify this path to your desired directory.

## How to Run

To use this script:

1. Open a terminal or command prompt.
2. Run the Python script with the YouTube video link as an argument:

    ```bash
    python download_video.py "<YouTube video link>"
    ```

   
