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

class Student():
    def __init__(self, name, mark1, mark2, mark3):
        self.name =name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def average(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        print("Name:", self.name)
        print("Average:", average)
    
student1 = Student("Manu", 40, 50 ,60)
student2 = Student("Syam", 37,67,49)

student1.average()
student2.average()

