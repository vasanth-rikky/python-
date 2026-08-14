# =========================================================
# Assignment-3: Loops & Control Flow in Python
# =========================================================


# =========================================================
# 1. Print a Message Multiple Times
# =========================================================

print("1. Print a Message Multiple Times")

for i in range(10):
    print("Bright IT Career")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Print Numbers Using While Loop
# =========================================================

print("2. Print Numbers Using While Loop")

number = 1

while number <= 20:
    print(number)
    number += 1

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Equal and Not Equal Check
# =========================================================

print("3. Equal and Not Equal Check")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

print("Using != operator:", num1 != num2)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Odd and Even Numbers
# =========================================================

print("4. Odd and Even Numbers from 1 to 50")

for num in range(1, 51):

    if num % 2 == 0:
        print(num, "- Even")
    else:
        print(num, "- Odd")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Largest Among Three Numbers
# =========================================================

print("5. Largest Among Three Numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

print("Largest Number:", largest)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Even Numbers in a Range
# =========================================================

print("6. Even Numbers Between 10 and 20")

num = 10

while num <= 20:

    if num % 2 == 0:
        print(num)

    num += 1

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Armstrong Number
# =========================================================

print("7. Armstrong Number Check")

number = int(input("Enter a number: "))

temp = number
digits = len(str(number))
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if number == sum_of_powers:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Prime Number Check
# =========================================================

print("8. Prime Number Check")

number = int(input("Enter a number: "))

if number > 1:

    is_prime = True

    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a Prime Number.")
    else:
        print(number, "is not a Prime Number.")

else:
    print(number, "is not a Prime Number.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 9. Palindrome Check
# =========================================================

print("9. Palindrome Check")

number = input("Enter a number: ")

if number == number[::-1]:
    print(number, "is a Palindrome.")
else:
    print(number, "is not a Palindrome.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 10. Even or Odd (Using Conditions)
# =========================================================

print("10. Even or Odd Check")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even.")
else:
    print(number, "is Odd.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 11. Gender Identification
# =========================================================

print("11. Gender Identification")

gender = input("Enter gender (M/F): ").upper()

if gender == "M":
    print("Male")

elif gender == "F":
    print("Female")

else:
    print("Invalid Input")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 12. Multiplication Table Generator
# =========================================================

print("12. Multiplication Table Generator")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 13. Count Digits in a Number
# =========================================================

print("13. Count Digits in a Number")

number = int(input("Enter a number: "))

count = 0

temp = abs(number)

if temp == 0:
    count = 1

else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of Digits:", count)

print("\n" + "=" * 50 + "\n")
