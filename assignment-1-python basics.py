# =========================================================
# Assignment-1: Python Basics & Variables
# =========================================================


# =========================================================
# 1. Print Your Name
# =========================================================

print("1. Print Your Name")
print("My name is L.vasanth.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Comments in Python
# =========================================================

print("2. Comments in Python")

# This is a single-line comment

"""
This is a multi-line comment.
Python uses triple quotes for multi-line comments or documentation.
"""

print("Comments are used to explain code and improve readability.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Working with Basic Data Types
# =========================================================

print("3. Working with Basic Data Types")

# Integer
integer_value = 100

# Float
float_value = 10.5

# Boolean
boolean_value = True

# String
string_value = "A"

print("Integer Value:", integer_value, "| Type:", type(integer_value))
print("Float Value:", float_value, "| Type:", type(float_value))
print("Boolean Value:", boolean_value, "| Type:", type(boolean_value))
print("String Value:", string_value, "| Type:", type(string_value))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Local vs Global Variables
# =========================================================

print("4. Local vs Global Variables")

# Global variable
value = "Global Variable"


def variable_scope_demo():
    global value

    # Printing global variable before modification
    print("Inside Function - Before Modification:", value)

    # Modifying global variable
    value = "Modified Global Variable"

    # Local variable
    local_value = "Local Variable"

    print("Inside Function - Local Variable:", local_value)
    print("Inside Function - Modified Global Variable:", value)


# Calling function
variable_scope_demo()

# Printing global variable after function call
print("Outside Function - Global Variable:", value)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Type Checking & Dynamic Typing
# =========================================================

print("5. Type Checking & Dynamic Typing")

dynamic_variable = 10
print(dynamic_variable, "| Type:", type(dynamic_variable))

dynamic_variable = 15.75
print(dynamic_variable, "| Type:", type(dynamic_variable))

dynamic_variable = "Python"
print(dynamic_variable, "| Type:", type(dynamic_variable))

dynamic_variable = False
print(dynamic_variable, "| Type:", type(dynamic_variable))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. User Input Practice
# =========================================================

print("6. User Input Practice")

# Taking user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Printing formatted output
print(f"Hello {name}, you are {age} years old!")

print("\n" + "=" * 50 + "\n")
