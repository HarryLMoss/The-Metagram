# Author: Harry Moss
# Date: 11 February, 2024

import json

# Path to the JSON file
jsonFilePath = 'YOUR_JSON_PATH'

# Function to count the number of reels in the JSON file
def countReelsInJson(file_path):
    # Open and load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Assuming the JSON structure is a list of reels
    # The length of the list gives you the total number of reels
    totalReels = len(data)
    
    return totalReels

# Call the function and print the total number of reels
totalReels = countReelsInJson(jsonFilePath)
print(f"Total number of reels: {totalReels}")
