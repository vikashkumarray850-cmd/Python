# ==========================================
# Python Functions — **kwargs + if-else
# ==========================================


# Q1. Check Key
# Create a function using **kwargs.
# Check whether "city" is present or not.
# Call the function with name, age and city.
# def details(**info):
#     if "city" in info:
#         print("present")
#     else:
#         print("not present")
# details(name ="vikash", age = 25, city ="kolkata" )

# Q2. Check Value
# Create a function using **kwargs.
# Check whether the age is 18 or above.
# Call the function with name and age.
# def details(**info):
#     if "age" in info:
#         if info["age"] >= 18:
#             print("adult")
#         else:
#             print("minor")

# details(name ="vikash", age = 25)

# Q3. Compare Value
# Create a function using **kwargs.
# Check whether the salary is 30000 or above.
# Call the function with name and salary.
# def details(**kwargs):

#     if "salary" in kwargs:
#         if kwargs["salary"]>= 30000:
#             print("High")
#         else:
#             print("medium")
# details(name ="vikash", salary = 30000)


# Q4. Check Matching Value
# Create a function using **kwargs.
# Check whether the city is "Kolkata".
# Call the function with name and city.
# def details(**info):
#     if "city" in info:
#         if info["city"]== "kolkata":
#             print("kolkata")
#         else:
#             print("other city")
# details(name ="vikash", city ="kolkata" )

# Q5. Even or Odd
# Create a function using **kwargs.
# Check whether the given number is even or odd.
# Call the function with number.
# def numbers(**info):

#     if "number" in info:
#         if info["number"] % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")

# numbers(number=2)

# Q6. Pass or Fail
# Create a function using **kwargs.
# Check whether marks are 50 or above.
# Call the function with name and marks.

# def value(**info):
#     if "marks" in info:
#         if info["marks"] >= 50:
#             print("Pass")
#         else:
#             print("Fail")

# value(Name = "raj", marks =35)

#-------------------------------------------------------------------

# ==========================================
# Python Functions — **kwargs + Multiple Conditions
# ==========================================


# Q1. Age and Salary
# Create a function using **kwargs.
# Check whether age is 18 or above and salary is 30000 or above.
# Print "Eligible" when both conditions are true.
# def values(**info):

#     if info["age"] >= 18 and info["salary"]>= 30000:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# values(age = 25, salary = 30000)

#And mein dono conditions True honi chahiye. Ek False hai, isliye else chalega.
#----------------------------------------------
# Q2. Marks and Attendance
# Create a function using **kwargs.
# Check whether marks are 50 or above and attendance is 75 or above.
# Print "Pass" when both conditions are true.

# def details(**info):

#     if info["marks"] >= 50 and info["attendance"]>= 75:
#         print("Pass")
# details(marks = 50, attendance = 75)

# Q3. Age or Salary
# Create a function using **kwargs.
# Check whether age is 18 or above or salary is 30000 or above.
# Print "Qualified" when either condition is true.
# def values(**info):

#     if info["age"] >= 18 or info["salary"]>= 30000:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# values(age = 25, salary = 20000)

# Q4. Age and City
# Create a function using **kwargs.
# Check whether age is 18 or above and city is "Kolkata".
# Print "Selected" when both conditions are true.
# def details(**info):
#     if info["age"]>= 18 and info["city"] == "kolkata":
#         print("Selected")
# details(age = 25, city = "kolkata")

#-----------------------------------------------------------------------------------

# ==========================================
# Python Functions — **kwargs + if-elif-else
# ==========================================


# Q1. Marks Grade
# Create a function using **kwargs.
# Check the marks and print a suitable result for three different ranges.
# Call the function with marks.
# def details(**info):

#     if info["marks"] >= 90:
#         print("good")
#     elif info["marks"] >= 65: 
#         print("average")
#     else:
#         print("bad")

# details(marks = 70)

# Q2. Age Category
# Create a function using **kwargs.
# Check the age and print a suitable category for three different age ranges.
# Call the function with age.

