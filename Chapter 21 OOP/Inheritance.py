#INHERITANCE

# Inheritance
# │
# ├── Basic Inheritance          ✅
# ├── Child Method               ✅
# ├── __init__()                 ✅
# ├── super()                    ✅
# ├── Method Overriding          ✅
# ├── Multilevel Inheritance     ✅
# └── Multiple Inheritance       ✅

# ==========================================
# Inheritance — Basic Practice
# ==========================================

# Socho:

# Parent = Father
# Child = Son

# Agar Father ke paas koi property/feature hai, to Son usko use kar sakta hai.

# Python mein bhi same idea hai.

# class Father:
#     def car(self):
#         print("Father has a car")


# class Son(Father):
#     pass

# Yahan:

# class Son(Father):

# iska simple meaning hai:

# Son class, Father class ki cheezein le sakti hai.

# Ab:

# son1 = Son()
# son1.car()

# Output:

# Father has a car

# Dhyan do — car() method Son ke andar likha hi nahi hai.

# Phir bhi:

# son1.car()

# kaam kar raha hai.

# Kyun?

# Kyuki Son ne Father se car() method inherit kiya hai.

# Ek line mein
# Father
#   ↓
# Son

# Father ka method → Son use kar sakta hai.

# ==========================================
# Inheritance — Basic Practice
# ==========================================

# Q1. Create a class named Parent.
# Create a method named show_message().
# Print "This is Parent class" inside the method.
#
# Create another class named Child that inherits from Parent.
# Create a Child object.
# Call show_message() using the Child object.

# class Parent:
#     def show_message(self):
#         print("This is Parent class")

# class Child(Parent):
#     pass

# child1 = Child()
# child1.show_message()

#-------------------------------------

# Q2. Create a class named Animal.
# Create a method named eat().
# Print "Animal is eating" inside the method.
#
# Create another class named Dog that inherits from Animal.
# Create a Dog object.
# Call the eat() method using the Dog object.

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     pass

# dog1 = Dog()
# dog1.eat()

#---------------------------------------------------

# Q3. Create a class named Employee.
# Create a method named company().
# Print "Employee works in a company" inside the method.
#
# Create another class named Manager that inherits from Employee.
# Create a Manager object.
# Call the company() method using the Manager object.

# class Employee:
#     def company(self):
#         print("Employee works in a company")
    
# class Manager(Employee):
#     pass

# manager1= Manager()
# manager1.company()

#---------------------------------------------------------------------------
# ==========================================
# Inheritance — Parent + Child Methods
# ==========================================

# Ab next step: Child class ka apna method + Parent ka inherited method.

# Example:

# class Animal:
#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")


# dog1 = Dog()

# dog1.eat()    # Parent ka method
# dog1.bark()   # Child ka apna method

# Yahan Dog ke paas 2 methods hain:

# eat()  → Parent se inherited
# bark() → Child ka apna

# Iska matlab Child class Parent ki cheezein use bhi kar 
# sakti hai aur apni nayi cheezein bhi bana sakti hai.

# ==========================================
# Inheritance — Parent + Child Methods
# ==========================================

# Q1. Create a class named Animal.
# Create a method named eat().
# Print "Animal is eating" inside the method.
#
# Create a class named Dog that inherits from Animal.
# Create a method named bark() inside Dog.
# Print "Dog is barking" inside the method.
#
# Create a Dog object.
# Call both eat() and bark() using the Dog object.

# class Animal:
#     def eat(self):
#         print("Animal is eating")
    
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# dog1 = Dog()

# dog1.eat()
# dog1.bark()

# Q2. Create a class named Employee.
# Create a method named work().
# Print "Employee is working" inside the method.
#
# Create a class named Manager that inherits from Employee.
# Create a method named manage().
# Print "Manager is managing the team" inside the method.
#
# Create a Manager object.
# Call both work() and manage() using the Manager object.

# class Employee:
#     def work(self):
#         print("Employee is working")

# class Manager(Employee):
#     def manage(self):
#         print("Manager is managing the team")

# manager1 = Manager()

# manager1.work()
# manager1.manage()


# Q3. Create a class named Vehicle.
# Create a method named start().
# Print "Vehicle is starting" inside the method.
#
# Create a class named Car that inherits from Vehicle.
# Create a method named drive().
# Print "Car is driving" inside the method.
#
# Create a Car object.
# Call both start() and drive() using the Car object.

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")
    
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
    
# car1 =Car()

# car1.start()
# car1.drive()
#------------------------------------------------------------------------------------------------------------
# ==========================================
# Inheritance + __init__() — Practice
# ==========================================

# Ab hum Inheritance + __init__() ko slowly samjhenge.

# Pehle ye example dekho:

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def work(self):
#         print(self.name, "is working")


# class Manager(Employee):
#     pass


# manager1 = Manager("Vikash")

# manager1.work()

# Yahan Manager ke andar __init__() nahi hai.

# Lekin Manager ne Employee se inherit kiya hai, 
# isliye Manager Parent ka __init__() bhi use kar sakta hai.

# Flow:

# Employee
#   ├── __init__()
#   └── work()
#        ↓
# Manager
#        ↓
# manager1

# Isliye:

# manager1 = Manager("Vikash")

# mein "Vikash" Parent ke __init__() mein chala jata hai.

# Aur:

# manager1.work()

# Parent ka work() method use karta hai.

# ==========================================
# Inheritance + __init__() — Practice
# ==========================================

# Q1. Create a class named Employee.
# Use __init__() to store the employee's name.
# Create a method named work().
# Print the employee's name and "is working".
#
# Create a class named Manager that inherits from Employee.
# Create a Manager object with a name.
# Call the work() method using the Manager object.

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def work(self):
#         print(self.name, "is working")

# class Manager(Employee):
#     pass

# manager1 =Manager("Vikash")

# manager1.work()
#------------------------------------------
# Q2. Create a class named Animal.
# Use __init__() to store the animal's name.
# Create a method named show_name().
# Print the animal's name.
#
# Create a class named Dog that inherits from Animal.
# Create a method named bark().
# Print "Dog is barking".
#
# Create a Dog object with a name.
# Call both show_name() and bark().

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show_name(self):
#         print("Name:", self.name)

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")


# dog1 = Dog("Tommy")

# dog1.show_name()
# dog1.bark()


# Q3. Create a class named Product.
# Use __init__() to store product_name and price.
# Create a method named show_product().
# Print the product name and price.
#
# Create a class named ElectronicProduct that inherits from Product.
# Create a method named category().
# Print "This is an electronic product".
#
# Create an ElectronicProduct object with a product name and price.
# Call both show_product() and category().

# class Product:
#     def __init__(self, product_name, price):
#         self.product_name = product_name
#         self.price = price

#     def show_product(self):
#         print("product_name:",self.product_name )
#         print("Price:", self.price)

# class ElectronicProduct(Product):
#     def category(self):
#         print("This is an electronic product")

# product1 = ElectronicProduct("Air Condition", 40000)

# product1.show_product()
# product1.category()