# The-Metagram
This repository is a collection of Python scripts that together make 'The Metagram' - a project which allows a user to scrape content from a user's Instagram in an ethical manner without having to log in using their own Instagram account and potentially risking account closure/ban.

_An overview of the Python scripts are as follows:_
1. **instaScrape.py** - the main program which utlises the Instagram Graph API to scrape the metadata from a user's profile and store it in a JSON array in a path of one's own liking.
2. **downloadReels.py** - this program will download the videos in lossless mp4 format using the link provided by the output of the instaScrape.py JSON file. The video name will be the caption of the original Instagram Reel.
3. **countReels.py** - a simple means to count the number of reels in the JSON file.
4. **missingVideos.py** - this is a safety checking measure to tell whether or not there are missing videos by comparing the first 50 characters of the downloaded videos' name with the respective contents of the original JSON file.
5. **orientation.py** - a short program designed to check whether a video is landscape or portrait, thus categorising the video as either portrait, a reel, or landscape, which is the older IGTV format.

There is also a 'Reels' folder provided in this repository which contains example JSON and csv metadata files of approx. 700 Instagram Reels of a user's account. The code will work with this data, however please note that one will need to replace the file paths with the correct pathway within each Python program in order for them to work.

Also note that the link provided for each Instagram Reel in the JSON file will expire after approx. 2 days. After this date, instaScrape.py will need to be ran again in order to generate a fresh JSON file.
