import json
import csv

# Path to your JSON file
jsonFilePath = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/missingVideos.json'

# Path where you want to save the CSV file
csvFilePath = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/Instagram Graph API/missingVideos.csv'

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
