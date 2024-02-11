# Author: Harry Moss
# Date: 11 February, 2024

import json
import os

# File paths
jsonFilePath = 'YOUR_JSON_PATH'  
videosFolderPath = 'YOUR_VIDEO_FOLDER_PATH'  
outputJsonPath = 'YOUR_OUTPUT_PATH'

def cleanTextForFilename(text):
    """Adjust text to match filename conversion rules."""
    for char in ['\n', '\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        text = text.replace(char, '_')
    return text[:50].lower()

def loadAndProcessCaptions(jsonPath):
    """Load JSON data and prepare for comparison."""
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    # Process captions for comparison and keep original data
    processedData = [{'cleanedCaption': cleanTextForFilename(item['caption']), 'originalData': item} for item in data]
    return processedData

def listAndProcessVideoNames(folderPath):
    """List and process video file names."""
    videoNames = [cleanTextForFilename(os.path.splitext(file)[0]) for file in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, file))]
    return videoNames

def findMissingVideos(processedData, videoNames):
    """Find missing videos and return their original JSON data."""
    missingVideosData = [item['originalData'] for item in processedData if item['cleanedCaption'] not in videoNames]
    return missingVideosData

# Load and process the data
processedData = loadAndProcessCaptions(jsonFilePath)
processedVideoNames = listAndProcessVideoNames(videosFolderPath)

# Identify missing videos
missingVideosData = findMissingVideos(processedData, processedVideoNames)

# Write the missing videos data to a new JSON file
with open(outputJsonPath, 'w') as outputFile:
    json.dump(missingVideosData, outputFile, indent=4)

# Output the results
print(f"Total processed captions: {len(processedData)}")
print(f"Total video files: {len(processedVideoNames)}")
print(f"Missing videos identified: {len(missingVideosData)}")
