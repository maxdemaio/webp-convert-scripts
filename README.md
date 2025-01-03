# webp-convert-scripts

This repository contains 3 scripts:

1. `webp-convert.py`
  - This script can be run like `python3 convert.py <directory>` and it will take all the png/jpg files and then convert them to webp. The original files will be kept.
2. `find-replace.py`
  - This script can be run like `python3 replace_references.py <image_directory> <codebase_directory>`. This will take all the png/jpg images in `<image directory>` and update their references in `<codebase_directory>`. Make sure to set the `PREFIX` variable as needed and then the file endings array.
3. `delete-files.py`
  - This script can be run like `python3 script.py <directory_path>`. The previous script will output all the png/jpg filenames. This will only delete the given filenames in the hardcoded array from the specified directory path.