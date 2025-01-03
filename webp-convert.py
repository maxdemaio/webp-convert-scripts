import os
import sys
import subprocess


def convert_images_to_webp(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Process only .png and .jpg files
        if filename.endswith(('.png', '.jpg')):
            image_path = os.path.join(directory, filename)
            webp_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.webp")
            
            # Run cwebp command
            command = [
                'cwebp',
                image_path,
                '-q', '80',
                '-o', webp_path
            ]
            
            try:
                subprocess.run(command, check=True)
                print(f"Converted: {image_path} -> {webp_path}")
            except subprocess.CalledProcessError:
                print(f"Failed to convert {image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <directory>")
    else:
        convert_images_to_webp(sys.argv[1])

# Get all unique file types in a directory:
# `find . -type f -name '*.*' | sed 's|.*\.||' | sort -u``

# Get file size of directory:
# Use `du -sk`` to show the size in kilobytes (default is to show number of 512-byte blocks), 
# or `du -sh`` for a more human-friendly output. For more options, type man du.