# def details(**info):

#     if info["age"]>= 18:
#         print("Adult")

#     elif info["age"] >= 15:
#         print('minor')

#     else :
#         print("Child")
# details(age = 20)
# Q3. Salary Level
# Create a function using **kwargs.
# Check the salary and print a suitable level for three different salary ranges.
# Call the function with salary.

# def details(**info):

#     if info["salary"]>= 50000:
#         print("High")

#     elif info["salary"] >= 25000:
#         print("Medium")

#     else :
#         print("Low")
# details(salary = 15000)

# Q4. Temperature
# Create a function using **kwargs.
# Check the temperature and print a suitable result for three different ranges.
# Call the function with temperature.

# def details(**info):

#     if info["Temperature"]>= 50:
#         print("High")

#     elif info["Temperature"] >= 35:
#         print("Medium")

#     else :
#         print("Low")
# details(Temperature = 40)

#-------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — return + Conditions
# ==========================================


# Q1. Check Age
# Create a function that takes age as an argument.
# Check whether the person is an adult or minor.
# Return the result and print it outside the function.
# def check_age(age):

#     if age >= 18:
#         return "Adult"
#     else :
#         return "minor"
# result = check_age(25)
# print(result)

# Q2. Check Marks
# Create a function that takes marks as an argument.
# Check whether the student has passed or failed.
# Return the result and print it outside the function.

# def check_marks(marks):

#     if marks >= 85:
#         return "Excellent"
#     else:
#         return "Good"

# result = check_marks(95)
# print(result)

# Q3. Check Salary
# Create a function that takes salary as an argument.
# Check the salary level using if-else.
# Return the result and print it outside the function.

# def check_salary(salary):

#     if salary >= 50000:
#         return "HIGH"

#     else :
#         return "MEDIUM"

# result = check_salary(40000)
# print(result)

# Q4. Check_Number
# Create a function that takes a number as an argument.
# Check whether the number is positive or negative.
# Return the result and print it outside the function.

# def check_number(number):

#     if number >= 0:
#         return "Positive"
#     else:
#         return "Negative"

# result = check_number(95)
# print(result)
#------------------------------------------------------------------------------------

# ==========================================
# Python Functions — return + if-elif-else
# ==========================================


# Q1. Marks Grade
# Create a function that takes marks as an argument.
# Use three conditions to decide the result.
# Return the result and print it outside the function.

# def check_marks(marks):

#     if marks >= 85:
#         return "Excellent"

#     elif marks >= 65:
#         return "Good"

#     else:
#         return "Average"

# result = check_marks(75)
# print(result)

# Q2. Age Category
# Create a function that takes age as an argument.
# Use three conditions to decide the age category.
# Return the category and print it outside the function.

# def check_age(age):

#     if age >= 18:
#         return "Adult"

#     elif age >= 15:
#         return "Minor"
    
#     else :
#         return "Child"
    
# result = check_age(25)
# print(result)


# Q3. Salary Level
# Create a function that takes salary as an argument.
# Use three conditions to decide the salary level.
# Return the level and print it outside the function.

# def check_salary(salary):

#     if salary >= 50000:
#         return "HIGH"

#     elif salary >= 40000:
#         return "MEDIUM"

#     else :
#         return "LOW"

# result = check_salary(30000)
# print(result)

# Q4. Temperature
# Create a function that takes temperature as an argument.
# Use three conditions to decide the temperature level.
# Return the result and print it outside the function.

# def Check_Temperature(Temperature):
#     if Temperature >= 50:
#         return "HIGH"

#     elif Temperature >= 35:
#         return "MEDIUM"

#     else:
#         return "LOW"
# result = Check_Temperature(30)
# print(result)

#------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — return + and / or
# ==========================================


# Q1. Age and Salary
# Create a function with age and salary as parameters.
# Check both conditions using a logical operator.
# Return "Eligible" or "Not Eligible".
# Call the function and print the result.

# def check_details(age,salary):

