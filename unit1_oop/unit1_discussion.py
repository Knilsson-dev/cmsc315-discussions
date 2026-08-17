"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Motorcycles:
    wheels = 2

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def  get_info(self):
        return (self.make, self.model, self.year)





# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class EngineType(Motorcycles):
    fuel_type = "Gasoline"

    def __init__(self, make, model, year, engine_type, engine_size):
        super().__init__(make, model, year)
        self.engine_type = engine_type
        self.engine_size = engine_size

    def get_engine_info(self):
        return (self.engine_type, self.engine_size)

    def get_info(self):
        return (self.make, self.model, self.year, self.engine_type, self.engine_size)








# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    bike1 = EngineType("Honda", "CBR600RR", 2023, "Inline-4", 0.6)
    bike2 = EngineType("Harley-Davidson", "Street Glide", 2014, "V-twin", 1.868 )
    #Access the class variable through the class itself
    print(f"Fuel Type: {EngineType.fuel_type}")
    #Access the same class variable through an object
    print(f"Bike 1 Fuel Type: {bike1.fuel_type}")
    #Add a new attribute to only one object after it is created
    bike1.turbo = True
    #Display each objects namespace using __dict__
    print(f"Bike 1: {bike1.__dict__}")
    print(f"Bike 2: {bike2.__dict__}")
    #Display information about the class namespace
    print(f"Engine Type Dict: {EngineType.__dict__}")



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.
import copy
def demonstrate_copying():
   bike1 = EngineType("Honda", "CBR600RR", 2023, "Inline-4", 0.6)
   bike1.mods = ["exhaust", "tires"]
    #Shallow copy of bike 1
   bike3 = copy.copy(bike1)
    #Deepcopy of bike 1
   bike4 = copy.deepcopy(bike1)
    #Modifying the original object nested data
   bike1.mods.append("frame sliders")

    #Displaying the orignal object as well as the shallow and deep copy
   print(f"Original (bike1): {bike1.get_info()}, mods: {bike1.mods}")
   print(f"Shallow Copy (bike3): {bike3.get_info()}, mods: {bike3.mods}")
   print(f"Deep Copy (bike4): {bike4.get_info()}, mods: {bike4.mods}")




# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    bike = Motorcycles("Yamaha", "YZ250", 2023)
    print(bike.get_info())
    print(f"Wheels: {bike.wheels}")

    print("\nTODO: Create and test your child object")
    bike = EngineType("Yamaha", "YZ250", 2023, "4 stroke", 250)

    print(bike.get_engine_info())

    print(bike.get_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()