import re

##---------------re.search => group--------------------------
# username = input("Enter your username: ").strip()
# match = re.search(r"^https:\/\/twitter.com\/([a-zA-Z0-9_]{3,20})$", username)
# if match:
#   print(f"Username {match.group(1)}")

##---------------replace--------------------------
# url = input("Enter your username: ").strip()
# username = url.replace("https://twitter.com/", "")
# print(f"Username {username}")

##-----------------removeprefix------------------------
# url = input("Enter your username: ").strip()
# username = url.removeprefix("https://twitter.com/")
# print(f"Username {username}")

##---------------re.sub(pattern, repl, string, count=0, flags=0) | to clean up data --------------------------
# url = input("Enter your username: ").strip()
# username = re.sub(r"^(\w *)*(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username {username}")

##---------------re.search | capturing | (...) --------------------------
# url = input("Enter your username: ").strip()
# # mind the paranthese as we are using re.search(), so it will be consider as group() as well
# if username := re.search(r"^.*(https?://)?(www\.)?twitter\.com/(\w{3,20})/?.*$", url, re.IGNORECASE):
#   print(f"Your twitter username is ({username.group(3)})")

##---------------re.search | non-capturing | (?:...) --------------------------
url = input("Enter your username: ").strip()
# mind the paranthese as we are using re.search(), so it will be consider as group() as well
if username := re.search(r"^.*(?:https?://)?(?:www\.)?twitter\.com/(\w{3,20})/?.*$", url, re.IGNORECASE):
  print(f"Your twitter username is ({username.group(1)})")


## ------------------------ other examples of re --------------------------
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, text)

## starts matching from begining from string and don't need the carret symbol at the begining
# re.match(pattern, string, flags=0)

## exact match | start and begining
# re.fullmatch(pattern, string, flags=0)

