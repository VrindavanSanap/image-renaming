#!/usr/bin/env python3
# Created by Vrindavan Sanap
# smart_rename_images.py
# This program lets people rename images in a particular folder
# ALl rights reserved
#

import glob
import os
import re

from image_to_text import image_to_text
from string_utilities import sanitize_name
from tqdm import tqdm

PROMPT = "Generate a short, descriptive title for this image, ideally no more than 5 words, as if written by an Apple copywriter."


def smart_rename_image(img_loc, prompt=PROMPT):
  """
  Renames an image file based on its content. This function takes an image location and an optional prompt as input.
  It uses the image_to_text function to generate a new name for the image based on its content and the provided prompt.
  The new name is then sanitized to ensure it is a valid filename. The image is renamed inplace.

  Parameters:
  img_loc (str): The location of the image file to be renamed.
  prompt (str): An optional prompt to guide the generation of the new name. Defaults to PROMPT.
  """
  new_name = image_to_text(img_loc, prompt=PROMPT)
  file_extension = os.path.splitext(img_loc)[1]
  new_name = f"{sanitize_name(new_name)}{file_extension}"
  os.rename(img_loc, os.path.join(os.path.dirname(img_loc), new_name))


def smart_rename_folder(folder_loc):
  """
  Renames all image files in a given folder based on their content. This function iterates over all files in the specified folder,
  filters out non-image files, and attempts to rename each image file using the smart_rename_image function. If an error occurs during
  the renaming process, it prints an error message.

  Parameters:
  folder_loc (str): The location of the folder containing the images to be renamed.
  """
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
