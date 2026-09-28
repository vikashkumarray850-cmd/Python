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

# Simple rule:# ==========================================
# Multilevel Inheritance — Practice Questions
# ==========================================

# Q1. Create a class named Grandparent.
# Create a method named house().
# Print "Grandparent has a house".

# Create a class named Parent that inherits from Grandparent.
# Create a method named car().
# Print "Parent has a car".

# Create a class named Child that inherits from Parent.
# Create a method named bike().
# Print "Child has a bike".

# Create a Child object.
# Call house(), car() and bike().

class Grandparent:
    def house(self):
        print("Grandparent has a house")

class Perent(Grandparent):
    def Car(self):
        print("Parent has a car")

class Child(Perent):
    def bike(self):
        print("Child has a bike")

child1 = Child()

child1.house()
child1.Car()
child1.bike()
# ----------------------------------

# Q2. Create a class named Animal.
# Create a method named eat().
# Print "Animal is eating".

# Create a class named Dog that inherits from Animal.
# Create a method named bark().
# Print "Dog is barking".

# Create a class named Puppy that inherits from Dog.
# Create a method named play().
# Print "Puppy is playing".

# Create a Puppy object.
# Call eat(), bark() and play().

# class Animal:
#     def eat(self):
#         print("Animal is eatiing")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Puppy(Dog):
#     def play(self):
#         print("Puppy is playing")

# puppy1 = Puppy()

# puppy1.eat()
# puppy1.bark()
# puppy1.play()

# ------------------------------

# Q3. Create a class named Employee.
# Create a method named work().
# Print "Employee is working".

# Create a class named Manager that inherits from Employee.
# Create a method named manage().
# Print "Manager is managing".

# Create a class named SeniorManager that inherits from Manager.
# Create a method named report().
# Print "Senior Manager is creating a report".

# Create a SeniorManager object.
# Call work(), manage() and report().

# # Ek class → doosri class → teesri class, yani inheritance ki 
# # chain = Multilevel Inheritance.
  


# class Employee:
#     def work(self):
#         print("Employee is working")

# class Manager(Employee):
#     def manage(self):
#         print("Manager is managing")

# class SeniorManager(Manager):
#     def report(self):
#         print("Senior Manager is creating a report")

# seniorManager1 = SeniorManager()

# seniorManager1.work()
# seniorManager1.manage()
# seniorManager1.report()
