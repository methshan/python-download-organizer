import os, shutil, time

src = r"C:\Users\meths\Downloads"

dest_map = {
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".pdf": "Documents",
    ".zip": "Archives",
    ".docx": "Documents",
    ".xlsx": "Excel Documents",   
    ".mp3": "Music",
    ".txt": "Documents",
    ".rar": "Archives",
    ".mkv": "Videos",
    ".gif": "Images",
    ".avi": "Videos",
    ".pptx": "Documents",
    ".wav": "Music",
    ".flac": "Music",
    ".mov": "Videos",
    ".exe": "Applications",
    ".bat": "Applications",
    ".iso": "Archives",
    ".csv": "Excel Documents",
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".doc": "Documents",
    ".rtf": "Documents",
    ".epub": "Documents",
    ".m4a": "Music",
    ".ogg": "Music",
    ".wmv": "Videos",
    ".swf": "Videos",
    ".psd": "Images",
    ".ai": "Images",
    ".svg": "Images",
    ".tiff": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".flv": "Videos",
    ".aac": "Music",
    ".aac": "Music",
    ".mov": "Videos",
    ".wma": "Music",
    ".aac": "Music",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".m4v": "Videos",
    ".aac": "Music",
    ".jfif": "Images",
    ".heic": "Images",
    ".avif": "Images",
    ".avi": "Videos",
    ".avif": "Images",
    ".heic": "Images",
    ".msix": "Applications",
    ".msi": "Applications",
    ".apk": "Applications",
    ".bat": "Applications",
    ".env": "Documents",
    ".enc": "Documents",
    ".docx": "Word Documents",


    
}

while True:
    for filename in os.listdir(src):
        ext = os.path.splitext(filename)[1].lower()
        if ext in dest_map:
            dest_dir = os.path.join(src, dest_map[ext])
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(os.path.join(src, filename), os.path.join(dest_dir, filename))
    time.sleep(10)  # check every 10 seconds
