import re

"""
	Keep only alphanumeric characters and spaces.
	Convert to lowercase.
	Replace all spaces with underscores.
"""


def sanitize_name(name):
  name = name.strip().lower()
  name = re.sub(r"[^a-zA-Z0-9\s]", "", name)
  name = re.sub(r"\s", "_", name)





  return name


if __name__ == "__main__":
  print(sanitize_name("hello1 2!@#!@3"))
