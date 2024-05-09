#csv reader / dict reader
#standardize or canoicalize the data
# name = input("Your name is: ").strip()

# if "," in name:
#   last, first = name.split(", ") # throw error if no space after comma
#   name = f"{first} {last}"

# print(f"Hello, {name}")

"""
import re

name = input("Your name is: ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# matches = re.search(r"^(.+), ?(.+)$", name)
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
  # 0 index holds different value for re
  name = matches.group(2) + " " + matches.group(1)
  # last, first = matches.groups()
  # name = f"{first} {last}"

print(f"Hello, {name}")
"""


import re

name = input("Your name is: ").strip()

# Assignment expression operator AKA <walrus operator>
#The walrus operator < := > allows you to assign a value to a variable as part of an expression. This can be helpful in situations where you want to assign a value to a variable and use that value in the expression at the same time.
if matches := re.search(r"^(.+), *(.+)$", name):
  name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
