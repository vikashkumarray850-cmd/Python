# ==========================================
# METHOD OVERRIDING ✔️👍❤️
# ==========================================

# Socho Parent kehta hai:

# Animal → "Main sound karta hoon"

# Lekin Dog apna specific sound batana chahta hai:

# Dog → "Main bark karta hoon"

# Python mein:

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# Dhyan do — dono classes mein same naam sound() hai.

# Ab:

# animal1 = Animal()
# dog1 = Dog()

# animal1.sound()
# dog1.sound()

# Output:

# Animal makes a sound
# Dog barks
# Yahan actual mein kya hua?

# Dog ne Parent ka sound() delete nahi kiya.

# Bas Child ne bola:

# "Agar Dog ka sound() poocha jaaye, toh mera wala use karo."

# Isliye:

# dog1.sound()

# → Dog ka sound() chalega.

# Aur:

# animal1.sound()

# → Animal ka sound() chalega.

# Ek line mein

# Parent aur Child mein same method name ho, aur Child apna 
# version define kare → Method Overriding.

# ==========================================
# Method Overriding — Practice Questions
# ==========================================

# Q1. Create a class named Animal.
# Create a method named sound().
# Print "Animal makes a sound".
#
# Create a class named Dog that inherits from Animal.
# Create the same sound() method inside Dog.
# Print "Dog barks".
#
# Create a Dog object.
# Call the sound() method.

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#       print("Dog barks")  

# dog1 = Dog()
# animal1 = Animal()

# animal1.sound()
# dog1.sound()

#-----------------------

# Q2. Create a class named Employee.
# Create a method named work().
# Print "Employee is working".
#
# Create a class named Manager that inherits from Employee.
# Create the same work() method inside Manager.
# Print "Manager is managing".
#
# Create a Manager object.
# Call the work() method.

# class Employee:
#     def work(self):
#         print("Employee is working")

# class Manager(Employee):
#     def work(self):
#        print("Manager is managing")

# employee1 = Employee()
# manager1 = Manager()

# employee1.work()
# manager1.work()

#------------------------
# Q3. Create a class named Vehicle.
# Create a method named start().
# Print "Vehicle is starting".
#
# Create a class named Car that inherits from Vehicle.
# Create the same start() method inside Car.
# Print "Car engine is starting".
#
# Create a Car object.
# Call the start() method.

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting") 

# class Car(Vehicle):
#     def start(self):
#         print("Car engine is starting") 

# Vehicle1 = Vehicle()
# Car1 = Car()

# Vehicle1.start()
# Car1.start()

#-------------------------------------------------------------------------------------------

# ==========================================
# MULTILEVEL INHERITANCE —
# ==========================================

# Multilevel Inheritance start karte hain.

# Isme inheritance ki chain banti hai:

# Grandparent
#      ↓
#    Parent
#      ↓
#    Child

# Example:

# class Grandparent:
#     def house(self):
#         print("Grandparent has a house")


# class Parent(Grandparent):
#     def car(self):
#         print("Parent has a car")


# class Child(Parent):
#     def bike(self):
#         print("Child has a bike")


# child1 = Child()

# child1.house()
# child1.car()
# child1.bike()

# Output:

# Grandparent has a house
# Parent has a car
# Child has a bike
# Yahan kya hua?

# Child ne directly Grandparent se inheritance nahi li.

# Child(Parent)

# Aur Parent ne:

# Parent(Grandparent)

# Isliye chain ke through Child ko dono ke methods mil gaye.
#------------------------------------------------------------------------------------------

