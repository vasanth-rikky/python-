# =========================================================
# Assignment-7: Inheritance & Polymorphism in Python
# =========================================================


# =========================================================
# 1. Create Class Hierarchy
# 2. Define Methods
# 7. Method Call Order
# =========================================================

class A:

    def __init__(self):

        self.value = "Value from Class A"

        print("Constructor of Class A called")

    # Specific Method 1
    def method_a1(self):
        print("Specific Method A1")

    # Specific Method 2
    def method_a2(self):
        print("Specific Method A2")

    # Common Method
    def common_method(self):
        print("Common Method from Class A")


class B(A):

    def __init__(self):

        super().__init__()

        self.value = "Value from Class B"

        print("Constructor of Class B called")

    # Specific Method 1
    def method_b1(self):
        print("Specific Method B1")

    # Specific Method 2
    def method_b2(self):
        print("Specific Method B2")

    # Overridden Method
    def common_method(self):

        print("Common Method from Class B")

        # Calling parent method
        super().common_method()


class C(B):

    def __init__(self):

        super().__init__()

        self.value = "Value from Class C"

        print("Constructor of Class C called")

    # Specific Method 1
    def method_c1(self):
        print("Specific Method C1")

    # Specific Method 2
    def method_c2(self):
        print("Specific Method C2")

    # Overridden Method
    def common_method(self):

        print("Common Method from Class C")

        # Calling parent method
        super().common_method()


print("\n" + "=" * 50)
print("3. Object Creation and Method Calls")
print("=" * 50 + "\n")


# =========================================================
# Object of Class A
# =========================================================

print("Creating Object of Class A")

object_a = A()

object_a.method_a1()
object_a.method_a2()
object_a.common_method()

print("\n" + "-" * 50 + "\n")


# =========================================================
# Object of Class B
# =========================================================

print("Creating Object of Class B")

object_b = B()

object_b.method_a1()
object_b.method_a2()

object_b.method_b1()
object_b.method_b2()

object_b.common_method()

print("\n" + "-" * 50 + "\n")


# =========================================================
# Object of Class C
# =========================================================

print("Creating Object of Class C")

object_c = C()

object_c.method_a1()
object_c.method_a2()

object_c.method_b1()
object_c.method_b2()

object_c.method_c1()
object_c.method_c2()

object_c.common_method()

print("\n" + "=" * 50)
print("4. Runtime Polymorphism")
print("=" * 50 + "\n")


# =========================================================
# 4. Superclass Reference Behavior
# =========================================================

reference_a = B()

print("\nCalling common_method() using reference_a:")
reference_a.common_method()

print("\n" + "-" * 50 + "\n")

reference_a = C()

print("Calling common_method() using reference_a:")
reference_a.common_method()

print("\n" + "=" * 50)
print("6. Instance Variables Behavior")
print("=" * 50 + "\n")


# =========================================================
# Accessing instance variables
# =========================================================

print("Object A value:", object_a.value)
print("Object B value:", object_b.value)
print("Object C value:", object_c.value)

print("\nSuperclass Reference Example:")

reference_variable = C()

print(reference_variable.value)

print("\n" + "=" * 50)
print("8. Real-World Example")
print("=" * 50 + "\n")


# =========================================================
# Real-World Example
# Vehicle -> Car -> ElectricCar
# =========================================================

class Vehicle:

    def start_engine(self):
        print("Vehicle engine started")


class Car(Vehicle):

    def start_engine(self):

        print("Car engine started")

        super().start_engine()


class ElectricCar(Car):

    def start_engine(self):

        print("Electric Car started silently")

        super().start_engine()


# Creating object
electric_car = ElectricCar()

electric_car.start_engine()

print("\n" + "=" * 50 + "\n")inhe
