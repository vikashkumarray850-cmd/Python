# ==========================================
# Encapsulation — Private Attribute Practice
# ==========================================


# Encapsulation — Progress
# Private Attribute              ✅
# Class ke andar Access          ✅
# Method se Update               ✅
# Data Validation                ✅
# Getter                         ✅
# Setter                         ✅

# ENCAPSULATION KYA HOTA HAI?

# Simple language mein:

# Encapsulation = data aur us data par kaam karne wale methods ko ek class ke 
# andar rakhna, aur zarurat ke hisaab se data ko protect/control karna.

# Real-life example:

# Socho Bank Account hai.

# Tumhare account ka balance important/private data hai. Har koi directly balance ko change nahi kar sakta. Uske liye deposit() ya withdraw() jaise methods use hote hain.

# BankAccount
# │
# ├── balance       → data
# │
# ├── deposit()     → method
# └── withdraw()    → method

# Python mein encapsulation samjhane ke liye hum private variable use karte hain.

# Private variable ke liye __ lagate hain:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

# Yahan:

# self.__balance

# mein __balance ko private attribute banaya gaya hai.

# Phir method ke through access kar sakte hain:
# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def show_balance(self):
#         print("Balance:", self.__balance)


# account1 = BankAccount(50000)

# account1.show_balance()

# Output:

# Balance: 50000

# Yahan user directly __balance ko use karne ke bajay show_balance() method ke through balance dekh raha hai.

# Ek line mein yaad rakho 🧠

# Encapsulation = Data ko class ke andar protect/control karna.

# ==========================================
# Encapsulation — Private Attribute Practice
# ==========================================

# Q1. Create a class named BankAccount.
# Use __init__() to create a private attribute named __balance.
# Store the balance passed during object creation.
#
# Create one BankAccount object with a balance of 50000.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

# account1 = BankAccount(559999)

# Q2. Create a class named Employee.
# Use __init__() to create a private attribute named __salary.
# Store the salary passed during object creation.
#
# Create one Employee object with a salary of 40000.

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

# employee1 = Employee(559999)


##❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️

# ==========================================
# Encapsulation — Private Attribute + Method
# ==========================================

# sirf ek chhota step samjho.

# Private attribute:

# self.__salary

# ko class ke andar method se access kar sakte hain.

# class Employee:

#     def __init__(self, salary):
#         self.__salary = salary

#     def show_salary(self):
#         print("Salary:", self.__salary)


# employee1 = Employee(559999)

# employee1.show_salary()

# Yahan:

# def show_salary(self):
#     print("Salary:", self.__salary)

# show_salary() method class ke andar hai, isliye ye __salary ko access kar sakta hai.

# ==========================================
# Encapsulation — Private Attribute + Method
# ==========================================

# Q1. Create a class named Employee.
# Use __init__() to create a private attribute named __salary.
# Store the salary passed during object creation.
#
# Create a method named show_salary().
# Inside the method, print the private salary.
#
# Create an Employee object with salary 50000.
# Call show_salary().

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def show_salary(self):
#         print("Salary:", self.__salary)

# employee1 = Employee(6889977)

# employee1.show_salary()
#----------------------------------------


# Q2. Create a class named BankAccount.
# Use __init__() to create a private attribute named __balance.
# Store the balance passed during object creation.
#
# Create a method named show_balance().
# Inside the method, print the private balance.
#
# Create a BankAccount object with balance 75000.
# Call show_balance().

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def show_balance(self):
#         print("Balance:", self.__balance)

# account1 = BankAccount(57874)

# account1.show_balance()


#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️

# ==========================================
# Encapsulation — Updating Private Attribute
# ==========================================


# Private attribute ko method se update karna

# Abhi humne dekha:

# self.__balance

# ko method ke andar read/access kar sakte hain.

# Ab maan lo account ka balance 50000 hai, aur humein usko 60000 karna hai.

# Iske liye class ke andar ek method bana sakte hain:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def update_balance(self, new_balance):
#         self.__balance = new_balance

# Yahan:

# self.__balance = new_balance

# ka matlab hai:

# Private __balance ki purani value ko new_balance ki value se replace kar do.

# Example:

# account1 = BankAccount(50000)

# account1.update_balance(60000)

