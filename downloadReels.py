# Constants
START_VIDEO = 1
END_VIDEO = 715

import json
import os
import re
import requests

import os

def validFileName(filename, savePath, maxLength=255):
    """Truncate and clean the filename to make it valid, considering the save path."""
    # Clean the filename
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    # Calculate max filename length allowed (considering save path length)
    maxFilenameLength = maxLength - len(savePath) - len(os.sep) - len('.mp4')  # accounting for separators and extension
    return filename[:max(maxFilenameLength, 1)]  # Ensure we don't end up with a zero-length filename

def downloadVideo(url, filename, savePath):
    """Download the video from the URL and save it to the specified path."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(savePath, filename), 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

def processVideos(jsonFile, savePath, startVideo=START_VIDEO, endVideo=END_VIDEO):
    """Process videos in the specified range in the JSON file."""
    with open(jsonFile, 'r') as file:
        videos = json.load(file)

    # Adjust indices to be zero-based
    startVideo -= 1
    endVideo = min(endVideo, len(videos))

    for video in videos[startVideo:endVideo]:
        videoUrl = video.get('videoUrl')
        caption = video.get('caption', 'Untitled')
        filename = validFileName(caption, savePath) + '.mp4'  # Pass savePath to validFileName

        print(f'Downloading: {filename}')
        downloadVideo(videoUrl, filename, savePath)
        print(f'Saved: {filename}')

# Example usage
jsonFilePath = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/missingVideos.json'  # Replace with your JSON file path
saveDirectory = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/sadhguruReels'  # Replace with your desired save directory

# Ensure the save directory exists
os.makedirs(saveDirectory, exist_ok=True)

processVideos(jsonFilePath, saveDirectory, startVideo=START_VIDEO, endVideo=END_VIDEO)
