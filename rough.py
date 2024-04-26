# # string
# name = "saru"
# print(type(name) == str)
# print(isinstance(name, str))

# age = int("25")
# print(isinstance(age, int))

# age += 8
# print(age)

# khaled = """
# Khaled is a good Boy
# Hello
# Love Sara and Food

# Love Panda
# """

# print(khaled)
# print("khaled".upper())
# print("KhaLed".lower())
# print("khlaed".islower())

# print("khlaed hasan".title())
# print("kh" in "khlaed hasan")
# print("khlaed\"hasan".title())
# print("khlaed\nhasan".title())
# print(khaled[2:7])
# print(khaled[:7])
# print(khaled[2:])

# # global method
# book_1 = True
# book_2 = True

# any_meth = any([book_1, book_2])
# all_meth = all([book_1, book_2])

# print(any_meth)
# print(all_meth)

# # imaginary numbers - complex numbers
# imaginary_num_1 = 2+3j
# imaginary_num_2 = complex(5,7)

# print(imaginary_num_1.real, imaginary_num_1.imag)
# print(imaginary_num_2.real, imaginary_num_2.imag)

# # built-in functions
# print(abs(-5.5))
# print(round(5.4944,1))

# # Enum - Only way to use Constant in Python
# from enum import Enum
# class State(Enum):
#   ACTIVE = 1
#   INACTIVE = 0

# print(State.ACTIVE)
# print(State.ACTIVE.value)
# print(State(1))
# print(State["ACTIVE"].value)
# print(list(State))
# print(len(State))

# # User input
# age = input("What is your age?\n")
# print("Your age is " + age)

# # list
# dogs = ["Roger", "beau", "tulu", "Syd", "lulu", "Quincy", "vulu"]

# dogs[2] = "Beau"

# print("Roger" in dogs)

# print(dogs[-2])
# print(dogs[2:4])
# print(dogs[2:])
# print(dogs[:4])

# dogs.append("Judah")

# dogs.extend(["Judah1", "nothing1"])
# dogs += ["Judah2", "nothing2"]

# dogs.remove("Quincy")

# print(dogs)
# popped_dog = dogs.pop()
# print(popped_dog)

# dogs.insert(2, popped_dog)
# dogs[1:1] = ["Test1", "Test2"]

# #copy the dogs list
# dogs_copy = dogs[:]
# print(dogs_copy)

# #sort the list without modifying
# unmodified_sorted_dogs = sorted(dogs, key=str.lower)
# print("unmodified_dogs")
# print(unmodified_sorted_dogs)
# print("unmodified_dogs")
# print(dogs)

# #data-types needs to be same and sort changes the list contents
# dogs.sort()
# print(dogs)

# #sort the list in proper order
# dogs.sort(key=str.lower)

# #reverse the list
# new_list = [1,2,5]
# new_list.reverse()
# print(new_list)

# print(len(dogs))
# print(dogs)

# #tuples - immutable
# names = ("Roger", "Syd", "Beau")

# new_tuple_names = names + ("Tina", "Quincy") #add new values to tuple and create new tuple
# names += ("Tina", "Quincy")

# new_tuple_list = list(names)
# print(type(new_tuple_list))

# new_list_tuple = tuple(new_tuple_list)
# print(type(new_list_tuple))

# print(names)
# print(new_tuple_names)
# print(sorted(names)) #don't modify because tuple can't be modified
# print(names[0])
# print(names[-1])
# print(names.index("Syd"))
# print(len(names))
# print(names[1:2])
# print(names)
# print("Roger" in names)
# print(names[0:2])

# #dictionary
# dog = {"name": "Roger", "age": 8, "color": "green"}

# print(dog["name"])
# print(dog.get("age"))
# print(dog.get("color", "brown"))
# dog["color"] = "yellow"

# print(dog.get("color", "brown"))
# print(dog.get("gender", "female"))

# dog["gender"] = "male"
# print(dog.get("gender", "female"))

# print(dog.keys())
# print(list(dog.keys()))
# print(dog.values())
# print(list(dog.values()))

# print(dog.items())
# print(list(dog.items()))

# new_dict_list = list(dog.items())
# print(type(new_dict_list[0]))

# print(len(dog)) #length of dictionary

# print(dog.pop("color"))  #return and delete the item
# print(dog)

# print(dog.popitem())  #return and remove the last item
# print(dog)

# print("name" in dog) #check if the key is present

# dog_copy = dog.copy() #copy the dictionary

# del dog["age"]  #delete an item

# print(dog)
# print(dog_copy)

# ## Sets
# set1 = {"Roger", "Syd"}
# set2 = {"Roger", "Luna"}
# set3 = {"Luna"}

# #intersection | all items that are common in both sets
# intersect_set = set1 & set2
# print(intersect_set)

# # unioin | all items that are in either set
# union_set = set1 | set2 | set3
# print(union_set)

# # difference - items that are in one set but not the other
# diff_set1 = set1 - set2
# diff_set2 = set2 - set1
# print(diff_set1)
# print(diff_set2)

# # superset - items that are in both sets - set2 has all items in set3 then True else False
# super_set = set2 > set3
# super_set2 = set2 < set3
# print(super_set)
# print(super_set2)
# print(len(set2))
# print(list(set2))
# print("Roger" in set2)

# # subsets - set2 is a subset of set3 if all items in set2 are in set3
# sub_set = set2 <= set3
# sub_set2 = set3 <= set2
# print(sub_set)
# print(sub_set2)

# #Nested function
# def talk(phrase):
#   def say(word):
#     print(word)

