#!/usr/bin/env python3
# Created by Vrindavan Sanap
# image_to_text.py 
# This program is wrapper for cloudflare workers AI in python
# ALl rights reserved
#

import os
import time

import requests
from dotenv import load_dotenv

""
load_dotenv()
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
API_KEY = os.getenv("API_KEY")
API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


LLAVA_HF_MODEL = "@cf/llava-hf/llava-1.5-7b-hf"


def image_to_text(image_path: str, prompt: str = "Get kawaii description for this image", model=LLAVA_HF_MODEL) -> str:
  """
  Converts an image to a concise text description using the Cloudflare AI model.

  Args:
  image_path (str): The path to the image file.

  Returns:
  str: A concise text description of the image.
  """
  if not image_path:
    raise ValueError("Image to text conversion failed: No image path provided.")

  try:
    with open(image_path, "rb") as file:
      image_blob = file.read()
      image_array = list(image_blob)
  except FileNotFoundError:
    raise FileNotFoundError(f"Image to text conversion failed: File not found at {image_path}.")
  except Exception as e:
    raise Exception(f"Image to text conversion failed: {str(e)}")

  inputs = {"image": image_array, "prompt": prompt, "maxtoken": 2024}

  try:
    FULL_URL = f"{API_BASE_URL}{model}"
    resp = requests.post(FULL_URL, headers=HEADERS, json=inputs)
    resp.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
  except requests.exceptions.HTTPError as e:
    raise Exception(f"Image to text conversion failed: HTTP error occurred - {str(e)}")
  except Exception as e:
    raise Exception(f"Image to text conversion failed: {str(e)}")

  resp_json = resp.json()
  description = resp_json.get("result", {}).get("description", "")
  if description:
    return description  # Remove the first and last characters as per the original implementation
  else:
    raise Exception("Image to text conversion failed: Description not found in the response.")

