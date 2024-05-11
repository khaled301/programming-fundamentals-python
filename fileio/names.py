# name = input("Enter a name: ").strip().title()

# with open("names.txt", "a") as file:
  # file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#   for line in file:
#     print("hello", line.rstrip())


# if we want read the file then it's not mandatory to use the "r" flag
#sorted
names = []
# with open("names.txt") as file:
#   for line in sorted(file):
#     print(f"hello {line.rstrip()}")

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())
    
for name in sorted(names, reverse=True):
  print(f"hello {name}")

