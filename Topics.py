#What is OOP?
# Object-Oriented Programming
#(OOP) is a programming paradigm that uses "objects" to design applications and computer programs.
#It utilizes several key concepts, including encapsulation, inheritance, polymorphism, and abstraction.
#OOP allows for organizing code into reusable components,
#which can make programs easier to manage and extend.

# Example of OOP in Python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.speak()) 
#------------------------------------------------------------------------------------------------------------------------------
#What is a Class?
#A class is a blueprint for creating objects. 
#It defines a set of attributes and methods that the created objects will have.
#Classes encapsulate data for the object and the methods that operate on that data.
# Example of a Class
class Car:
    def __init__(self, make, model):
        self.make = make  
        self.model = model  

    def display_info(self):  
        return f"{self.make} {self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.display_info())  
#-------------------------------------------------------------------------------------------------------------------------------

#What is an Object?
#An object is an instance of a class. It contains data (attributes) and methods (functions) that can manipulate that data.
#Each object can hold different values for its attributes.
# Continuing from the Car class example
another_car = Car("toyota", "porcha")  
print(another_car.display_info())
#-------------------------------------------------------------------------------------------------------------------------------

#What is a Constructor?
#A constructor is a special method called when an object is instantiated. 
#In Python, the constructor method is defined using __init__(). It initializes the object's attributes.
# Example of a Constructor
class Person:
    def __init__(self, name, age):  
        self.age = age

    def display(self):
        return f"{self.name} is {self.age} years old."


person1 = Person("Alice", 30)
print(person1.display()) 
#-------------------------------------------------------------------------------------------------------------------------------
#What is Inheritance?
#Inheritance is a mechanism where a new class inherits properties and behaviors (methods) from an existing class.
#This promotes code reusability and establishes a relationship between classes.
# Example of Inheritance
class Vehicle:  
    def __init__(self, wheels):
        self.wheels = wheels

class Bike(Vehicle): 
    def __init__(self, wheels, type_of_bike):
        super().__init__(wheels)  
        self.type_of_bike = type_of_bike


my_bike = Bike(2, "Mountain")
print(f"My bike has {my_bike.wheels} wheels and is a {my_bike.type_of_bike} bike.") 
#-------------------------------------------------------------------------------------------------------------------------------
#What is Concatenation?
#Concatenation refers to joining two or more strings together to form a single string. 
#In Python, this can be done using the + operator. 

# Example of String Concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2  
print(result) 
#-------------------------------------------------------------------------------------------------------------------------------
#What is the self keyword in a Class?
#The self keyword in Python refers to the instance of the class itself. 
#It allows access to the attributes and methods of the class in Python. It must be the first parameter of any method in the class.
# Example using self keyword
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
print(counter.get_count())
#-------------------------------------------------------------------------------------------------------------------------------
#What is File Handling?
#File Handling in programming refers to the process of creating, reading, writing, 
#and deleting files on a storage medium. Python provides built-in functions to handle files.
# Example of File Handling in Python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, World!
#-------------------------------------------------------------------------------------------------------------------------------
#What is NumPy?
#NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides support for arrays, matrices, 
#and many mathematical functions to operate on these data structures efficiently.
# Example of using NumPy
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)  
squared_array = array ** 2
print("Squared Array:", squared_array)  















