# facial-recognition-attendance-system

This project is a real-time facial recognition-based attendance system built with Python, OpenCV, and the `face_recognition` library. It uses your webcam to detect and identify faces based on reference images, then logs attendance automatically.

## Features

- Load and encode faces from `.jpeg` photos stored in the `faces/` folder.
- Real-time face detection and recognition via webcam.
- Automatically logs attendance with timestamps in a CSV file named by the current date (e.g., `07-28-25.csv`).
- Displays the name of the recognized person on the video feed.
- Press **"q"** to exit the program gracefully.

## Usage

1. Add clear `.jpeg` photos of individuals you want to recognize to the `faces/` directory.
2. Make sure to update the script to load and encode these photos.
3. Run the script:
   ```bash
   python main.py