# Author: Harry Moss
# Date: 11 February, 2024

import json
import csv

# Path to JSON file
jsonFilePath = 'PATH_TO_JSON'

# Path to saving the CSV file
csvFilePath = 'PATH_TO_OUTPUT_CSV'

# Open the JSON file and load its content
with open(jsonFilePath, 'r') as json_file:
    data = json.load(json_file)

# Open the CSV file for writing
with open(csvFilePath, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Publish Date', 'Likes Count', 'Comments Count', 'Video URL', 'Video View Count', 'Short Code', 'Caption'])

    # Write the data rows
    for item in data:
        csv_writer.writerow([
            item['publishDate'],
            item['likesCount'],
            item['commentsCount'],
            item['videoUrl'],
            item['videoViewCount'],
            item['shortCode'],
            item.get('caption', '')  # Add the caption, default to empty string if not present
        ])
