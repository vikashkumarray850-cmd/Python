# # function
# def sum_of_two_nums(a, b):
#     # print(a + b)
#     return a + b

# # print(sum_of_two_nums(1, 3) * 100)



# def greet(name, age, salary=10000,  address="India"): # parametrs
#     print(f'Hello {name}, your age is {age}, you r from {address}, your salary is {salary}')

# greet("Harish", 12, 12000, "Kolkata") 
# greet(name="Tushar",age= 20, address="Kolkata") # arguments


# *args/**kwargs
# lambda
# recursion


# def addition(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum



# print(addition(1, 2, 3, 6))
# print(addition(1, 2))
# print(addition(1, 2, 45))




# def me_kon_kon_sub_paratahu(**subs):
#     for sub, sub_name in enumerate(subs):
#         print(sub_name, sub, subs[sub_name])

# me_kon_kon_sub_paratahu(sub1="MERN", sub2="DA", sub3="PYTHON", sub4="PHP")


# lambda
# recursion
# list
#-----------------------------------------------------------------------------------------------------------

#🐍 Functions — Basic Practice

# Q1.
# Create a function named greet().
# Print "Hello Python" inside the function.
# Call the function.

# def greet ():
#     print("Hello")

# greet()

# Q2.
# Create a function named welcome().
# Print "Welcome to Python" inside the function.
# Call the function.

# def welcome():
#     print("Welcome to Python")

# welcome()


# Q3.
# Create a function named show_name().
# Print your name inside the function.
# Call the function.

# def show_name():
#     print("VIKASH")
# show_name()
#--------------------------------------------------------------------------------------------

#🐍 FUNCTIONS — PARAMETERS PRACTICE

# # Q1. Create a function greet that takes a name as a parameter.
# Print a greeting using the name and call the function.

# def greet(name):
#     print("Hello", name)
# greet("Rohit")

# Q2. Create a function show_age that takes an age as a parameter.
# Print the age and call the function.

# def show_age(age):
#     print(age)
# show_age(25)

# Q3. Create a function introduce that takes name and city as parameters.
# Print both values and call the function.

# def introduce (name,city):
#     print(name)
#     print(city)

# introduce("vikash", "kolkata")
#------------------------------------------------------------------------------------------------

#🐍 FUNCTIONS — ARGUMENTS
# Q1. Create a function that takes two numbers as parameters.
# Call the function by passing two numbers as arguments.

# def add(a,b):
#     print(a+b)
# add(29,53)

# Q2. Create a function that takes a name as a parameter.
# Call the function by passing your name as an argument.

# def greet(name):
#     print("Hello", name)

# greet("Vikash")


# Q3. Create a function that takes three values as parameters.
# Call the function by passing three arguments.

# def show_values(a,b,c):
#     print(a,b,c)
# show_values(10,20,30)

#--------------------------------------------------------------------------------------------

# Q11. Create a function that prints your name, age and city.
# Call the function.
# def show_info():
#     print("vikash")
#     print(25)
#     print("kolkata")

# show_info()


# Q12. Create a function that prints the result of 25 + 35.
# Call the function.
# def add():
#     print(25+35)

# add()

# Q13. Create a function that prints the result of 100 - 45.
# Call the function.
# def less():
#     print(100-45)

# less()

# Q14. Create a function that prints the result of 12 * 5.
# Call the function.
# def multiply():
#     print(12*5)
# multiply()

# Q15. Create a function that prints the result of 100 / 4.
# Call the function.

# def divide():
#     print(100/4)
# divide()

# Q16. Create a function that checks whether 10 is even or odd.
# Call the function.

# def check_number():
#     if 10 % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_number()

# Q17. Create a function that prints the multiplication table of 5.
# Call the function.
# def table():
#     for i in range(1,11):
#         print(5 * i)

# table()

# Q18. Create a function that prints numbers from 1 to 10.
# Call the function.

# def table():
#     for i in range(1,11):
#         print(i)
# table()
#-------------------------------------------------------------------------------------------------

#🐍 FUNCTIONS — MULTIPLE PARAMETERS PRACTICE

# Q1. Create a function that takes two numbers as parameters.
# Print both numbers and call the function.
# def show_number(a, b):
#     print(a)
#     print(b)

# show_number(10,20)

# Q2. Create a function that takes two numbers as parameters.
# Print their sum and call the function.

# def sum(a,b):
#     print(a+b)

# sum(10,20)

# Q3. Create a function that takes two numbers as parameters.
# Print their difference and call the function.

# def subtract(a, b):
#     print(a - b)
# subtract(50, 20)

# Q4. Create a function that takes two numbers as parameters.
# Print their multiplication and call the function.

# def multiplication(a,b):
#     print(a * b)

# multiplication(10,20)

# Q5. Create a function that takes two numbers as parameters.
# Print their division and call the function.
# def division(a,b):
#     print(a / b)
# division(10,2)

# Q6. Create a function that takes two names as parameters.
# Print both names and call the function.

# def names(a, b):
#     print(a)
#     print(b)
# names("rohan","vikash")

# Q7. Create a function that takes name and age as parameters.
# Print both values and call the function.
# def values(a, b):
#     print(a)
#     print(b)
# values("vikash", 25)

# Q8. Create a function that takes name and city as parameters.
# Print both values and call the function.
# def values(a,b):
#     print(a)
#     print(b)
# values("vikash", "kolkata")

# Q9. Create a function that takes name, age and city as parameters.
# Print all three values and call the function.
# def values(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# values("vikash", 25, "kolkata")


# Q10. Create a function that takes name, city and job as parameters.
# Print all three values and call the function.

# def values(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# values("vikash", "kolkata", "teacher")
#---------------------------------------------------------------------------------------------

