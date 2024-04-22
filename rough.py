from enum import Enum


name = "saru"
print(type(name) == str)
print(isinstance(name, str))

age = int("25")
print(isinstance(age, int))

age += 8
print(age)

khaled = """
Khaled is a good Boy
Hello
Love Sara and Food

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

book_1 = True
book_2 = True

any_meth = any([book_1, book_2])
all_meth = all([book_1, book_2])

print(any_meth)
print(all_meth)

imaginary_num_1 = 2+3j
imaginary_num_2 = complex(5,7)

print(imaginary_num_1.real, imaginary_num_1.imag)
print(imaginary_num_2.real, imaginary_num_2.imag)
print(abs(-5.5))
print(round(5.4944,1))

class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State["ACTIVE"].value)
print(list(State))
print(len(State))





