import os
import sys
import re
from collections import defaultdict

# Hardcoded prefix for image path matching
PREFIX = "images/blog/"

def replace_image_references(image_dir, codebase_dir):
    # Create a list of all .png and .jpg files in the image directory
    images = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg'))]
    updated_files = defaultdict(list)

    # Walk through all files in the codebase directory
    for root, _, files in os.walk(codebase_dir):
        for file in files:
            # Process files with relevant extensions
            if file.endswith(('.html', '.css', '.js', '.jsx', '.ts', '.tsx', '.md', '.mdoc', '.astro')):
                file_path = os.path.join(root, file)
                
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                updated_content = content

                # Replace references to .png/.jpg with .webp
                for image in images:
                    base_name = os.path.splitext(image)[0]
                    image_path = f"{PREFIX}{image}"
                    if re.search(rf'{re.escape(image_path)}', content):
                        updated_content = re.sub(rf'{re.escape(image_path)}', f'{PREFIX}{base_name}.webp', updated_content)
                        updated_files[image].append(file)

                # Write back to the file if changes were made
                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

    # Print the summary of changes
    total_files_updated = 0
    files_updated_set = set()
    images_updated_set = set()

    for image, files in updated_files.items():
        print(f"{image} updated in: {', '.join(files)}")
        total_files_updated += len(files)
        files_updated_set.update(files)
        images_updated_set.add(image)

    # Display the total count of updated files and images
    total_images_updated = len(images_updated_set)
    print(f"\nTotal files updated: {total_files_updated}")
    print(f"Total images updated: {total_images_updated}/{len(images)}")
    print(f"Files updated: {', '.join(files_updated_set)}")
    print("Images updated", images_updated_set)

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python replace_references.py <image_directory> <codebase_directory>")
    else:
        image_directory = sys.argv[1]
        codebase_directory = sys.argv[2]
        replace_image_references(image_directory, codebase_directory)
