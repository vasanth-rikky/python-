# =========================================================
# Assignment-5: Class Variables in Python
# =========================================================


# =========================================================
# 1. Define and Access via Class
# =========================================================

print("1. Define and Access via Class")


class Company:

    company_name = "Bright IT"


print("Access using class name:")
print(Company.company_name)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Access via Object (Instance)
# =========================================================

print("2. Access via Object (Instance)")

company_object = Company()

print("Access using object:")
print(company_object.company_name)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Modify Class Variable via Instance
# =========================================================

print("3. Modify Class Variable via Instance")

instance_one = Company()

# Modifying using instance
instance_one.company_name = "Tech Solutions"

print("Value using instance:")
print(instance_one.company_name)

print("Value using class:")
print(Company.company_name)

print("\nExplanation:")
print("Modifying through instance creates a new instance variable.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Modify Class Variable via Class
# =========================================================

print("4. Modify Class Variable via Class")

# Modifying class variable using class name
Company.company_name = "Global Tech"

instance_two = Company()
instance_three = Company()

print("Access using class:")
print(Company.company_name)

print("Access using instance two:")
print(instance_two.company_name)

print("Access using instance three:")
print(instance_three.company_name)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Class Variable vs Instance Variable
# =========================================================

print("5. Class Variable vs Instance Variable")


class Employee:

    # Class variable
    company = "ABC Corporation"

    def __init__(self, name):

        # Instance variable
        self.name = name


employee_one = Employee("John")
employee_two = Employee("Emma")

print("Class Variable:")
print(employee_one.company)
print(employee_two.company)

print("\nInstance Variables:")
print(employee_one.name)
print(employee_two.name)

# Modifying class variable
Employee.company = "XYZ Corporation"

print("\nAfter modifying class variable:")

print(employee_one.company)
print(employee_two.company)

# Modifying instance variable
employee_one.name = "Michael"

print("\nAfter modifying instance variable:")

print(employee_one.name)
print(employee_two.name)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Shared Counter Program
# =========================================================

print("6. Shared Counter Program")


class Student:

    # Class variable
    student_count = 0

    def __init__(self, name):

        self.name = name

        # Increment counter whenever object is created
        Student.student_count += 1


student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

print("Total Students Created:", Student.student_count)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Configuration Setting Example
# =========================================================

print("7. Configuration Setting Example")


class Course:

    # Class variable acting as global configuration
    course_name = "Python Basics"

    def __init__(self, student_name):

        self.student_name = student_name


course1 = Course("David")
course2 = Course("Sophia")

print("Original Course Name:")
print(course1.course_name)
print(course2.course_name)

# Modify configuration using class name
Course.course_name = "Advanced Python"

print("\nUpdated Course Name:")
print(course1.course_name)
print(course2.course_name)

print("\n" + "=" * 50 + "\n")