#     if age >= 18 and salary >= 35000:
#         return "Eligible"

#     else:
#         return "Not Eligible"
# result = check_details(28, 40000)
# print(result)

# Q2. Marks and Attendance
# Create a function with marks and attendance as parameters.
# Check whether both requirements are satisfied.
# Return "Pass" or "Fail".
# Call the function and print the result.

# def check_performance(marks,Attendance):

#     if marks >= 89 and Attendance >= 65:
#         return "Pass"

#     else:
#         return "Fail"

# result = check_performance(90,66)
# print(result)

# Q3. Age or Experience
# Create a function with age and experience as parameters.
# Check whether either requirement is satisfied.
# Return "Qualified" or "Not Qualified".
# Call the function and print the result.

# def check_requirment(age,Experience):

#     if age >=25 or Experience < 3 :
#         return "Qualified"

#     else:
#         return "Not Qualified"

# result = check_requirment(26,4)
# print(result)

# Q4. Marks, Attendance and Fee
# Create a function with marks, attendance and fee as parameters.
# Use multiple conditions to decide whether the student is eligible.
# Return the appropriate result.
# Call the function and print the result.

# def check_eligibility(marks, attendance, fee):

#     if marks >= 50 and attendance >= 75 and fee <= 50000:
#         return "Eligible"
#     else:
#         return "Not Eligible"


# result = check_eligibility(65, 80, 40000)
# print(result)
#--------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — Multiple Parameters + return
# ==========================================


# Q1. Price and Discount
# Create a function that takes price and discount as parameters.
# Subtract the discount from the price and return the final price.
# Call the function and print the result.
# def final_price(Price, Discount):
#     result = Price - Discount
#     return result

# result = final_price(300 , 25)
# print(result)

# Q2. Salary
# Create a function that takes basic salary and bonus as parameters.
# Add them together and return the final salary.
# Call the function and print the result.

# def salary_details(salary, bonus):

#     result = salary + bonus
#     return result
# result= salary_details(25000 , 2500)
# print (result)

# Q3. Shopping Total
# Create a function that takes price, quantity and delivery_charge as parameters.
# Calculate the total shopping cost and return it.
# Call the function and print the result.

# def shopping_deatils(price, quantity,delivery_charge):
#     total = price * quantity + delivery_charge
#     return total

# result = shopping_deatils(500,5,75)
# print(result)

# Q4. Average Marks
# Create a function that takes marks1, marks2 and marks3 as parameters.
# Calculate the average marks and return the result.
# Call the function and print the result.

# def check_avg(marks1, marks2, marks3):

#     total = (marks1 + marks2 + marks3) / 3

#     return total
# result = check_avg(100,90,80) 
# print(result)

# Q5. Simple Interest
# Create a function that takes principal, rate and time as parameters.
# Calculate the simple interest and return the result.
# Call the function and print the result.

# def simple_interest(principal, rate, time):

#     interest = (principal * rate * time) / 100

#     return interest

# result = simple_interest(50000, 8, 2)
# print(result)
#=-----------------------------------------------------------------------------------------

# ==========================================
# Python Functions — Function inside Function
# ==========================================


# Q1. Addition
# Create one function that takes two numbers and returns their sum.
# Create another function that calls the first function.
# Return the result from the second function.
# Call the second function and print the result.

# def add(a,b):
#     return a + b
# result = add(10,20)


# def calculation():
#     result = add(10,20)
#     return result

# print(calculation())


# Q2. Multiplication
# Create one function that takes two numbers and returns their product.
# Create another function that calls the first function.
# Return the result from the second function.
# Call the second function and print the result.

# def Multiplication(a,b):
#     return a * b


# def product():
#     result = Multiplication(10,10)
#     return result

# print(product())

# Q3. Total Shopping Cost
# Create one function that calculates price × quantity and returns the total.
# Create another function that adds a delivery charge to that total.
# Return the final amount.
# Call the second function and print the result.

