# Author: Harry Moss
# Date: 11 February, 2024

import os
from moviepy.editor import VideoFileClip

def organiseVideosByOrientation(sourceFolder):
    # Paths for the destination folders
    portraitFolder = os.path.join(sourceFolder, "Portrait")
    landscapeFolder = os.path.join(sourceFolder, "Landscape")

    # Create destination folders if they don't exist
    if not os.path.exists(portraitFolder):
        os.makedirs(portraitFolder)
    if not os.path.exists(landscapeFolder):
        os.makedirs(landscapeFolder)

    # Iterate through all files in the source folder
    for file in os.listdir(sourceFolder):
        if file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Add any other video formats you need
            filePath = os.path.join(sourceFolder, file)
            try:
                with VideoFileClip(filePath) as video:
                    # Determine video orientation
                    if video.size[0] < video.size[1]:  # If width < height, it's portrait
                        destPath = os.path.join(portraitFolder, file)
                    else:
                        destPath = os.path.join(landscapeFolder, file)

                    # Move the video file to the appropriate folder
                    os.rename(filePath, destPath)
                    print(f"Moved {file} to {destPath}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Usage
sourceFolder = 'PATH_TO_SOURCE_FOLDER'
organiseVideosByOrientation(sourceFolder)
