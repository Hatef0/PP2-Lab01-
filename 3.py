# ==============================================
# Python Variables
# ==============================================
# Variables store data values.
# You don't need to declare the type.

x = 5          # integer
name = "Alice" # string
price = 19.99  # float

print(x, name, price)

# Valid variable names:
user_name = "Bob"
age = 25
print(user_name, age)

#Python allows you to assign values to multiple variables in one line :
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
ames
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.


Example
Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
