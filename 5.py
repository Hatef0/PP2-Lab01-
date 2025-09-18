# ==============================================
# Python Numbers
# ==============================================
# There are three numeric types in Python:
# 1. int      -> Integer numbers (whole numbers)
# 2. float    -> Floating point numbers (decimals)
# 3. complex  -> Complex numbers (real + imaginary)

# Variables of numeric types are created when you assign a value to them
x = 1      # int
y = 2.8    # float
z = 1j     # complex

# To check the type of a variable, use type()
print("Type of x:", type(x))  # <class 'int'>
print("Type of y:", type(y))  # <class 'float'>
print("Type of z:", type(z))  # <class 'complex'>

# ----------------------------------------------
# Integer (int)
# Integers are whole numbers, positive or negative, without decimals.
x = 1
y = 35656222554887711
z = -3255522

print("\nIntegers:")
print(x, type(x))
print(y, type(y))
print(z, type(z))

# ----------------------------------------------
# Float
# Float is a number with a decimal point, positive or negative.
x = 1.10
y = 1.0
z = -35.59

print("\nFloats:")
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Float can also be written in scientific notation
x = 35e3    # 35 * 10^3
y = 12E4    # 12 * 10^4
z = -87.7e100

print("\nScientific notation:")
print(x, type(x))
print(y, type(y))
print(z, type(z))

# ----------------------------------------------
# Complex
# Complex numbers have a real part and an imaginary part (written with "j")
x = 3 + 5j
y = 5j
z = -5j

print("\nComplex numbers:")
print(x, type(x))
print(y, type(y))
print(z, type(z))

# ----------------------------------------------
# Type Conversion
# Convert from one type to another using int(), float(), complex()
x = 1      # int
y = 2.8    # float
z = 1j     # complex

a = float(x)    # int -> float
b = int(y)      # float -> int
c = complex(x)  # int -> complex

print("\nType Conversion:")
print("a =", a, type(a))
print("b =", b, type(b))
print("c =", c, type(c))

# Note: You cannot convert complex numbers to int or float

# ----------------------------------------------
# Random Number
# Python has a built-in module called 'random' to generate random numbers

import random

# Generate a random number from 1 to 9
rand_num = random.randrange(1, 10)
print("\nRandom number from 1 to 9:", rand_num)

# Exercise:
# Generate 5 random numbers between 10 and 50 and print them
print("5 random numbers between 10 and 50:")
for i in range(5):
    print(random.randrange(10, 51), end=" ")

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (float)
print(a // b)  # Division (integer/floor)
print(a % b)   # Modulus (remainder)
print(a ** b)  # Exponentiation (power)