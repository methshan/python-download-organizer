# Download Organizer App

A Python-based automation script that automatically organizes files in the Downloads folder into separate folders based on file type.

## Overview
This project monitors the Downloads folder and automatically sorts files into categorized folders such as Images, Videos, Documents, Music, Archives, and Applications.

I built this project as a practical way to improve my Python skills while solving a real personal productivity problem.

## Features
- Automatically scans the Downloads folder
- Detects file types based on file extension
- Creates folders automatically if they do not already exist
- Moves files into the correct category
- Runs continuously and checks for new files every 10 seconds

## Categories Included
The script currently organizes files into folders such as:
- Images
- Videos
- Documents
- Word Documents
- Excel Documents
- Music
- Archives
- Applications

## Technologies Used
- Python
- `os`
- `shutil`
- `time`

## How It Works
1. The script scans the Downloads folder
2. It checks each file extension
3. It matches the extension to a predefined category
4. It creates the destination folder if needed
5. It moves the file into the correct folder
6. It repeats this process every 10 seconds

## Example File Types Supported
- Images: `.jpg`, `.png`, `.gif`, `.svg`, `.bmp`, `.webp`, `.heic`, `.avif`
- Videos: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.mpeg`, `.m4v`
- Documents: `.pdf`, `.txt`, `.doc`, `.docx`, `.pptx`, `.rtf`, `.epub`
- Music: `.mp3`, `.wav`, `.flac`, `.m4a`, `.ogg`, `.aac`, `.wma`
- Archives: `.zip`, `.rar`, `.tar`, `.gz`, `.iso`
- Applications: `.exe`, `.bat`, `.msi`, `.msix`, `.apk`

## Why I Built This
I wanted to build something useful that solves a real everyday problem instead of only doing tutorial-based coding. This project helped me practice:
- Python scripting
- file handling
- automation logic
- folder and path management
- problem-solving through code

## Future Improvements
Possible future improvements include:
- Add a graphical user interface (GUI)
- Allow users to customize categories
- Add logging for moved files
- Improve duplicate file handling
- Make the source folder configurable

## How to Run
1. Install Python
2. Update the source folder path in the script
3. Run the script:

```bash
python organizer.py
```

## Note
This project was built as a personal learning and automation tool and may be expanded further in the future.
