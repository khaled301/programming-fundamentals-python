Handbook URL:
https://www.freecodecamp.org/news/the-python-handbook/#pythonbasics
Python:
Python is a dynamically typed language. So we do not need to define a type before declaring any variables

Dictionaries:
Store key-value pair.
Libraries:
A set of functions to avoid writing codes from scratch
List: 
List of variables

f-String:
It helps to use variables and Python code inside a string

Refactoring:
It’s a process of restructuring code without changing the original functionality. To make it more straightforward and more understandable
Invalid variables naming:
Start with numbers like 123age
Use special chars like !, % etc
Python keywords like for, if, while, import and so on

Expression and statements:
An Expression is any sort of code that returns a value.
A statement is an operation on a value.
A program is a series of statements

Data types (all types in Python are objects):
Immutable data types (which are objects)
Integer
Float
String
Boolean
Tuples
String = str
Multiline string
Triple quotes = “”” khaled hasan“””
Upper, lower, title, islower(), isupper()
Isalpha
To check if a string contains chars or digits and is not empty
isdecimal()
To check if a string contains digits and is not empty
startsswith()
To check if a the string start with a specific substring
endswith() 
To check if the string ends with a specific substring
replace()
To replace a part of the string
split()
strip()
join()
find()
Global functions
len(str)
In = (au in beauty)
Escaping
 “Khaled\”au”
New line
“\n”
Characters
print(name[-1]) #last chars from reverse
print(name[2]) # 3rd chars from the beginning
Slicing
print(name[1:7]) #slice from index 1 and upto length 7 of the string
print(name[:7]) #from start upto 7 length of the string
print(name[7:]) # from the length 7 to the end of the string 


Integer = int
Float = float
abs(-5.5) # 5.5
Complex numbers = complex
The imaginary part is written in (j) suffix
Complex = 2 + 3j
Complex constructor
Num = complex(2,3) #3 is the imaginary part
print(num.real, num.imag)
Booleans = bool
All numbers are TRUE except for the number zero (0)
All strings are TRUE except the empty string
Lists, Tuples, Sets, and Dictionaries are FALSE only when empty
any() 
This method will return TRUE if ANY of the values of the iterable which is passed as param is TRUE
all()
This method will return TRUE only if ALL of the values of the iterable which is passed as param is TRUE
Lists = list
Mutable
Sorting changes the list's contents
Dogs = [“Roger”, “Syd”]

Tuples = tuple
Immutable
Dogs = (“Roger”, “Syd”)
Ranges = range
Dictionaries = dict
Key-value pair
{“name”: “roger” }
Key can be any immutable value such a string, number or a tuple


Sets = set
Not ordered
Holds only unique values
set1 = {"Roger", "Syd"}
intersection(&), union(|), superset(>), subset(<=), difference(-)
Frozen set
An immutable version of the set

Operators:
Assignment 
Age = 8 
Arithmetic
5 // 2 # 2 = floor operator
4 ** 2  # 16 = power operator
4 % 3 # 1 = remainder operator
4 + 1 # 5
Logical or Boolean
Not = not
And = and
If X is false then X else Y
Or = or
If X is false then Y else X
Bitwise
Binary AND = &
Binary OR = |
Binary XOR = ^
Binary NOT = ~
Shift left operation = <<
Shift right operation = >>
Comparison
A == b #false
A != b #true
A > b # false
A <= b # true
Is and in 
Identity op, to compare for two objects = is


Membership op, for lists or sequences = in 
Ternary
Quickly define a conditional
True if age > 18 else False

Bult-in-function:
Absolute
abs(-5.5) #5.5
Round = round(5.5) # 6
Round = round(5.49) # 5
Decimal round = round(5.49, 1)
sorted(dogs, key=str.lower)
Enum / Create Constant:
The only way to create CONSTANT in Python
Import enum
from enum import Enum
EnumVar.EnumProperty.value = print the enum value
EnumVar(value) = print the enum property
list(EnumVar) = list all the possible values
len(EnumVar) = count the total enum properties
Input:
The program will stop the execution.
Control statement:
Such as If, else, elif
Lists:
A list can have different kinds of values. 
We can mix different types of data types.
We can check if the values present in the List by using the (in) operator
Functions:
Parameter:
The values excepted by the function inside the function definition
Parameters are passed by reference because all types in Python are Objects
Arguments:
The values that we pass to a function when we call it.
The argument can have a default value
A function can return values

Global Functions:
Provided by Python
id(items)) # return the memory address of the object (item list)
Map,
The original list remain same
Return new map object 
triple = lambda a : a * 3

result2 = map(triple, map_items)
print(list(result2))

#using simplified lambda
result3 = map(lambda a : a * 4, map_items)
print(list(result3)) # [4, 8, 12, 16]


Filter, 
# ##filter | takes an iterable and returns filter(ed) object which another iterable
filter_items = [1,2,3,4,5,6,7,8,9,10]
def isEven(n):
return n % 2 == 0

