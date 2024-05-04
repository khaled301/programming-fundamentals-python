# @classmethod
# this method will be same for all the instances

# class variables | class attributes | static variables
# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# we do not instantiate the class | it's a kind of container

import random

class Hat():
  houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  def sort(cls, name):
    print(f"The {name}'s hat is sorted and lives in {random.choice(cls.houses)}.")

# accessing the classmethod inside a class
Hat.sort("Harry")
# accessing the classvariables inside a class
print(Hat.houses)

# encapsulation | Encapsulation in object-oriented programming is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit known as a class.

#Encapsulation helps in data hiding, as the internal state of the object is hidden from the outside world and can only be accessed through public methods (getter and setter methods). This protects the data from direct access and modification, which helps in maintaining the integrity of the data.

#Encapsulation also helps in achieving abstraction by exposing only the necessary details and hiding the unnecessary details of an object.