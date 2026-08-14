# =========================================================
# Assignment-8: Encapsulation & Data Control in Python
# =========================================================


# =========================================================
# 1. Create a Simple Class
# =========================================================

print("1. Create a Simple Class")


class Student:

    def set_values(self, name, age):

        self.name = name
        self.age = age

    def get_values(self):

        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student()

student1.set_values("John", 21)

student1.get_values()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Validation Using Methods
# =========================================================

print("2. Validation Using Methods")


class ValidStudent:

    def set_values(self, name, age):

        self.name = name

        if age > 0:
            self.age = age
        else:
            print("Invalid age. Age should be greater than 0.")
            self.age = None

    def get_values(self):

        print("Name:", self.name)
        print("Age:", self.age)


student2 = ValidStudent()

student2.set_values("Emma", -5)

student2.get_values()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Property Decorator
# =========================================================

print("3. Property Decorator")


class PropertyStudent:

    def __init__(self, name, age):

        self.name = name
        self._age = None

        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value > 0:
            self._age = value

        else:
            print("Invalid age. Age should be greater than 0.")


student3 = PropertyStudent("Sophia", 22)

print("Student Age:", student3.age)

student3.age = -10

print("Updated Age:", student3.age)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Read-Only Property
# =========================================================

print("4. Read-Only Property")


class Employee:

    def __init__(self, employee_id):

        self._id = employee_id

    @property
    def employee_id(self):
        return self._id


employee = Employee(101)

print("Employee ID:", employee.employee_id)

# employee.employee_id = 200
# This will raise an error because no setter is defined.

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Bank Account System
# =========================================================

print("5. Bank Account System")


class BankAccount:

    def __init__(self, account_holder, balance=0):

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print("Deposited:", amount)

        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient balance.")

        elif amount <= 0:
            print("Invalid withdrawal amount.")

        else:

            self.balance -= amount

            print("Withdrawn:", amount)

    def display_balance(self):

        print("Current Balance:", self.balance)


account = BankAccount("Michael", 1000)

account.deposit(500)

account.withdraw(300)

account.withdraw(2000)

account.display_balance()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Internal Variables
# =========================================================

print("6. Internal Variables")


class InternalExample:

    def __init__(self):

        self.public_variable = "Public Variable"

        self._internal_variable = "Internal Variable"


example = InternalExample()

print("Public Variable:", example.public_variable)

# Internal variable can still be accessed
print("Internal Variable:", example._internal_variable)

print("\nNote:")
print("Variables with '_' are meant for internal use only.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Computed Property
# =========================================================

print("7. Computed Property")


class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    @property
    def area(self):

        return self.length * self.width


rectangle = Rectangle(10, 5)

print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.area)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Password Validation System
# =========================================================

print("8. Password Validation System")


class PasswordValidator:

    def __init__(self, password):

        self.password = password

    def validate_password(self):

        has_number = any(char.isdigit() for char in self.password)

        if len(self.password) >= 8 and has_number:
            print("Valid Password")

        else:
            print("Invalid Password")
            print("Password must be at least 8 characters long")
            print("and contain at least one number.")


password1 = PasswordValidator("Python123")

password1.validate_password()

password2 = PasswordValidator("hello")

password2.validate_password()

print("\n" + "=" * 50 + "\n")
