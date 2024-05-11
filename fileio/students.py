
import csv

students = []

name = input(f"Enter a name: ")
home = input(f"Enter a home: ")

with open("students.csv", "a") as file:
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