# def calculate_total(price, quantity):
#     total = price * quantity
#     return total


# def final_amount(price, quantity, delivery_charge):
#     total = calculate_total(price, quantity)
#     result = total + delivery_charge
#     return result


# result = final_amount(500, 3, 75)
# print(result)

# Q4. Salary
# Create one function that adds basic salary and bonus.
# Create another function that calls the first function and subtracts tax.
# Return the final salary.
# Call the second function and print the result.

# def add(salary,bonus):
#     total = (salary + bonus)
#     return total

# def final_salary(salary,bonus,tax):
#     total = add(salary,bonus)
#     result = total - tax
#     return result

# result = final_salary(25000, 20000, 3000)

# print(result)

# Q5. Student Result
# Create one function that calculates the total of three marks.
# Create another function that calls the first function and calculates the average.
# Return the average marks.
# Call the second function and print the result.

# def total_marks(marks1, marks2, marks3):
#     total = marks1 + marks2 + marks3
#     return total


# def average_marks(marks1, marks2, marks3):
#     total = total_marks(marks1, marks2, marks3)
#     average = total / 3
#     return average


# result = average_marks(80, 90, 70)
# print(result)
#------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — Local & Global Scope
# ==========================================


# Q1. Local Variable
# Create a function named show_details().
# Create a variable inside the function.
# Print the variable inside the function.
# Call the function.

# def show_details():

#     name ="vikash"
#     print(name)
# show_details()

# Q2. Global Variable
# Create a variable outside a function.
# Create a function that prints that variable.
# Call the function.
# name = "vikash"
# def show():
#     print(name)

# show()

# Q3. Local vs Global
# Create a variable outside a function.
# Inside the function, create another variable with the same name.
# Print the variable inside the function and then outside the function.
# Observe both outputs.

# name = "vikash"

# def show_deatils():
#     name = "vikash"
#     print(name)

# show_deatils()
# print(name)


# Q4. Global Keyword
# Create a salary variable outside a function.
# Create a function that changes its value.
# Use the appropriate keyword so that the original global variable is changed.
# Call the function and print the salary.

# salary = 25000

# def update():
#     global salary
#     salary = 30000
# update()
# print(salary)

# Q5. Local Calculation
# Create a function that takes price and quantity.
# Create a total variable inside the function.
# Calculate and print the total.
# Try to access total outside the function and observe what happens.

# def details():
#     price = 500
#     quantity = 5

#     total = price * quantity
#     print(total)

# details()

# ==========================================
# Python Functions — Global Update & Calculation Practice
# ==========================================


# Q1. Global Variable Update
# Create a salary variable outside the function.
# Create a function named update_salary().
# Change the salary inside the function.
# Use the required keyword to update the global variable.
# Call the function and print the salary.

# salary = 25000

# def update_salary():
#     global salary
#     salary = 30000

# update_salary()
# print(salary)

# Q2. Global Variable Calculation
# Create price and quantity variables outside the function.
# Create a function named calculate_total().
# Calculate the total inside the function.
# Print the result inside the function.
# Call the function.

# price = 500
# quantity = 5
# def calculate_total():

#     total = price * quantity
#     print(total)

# calculate_total()


# Q3. Update + Calculation
# Create a global salary variable.
# Create a function named update_salary().
# Increase the salary by 5000 inside the function.
# Update the global salary and print the new salary.
# Call the function.

# salary = 30000

# def update_salary():
#     global salary
#     salary = salary + 5000
#     print(salary)

# update_salary()


# Q4. Global Variables + Calculation
# Create global variables price and delivery_charge.
# Create a function named final_amount().
# Calculate the final amount using both variables.
# Print the final amount.
# Call the function.

# price = 500
# delivery_charge = 50

# def final_amount():
#     total = price + delivery_charge

#     print(total)
# final_amount()


# Q5. Update + Calculation
# Create a global variable balance.
# Create a function named withdraw().
# Subtract an amount from the balance.
# Update the global balance.
# Print the updated balance.
# Call the function.

