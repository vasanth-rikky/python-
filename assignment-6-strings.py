# =========================================================
# Assignment-6: Strings in Python
# =========================================================

import re


# =========================================================
# 1. Creating Strings in Different Ways
# =========================================================

print("1. Creating Strings in Different Ways")

single_quote = 'Hello using single quotes'
double_quote = "Hello using double quotes"
triple_quote = """Hello using
triple quotes"""

print(single_quote)
print(double_quote)
print(triple_quote)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. String Concatenation
# =========================================================

print("2. String Concatenation")

first_name = "Python"
last_name = "Programming"

full_text = first_name + " " + last_name

print("Concatenated String:", full_text)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Length of a String
# =========================================================

print("3. Length of a String")

text = "Bright IT Career"

print("Length of String:", len(text))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Extract Substring
# =========================================================

print("4. Extract Substring")

message = "Python Programming"

substring = message[0:6]

print("Substring:", substring)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Search in String
# =========================================================

print("5. Search in String")

sentence = "Learning Python is easy"

# Using find()
position_find = sentence.find("Python")

print("Position using find():", position_find)

# Using index()
try:
    position_index = sentence.index("Python")
    print("Position using index():", position_index)

except ValueError:
    print("Substring not found using index().")

# Searching for unavailable substring
missing = sentence.find("Java")

if missing == -1:
    print("Substring 'Java' not found.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Compare Strings
# =========================================================

print("6. Compare Strings")

string1 = "Python"
string2 = "Python"
string3 = "Java"

print("string1 == string2 :", string1 == string2)
print("string1 != string3 :", string1 != string3)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. startswith() and endswith()
# =========================================================

print("7. startswith() and endswith()")

website = "www.python.org"

print("Starts with 'www':", website.startswith("www"))
print("Ends with '.org':", website.endswith(".org"))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Lexicographical Comparison
# =========================================================

print("8. Lexicographical Comparison")

word1 = "Apple"
word2 = "Banana"

if word1 < word2:
    print(word1, "comes before", word2)

elif word1 > word2:
    print(word1, "comes after", word2)

else:
    print("Both strings are equal.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 9. Trim Whitespaces
# =========================================================

print("9. Trim Whitespaces")

text_with_spaces = "   Python Programming   "

print("Before strip():", repr(text_with_spaces))
print("After strip():", repr(text_with_spaces.strip()))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 10. Replace Characters
# =========================================================

print("10. Replace Characters")

sentence = "I like Java"

updated_sentence = sentence.replace("Java", "Python")

print("Updated String:", updated_sentence)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 11. Split a String
# =========================================================

print("11. Split a String")

colors = "Red,Blue,Green,Yellow"

color_list = colors.split(",")

print("Split List:", color_list)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 12. Convert Integer to String
# =========================================================

print("12. Convert Integer to String")

number = 100

string_number = str(number)

print("Converted Value:", string_number)
print("Type:", type(string_number))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 13. Uppercase and Lowercase
# =========================================================

print("13. Uppercase and Lowercase")

text = "Python Programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("\n" + "=" * 50 + "\n")


# =========================================================
# 14. Pattern Matching using re module
# =========================================================

print("14. Pattern Matching using re module")

email = "student@example.com"

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(email_pattern, email):
    print("Valid Email Address")

else:
    print("Invalid Email Address")

digits = "123456"

if re.fullmatch(r'\d+', digits):
    print("The string contains only digits.")

else:
    print("The string does not contain only digits.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 15. Count Vowels and Consonants
# =========================================================

print("15. Count Vowels and Consonants")

text = "Python Programming"

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for char in text:

    if char.isalpha():

        if char in vowels:
            vowel_count += 1

        else:
            consonant_count += 1

print("Vowels Count:", vowel_count)
print("Consonants Count:", consonant_count)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 16. Reverse a String
# =========================================================

print("16. Reverse a String")

text = "Python"

reversed_text = text[::-1]

print("Reversed String:", reversed_text)

print("\n" + "=" * 50 + "\n")