# Ab balance:

# 50000 → 60000
# Simple difference
# show_balance()
#     ↓
# Private data ko dekhna

# update_balance()
#     ↓
# Private data ko change karnaPrivate attribute ko method se update karna

# Abhi humne dekha:

# self.__balance

# ko method ke andar read/access kar sakte hain.

# Ab maan lo account ka balance 50000 hai, aur humein usko 60000 karna hai.

# Iske liye class ke andar ek method bana sakte hain:

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def update_balance(self, new_balance):
#         self.__balance = new_balance

# Yahan:

# self.__balance = new_balance

# ka matlab hai:

# Private __balance ki purani value ko new_balance ki value se replace kar do.

# Example:

# account1 = BankAccount(50000)

# account1.update_balance(60000)

# Ab balance:

# 50000 → 60000
# Simple difference
# show_balance()
#     ↓
# Private data ko dekhna

# update_balance()
#     ↓
# Private data ko change karna

# ==========================================
# Encapsulation — Updating Private Attribute
# ==========================================

# Q1. Create a class named Employee.
# Use __init__() to create a private attribute named __salary.
# Store the salary passed during object creation.
#
# Create a method named update_salary().
# The method should take new_salary as a parameter.
# Update the private __salary using new_salary.
#
# Create an Employee object with salary 40000.
# Update the salary to 50000.
#
# Create another method named show_salary().
# Print the updated salary.
#
# Call update_salary() and then show_salary().

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def update_salary(self, new_salary):
#         self.__salary = new_salary

#     def show_salary(self):
#         print("Salary:", self.__salary)

# employee1 = Employee(50000)

# employee1.update_salary(70000)

# employee1.show_salary()



# Q2. Create a class named BankAccount.
# Use __init__() to create a private attribute named __balance.
# Store the balance passed during object creation.
#
# Create a method named update_balance().
# The method should take new_balance as a parameter.
# Update the private __balance using new_balance.
#
# Create a BankAccount object with balance 60000.
# Update the balance to 75000.
#
# Create another method named show_balance().
# Print the updated balance.
#
# Call update_balance() and then show_balance().

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def update_balance(self, new_balance):
#         self.__balance = new_balance

#     def show_balance(self):
#         print("Balance:", self.__balance)

# account1 = BankAccount(59999)
# account1.update_balance(100000)
# account1.show_balance()

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️

#ENCAPSULATION — DATA VALIDATION PRACTICE

# ab data ko control karna samjhte hain. Ye Encapsulation ka practical benefit hai.

# Maan lo salary hai:

# self.__salary = salary

# Agar koi galti se negative salary de de:

# employee1 = Employee(-50000)

# toh problem ho sakti hai.

# Isliye hum method ke andar condition laga sakte hain:

# class Employee:

#     def __init__(self, salary):
#         self.__salary = salary

#     def update_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary
#         else:
#             print("Salary cannot be negative")

# Ab:

# employee1.update_salary(50000)

# ✅ salary update hogi.

# Lekin:

# employee1.update_salary(-10000)

# ❌ salary update nahi hogi.

# Yahan Encapsulation ka fayda kya hua?

# Humne private data ko directly change karne ke bajay method ke through control kiya.

# Private Data
#      ↓
#  update_salary()
#      ↓
#    Check
#   ↙     ↘
# Valid   Invalid
#  ↓         ↓
# Update    Reject

# ==========================================
# Encapsulation — Data Validation Practice
# ==========================================

# Q1. Create a class named Employee.
# Create a private attribute __salary.
# Create a method update_salary(new_salary).
#
# If new_salary is greater than or equal to 0,
# update the salary.
# Otherwise, print "Invalid salary".
#
# Create an Employee object with salary 40000.
# Try to update the salary to -5000.

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def update_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary
        
#         else:
#             print("Invalid salary")

# employee1 = Employee(40000)

# employee1.update_salary(75995)
#----------------------------------------

# Q2. Create a class named BankAccount.
# Create a private attribute __balance.
# Create a method update_balance(new_balance).
#
# If new_balance is greater than or equal to 0,
# update the balance.
# Otherwise, print "Invalid balance".
#
# Create a BankAccount object with balance 50000.
# Try to update the balance to -1000.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def update_balance(self, new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance

