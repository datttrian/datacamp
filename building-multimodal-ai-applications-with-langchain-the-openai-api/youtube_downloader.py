# Importing the Required Packages including: "os" "openai" "yt_dlp as youtube_dl" and "from yt_dl import Download Error"

# Import the os package
import os

# Import the glob package
import glob

# Import the openai package
import openai

# Import the yt_dlp package as youtube_dl
import yt_dlp as youtube_dl

# Import DownloadError from yt_dlp
from yt_dlp import DownloadError

# Import DocArray
import docarray

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# An example YouTube tutorial video
youtube_url = "https://www.youtube.com/watch?v=aqzxYofJ_ck"
# Directory to store the downloaded video
output_dir = "files/audio/"

# Config for youtube-dl
ydl_config = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    "verbose": True
}

# Check if the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Print a message indicating which video is being downloaded

print(f"Downloading video from {youtube_url}")


# Attempt to download the video using the specified configuration
# If a DownloadError occurs, attempt to download the video again

try:
    with youtube_dl.YoutubeDL(ydl_config) as ydl:
        ydl.download([youtube_url])
except DownloadError:
    with youtube_dl.YoutubeDL(ydl_config) as ydl:
        ydl.download([youtube_url])
