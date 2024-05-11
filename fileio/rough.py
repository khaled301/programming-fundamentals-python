# if we do not want to use the variable of the loop then we can use underscore < _ >
names = []

for _ in range(3):
  names.append(input("What's your name? "))

for name in sorted(names):
  print(f"Hello {name}")

# everytime it will recreate with "w" when we use open
name = input("Enter a name: ").strip().title()
file = open("names.txt", "w")
file.write(name)
file.close()

name = input("Enter a name: ").strip().title()

# everytime it will append with "a" when we use open
file = open("names.txt", "a")
# file.write(name)
file.write(f"{name}\n")
file.close()

# name = input("Enter a name: ").strip().title()

# with open("names.txt", "a") as file:
# file.write(f"{name}\n")

with open("names.txt", "r") as file:
  lines = file.readlines()

  for line in lines:
    # print(line.strip())
    print(line.rstrip())

# with open("students.csv") as file:
#   for line in file:
#     # row = line.rstrip().split(",")
#     # print(f"{row[0]} is in {row[1]}")
#     name, house = line.rstrip().split(",")
#     print(f"{name} is in {house}")

# students = []
# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append(f"{name} is in {house}")

# for student in sorted(students):
#   print(student)

students = []
with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    # student = {}
    # student["name"] = name
    # student["house"] = house
    student = {"name": name, "house": house}
    students.append(student)

# def get_name(student):
#   return student["name"]

# def get_house(student):
#   return student["house"]

# the function as the value of key in the sorted function, is automatcially called with each of the student dict value by the sorted function itself

# for student in sorted(students, key=get_name, reverse=True):
#   print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=get_house, reverse=True):
#   print(f"{student['name']} is in {student['house']}")

students = []
with open("students.csv") as file:
  for line in file:
    name, home = line.rstrip().split(",")
    student = {"name": name, "home": home}
    students.append(student)

# anonymous function | need only in once place to execute
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is from {student['home']}")


import csv

students = []
# with open("students.csv") as file:
#   for line in file:
#     name, home = line.rstrip().split(",")
#     student = {"name": name, "home": home}
#     students.append(student)

# # anonymous function | need only in once place to execute
# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is from {student['home']}")


with open("students.csv") as file:
  # csv library will help us to handle the corner cases like extra comma in a value
  reader = csv.reader(file)
  # for row in reader:
  #   students.append({"name": row[0], "home": row[1]})

  # if we know that we have only two data, name & home in csv, then we can do this
  for name, home in reader:
    students.append({"name": name, "home": home})

# anonymous function | need only in once place to execute
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is from {student['home']}")


# with open("students.csv") as file:
#   ## csv library will help us to handle the corner cases like extra comma in a value

#   # reader = csv.reader(file)
#   # for row in reader:
#   #   students.append({"name": row[0], "home": row[1]})
#   ## if we know that we have only two data, name & home in csv, then we can do this

#   # the file must have the headers
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "home": row["home"]})
#   reader = csv.DictReader(file)

# ## anonymous function | need only in once place to execute
# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is from {student['home']}")


import csv

students = []

name = input(f"Enter a name: ")
home = input(f"Enter a home: ")

with open("students.csv", "a") as file:
  # writer = csv.writer(file)
  # writer.writerow([name, home])
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"name": name, "home": home})


with open("students.csv") as file:
  # the file must have the headers
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name": row["name"], "home": row["home"]})
  reader = csv.DictReader(file)

## anonymous function | need only in once place to execute
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is from {student['home']}")