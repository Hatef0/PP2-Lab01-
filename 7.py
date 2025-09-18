# ==============================================
# Python Strings
# ==============================================
# Strings are sequences of characters, used to store text in Python.

# ----------------------------------------------
# 1. Slicing Strings
# You can return a range of characters using slice syntax: start_index:end_index
b = "Hello, World!"
print("Characters from position 2 to 5:", b[2:5])  # Note: first character has index 0

# Slice from the start
print("Start to position 5:", b[:5])

# Slice to the end
print("From position 2 to end:", b[2:])

# Negative indexing
print("Characters from -5 to -2:", b[-5:-2])

# ----------------------------------------------
# 2. Modify Strings (Built-in Methods)
a = " Hello, World! "

# Uppercase
print("Uppercase:", a.upper())

# Lowercase
print("Lowercase:", a.lower())

# Remove whitespace
print("Stripped:", a.strip())

# Replace string
print("Replace 'H' with 'J':", a.replace("H", "J"))

# Split string
print("Split by comma:", a.split(","))

# ----------------------------------------------
# 3. String Concatenation
a = "Hello"
b = "World"

# Simple concatenation
c = a + b
print("Concatenated:", c)

# Concatenation with space
c = a + " " + b
print("Concatenated with space:", c)

# ----------------------------------------------
# 4. String Formatting

# Using f-strings (Python 3.6+)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

# With formatting (2 decimals)
txt = f"The price is {price:.2f} dollars"
print(txt)

# Using operations inside placeholders
txt = f"The price is {20 * 59} dollars"
print(txt)

# ----------------------------------------------
# 5. Escape Characters
# Use backslash '\' to insert characters that are normally illegal

# Example: quotes inside quotes
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Common escape characters:
print("Single quote: \'")
print("Backslash: \\")
print("New line: \nHello")
print("Carriage return: Hello\rWorld")
print("Tab: \tTabbed")
print("Backspace: ABC\bD")  # removes previous character
print("Form feed: Hello\fWorld")
print("Octal value: \110")  # prints 'H'
print("Hex value: \x48")    # prints 'H'

# ----------------------------------------------
# Exercise:
# 1. Create a string variable with your favorite sentence
# 2. Print the first and last character
# 3. Make it uppercase and replace one word
my_sentence = "Python is amazing!"
print("First character:", my_sentence[0])
print("Last character:", my_sentence[-1])
print("Uppercase:", my_sentence.upper())
print("Replace 'amazing' with 'awesome':", my_sentence.replace("amazing", "awesome"))