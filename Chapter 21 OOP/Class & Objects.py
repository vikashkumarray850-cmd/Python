# OOP
# │
# ├── 1. Class & Object              ✅
# ├── 2. Attributes                  ✅
# ├── 3. __init__()                  ✅
# ├── 4. self                        ✅
# ├── 5. Methods                     ✅
# ├── 6. Methods + Calculation       ✅


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