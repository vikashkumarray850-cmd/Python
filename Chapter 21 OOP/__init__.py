# __init__() — CONSTRUCTOR

# YAHIN SE OOP KA ACTUAL POWERFUL PART START HOTA HAI. 
# ISKO BHI SLOWLY, EXAMPLE KE SAATH SAMJHENGE.

# __init__() kya karta hai?

# Abhi hum object banane ke baad data alag-alag likh rahe the:

# class Student:
#     pass

# student1 = Student()

# student1.name = "Ravi"
# student1.age = 25

# Problem ye hai ki agar bahut saare students hon, 
# toh har object ke liye baar-baar attributes likhne padenge.

# __init__() se hum object create hote hi uska data set kar sakte hain.

# Example:

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Ab object banate waqt:

# student1 = Student("Ravi", 25)
# student2 = Student("Mohit", 23)

# Yahan automatically:

# student1
#   name → Ravi
#   age  → 25

# student2
#   name → Mohit
#   age  → 23
# Sabse important line
# def __init__(self, name, age):

# __init__() ek special method hai jo object create hone par automatically call hota hai.

# Aur:

# self.name = name

# ka matlab hai:

# Is particular object ke name attribute mein name ki value rakho.

# Abhi self ko lekar tension mat lo. Usko alag se bahut clearly samjhenge, 
# kyunki ye OOP ka important concept hai.

# Pehle __init__() ka basic flow samjho:

# Student("Ravi", 25)
#         ↓
#    __init__() call
#         ↓
#  name = Ravi
#  age = 25
#         ↓
#    student1 ready

# Abhi practice nahi. Pehle next message mein self ko simple example se samjhenge, 
# phir __init__() ka practice karenge

# ==========================================
# OOP — __init__() & self Practice
# ==========================================

# Q1. Create a class named Student.
# Use __init__() to store name and age.
# Create one Student object with your own values.
# Print the name and age.

# class student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student1 = student("Vikash", 25)

# print(student1.name)
# print(student1.age)

#-------------------------------------------------
# Q2. Create a class named Employee.
# Use __init__() to store name, salary and city.
# Create two Employee objects with different values.
# Print all attributes of both objects.

# class employee:

#     def __init__(self,name,salary,city):
#         self.name = name
#         self.salary = salary
#         self.city = city

# employee1 = employee("Mathur", 30000, "UP")
# employee2 = employee("Narendra", 100000, "Gujrat")

# print(employee1.name)
# print(employee1.salary)
# print(employee1.city)

# print(employee2.name)
# print(employee2.salary)
# print(employee2.city)
#------------------------------------

# Q3. Create a class named Product.
# Use __init__() to store product_name and price.
# Create two Product objects with different products.
# Print the product name and price of both objects.

# class Product:

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# Product1 = Product("Milk", 31)
# Product2 = Product("Dahi", 32)

# print(Product1.name)
# print(Product1.price)

# print(Product2.name)
# print(Product2.price)

#----------------------------------------------------
# Q4. Create a class named Car.
# Use __init__() to store brand and price.
# Create three Car objects with different values.
# Print the brand and price of all three objects.

# class Car:

#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# car1 = Car("Audi", 100000)
# car2 = Car("Maruti", 50000)
# car3 = Car("BMW 7s", 2500000)

# print(car1.brand)
# print(car1.price)

# print(car2.brand)
# print(car2.price)

# print(car3.brand)
# print(car3.price)
