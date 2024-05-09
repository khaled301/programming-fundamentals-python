import re

email = input("What's your email?").strip()

regex_input = re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE)

if regex_input:
    print("Valid email")
else:
    print(f"Invalid email")

##-----------------------------------------
text = "apple orange banana"
pattern = r"\b(?:mango|orange)\b (\w+)"  # Match "apple" or "orange" followed by a space and capture the next word
matches = re.findall(pattern, text)
for match in matches:
    print(match)

