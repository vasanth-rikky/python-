# =========================================================
# Assignment-9: Abstract Classes in Python
# =========================================================

from abc import ABC, abstractmethod
import math


# =========================================================
# 1. Abstract and Non-Abstract Methods
# =========================================================

print("1. Abstract and Non-Abstract Methods")


class Animal(ABC):

    # Abstract Method
    @abstractmethod
    def sound(self):
        pass

    # Non-Abstract Method
    def sleep(self):
        print("Animal is sleeping")


# =========================================================
# 2. Create a Child Class
# =========================================================

print("\n2. Create a Child Class")


class Dog(Animal):

    # Implementing abstract method
    def sound(self):
        print("Dog barks")


# =========================================================
# 3. Access Non-Abstract Method via Child Object
# =========================================================

print("\n3. Access Non-Abstract Method via Child Object")

dog = Dog()

dog.sleep()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Call Abstract Method Implementation
# =========================================================

print("4. Call Abstract Method Implementation")

dog.sound()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Attempt to Instantiate Abstract Class
# =========================================================

print("5. Attempt to Instantiate Abstract Class")

try:

    animal = Animal()

except TypeError as error:

    print("Error:", error)

print("\nExplanation:")
print("Abstract classes cannot be instantiated directly")
print("because abstract methods are incomplete.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Multiple Abstract Methods
# =========================================================

print("6. Multiple Abstract Methods")


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def vehicle_info(self):
        print("This is a vehicle")


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


car = Car()

car.vehicle_info()
car.start()
car.stop()

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Real-World Example
# =========================================================

print("7. Real-World Example")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("Calculating Area")


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return math.pi * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width


# Circle Object
circle = Circle(5)

circle.display()

print("Circle Area:", circle.area())

print("\n" + "-" * 50 + "\n")

# Rectangle Object
rectangle = Rectangle(10, 4)

rectangle.display()

print("Rectangle Area:", rectangle.area())

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Partial Implementation
# =========================================================

print("8. Partial Implementation")


class PartialVehicle(Vehicle):

    # Only one abstract method implemented
    def start(self):
        print("Partial Vehicle Started")


try:

    partial_object = PartialVehicle()

except TypeError as error:

    print("Error:", error)

print("\nExplanation:")
print("The class cannot be instantiated because")
print("not all abstract methods are implemented.")

print("\n" + "=" * 50 + "\n")
