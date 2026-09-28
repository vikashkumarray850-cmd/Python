# ==========================================
# super() — Practice
# ==========================================

# real projects mein super() tab use karte hain jab Child class ko Parent ka 
# existing setup bhi chahiye, aur Child ko apna extra setup bhi karna ho.

# Data Analyst perspective se ek simple example:

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

# Manager ko 3 cheezein chahiye:

# name       → Employee se
# salary     → Employee se
# team_size  → Manager ka extra data

# Isliye:

# super().__init__(name, salary)

# Parent ka existing __init__() reuse karta hai.

# Real-world idea

# Socho company mein already Employee class bani hui hai:

# Employee
# ├── name
# ├── salary
# └── department

# Baad mein Manager banana hai:

# Manager
# ├── name
# ├── salary
# ├── department
# └── team_size

# Agar Parent ka setup already bana hua hai, usko dobara likhne ke bajay super() se reuse kar sakte ho.

# Simple rule:

# Child ka __init__() banaya + Parent ka __init__() bhi chahiye → super().


# ==========================================
# super() — Practice
# ==========================================

# Q1. Create a class named Employee.
# Use __init__() to store name and salary.
#
# Create a class named Manager that inherits from Employee.
# Use __init__() to store name, salary and team_size.
# Use super() to call the Parent class __init__().
#
# Create one Manager object.
# Print the name, salary and team_size.

#SOLUTION-------👇

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

# manager1 = Manager("Vikash", 5000, 5)

# print("Name:",manager1.name)
# print("Salary:",manager1.salary)
# print("Team_size:",manager1.team_size)

#-------------
# Q2. Create a class named Vehicle.
# Use __init__() to store brand and price.
#
# Create a class named Car that inherits from Vehicle.
# Use __init__() to store brand, price and fuel_type.
# Use super() to call the Parent class __init__().
#
# Create one Car object.
# Print the brand, price and fuel_type.

class Vehicle:
    def __init__(self, brand , price):
        self.brand = brand
        self.price = price

class Car(Vehicle):
    def __init__(self, brand , price , fuel_type):
        super().__init__(brand, price)
        self.fuel_type = fuel_type

car1 = Car("Audi", 20000, "Petrol")
car2 = Car("BMW 7s", 67999, "Disel")

print("Brand:",car1.brand)
print("Price:",car1.price)
print("Fuel_type:",car1.fuel_type)

print("Brand:",car2.brand)
print("Price:",car2.price)
print("Fuel_type:",car2.fuel_type)







#------------

# Q3. Create a class named Student.
# Use __init__() to store name and age.
#
# Create a class named CollegeStudent that inherits from Student.
# Use __init__() to store name, age and course.
# Use super() to call the Parent class __init__().
#
# Create one CollegeStudent object.
# Print the name, age and course.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# class CollegeStudent(Student):
#     def __init__(self, name, age, course):
#         super().__init__(name,age)
#         self.course =course

# student1 = CollegeStudent("Vipin", 24, "DA")

# print("Name:",student1.name)
# print("Age:",student1.age)
# print("Course:",student1.course)
