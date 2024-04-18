# The Metagram

## Overview
The Metagram is a comprehensive toolset designed to ethically scrape content from Instagram profiles without requiring users to log in with their Instagram accounts. This approach minimises the risk of account closures or bans, offering a safer alternative for data collection and analysis. Utilising the Instagram Graph API, The Metagram extracts metadata from user profiles, downloads Reels in lossless MP4 format, and performs several utility functions to manage and analyse the collected data.

## Features
- **instaScrape.py**: Main script for scraping Instagram profile metadata using the Instagram Graph API, storing results in a JSON array.
- **downloadReels.py**: Downloads Instagram Reels as lossless MP4 files, using URLs from the instaScrape.py output. Video names are set to the original Reels' captions.
- **countReels.py**: Counts the number of Reels listed in the JSON file.
- **missingVideos.py**: Checks for missing videos by comparing downloaded video names with JSON file entries.
- **orientation.py**: Determines whether a video is in landscape or portrait format, categorising it accordingly.
- **mp4Tomp3.py**: Converts MP4 videos to MP3 audio format, aiding in transcript creation by reducing file size.

Additionally, this repository includes a 'Reels' folder containing example JSON and CSV metadata files for approximately 700 Instagram Reels from a user's account.

## Installation
To use The Metagram, start by cloning the repository:
```bash
git clone https://github.com/harrylmoss/The-Metagram.git
cd The-Metagram
```
## Usage
Replace the file paths within each Python script to match your environment. Here's a brief overview of how to run the main scripts:

1. Metadata Scraping:
```bash
python instaScrape.py
```
2. Download Reels:
```bash
python downloadReels.py
```
3. Count Reels:
```bash
python countReels.py
```

Note: The links to Instagram Reels in the JSON file expire after approximately 2 days. Run instaScrape.py again to refresh the data.

## Contributing
Contributions to improve Bhairagini AI are welcome. Please follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Acknowledgements
Thanks to the Python community for providing extensive resources and libraries that support projects like this, along with the Instagram Graph API for enabling access to Instagram profile data.

## Contact
For any inquiries or collaboration requests, please contact me at harrymoss33@gmail.com.

Other AI/Digital Signal Processing projects can be found on my [GitHub Profile](https://github.com/HarryLMoss)

---

© 2024 Harry Moss. All Rights Reserved.