#   words = phrase.split(' ')
#   for word in words:
#     say(word)

# talk('I am going to buy the milk')

# def count():
#   count = 0

#   def increment():
#     nonlocal count
#     count += 1
#     print(count)

#   increment()

# count()

# # Closuers
# def counter():
#   count = 0

#   def increment():
#     nonlocal count
#     count += 1
#     return count

#   return increment

# increment = counter()
# print(increment())
# print(increment())
# print(increment())

# # Objects
# age = 8
# print(age.real)
# print(age.imag)
# print(age.bit_length()) # number of bit necessary to store the value 8 in the binary notations

# items = [1,2]
# items.append(3)
# items.pop()
# print(items)
# print(id(items)) # return the memory address of the object (item list)

# # # Loops
# condition = True
# temp_counter = 0
# while condition == True:
#   print(f"The condition is True{temp_counter}")
#   temp_counter = temp_counter + 1;
#   if(temp_counter == 15):
#     condition = False

# temp_count = 0
# print(range(15)) # From 0 to 14, so total 15

# for item in range(15):
#   temp_count += 1

#   if(temp_count == 9):
#     continue

#   print(temp_count)

#   if(temp_count == 12):
#     break

# items = [1,2,3,4]

# for item in items:
#   print(item)

# str_items = ["khaled", "hasan", "sara"]

# #enumerate returns the index and the value
# for index, item in enumerate(str_items):
#   print(index, item)

## Class | Inheritance
# class Animal:
#   def walk(self):
#     print("Walking...")

# class dog(Animal):
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def bark(self):
#     print("woof!")
#     return "woof!"

# roger = dog("Roger", 8)
# print(type(roger))
# print(roger.name, roger.age)
# roger.bark()
# roger.walk()

# # Modules | every Python file is a module | __init__.py in folder indicates that this is a module
# import dog
# from lib import cat
# from lib.cat import cat_call
# from dog import bark

# dog.bark()
# bark()
# cat.cat_call()
# cat_call()

# # Python standard Modules | Library
# import math
# print(math.sqrt(4))
# from math import sqrt
# print(sqrt(4))

# # Accepting Arguments | command line
# import sys
# name = sys.argv[1]
# print(sys.argv)
# print("Hello " + name)

# import argparse

# parser = argparse.ArgumentParser(
#   description='This program prints the name of my dogs'
# )

# parser.add_argument(
#   '-c', '--color', metavar="color",required=True, choices={"red", "blue"}, help="the color to search for")

# args = parser.parse_args
()

# print("the color is " + args.color)

# # Lambda Functions
# lambda num: num * 2
# multiply = lambda a, b: a * b
# print(multiply(2,4))


# ##geneartor expression |  When list(gen_result) is called, the generator is evaluated. This approach is memory-efficient as it does not create an intermediate list of all the multiplied values upfront.
# gen_items = [1,2,3,4,5]
# gen_result = (a * 5 for a in gen_items)
# print(list(gen_result))

# ##list comprehension | In Python, list comprehensions are a way to create lists by applying an expression to each element in a sequence. When you use list comprehensions, the new list is created and populated with all the values immediately. This means that all the elements are generated at once.

# list_compr_items = [a ** 2 for a in range(1,6)]
# print(list(list_compr_items))

# # # map, filter, reduce

# #map | returns map object
# map_items = [1,2,3,4]

# def double(a):
#   return a * 2

# result = map(double, map_items)
# print(list(result))

# #using lambda 
# triple = lambda a : a * 3

# result2 = map(triple, map_items)
# print(list(result2))

# #using simplified lambda
# result3 = map(lambda a : a * 4, map_items)
# print(list(result3))

# ##filter | takes an iterable and returns filter(ed) object which another iterable

# filter_items = [1,2,3,4,5,6,7,8,9,10]
# def isEven(n):
#   return n % 2 == 0

# result_filter = filter(isEven, filter_items)
# result_filter2 = filter((lambda num: num % 2 == 0), filter_items)

# print(result_filter)
# print(list(result_filter))
# print(list(result_filter2))


### reduce | takes a function and a sequence and returns a single value | its different from map and filter | needs to import from functools

##without reduce
# expenses = [("Dinner", 80), ("Car Repair", 170)]

# def expenseCalculation():
#   sum = 0 
#   for expense in expenses:
#     sum += expense[1]

#   return sum

# print(expenseCalculation())

# ##with reduce
# from functools import reduce
# expenses_reduce = [("Dinner", 57), ( "Car Repair", 110)]

# # here "a" is the accumulator and "b" is the current item
# total_expense = reduce((lambda a, b: a[1] + b[1]), expenses_reduce)
# print(total_expense)

# ## replicate the above reduce function using generator expression
# total_expense_gen = sum((expense[1] for expense in expenses_reduce))
# print(total_expense_gen)

# ## replicate the above reduce function using list comprehension 
# total_expense_gen2 = sum([expense[1] for expense in expenses_reduce])
# print(total_expense_gen2)


## recursion | a function call itself | needs to have one base case and one recursive case | bas case is the condition that stops the recursion | recursive case is the condition that calls the function again

# def factorial(n):
#   if n == 1: return 1 
#   return n * factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


## decorators | a function that wraps another function and enhances it | it is a function that takes another function as an argument and returns a new function | it is a way to modify the behavior of a function without modifying its source code 

# def logtime(func):
#   def wrapper():
#     print("before")
#     val = func()
#     print("after")
#     return val
#   return wrapper


def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val
    return wrapper

@logtime
def sayHello():
    x = 10
    print(f"Hello! {x}")


sayHello()