#!/usr/bin/env python3

import glob
import os
import re

from tqdm import tqdm

from image_to_text import image_to_text
from string_utilities import sanitize_name

SOURCE_FOLDER = "/Users/vrindavan/Downloads/pngs/"
PROMPT = "Generate a short, descriptive title for this image, ideally no more than 5 words, as if written by an Apple copywriter."


def smart_rename_image(img_loc, prompt=PROMPT):
  new_name = image_to_text(img_loc, prompt=PROMPT)
  new_name = f"{sanitize_name(new_name)}.jpg"
  os.rename(img_loc, os.path.join(os.path.dirname(img_loc), new_name))


def smart_rename_folder(folder_loc):
  images_locations = [os.path.join(folder_loc, f) for f in os.listdir(folder_loc) if f.endswith((".jpeg", ".jpg", ".png"))]
  images_locations.sort()
  for img_loc in images_locations:
    try:
      smart_rename_image(img_loc)
    except Exception as e:
      print(f"Error getting file name for {img_loc}: {str(e)}")


if __name__ == "__main__":
  smart_rename_folder(SOURCE_FOLDER)
