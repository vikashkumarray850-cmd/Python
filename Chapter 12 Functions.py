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
# -----------------------------------------------------------------------------------------------------------

# 🐍 Functions — Basic Practice

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
# --------------------------------------------------------------------------------------------

# 🐍 FUNCTIONS — PARAMETERS PRACTICE

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
# ------------------------------------------------------------------------------------------------

# 🐍 FUNCTIONS — ARGUMENTS
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

# --------------------------------------------------------------------------------------------

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
# -------------------------------------------------------------------------------------------------

# 🐍 FUNCTIONS — MULTIPLE PARAMETERS PRACTICE

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
# ---------------------------------------------------------------------------------------------

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
# -----------------------------------------------------------------------------------------------------

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
# ------------------------------------------------------------------------------------------------

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
# ---------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — *args Basic Practice
# ==========================================


# Q1. Create a function that accepts any number of values.
# Print all the values.
# def show(*values):
#     print(values)

# show(1,1,1,1,1,11,1,)

# Q2. Create a function that accepts any number of names.
# Print all the names.
# Q2. Create a function that accepts any number of names.
# Print all the names.

# def show_names(*names):
#     print(names)

# show_names("Vikash", "Rohan", "Amit", "Rahul")

# Q3. Create a function that accepts any number of numbers.
# Print all the numbers.

# def show_numbers(*number):
#     print(number)

# show_numbers(109,26,72,829,729,62729,55)

# Q4. Create a function that accepts any number of values.
# Call the function with 5 values.
# def show_number(*values):
#     print(values)
# show_number(10,20,30,40,50)

# Q5. Create a function that accepts any number of numbers.
# Call the function with 6 numbers.
# def show_number(*values):
#     print(values)
# show_number(10,20,30,40,50,60)

# Q6. Create a function that accepts any number of values.
# Call the function with different types of values.
# def show_number(*values):
#     print(values)
# show_number(10,20,30,40,50)


# Q7. Create a function that accepts any number of names.
# Call the function with 4 names.
# def show_names(*names):
#     print(names)

# show_names("Vikash", "Rohan", "Amit", "Rahul")

# Q8. Create a function that accepts any number of numbers.
# Call the function with 8 numbers.
# def show_number(*values):
#     print(values)
# show_number(10,20,30,40,50,36,36,28)
# -------------------------------------------------------------------------------------

# ==========================================
# 🐍 Python Functions — *args + Indexing
# ==========================================

# Q1. Create a function using *args.
# Print the first value.
# Call the function with three values.
# def show_values(*values):
#     print(values[0])

# show_values(10,20,30)

# Q2. Create a function using *args.
# Print the second value.
# Call the function with three values.
# def show_values(*args):
#     print(args[1])
# show_values(10,20,30)

# Q3. Create a function using *args.
# Print the third value.
# Call the function with four values.
# def show_values(*args):
#     print(args[2])
# show_values(10,20,30,40)

# Q4. Create a function using *args.
# Print the first and second values.
# Call the function with four values.
# def show_values(*args):
#     print(args[0:2])
# show_values(10,20,30,40)

# Q5. Create a function using *args.
# Print the last value.
# Call the function with four values.
# def show_values(*args):
#     print(args[-1])
# show_values(10,20,30,40)

# Q6. Create a function using *args.
# Print the second-last value.
# Call the function with four values.
# def show_values(*args):
#     print(args[-2])
# show_values(10,20,30,40)

# Q7. Create a function using *args.
# Print the first and last values.
# Call the function with five values.
# def show_values(*args):
#     print(args[0])
#     print(args[-1])
# show_values(10,20,30,40,50)

# Q8. Create a function using *args.
# Print the first three values.
# Call the function with five values.

# def show_values(*args):
#     print(args[0:3])
# show_values(10,20,30,40,50)
# ------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — *args + Loop
# ==========================================


# Q1. Create a function using *args.
# Print each value one by one.
# Call the function with five values.
# def show(*args):
#     for value in args:
#         print(value)
# show(10,20,30,40,50)

# Q2. Create a function using *args.
# Print each number one by one.
# Call the function with four numbers.

# def show_number(*args):
#     for x in args:
#         print(x)
# show_number(10,20,30,40)

# Q3. Create a function using *args.
# Print each name one by one.
# Call the function with four names.
# def show_names(*values):
#     for x in values:
#         print(x)
# show_names("Vikash","Rohit","Arun","Vajinder")

# Q4. Create a function using *args.
# Print each value one by one.
# Call the function with six values.
# def show(*args):
#     for value in args:
#         print(value)
# show(10,20,30,40,50,60)
# ------------------------------------------------------------------------------------

# ==========================================
# Python Functions — *args + Calculation
# ==========================================


# Q1. Create a function using *args.
# Calculate the sum of all numbers.
# Call the function with three numbers.

# result = 0
# def sum(*args):
#     result = 0
    
#     for x in args:
#        result = result + x

#     print(result)

# sum(10,20,30)

# Q2. Create a function using *args.
# Calculate the sum of all numbers.
# Call the function with five numbers.

# def sum(*values):
#     result=0

#     for number in values:
#         result = result + number

#     print(result)

# sum(10,20,30,40,50)


# Q3. Create a function using *args.
# Calculate the total of all numbers.
# Call the function with six numbers.
# def total(*value):
#     result = 0

#     for number in value:
#         result = result + number

#     print(result)

# total(10,20,30,40,50,50)

# Q4. Create a function using *args.
# Calculate the sum of all numbers and print the result.
# Call the function with four numbers.
# def sum(*values):
#     result=0

#     for number in values:
#         result = result + number

#     print(result)

# sum(10,20,30,40)

# Q5. Create a function using *args.
# Calculate the sum of all numbers and return the result.
# Call the function with five numbers.

