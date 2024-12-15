import cv2
import os
import argparse
import time

# Set up the argument parser
parser = argparse.ArgumentParser(description="Extract frames from a video file.")
parser.add_argument("video_file", type=str, help="Path to the video file")
parser.add_argument("--output_folder", type=str, default="frames", help="Folder to save extracted frames")
args = parser.parse_args()

# Assign command-line arguments to variables
video_path = args.video_file
frames_folder = args.output_folder

# Create the frames folder if it doesn't exist
if not os.path.exists(frames_folder):
    os.makedirs(frames_folder)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

# Get the frame rate of the video (frames per second)
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the interval in frames for capturing four frames per second
frame_interval = fps // 6

frame_count = 0

# Loop through the video and capture frames at regular intervals
while True:
    ret, frame = cap.read()

    # If no frame is returned, the video has ended
    if not ret:
        break

    # Save a frame at every quarter-second interval
    if frame_count % frame_interval == 0:
        # Get the current time in milliseconds
        millis = int(time.time() * 1000)
        frame_name = os.path.join(frames_folder, f'frame_{millis}.jpg')
        cv2.imwrite(frame_name, frame)
        print(f'Saved {frame_name}')

    frame_count += 1

# Release the video capture object
cap.release()
print(f'All frames saved in {frames_folder}.')