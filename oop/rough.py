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

class Student():
  def __init__(self, name, house):
    self.name = name
    self.house = house 

  def __str__(self):
    return f"{self.name} from {self.house}"

def main():
  student = get_student()
  print(f'Your name {student.name} and you are from {student.house}.')


def get_student():
  name = input("Your name: ")
  house = input("Your house is in: ")
  # creating an student object of the class Student template
  # constructor call
  student = Student(name, house) 
  student2 = Student("Padma", "Ravenclaw")
  print(student)
  print(student2)

  return student

if __name__ == "__main__":
  main()
