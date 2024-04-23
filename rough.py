from enum import Enum

# string
name = "s"
print(type(name) == str)
print(isinstance(name, str))

age = int("25")
print(isinstance(age, int))

age += 8
print(age)

khaled = """
K is a good Boy
Hello
Love S and Food

Love Panda
"""

print(khaled)
print("khaled".upper())
print("KhaLed".lower())
print("khlaed".islower())

print("khlaed hasan".title())
print("kh" in "khlaed hasan")
print("khlaed\"hasan".title())
print("khlaed\nhasan".title())
print(khaled[2:7])
print(khaled[:7])
print(khaled[2:])

# global method
book_1 = True
book_2 = True

any_meth = any([book_1, book_2])
all_meth = all([book_1, book_2])

print(any_meth)
print(all_meth)

# imaginary numbers - complex numbers
imaginary_num_1 = 2+3j
imaginary_num_2 = complex(5,7)

print(imaginary_num_1.real, imaginary_num_1.imag)
print(imaginary_num_2.real, imaginary_num_2.imag)
print(abs(-5.5))
print(round(5.4944,1))

# Enum - Only way to use Constant in Python
class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State["ACTIVE"].value)
print(list(State))
print(len(State))

# User input
age = input("What is your age?\n")
print("Your age is " + age)

# list
dogs = ["Roger", "beau", "tulu", "Syd", "lulu", "Quincy", "vulu"]

dogs[2] = "Beau"

print("Roger" in dogs)

print(dogs[-2])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:4])

dogs.append("Judah")

dogs.extend(["Judah1", "nothing1"])
dogs += ["Judah2", "nothing2"]

dogs.remove("Quincy")

print(dogs)
popped_dog = dogs.pop()
print(popped_dog)

dogs.insert(2, popped_dog)
dogs[1:1] = ["Test1", "Test2"]

#copy the dogs list
dogs_copy = dogs[:]
print(dogs_copy)

#sort the list without modifying
unmodified_sorted_dogs = sorted(dogs, key=str.lower)
print("unmodified_dogs")
print(unmodified_sorted_dogs)
print("unmodified_dogs")
print(dogs)

#data-types needs to be same and sort changes the list contents
dogs.sort()
print(dogs)

#sort the list in proper order
dogs.sort(key=str.lower)

#reverse the list
new_list = [1,2,5]
new_list.reverse()
print(new_list)

print(len(dogs))
print(dogs)

#tuples - immutable
names = ("Roger", "Syd", "Beau")

new_tuple_names = names + ("Tina", "Quincy") #add new values to tuple and create new tuple
names += ("Tina", "Quincy")

new_tuple_list = list(names)
print(type(new_tuple_list))

new_list_tuple = tuple(new_tuple_list)
print(type(new_list_tuple))

print(names)
print(new_tuple_names)
print(sorted(names)) #don't modify because tuple can't be modified
print(names[0])
print(names[-1])
print(names.index("Syd"))
print(len(names))
print(names[1:2])
print(names)
print("Roger" in names)
print(names[0:2])

#dictionary
dog = {"name": "Roger", "age": 8, "color": "green"}

print(dog["name"])
print(dog.get("age"))
print(dog.get("color", "brown"))
dog["color"] = "yellow"

print(dog.get("color", "brown"))
print(dog.get("gender", "female"))

dog["gender"] = "male"
print(dog.get("gender", "female"))

print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))

print(dog.items())
print(list(dog.items()))

new_dict_list = list(dog.items())
print(type(new_dict_list[0]))

print(len(dog))

print(dog.pop("color"))  #pop will return the value and delete the item
print(dog)
print(dog.popitem())  #remove the last item from the dictionary
print(dog)
print("name" in dog)

dog_copy = dog.copy()

del dog["age"]  #delete an item

print(dog)
print(dog_copy)
