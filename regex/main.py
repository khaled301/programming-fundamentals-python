
# . => any character except a new line
# * => 0 or more occurences
# + => 1 or more occurences
# ? => 0 or 1 occurence
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

# (?P<first>\w+): This part creates a named capturing group with the name "first". It captures one or more word characters (letters, digits, or underscores) and assigns them to the "first" group.

# (?P=first): This part matches the named capturing group "first" in the replacement string.

# if re.search(".*@.*", email):
# start =====> (q1).repeat ===== @ =====> ((q2)).repeat

# if re.search(".+@.+", email):
# start => (q1).repeat = <.> => (q2).repeat = <@> => (q3) = <.> => ((q2)).repeat

# (r".+@.+\.edu") | here <r> means RAW string



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

# if re.search("..*@..*", email):
#   print("Valid email")

if re.search(r".+@.+\.edu", email):
    print("Valid email")
else:
    print(f"Invalid email")

