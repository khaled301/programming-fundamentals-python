class Student():
  def __init__(self, name, house, patronus):
    self.name = name
    # self.house will also call the setter method
    self.house = house
    self.patronus = patronus

  # meant for users of the program to print the object
  def __str__(self):
    return f"{self.name} from {self.house}"

  # meant for the dev of the program to print the object
  def __repr__(self):
    return f"Your name is {self.name} and you are from {self.house}"

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Invalid name")
    self._name = name

  # Getter
  @property
  def house(self):
    return self._house

  # Setter
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self._house = house

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

  # we can call this method without instanciating the class
  @classmethod
  def get(cls):
    name = input("Your name: ")
    house = input("Your house is in: ")
    patronus = input("Your patronus is in: ")
    return cls(name, house, patronus)


def main():
  student = Student.get()
  # student._house = "Something else"
  print(student)
  print("Expecto Patronum!")
  print(student.charm())

# this needs to be at the end of the file
if __name__ == "__main__":
  main()


# class will be used to represent the real world entity
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

# class method <@classmethod> and class variables works on all of the objects of the class
# on the other hand instance variables and instance methods works on the specific object of the class instance