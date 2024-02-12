from moviepy.editor import VideoFileClip
import os

# Directory containing the MP4 files
video_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/IDY Upa Yoga Videos/Guided Videos'
# Directory where you want to save the MP3 files
audio_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/IDY Upa Yoga Videos/Audio Files'

# Ensure the audio directory exists
os.makedirs(audio_dir, exist_ok=True)

# Loop through all MP4 files in the video directory
for video_file in os.listdir(video_dir):
    if video_file.endswith(".mp4"):
        # Construct the full path to the video file
        video_path = os.path.join(video_dir, video_file)
        # Construct the path for the output MP3 file
        audio_path = os.path.join(audio_dir, video_file.replace(".mp4", ".mp3"))
        
        # Load the video file
        video_clip = VideoFileClip(video_path)
        # Extract the audio
        audio_clip = video_clip.audio
        # Save the audio clip as an MP3 file
        audio_clip.write_audiofile(audio_path)
        
        # Close the clips to release resources
        audio_clip.close()
        video_clip.close()

print("Audio extraction completed.")
