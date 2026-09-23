# #  OOP (OBJECT-ORIENTED PROGRAMMING) ⏳

# OOP ko sabse pehle simple example se samjho

# Maan lo hume students ka data manage karna hai.

# Har student ke paas kuch information ho sakti hai:

# Name
# Age
# City

# Agar hum normal variables se karein:

# name1 = "Ravi"
# age1 = 25
# city1 = "Kolkata"

# name2 = "Mohit"
# age2 = 23
# city2 = "Delhi"

# Agar 100 students ho gaye, toh bahut saare variables manage karne padenge. 😵

# OOP isi problem ko organize karne mein help karta hai.

# 1. Class kya hai?

# Class ko blueprint/design samjho.

# Jaise ghar banane se pehle ek blueprint hota hai:

# House Blueprint
#      ↓
#   Rooms
#   Doors
#   Windows

# Blueprint khud ghar nahi hai.

# Waise hi:

# class Student:
#     pass

# Yahan Student ek Class hai.

# Class basically batati hai:

# "Student naam ki cheez ke andar hum kya-kya rakhenge aur kya-kya kaam karwa sakte hain."

# 2. Object kya hai?

# Ab isi Student class se actual students bana sakte hain.

# class Student:
#     pass

# student1 = Student()
# student2 = Student()

# Yahan:

# Student       → Class
# student1      → Object
# student2      → Object

# Socho:

#              Student
#               CLASS
#                 │
#        ┌────────┴────────┐
#        ↓                 ↓
#    student1           student2
#     OBJECT              OBJECT

# Ek class se multiple objects ban sakte hain.

# 3. Student() ka kya matlab hai?

# Ye bahut important hai.

# student1 = Student()

# Student() ka matlab hai:

# Student class ka ek naya object banao.

# Aur us object ko student1 naam se store karo.

# Phir:

# student2 = Student()

# ek doosra object ban gaya.

# 4. Real-life example
# Class = Student ka blueprint

#        Student
#           │
#     ┌─────┼─────┐
#     ↓     ↓     ↓
#   Ravi  Mohit  Aman

# Yahan Student class hai aur Ravi, Mohit, Aman ko hum objects ke roop mein soch sakte hain.

# 5. Abhi ek confusion clear karte hain

# Tumne dekha:

# class Student:
#     pass

# Abhi class ke andar kuch nahi hai.

# pass ka matlab:

# "Abhi class ke andar koi code nahi likhna hai."

# Baad mein hum class ke andar data aur functions (methods) rakhenge.

# Example future mein kuch aisa hoga:

# class Student:
#     # data
#     # methods

# Lekin abhi hum __init__ par nahi jayenge.

# OOP ka roadmap

# Hum OOP ko is order mein karenge:

# 17. OOP
# │
# ├── 1. Class & Object          ← abhi
# │
# ├── 2. __init__                ← baad mein
# │
# ├── 3. Attributes
# │
# ├── 4. Methods
# │
# ├── 5. Inheritance
# │
# ├── 6. Encapsulation
# │
# └── 7. Polymorphism

# Abhi sirf Class & Object ko strong karenge.

# Aur practice bhi 2 questions nahi, pehle basic → medium → थोड़ा practical karke 3–4 questions karenge. Lekin ek saath concept overload nahi karenge.

# Abhi ke liye sabse important line yaad rakho:

# Class = Blueprint
# Object = Class se bana actual instance

# Agar ye difference clear hai, tab hum Class & Object ka practical part karenge.

# ==========================================
# OOP — Class & Object
# ==========================================

# Q1. Create a class named Student.
# Create one object of the Student class.
# Print the object.

# class Student:
#     pass

# student1 = Student()

# ==========================================
# OOP — Object Attributes
# ==========================================

# Q1. Create a class named Student.
# Create one object named student1.
# Add name and age to the object.
# Print the name and age.

# class student:
#     pass

# student1 = student()

# student1.name = "Vilash"
# student1.age = 25

# print(student1.name)
# print(student1.age)

# Q2. Create a class named Employee.
# Create one object named employee1.
# Add name, salary and city to the object.
# Print all three attributes.

# class employee:      #→ EMPLOYEE CLASS BANAYI.
#     pass

# employee1 = employee()    #→ EMPLOYEE1 OBJECT BANAYA.

# employee1.name = "Mohit"
# employee1.salary = 50000   #→ OBJECT KE ANDAR 3 ATTRIBUTES ADD KIYE.
# employee1.city = "Mumbai"

# print(employee1.name)
# print(employee1.salary)      #→ ATTRIBUTES KO ACCESS KARKE PRINT KIYA
# print(employee1.city)


# Q3. Create a class named Product.
# Create two object named product1 & product2.
# Add product_name and price to the object.
# Print both attributes.

# class product :
#     pass

# product1 = product()
# product2 = product()

# product1.name = "Rice"
# product1.price = 100

# product2.name = "Dal"
# product2.price = 200

# print(product1.name)
# print(product1.price)

# print(product2.name)
# print(product2.price)
#-----------------------------------------------------------------------------------------

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

#===============================================================================

# ==========================================
# OOP — Methods Practice
# ==========================================

# OOP — Methods

# Abhi class ke andar hum data rakh rahe the:

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Ab maan lo Student kuch kaam bhi kar sake, jaise:

# Student
# ├── name
# ├── age
# └── introduce()  ← kaam

