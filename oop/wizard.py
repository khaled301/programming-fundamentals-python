# super class of Student and Teacher
class Wizard:
  def __init__(self, name):
    if not name:
      raise ValueError("Missing name")
    self.name = name

  def __str__(self):
    return f"Wizard {self.name}"

# subclass of Wizard
class Student(Wizard):
  def __init__(self, name, house):
    super().__init__(name)
    self.house = house

  def __str__(self):
    return f"Your name is {self.name} and you are from {self.house}"

# subclass of Wizard
class Teacher(Wizard):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

  def __str__(self):
    return f"Your name is {self.name} and you teach {self.subject}"

wizard = Wizard("Albus Dumbledore")
student = Student("Hailey", "Gryffindor")
teacher = Teacher("Severus", "Defense Against the Dark Arts")

print(wizard)
print(student)
print(teacher)


# Inheritence | Inheritence is a mechanism in Python to inherit attributes and methods from one class to another.
# subclass can have multiple super classes
# subclass can be nested super class | parent class can have multiple super classes

# In Python Exceptions are good example of the inheritence |
# whenever we use try-except it borrows the exception from the parent exception class | we can use precise exception subclass or more generic base parent exception class if we do not want to handle the exception precisely
# we should inherit the build in exception classes whenever we are creating our own exception class

#