#         else:
#             print("Invalid balance")

# account1 = BankAccount(50000)
# account1.update_balance(-1000)
#--------------------------------------------

# Q3. Create a class named Product.
# Create a private attribute __price.
# Create a method update_price(new_price).
#
# If new_price is greater than or equal to 0,
# update the price.
# Otherwise, print "Invalid price".
#
# Create a Product object with price 1000.
# Try to update the price to 500.

# class Product:
#     def __init__(self, price):
#         self.__price = price

#     def update_price(self,new_price):
#         if new_price >= 0:
#             self.__price = new_price
        
#         else:
#             print("Invalid price")

# product1 = Product(1000)

# product1.update_price(500)

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
#-----------------------------------------------------------------------------------------------------------

# ==========================================
# Encapsulation — Getter & Setter Practice
# ==========================================

# Encapsulation ka final important point aaram se dekhte hain: getter aur setter.

# Ye actually wahi concepts hain jo hum already kar chuke hain, bas unke common names hain:

# Getter → private data ko read/access karna
# Setter → private data ko update/change karna

# Example:

# class Employee:

#     def __init__(self, salary):
#         self.__salary = salary

#     # Getter
#     def get_salary(self):
#         return self.__salary

#     # Setter
#     def set_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary
#         else:
#             print("Invalid salary")

# Yahan:

# get_salary()

# → salary dekhne/access karne ke liye.

# set_salary()

# → salary change/update karne ke liye.

# Abhi bas itna yaad rakho:
# Getter → Get / Read data
# Setter → Set / Update data

# Ye new programming logic nahi hai—tum jo show_salary() aur update_salary() kar chuke ho,
# unhi ideas ko standard naming ke saath samajh rahe ho.

# ==========================================
# Encapsulation — Getter & Setter Practice
# ==========================================

# Q1. Create a class named Employee.
# Create a private attribute __salary.
#
# Create a getter method named get_salary().
# Return the private salary.
#
# Create an Employee object with salary 50000.
# Call get_salary() and print the returned salary.

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary
    
# employee1 = Employee(50000)
# print(employee1.get_salary())
#-----------------------------------------


# Q2. Create a class named Product.
# Create a private attribute __price.
#
# Create a getter method named get_price().
# Return the private price.
#
# Create a setter method named set_price(new_price).
# Update the private price using new_price.
#
# Create a Product object with price 1000.
# Update the price to 1500.
# Call get_price() and print the returned price.

# class Product:
#     def __init__(self, price):
#         self.__price = price

#     def get_price(self):
#         return self.__price

#     def set_price(self, new_price):
#         if new_price >= 0:
#             self.__price = new_price

#         else:
#             print("Invalid price")

# product1 = Product(1000)
# product1.set_price(1500)

# print(product1.get_price())

#----------------------------------

# ==========================================
# Encapsulation — Mixed Practice
# ==========================================

# Q1. Create a class named Employee.
# Store salary as a private attribute.
# Create a getter method to return the salary.
# Create a setter method to update the salary.
# Update the salary and print the new salary.

# class Employee:
#     def __init__(self, salary):
#         self.__salary =  salary

#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary
        
#         else:
#             print("Invalid salary")
        
# employee1 = Employee(40000)
# employee1.set_salary(50000)

# print(employee1.get_salary())
#--------------------------------

# Q2. Create a class named BankAccount.
# Store balance as a private attribute.
# Create a setter method to update the balance.
# Allow the update only if the balance is greater than or equal to 0.
# Create a getter method to return the balance.
# Try updating the balance with a valid value and print it.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance =  balance

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance
        
#         else:
#             print("Invalid balance")
        
# account1 = BankAccount(67000)
# account1.set_balance(80000)

# print(account1.get_balance())

# Q3. Create a class named Product.
# Store price as a private attribute.
# Create a getter method to return the price.
# Create a setter method to update the price.
# Do not allow a negative price.
# Try updating the price and print the final price.

# class Product:
#     def __init__(self, price):
#         self.__price =  price

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, new_price):
#         if new_price >= 0:
#             self.__price = new_price
        
#         else:
#             print("Invalid price")
        
# product1 = Product(30000)
# product1.set_price(20000)

# print(product1.get_price())
