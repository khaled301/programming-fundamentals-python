
# . => any character except a new line
# * => 0 or more occurences
# + => 1 or more occurences
# ? => 0 or 1 occurence aka Optional
# ^ => start of string
# $ => end of string
# \ => escape character
# [] : Matches any one of the characters in the brackets.
# [^] : Matches any character except the ones in the brackets.
# [abc] => any of the characters in the brackets
# [^abc] => any character except the ones in the brackets
# [a-z] => any character between a and z
# [a-z0-9] => any character between a and z or 0 to 9
# [a-z0-9_] => any character between a and z or 0 to 9 or _
# {m} => m repetitions
# {m,} => m or more repetitions
# {m,n} => m to n repetitions
# g => global search
# \g =>  \g notation is used in the replacement string to refer to these groups and swap them in the output.
# | : Matches either the expression before or after the pipe.
# i => ignore case
# \b : Matches a word boundary.
# \d : Matches any digit character [0-9].
# \D : Matches any non-digit character.
# \s : Matches any whitespace character.
# \S : Matches any non-whitespace character.
# \w : Matches any word character [a-zA-Z0-9_].
# \W : Matches any non-word character.
# (?=...) : Positive lookahead assertion.
# (?!...) : Negative lookahead assertion.
# r"..." : Raw string literal.
# (A|B): Matches either A or B.
# (...): Capture group.
# (?:...): Non-capturing group.

## ---------------------------------------------------------------------
# (?P<first>\w+): This part creates a named capturing group with the name "first". It captures one or more word characters (letters, digits, or underscores) and assigns them to the "first" group.

# (?P=first): This part matches the named capturing group "first" in the replacement string.


## finite state machine | nondeterministic finite automata
# read left to right | starts from start state

# if re.search(".*@.*", email):
# start =====> (q1).repeat ===== @ =====> ((q2)).repeat

# if re.search(".+@.+", email):
# start => (q1).repeat = <.> => (q2).repeat = <@> => (q3) = <.> => ((q2)).repeat

# (r".+@.+\.edu") | here <r> means RAW string

##----------------------------------------------------------------------
# we should use libraries 
##----------------------------------------------------------------------

# email = input("What's your email?").strip()

# new_email_split = email.split("@")
# username, domain = email.split("@")

# print(new_email_split)
# print(username, domain)

# if "@" not in email:
#   print("Invalid email")

# if username and "." in domain:
#   print("Valid email")

# if username and domain.endswith("edu"):
#   print(f"Email from education domain {domain}")


import re

email = input("What's your email?").strip()

# flags are configuration options (IGONORECASE, DOTALL, MULTILINE)
# re.search(pattern, string, flags=0)
##----------------------------------------

# if re.search("..*@..*", email):
#   print("Valid email")

# r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]\.[a-zA-Z0-9]+$"
# (r"^[^@]+@[^@]+\.[^@]+$")
# r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]\w+\.[a-zA-Z0-9-.]+$""

# space is not a word chars
# r"^\w+@\w+\.\w+$"
# r"^\w+@\w+\.\w+$"
# r"^(\w|\s)+@"
# regex_input = re.search(r"^.+@.+\.edu$", email)
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


#starts matching from begining from string and don't need the carret symbol at the begining
#re.match(pattern, string, flags=0)

# exact match | start and begining
# re.fullmatch(pattern, string, flags=0) 


# The regular expression pattern r"\b(?:apple|orange)\b (\w+)" uses a non-capturing group (?:apple|orange) to group the words "apple" or "orange" without capturing them as separate groups.
# The pattern then matches a word character (\w+) after the non-capturing group and captures this word into a group.
# The re.findall() function is used to find all matches of the pattern in the text.
# When you run this code with the provided text, it will match the word immediately following "apple" or "orange" in the text and print out the matches.

##---------------------------------------
