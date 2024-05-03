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


class Student():

  def __init__(self, name, house, patronus):
    if not name:
      raise ValueError("Missing name")

    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")

    self.name = name
    self.house = house
    self.patronus = patronus

  # meant for users of the program to print the object
  def __str__(self):
    return f"{self.name} from {self.house}"

  # meant for the dev of the program to print the object
  def __repr__(self):
    return f"Your name is {self.name} and you are from {self.house}"

  def charm(self):
    match self.patronus:
      case "Stag":
        return "Horse"
      case "Otter":
        return "Otter"
      case "Jack Russell Terrier":
        return "Dog"
      case _:
        return "Magical wand!"


def main():
  student = get_student()
  print("Expecto Patronum!")
  print(student.charm())


def get_student():
  name = input("Your name: ")
  house = input("Your house is in: ")
  patronus = input("Your patronus is in: ")
  # creating an student object of the class Student template
  # constructor call
  student = Student(name, house, patronus)

  return student


if __name__ == "__main__":
  main()
