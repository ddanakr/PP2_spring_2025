# 1, 2, 3
# HOME, Intro, Get started

print("Hello, World!")

# 4
# Syntax

if 5 > 2:
  print("Five is greater than two!")



# 5
# Comments

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



# 6
# Variables

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


"""
Global variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""



# 7
# Data Types

x = 5
print(type(x))



# 8
# Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



# 9
# Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3



# 10
# Strings

b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)