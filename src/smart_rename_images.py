#!/usr/bin/env python3
# Created by Vrindavan Sanap
# smart_rename_images.py 
# This program lets people rename images in a particular folder
# ALl rights reserved
#

import glob
import os
import re

from tqdm import tqdm

from image_to_text import image_to_text
from string_utilities import sanitize_name

PROMPT = "Generate a short, descriptive title for this image, ideally no more than 5 words, as if written by an Apple copywriter."
def smart_rename_image(img_loc, prompt=PROMPT):
  new_name = image_to_text(img_loc, prompt=PROMPT)
  file_extension = os.path.splitext(img_loc)[1]
  new_name = f"{sanitize_name(new_name)}{file_extension}"
  os.rename(img_loc, os.path.join(os.path.dirname(img_loc), new_name))


def smart_rename_folder(folder_loc):
  images_locations = [os.path.join(folder_loc, f) for f in os.listdir(folder_loc) if f.endswith((".jpeg", ".jpg", ".png", ".webp"))]
  images_locations.sort()
  for img_loc in images_locations:
    try:
      smart_rename_image(img_loc)
    except Exception as e:
      print(f"Error getting file name for {img_loc}: {str(e)}")
import sys

if __name__ == "__main__":
  if len(sys.argv) > 1:
    SOURCE_FOLDER = sys.argv[1]
    smart_rename_folder(SOURCE_FOLDER)
  else:
    print("Usage: ./smart_rename_images.py <folder_path>")