result_filter = filter(isEven, filter_items)
result_filter2 = filter((lambda num: num % 2 == 0), filter_items)
print(result_filter) # [2, 4, 6, 8, 10]


Reduce
# reduce | takes a function and a sequence and returns a single value | its different from map and filter | needs to import from functools

from functools import reduce
expenses_reduce = [("Dinner", 57), ( "Car Repair", 110)]

# here "a" is the accumulator and "b" is the current item
total_expense = reduce((lambda a, b: a[1] + b[1]), expenses_reduce)
print(total_expense) #167

Variable Scope:
Global
local
Nest Functions:
Function in Python can be nested inside other functions
Only visible to the function but not outside to support different utility 
To access the variable from the outer function to the nested inner function, we have to use the keyword “nonlocal” to declare it in the inner nested function


Closures:
Special way of writing a function
If we return a nested function from a function, that nested function will have access to the variables of that calling function even if the function is not active anymore
It will have access to the last state of the outer function variables and won’t reset the variable values to initial values as we are calling the inner nested function instead of the outer function
Outer function variable can be accessed from inner function using nonlocal keyword
Objects:
Objects are instances of a class 


Everything in Python is basically an Object. Even the basic primitive types like integer, float, string, and tuple.
Object has 
Attributes/properties
Methods
Objects attributes and methods can be accessed using the dot syntax
The Methods available for an object is determined by the Type of the Value
Some objects are mutable, and some are immutable, which depends on the Object itself
When we increment or add something to an immutable object, such as an integer or tuple, it creates an entirely new object
We can check the immutability of an Object by checking the Method availability to change the Object. If a Method exists to change an object, then it is mutable.
An example of a mutable object is a Dictionary; we can change the part of it while keeping the original dictionary Object.
Loops:
For loops
enumerate(items)
It will return each item and index the item
range(integer_value)
For item in items:
For item in range(15):
While Loops
Break and continue can be used in both While and For loops.
Class:
Class is a type of the Objects
Each new class create a new object and allows to creation new instances of that class
Class is like a template
Each instance keeps track of its own state 
When we call a class a init method runs for one time when the class gets initialized
We always specify self as an argument of a method inside a class whenever we define a method
Self denotes the current object/class instance. 
By using the self, a function can access the at attributes and methods of the class
The __str__ method in a class invoked when a print method is invoked on an object of the class
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



Modules:
Every file in a python is a module
Import dog
Allows us import everything that is in the dog file
From dog import bark
Only allow us to import the bark method from the dog file
__init__.py empty file tells Python that the folder is a Module and then we can import the file inside a folder
Python standard libraries:

Lambda Functions:
Only have one expression
Anonymous function, a tiny function with no name
Define by lambda keyword
It needs to have an expression but not a statement
The difference between expression and statement is that expression returns a value
The lambda function can’t be invoked directly rather, we have to assign them to a variable
It is used with other Python functions such as Map, Filter, Reduce and so on
The programming shepherds count their flock using the lambda function 

Generator Expression and List Comprehension:
In Python, you can use generators or list comprehensions to create iterable sequences based on some rules. Here's a breakdown of when to use each:
Generators: Use generators when you want to generate values on-the-fly without storing them all in memory at once. Generators are memory-efficient and are beneficial when dealing with large datasets or when you don't need to access all the generated values simultaneously. They use the () syntax.
##geneartor expression |  When list(gen_result) is called, the generator is evaluated. This approach is memory-efficient as it does not create an intermediate list of all the multiplied values upfront.
gen_items = [1,2,3,4,5]
gen_result = (a * 5 for a in gen_items)
print(list(gen_result))
List Comprehensions: Use list comprehensions when you need to create a new list by applying an expression to each element in an existing iterable. List comprehensions are suitable when you want to create a new list with all the computed values available immediately. They are easy to write and understand. List comprehensions use the [] syntax. In essence, if you need all the computed values at once or want to create a new list, go for list comprehensions. If you want to generate values one at a time and save memory, use generators.

##list comprehension | In Python, list comprehensions are a way to create lists by applying an expression to each element in a sequence. When you use list comprehensions, the new list is created and populated with all the values immediately. This means that all the elements are generated at once.
list_compr_items = [a ** 2 for a in range(1,6)]
print(list(list_compr_items))

### Recursion:
A function that can call itself
Has two cases
Base case (get out of recursive function). Required. Python helps to stop after 1k call
Recursive case
Decorators:
Decorators | a function that wraps another function and enhances it | it is a function that takes another function as an argument and returns a new function | it is a way to modify the behavior of a function without modifying its source code 
Change the functionality of a function without modifying the original function itself
Use to do 
Needed when we need to run same code in the multiple function
Logging
Perform Caching 
Test performance
Verify permissions etc
Use @ symbol to define a decorator

### Docstrings:
A way to add documentation to your functions | it is a string that appears as the first expression in a function or class | start and end with three double quotes | can be used to document the function, class, module, or program














