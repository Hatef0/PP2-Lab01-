# ==============================================
# Python Casting
# ==============================================
# Sometimes you may want to specify the type of a variable.
# This is done using "casting".
# Python uses classes to define data types, and casting is performed with constructor functions.

# Casting functions in Python:
# - int()   -> converts a value to an integer
# - float() -> converts a value to a float
# - str()   -> converts a value to a string

# ----------------------------------------------
# Integers
x = int(1)       # from integer literal
y = int(2.8)     # from float literal (decimals are removed)
z = int("3")     # from string literal (string must be a whole number)

print("Integer examples:")
print("x =", x, type(x))
print("y =", y, type(y))
print("z =", z, type(z))

# ----------------------------------------------
# Floats
x = float(1)       # from integer
y = float(2.8)     # from float
z = float("3")     # from string representing integer
w = float("4.2")   # from string representing float

print("\nFloat examples:")
print("x =", x, type(x))
print("y =", y, type(y))
print("z =", z, type(z))
print("w =", w, type(w))

# ----------------------------------------------
# Strings
x = str("s1")   # string remains string
y = str(2)      # integer -> string
z = str(3.0)    # float -> string

print("\nString examples:")
print("x =", x, type(x))
print("y =", y, type(y))
print("z =", z, type(z))

# ----------------------------------------------
# Notes:
# - int() removes decimals from floats
# - float() can convert integers and numeric strings
# - str() can convert most data types to string
# - You cannot cast a complex number directly to int or float

# Exercise:
# Convert the following values:
# 7 -> float
# 3.5 -> int
# 100 -> string
num1 = 7
num2 = 3.5
num3 = 100

print("\nCasting Exercise:")
print(float(num1))  # 7 -> 7.0
print(int(num2))    # 3.5 -> 3
print(str(num3))    # 100 -> '100'