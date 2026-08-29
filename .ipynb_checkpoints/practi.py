# ==========================================
# Python Functions - Practice Questions
# ==========================================


# Q1. Create a function
# that prints "Hello World".

# def greet():
#     print("Hello World")

# greet()

# Q2. Create a function
# that prints "Python is Easy"

# def python():
#     print("python is easy")

# python()


# Q3. Create a function
# that prints the following output.
#
# Welcome
# to
# Python

# def it_python():
#     print("Welcome")
#     print("to")
#     print("Python")
# it_python()

# Q4. Create a function
# that prints your name.
# def my_name():
#     print("vikash")
# # my_name()

# Q5. Create a function
# that prints "Good Morning".
# Call the function 3 times.

# def morning_wish():
#     print("Good Morning")
    
# morning_wish()
# morning_wish()
# morning_wish()

# Q6. Create a function
# that prints the following output.
#
# ----------------
# Welcome
# ----------------

# def welcome():
#     print("----------------")
#     print("Welcome")
#     print("----------------")

# welcome()

# Q7. Create a function
# that prints the following output.
#
# I am learning Python
# I want to become a Data Analyst

# def about_pyhton():
#     print("I am learning Python")
#     print("I want to become a Data Analyst")

# about_pyhton()


# Q8. Create a function
# that prints the result of 10 + 20.

# def add():
#     print(10 + 20)

# add()

# Q9. Create a function
# # that prints the result of 50 - 15.

# def less():
#     print(50 - 15)

# less()

# Q10. Create a function
# that prints the following output.
#
# **********
# Python
# **********

# def output():
#     print("**********")
#     print("Python")
#     print("**********")

# output()


# ==========================================
# Python Functions with Parameters
# ==========================================

# Q1. Create a function
# that takes a name as a parameter
# and prints:
# Hello <name>

# def greet(name):
#     print("Hello",name)

# greet("mohan")


# Q2. Create a function
# that takes an age as a parameter
# and prints:
# My age is <age>

# def your_age(age):
#     print("My age is",age)

# your_age(25)
# your_age(20)
# your_age(56)


# Q3. Create a function
# that takes a city name as a parameter
# and prints:
# I live in <city>

# def your_city(city):
#     print("I live in",city)
# your_city("delhi")

# Q4. Create a function
# that takes two numbers as parameters
# and prints their sum.

# def add(a,b):
#     print("sum =", a+b)

# add(55, 58)


# Q5. Create a function
# that takes two numbers as parameters
# and prints their multiplication.

# def multiply(a,b):
#     print("multiply=", a*b)

# multiply(56, 60)

# ==========================================
# Python Return Statement - Practice
# ==========================================


# Q1. Create a function
# that takes two numbers
# and returns their sum.

# def add(a,b):
#     return a+b
# print(add(17, 25))

# 2nd way

# def add(a, b):
#     return a + b

# result = add(10, 20)

# print(result)
#---------------------------------------------------------
# Q2. Create a function
# that takes two numbers
# and returns their multiplication.

# def multiply(a,b):
#     return a*b
# print(multiply(24, 56))


# both are same way
# better this one 
        # 👇
# def multiply(a,b):
#     return a*b
# x = multiply(56, 89)

# print(x)

#------------------------------------------------------

# Q3. Create a function
# that takes one number
# and returns its square.


# def square(num):
#     return num * num

# result = square(5)

# print(result)


# Q4. Create a function
# that takes one number
# and returns its cube.

# def cube(num):
#     return num * num * num

# result = cube(3)

# print(result)

# same way to write
 
# def cube(num):
#     return num ** 3

# print(cube(3))

# Q5. Create a function
# that takes a name
# and returns:
# Hello <name>

# def greet(name):
#     return "hello" + name

# result = greet(" mohit")

# print(result)

# ==========================================
# Python Default Parameters
# ==========================================

# Q1. Create a function
# that greets "Guest" by default.

# def greet(name = "Guest"):
#     print("Hello", name)

# greet()
# greet("Vikash")


# Q2. Create a function
# that prints a city.
# Default city should be "Kolkata".

# def city_name(city= "kolkata"):
#     print(city)

# city_name()
# city_name("delhi")

# Q3. Create a function
# that returns the square of a number.
# Default number should be 5.

# def square(num = 5):
#     return num * num
# print(square(2))

# Q4. Create a function
# that multiplies two numbers.
# Default value of second number should be 10.

# def multiply(a, b=10):
#     return a * b

# result = multiply(5)

# print(result)

# same same 👇

# def multiply(a, b=10):
#     print(a * b)

# multiply(5)


# Q5. Create a function
# that prints:
# Welcome <name>
# Default name should be "User".

# def greet(name= "User"):
#     print("Welcome", name)

# greet()
# greet("Vikash")


# Q1. Create a function
# that takes any number of values
# and prints them.

# def show_values(*values):
#     print(values)

# show_values(10, 20, 30, 40)



# Q2. Create a function
# that takes any number of numbers
# and returns their sum.

# def add(*numbers):
#     total = 0

#     for num in numbers:
#         total = total + num

#     return total

# result = add(10, 20, 30, 40)

# print(result)

# Q3. Create a function
# that takes multiple numbers
# and returns the largest number.

# def multiply(*numbers):


#sum 1 - n

