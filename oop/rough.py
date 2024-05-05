# def main():
#   #assignment is copying from right to left
#   # unpack sequence of values
#   # name, house = get_student()
#   # student = get_student()
#   # print(f"Your name is {name} and you are from {house}.")
#   # print(f"Your name is {student[0]} and you are from {student[1]}.")

#   student_dict = get_student_dict()
#   if(student_dict["name"] == "Padma"):
#     student_dict["house"] = "Ravenclaw"
#   print(f'{student_dict["name"]} is from {student_dict["house"]}.')

# def get_student_dict():
#   return {"name": input(f"Name: "), "house": input(f"House: ")}

# def get_student():
#   name = input("Enter your name: ")
#   house = input("Enter your house: ")
#   # returning sequence of values | acutally returning a tuple
#   return name, house
#   # same as above
#   # return (name, house)

# def get_name():
#   return input("Enter your name: ")

# def get_house():
#   return input("Enter you house: ")

# # to avoid running main blindly
# if __name__ == "__main__":
#   main()

# class is a blueprint | a mold or template | it is a datatype |
# classes have attributes | properties | variables
# anytime we create a class we create a object
# class has attributes, instance variables, methods/functions
# __new__ method initialize an object in the memory for the class
# ensure correctness of data | error check | handle complex program

# encapulation | data hiding | data protection

# dunder init method | initialization of object using the method
# instance var to object |
# method is just a function inside a class
# self is a reference to the object

# instance variables
# attributes
# methods
# properties

# class Student():
#   def __init__(self, name, house):
#     self.name = name
#     self.house = house

#   def __str__(self):
#     return f"{self.name} from {self.house}"

# def main():
#   student = get_student()
#   print(f'Your name {student.name} and you are from {student.house}.')

# def get_student():
#   name = input("Your name: ")
#   house = input("Your house is in: ")
#   # creating an student object of the class Student template
#   # constructor call
#   student = Student(name, house)
#   student2 = Student("Padma", "Ravenclaw")
#   print(student)
#   print(student2)

#   return student

# if __name__ == "__main__":
#   main()

# class Student():

#   def __init__(self, name, house, patronus):
#     if not name:
#       raise ValueError("Missing name")

#     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#       raise ValueError("Invalid house")

#     self.name = name
#     self.house = house
#     self.patronus = patronus

#   # meant for users of the program to print the object
#   def __str__(self):
#     return f"{self.name} from {self.house}"

#   # meant for the dev of the program to print the object
#   def __repr__(self):
#     return f"Your name is {self.name} and you are from {self.house}"

#   def charm(self):
#     match self.patronus:
#       case "Stag":
#         return "Horse"
#       case "Otter":
#         return "Otter"
#       case "Jack Russell Terrier":
#         return "Dog"
#       case _:
#         return "Magical wand!"

# def main():
#   student = get_student()
#   print("Expecto Patronum!")
#   print(student.charm())

# def get_student():
#   name = input("Your name: ")
#   house = input("Your house is in: ")
#   patronus = input("Your patronus is in: ")
#   # creating an student object of the class Student template
#   # constructor call
#   student = Student(name, house, patronus)

#   return student

# if __name__ == "__main__":
#   main()

# class is a blueprint | a mold or template | it is a datatype |
# classes have attributes | properties | variables
# anytime we create a class we create a object
# class has attributes, instance variables, methods/functions
# __new__ method initialize an object in the memory for the class
# ensure correctness of data | error check | handle complex program

# encapulation | data hiding | data protection

# dunder __init__ method | initialization of object using the method
# instance var to object |
# method is just a function inside a class
# self is a reference to the object

# import sys
# sys.exit("")

# properties | attributes with getter and setter | more control over the data |
# property is a special method in python

# decorators | @property | @property decorator
# getter (@property)
#setter (@house.setter)
# in both cases the method name needs to be as same as the attribute
# INSTANCE variable name and method name in a class can't be the same in Python
# so the property will be used to get and set the value of the instance variable. |
# For instance <house> will be the PROPERTY here, whereas <_house> will be the INSTANCE VARIABLE

# if attribute has setter or getter method with same name in a class, |
# then the setter and getter method will be called automatially by Python

# int is a class in Python | It creates a object with type <int> |
# class int(x, base=10)
# class str(object = "")
# class list([iterable]) | something can be iterable 1,2,3,4,5
# class dict({key:value})


# class Student():

#   def __init__(self, name, house, patronus):
#     self.name = name
#     # self.house will also call the setter method
#     self.house = house
#     self.patronus = patronus

#   # meant for users of the program to print the object
#   def __str__(self):
#     return f"{self.name} from {self.house}"

#   # meant for the dev of the program to print the object
#   def __repr__(self):
#     return f"Your name is {self.name} and you are from {self.house}"

#   @property
#   def name(self):
#     return self._name

#   @name.setter
#   def name(self, name):
#     if not name:
#       raise ValueError("Invalid name")
#     self._name = name

#   # Getter
#   @property
#   def house(self):
#     return self._house

#   # Setter
#   @house.setter
#   def house(self, house):
#     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#       raise ValueError("Invalid house")
#     self._house = house

#   def charm(self):
#     match self.patronus:
#       case "Stag":
#         return "Horse"
#       case "Otter":
#         return "Otter"
#       case "Jack Russell Terrier":
#         return "Dog"
#       case _:
#         return "Magical wand!"


# def main():
#   student = get_student()
#   student._name = "Number Four, Frawd"
#   print(student)
#   print("Expecto Patronum!")
#   print(student.charm())


# def get_student():
#   name = input("Your name: ")
#   house = input("Your house is in: ")
#   patronus = input("Your patronus is in: ")
#   # creating an student object of the class Student template
#   # constructor call
#   student = Student(name, house, patronus)

#   return student


# if __name__ == "__main__":
#   main()




# Polymorphism | Polymorphism is the ability of an object to take on many forms.
# Polymorphism: The ability of objects to take on different forms. Polymorphism allows objects of different classes to be treated as objects of a common superclass.

class Spell:
  def spell(self):
      return "Wand!"

class Stag(Spell):
  def spell(self):
      return "Horse"

class Otter(Spell):
  def spell(self):
      return "Otter"

spells = [Stag(), Otter()]
for spell in spells:
  print(spell.spell())