# balance = 10000

# def withdraw():
#     global balance

#     amount = 2500
#     balance = balance - amount

#     print(balance)

# withdraw()
#--------------------------------------------------------------------------------------------------


# ==========================================
# Python Functions — *args + **kwargs Practice
# ==========================================


# Q1. *args Basics
# Create a function that accepts multiple numbers using *args.
# Print all the values received by the function.
# Call the function with 5 different numbers.
# def values(*args):
#     print(args)
# values(1,2,3,3,4)

# Q2. *args Calculation
# Create a function that accepts multiple numbers using *args.
# Calculate the sum of all numbers.
# Return the total and print the returned value.

# def values(*info):
#     total = sum(info)
#     return total
# result = values(19,37,46,46,46)
# print(result)

# Q3. **kwargs Basics
# Create a function that accepts multiple details using **kwargs.
# Print each key and value using a loop.
# Call the function with name, age and city.

# def details(**info):
#     for key, value in info.items():
#         print(key,value)

# details(name = "vikash", age = 24, city = "kolkata")


# Q4. *args + **kwargs
# Create a function that accepts both *args and **kwargs.
# Print the positional values and keyword values separately.
# Call the function with 3 numbers and 3 details.
# def details(*args, **kwargs):
#     print(args)
#     print(kwargs)

# details(10, 20, 30, name="Vikash", city="Kolkata", age=25)

# Q5. *args + **kwargs Calculation
# Create a function that accepts numbers using *args and details using **kwargs.
# Calculate the total of all numbers and return it.
# Call the function with at least 4 numbers and 2 keyword details.

# def calculate(*args, **kwargs):
#     total = sum(args)
#     return total

# result = calculate(10, 20, 30, 40, name="Vikash", city="Kolkata")

# print(result)
#------------------------------------------------------------------------------------------------

# ==========================================
# Python Functions — Mixed Practice
# ==========================================


# Q1. Function + Return
# Create a function that takes price and quantity.
# Calculate the total amount and return it.
# Call the function and print the result.

# def product():
#     price = 500
#     quantity = 5

#     total = price * quantity
#     return total

# result = product()
# print(result)


# Q2. Function + Condition
# Create a function that takes marks.
# Return "Pass" if marks are 50 or above.
# Otherwise return "Fail".
# Call the function and print the result.

# def performance(marks):

#     if marks >= 50:
#         return "Pass"

#     else:
#         return "Fail"

# result = performance(55)
# print(result)


# Q3. Multiple Parameters + and
# Create a function that takes age and salary.
# Return "Eligible" if age is 18 or above AND salary is 30000 or above.
# Otherwise return "Not Eligible".
# Call the function and print the result.

# def cateria(age, salary):

#     if age >= 18 and salary >= 30000:
#         return  "Eligible"

#     else :
#         return "Not Eligible"

# result = cateria(23,25000)

# print(result)
    
# Q4. *args + Return
# Create a function that accepts multiple numbers using *args.
# Find the largest number.
# Return the largest number and print the result.

# def largest_number(*args):
#     largest = max(args)
#     return largest

# result = largest_number(10, 25, 7, 40, 18)
# print(result)

# Q5. **kwargs + Condition
# Create a function using **kwargs.
# Check the provided details and return "Eligible" if the person's age is 18 or above.
# Otherwise return "Not Eligible".
# Call the function with name and age.

# def details(**info):

#     if info["age"] >= 18:
#         return "Eligible"

#     else:
#         return "Not Eligible"

# result = details(age = 25)
# print(result)

# Q6. Function Calling Another Function
# Create one function to calculate the total salary using salary and bonus.
# Create another function that calls the first function and subtracts tax.
# Return the final salary and print the result.

# def calculation(salary,bonus):
#     total = salary + bonus
#     return total

# def final_salary(salary, bonus,tax):
#     total = calculation(salary , bonus)
#     result = total - tax
#     return result

# result = final_salary(25000, 5000 , 2000)
# print(result)