# Class ke andar banaya hua function method kehlata hai.

# Example:

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("My name is", self.name)

# Object:

# student1 = Student("Vikash", 25)

# student1.introduce()

# Output:

# My name is Vikash
# Yahan kya hua?
# def introduce(self):

# Ye class ke andar ek method hai.

# Aur:

# student1.introduce()

# se hum us method ko object ke through call kar rahe hain.

# Abhi ek important cheez notice karo:

# self.name

# self ki wajah se method ko pata hai ki kis object ka name use karna hai.

# Agar:

# student2 = Student("Ravi", 23)
# student2.introduce()

# toh Ravi ka name print hoga.

# Short mein:

# Attribute = object ka data
# Method = object ka kaam/function

# ==========================================
# OOP — Methods Practice
# ==========================================

# Q1. Create a class named Student.
# Use __init__() to store name and age.
# Create a method named introduce().
# The method should print the student's name and age.
# Create one Student object and call the introduce() method.

# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print("Name:",self.name)
#         print("Age",self.age)

# student1 = Student("vikash", 25)
# student1.introduce()

#-------------------------------------------------
# Q2. Create a class named Employee.
# Use __init__() to store name and salary.
# Create a method named show_salary().
# The method should print the employee's name and salary.
# Create two Employee objects and call the method for both.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def show_salary(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# employee1 = Employee("Virat", 10000)
# employee2 = Employee("Rohit", 9500)

# employee1.show_salary()
# employee2.show_salary()


#-------------------------------------------

# Q3. Create a class named Product.
# Use __init__() to store product_name and price.
# Create a method named show_product().
# The method should print the product name and price.
# Create two Product objects and call the method for both.

# class Product:
#     def __init__(self,product_name,price):
#         self.product_name = product_name
#         self.price = price
    
#     def show_product(self):
#         print("Name:", self.product_name)
#         print("Price:", self.price)

# product1 = Product("Egg", 7)
# product2 = Product("Maggi", 14)

# product1.show_product()
# product2.show_product()

# ==========================================


# Q4 Create a class named Car.
# Use __init__() to store brand and price.
# Create three Car objects with different values.
# Create a method named show_car() inside the class.
# The method should print the brand and price.
# Call the show_car() method for all three objects.

# class Car:

#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
    
#     def brand_name(self):
#         print("Brand:", self.brand)
#         print("Price:", self.price)

# Car1 = Car("Audi", 200000)
# Car2 = Car("BMW 7s", 400000)
# Car3 = Car("Porsche", 6000000)

# Car1.brand_name()
# Car2.brand_name()
# Car3.brand_name()

#--------------------------------------------------------------------------------------

# ==========================================
# OOP — Method with Calculation
# ==========================================

# Method ke andar calculation

# Abhi tak humne method mein sirf print kiya:

# def show_salary(self):
#     print("Salary:", self.salary)

# Ab method ke andar self.salary se calculation kar sakte hain.

# Example:

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def bonus(self):
#         bonus = self.salary * 10 / 100
#         print("Bonus:", bonus)

# Agar:

# employee1 = Employee("Ravi", 50000)
# employee1.bonus()

# to method self.salary यानी 50000 ko lekar 10% bonus calculate karega.

# Bas abhi itna concept samjho.


# ==========================================
# OOP — Methods with Calculation
# ==========================================

# Q1. Create a class named Employee.
# Use __init__() to store name and salary.
# Create a method named bonus().
# The method should calculate a 10% bonus from the salary.
# Print the bonus for two Employee objects.

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def bonus(self):
#         bonus = self.salary * 10 / 100
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Bonus:", bonus)


# employee1 = employee("Mathur", 25000)
# employee2 = employee("Vivek", 40000)

# employee1.bonus()
# employee2.bonus()

# Q2. Create a class named Product.
# Use __init__() to store product_name and price.
# Create a method named discount().
# The method should calculate a 20% discount on the price.
# Print the discount for two Product objects.

# class product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def discount(self):
#         discount = self.price * 20 / 100
#         print("Discount:", discount)

#     def product_name(self):
#         print("Name:",self.name)
#         print("Price:", self.price)
    
# product1 = product("Rice", 200)
# product2 = product("Dal", 300)

# product1.discount()
# product2.discount()

# product1.product_name()
# product2.product_name()



# Q3. Create a class named Student.
# Use __init__() to store name, marks1, marks2 and marks3.
# Create a method named average().
# The method should calculate the average of the three marks.
# Print the average for two Student objects.

# class Student():
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name =name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
    
#     def average(self):
#         average = (self.mark1 + self.mark2 + self.mark3) / 3
#         print("Name:", self.name)
#         print("Average:", average)
    
# student1 = Student("Manu", 40, 50 ,60)
# student2 = Student("Syam", 37,67,49)

# student1.average()
# student2.average()

#--------------------------------------------------------------------------------------

#INHERITANCE

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

class Product:
    def __init__(self,product_name, price ):
        self.product_name = product_name
        self.price = price
    
    def show_product(self):
        print("Product:", self.product_name)
        print("Price:", self.price)

class ElectronicProduct(Product):
    def category(self):
        print("This is an electronic product")

ElectronicProduct1 = ElectronicProduct("Air Condition", 50000)

ElectronicProduct1.show_product()
ElectronicProduct1.category()