# def sum(*values):
#     result=0

#     for number in values:
#         result = result + number

#     return result

# answer = sum(10,20,30,40,50)

# print(answer)
# ----------------------------------------------------------------------------------

# ==========================================
# Python Functions — *args + Average
# ==========================================


# Q1. Create a function using *args.
# Calculate and print the average of three numbers.

# def average(*values):
#     result = 0

#     for number in values:
#         result = result + number

#     return result / len(values)
    
# answer = average(10,20,30)

# print(answer)


# Q2. Create a function using *args.
# Calculate and print the average of five numbers.
# def average(*args):
#     result = 0

#     for x in args:
#         result = result + x

#     return result / len(args)

# answer = average(10,20,30,40,50)

# print(answer)


# Q3. Create a function using *args.
# Calculate and return the average of four numbers.

# def average(*args):
#     result = 0

#     for number in args:
#         result = result + number

#     return result / len(args)
# answer = average(10,20,30,40)

# print(answer)

# Q4. Create a function using *args.
# Calculate and return the average of six numbers.

# def average(*value):
#     result = 0

#     for number in value:
#         result = result + number

#     return result / len(value)

# answer = average(10,20,30,30,20,10)
# print(answer)

#-------------------------------------------------------------------------------------------

# ==========================================
# 🐍Python Functions — **kwargs Basic
# ==========================================


# Q1. Create a function using **kwargs.
# Print all the details.
# Call the function with name and age.
# def details(**kwargs):
#     print(kwargs)

# details(name="vikash", age=25)

# Q2. Create a function using **kwargs.
# Print all the details.
# Call the function with name, city and age.
# def details(**info):
#     print(info)

# details(name = "RAJDIP", city = "KOLKATA", age = 24)

# Q3. Create a function using **kwargs.
# Print all the details.
# Call the function with three different details.

# def details(**info):
#     print(info)

# details(name = "RAJDIP", city = "KOLKATA", age = 24)


# Q4. Create a function using **kwargs.
# Print all the details.
# Call the function with four different details.

# def details(**info):
#     print(info)

# details(name = "VIKASH", city = "KOLKATA", age = 25, job = "DATA ANALYST")
#---------------------------------------------------------------------------------------

# ==========================================
# 🐍Python Functions — **kwargs + Key Access
# ==========================================


# Q1. Create a function using **kwargs.
# Print the value of "name".
# Call the function with name and age.

# def values(**info):
#     print(info["name"])

# values(name = "vikash", age = 25)

# Q2. Create a function using **kwargs.
# Print the value of "city".
# Call the function with name, city and age.
# def value(**kwargs):
#     print(kwargs["city"])

# value(name ="vikash", city= "kolkata", age= 25)

# Q3. Create a function using **kwargs.
# Print the value of "age".
# Call the function with name, age and job.
# def details(**info):
#     print(info["age"])

# details(name = "VIKASH",  age = 25, job = "DATA ANALYST")

# Q4. Create a function using **kwargs.
# Print the value of "job".
# Call the function with name, city, age and job.
# def details(**info):
#     print(info["job"])

# details(name = "VIKASH", city = "KOLKATA", age = 25, job = "DATA ANALYST")
#------------------------------------------------------------------------------------------------------

# ==========================================
# 🐍Python Functions — **kwargs + Loop
# ==========================================


# Q1. Create a function using **kwargs.
# Print each key and value one by one.
# Call the function with name, age and city.
# def detail(**info):
#     for key, value in info.items():
#         print(key,value)
# detail(name ="vikash", age = 25, city = "kolkata")

# Q2. Create a function using **kwargs.
# Print each key and value one by one.
# Call the function with name, age, city and job.
# def detail(**info):
#     for key, value in info.items():
#         print(key, value)

# detail(name="mohi", age=19, city="delhi", job="DATA ANALYST")

# Q3. Create a function using **kwargs.
# Print each key and value one by one.
# Call the function with three details.
# def values(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# values(name ="mohit", age = 19, city = "delhi")

# Q4. Create a function using **kwargs.
# Print each key and value one by one.
# Call the function with four details.

# def details(**kwargs):
#     for key, values in kwargs.items():
#         print(key, values)

# details(name ="mohi", age = 19, city = "delhi", job = "DATA ANALYST")
#------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — **kwargs + Conditions
# ==========================================


# Q1. Create a function using **kwargs.
# Check if "city" key is present.
# If present, print "City Available".
# Call the function with name, age and city.

# def detail(**kwargs):
#     if "city" in kwargs:
#         print("City Available")

# detail(name = "vikash", age = 25, city = "kokkata")

# Q2. Create a function using **kwargs.
# Check if "age" key is present.
# If age is 18 or more, print "Adult".
# Call the function with name and age.
# def values(**info):

#     if "age" in info:
#         if info["age"] >= 18:
#             print("Adult")
            
# values(name = "vikash", age = 25)

# Q3. Create a function using **kwargs.
# Check if "salary" key is present.
# If salary is 30000 or more, print "Good Salary".
# Call the function with name and salary.
# def details(**info):

#     if "salary" in info:
#         if info["salary"] >= 30000:
#             print("Good Salary")

# details(Name = "raj", salary = 35000)

# Q4. Create a function using **kwargs.
# Check if "marks" key is present.
# If marks are 50 or more, print "Pass".
# Call the function with name and marks.

# def value(**info):
#     if "marks" in info:
#         if info["marks"] >= 50:
#             print("Pass")

# value(Name = "raj", marks = 50 )

# Q5. Create a function using **kwargs.
# Check if "name" key is present.
# If present, print the name.
# Call the function with name, age and city.

# def value(**info):
#     if "name" in info:
#             print(info["name"])

# value(name = "raj", age = 19, city = "delhi" )
