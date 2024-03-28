import os
import shutil

# Define the source directory (Downloads folder)
downloads_dir = os.path.expanduser("~/Downloads")

# Define destination directories for different file types on desktop
desktop_dir = os.path.expanduser("~/Desktop")
image_dir = os.path.join(desktop_dir, "myPictures")
document_dir = os.path.join(desktop_dir, "myDocuments")
video_dir = os.path.join(desktop_dir, "myVideos")
audio_dir = os.path.join(desktop_dir, "myMusic")
other_dir = os.path.join(desktop_dir, "myOther")

# List of file extensions for each category
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
document_extensions = [".txt", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"]
video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"]
audio_extensions = [".mp3", ".wav", ".ogg", ".flac", ".aac"]

# Create destination directories if they don't exist
for directory in [image_dir, document_dir, video_dir, audio_dir, other_dir]:
    os.makedirs(directory, exist_ok=True)

# Function to categorize files based on extension and move them
def organize_files():
    files = os.listdir(downloads_dir)
    for file in files:
        if os.path.isfile(os.path.join(downloads_dir, file)):
            extension = os.path.splitext(file)[1].lower()

            if extension in image_extensions:
                shutil.move(os.path.join(downloads_dir, file), image_dir)
                print(f"Moved {file} to {image_dir}")
            elif extension in document_extensions:
                shutil.move(os.path.join(downloads_dir, file), document_dir)
                print(f"Moved {file} to {document_dir}")
            elif extension in video_extensions:
                shutil.move(os.path.join(downloads_dir, file), video_dir)
                print(f"Moved {file} to {video_dir}")
            elif extension in audio_extensions:
                shutil.move(os.path.join(downloads_dir, file), audio_dir)
                print(f"Moved {file} to {audio_dir}")
            else:
                shutil.move(os.path.join(downloads_dir, file), other_dir)
                print(f"Moved {file} to {other_dir}")

if __name__ == "__main__":
    organize_files()