# 🐍 FUNCTIONS — PARAMETERS + CALCULATION
# Q1. Create a function that takes two numbers as parameters.
# Print their addition and call the function.
# def add(a,b):
#     print(a+b)
# add(10,20)

# Q2. Create a function that takes two numbers as parameters.
# Print their subtraction and call the function.
# def subtraction(a,b):
#     print(a-b)
# subtraction(10,20)

# Q3. Create a function that takes two numbers as parameters.
# Print their multiplication and call the function.
# def multiplication(a,b):
#     print(a*b)
# multiplication(10,20)

# Q4. Create a function that takes two numbers as parameters.
# Print their division and call the function.
# def division(a,b):
#     print(a/b)
# division(200,10)

# Q5. Create a function that takes three numbers as parameters.
# Print their total and call the function.
# def total(a,b,c):
#     print(a+b+c)
# total(10,20,30)

# Q6. Create a function that takes three numbers as parameters.
# Print their average and call the function.
# def average(a,b,c):
#     print((a+b+c)/3)
# average(10,20,30)

# Q7. Create a function that takes two numbers as parameters.
# Print the larger number and call the function.
# def large_number(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)

# large_number(1000,10000)

# Q8. Create a function that takes two numbers as parameters.
# Print the smaller number and call the function.
# def smaller_number(a,b):
#     if a < b:
#         print(a)
#     else:
#         print(b)
# smaller_number(10,30)

# Q9. Create a function that takes three numbers as parameters.
# Print the total after adding all three numbers and call the function.
# def total(a,b,c):
#     print(a+b+c)
# total(10,10,10)

# Q10. Create a function that takes two numbers as parameters.
# Print the square of both numbers and call the function.
# def square(a,b):
#     print(a ** 2)
#     print(b ** 2)
# square(10,20)
#-----------------------------------------------------------------------------------------------------

# ==========================================
# 🐍PYTHON FUNCTIONS — RETURN STATEMENT
# ==========================================

# Q1. Create a function that takes two numbers as parameters.
# Return their sum and call the function.

# def sum(a,b):
#     return (a+b)
# result =sum(10,20)

# print(result)

# Q2. Create a function that takes two numbers as parameters.
# Return their multiplication and call the function.
# def multiply(a,b):
#     return a * b
# result = multiply(10,10)
# print(result)

# Q3. Create a function that takes one number as a parameter.
# Return its square and call the function.
# def square(num):
#     return num ** 2
# result = square(5)
# print(result)

# Q4. Create a function that takes one number as a parameter.
# Return its cube and call the function.

# def cube(num):
#     return num ** 3
# result = cube(5)
# print(result)

# Q5. Create a function that takes a name as a parameter.
# Return "Hello" followed by the name and call the function.

# def greet(name): 
#     return "Hello " +  name
# result = greet ("vikash")
# print(result)
#------------------------------------------------------------------------------------------------

# ==========================================
# 🐍Python Functions — Return + Calculation
# ==========================================


# Q1. Create a function that takes two numbers as parameters.
# Return their difference and call the function.
# def difference(a,b):
#     return a - b
# result = difference(50,35)
# print(result)

# Q2. Create a function that takes two numbers as parameters.
# Return their division and call the function.
# def division(a,b):
#     return a/b
# result = division(10,5)
# print(result)

# Q3. Create a function that takes three numbers as parameters.
# Return their total and call the function.
# def total(x,y,z):
#     return x+y+z
# result = total(10,10,10)
# print(result)

# Q4. Create a function that takes three numbers as parameters.
# Return their average and call the function.

# def average(x,y,z):
#     return (x+y+z) /3
# result = average(10,10,10)
# print(result) 

# Q5. Create a function that takes two numbers as parameters.
# Return their product and call the function.
# def product(a,b):
#     return a*b
# result = product(10,20)
# print(result)

# Q6. Create a function that takes one number as a parameter.
# Return its double and call the function.
# def double(num):
#     return num * 2
# result = double(10)
# print(result)

# Q7. Create a function that takes one number as a parameter.
# Return its half and call the function.
# def half(num):
#     return num / 2
# result = half(50)
# print(result)

# Q8. Create a function that takes two numbers as parameters.
# Return the larger number and call the function.
# def larger_number(a,b):
#     if a > b:
#         return a
#     else :
#         return b
# result = larger_number(20,30)
# print(result)

# Q9. Create a function that takes two numbers as parameters.
# Return the smaller number and call the function.
# def smaller_number(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# result = smaller_number(50, 37)
# print(result)

# Q10. Create a function that takes three numbers as parameters.
# Return the largest number and call the function.

# def largest_number(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z

# result = largest_number(10, 30, 50)

# print(result)
#---------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — Default Parameters
# ==========================================

# Q1. Create a function that prints a name.
# Use "Guest" as the default name.

# def name_print(name="Guest"):
#     print(name)

# name_print()

# Q2. Create a function that prints a city.
# Use "Kolkata" as the default city.
# def city_print(city = "Kokata"):
#     print(city)
# city_print()

# Q3. Create a function that prints a language.
# Use "Python" as the default language.
# def language_print(language = "Python"):
#     print(language)
# language_print()

# Q4. Create a function that prints a number.
# Use 10 as the default number.
# def num_print(number = 10):
#     print(number)
# num_print()


# Q5. Create a function that prints "Hello" with a name.
# Use "User" as the default name.
# def greet(name ="User"):
#     print("hello",name)
# greet()

# Q6. Create a function that takes two numbers as parameters.
# Use 10 as the default value of the second number.
# def multiply(a, b=10):
#     print(a * b)

# multiply(5)
