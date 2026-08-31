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