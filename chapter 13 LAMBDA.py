# ==========================================
# Python Lambda Functions — Basic Practice
# ==========================================


# Q1. Square
# Create a lambda function that takes one number.
# Return the square of the number.
# Call the lambda function and print the result.

# square = lambda a: a * a

# print(square(5))

# Q2. Addition
# Create a lambda function that takes two numbers.
# Add both numbers and print the result.

# add = lambda a,b: a + b
# print(add(20,20))

# Q3. Multiplication
# Create a lambda function that takes two numbers.
# Multiply both numbers and store the returned value in a variable.
# Print the variable.

# Multiplication = lambda a,b: a * b
# print(Multiplication(200,5))

# Q4. Subtraction
# Create a lambda function that takes two numbers.
# Subtract the second number from the first number.
# Call the function and print the result.

# Subtraction = lambda a,b: a - b
# print(Subtraction(200,5))

# Q5. Average
# Create a lambda function that takes three numbers.
# Calculate their average and print the result.

# Average = lambda a , b, c: (a + b + c) / 3

# print(Average(10,10,10))
#--------------------------------------------------------------------------------------

# ==========================================
# Lambda Functions — Conditions
# ==========================================


# Q1. Even or Odd
# Create a lambda function that takes one number.
# Return "Even" if the number is even.
# Otherwise return "Odd".
# Call the function and print the result.

# check = lambda number : "Even" if number % 2 == 0 else "Odd"

# result = check(2)
# print(result)

# Q2. Pass or Fail
# Create a lambda function that takes marks.
# Return "Pass" if marks are 50 or above.
# Otherwise return "Fail".
# Call the function and print the result.

# details = lambda marks : "Pass" if marks >= 50 else "Fail"

# result = details(39)
# print(result)


# Q3. Adult or Minor
# Create a lambda function that takes age.
# Return "Adult" if age is 18 or above.
# Otherwise return "Minor".
# Call the function and print the result.

# info = lambda age : "Adult" if age >= 18 else "Minor"

# result = info(26)
# print(result)

# Q4. Positive or Negative
# Create a lambda function that takes a number.
# Return "Positive" if the number is greater than or equal to 0.
# Otherwise return "Negative".
# Call the function and print the result.

# status = lambda number : "Positive" if number >= 0 else "Negative"

# result = status(0)
# print(result)

# Q5. Salary Check
# Create a lambda function that takes salary.
# Return "Good Salary" if salary is 30000 or above.
# Otherwise return "Average Salary".
# Call the function and print the result.

# Salary_Check = lambda salary : "Good Salary" if salary >= 30000 else "Average Salary" 

# result = Salary_Check(25000)
# print(result)
#-------------------------------------------------------------------------------------------------------

# ==========================================
# Python Lambda — map() Practice
# ==========================================


# Q1. Double Numbers
# Create a list of numbers.
# Use map() and lambda to multiply every number by 2.
# Convert the result into a list and print it.

# number = [1, 2, 3, 4, 5]

# result = map(lambda x: x * 2, number)

# print(list(result))

# Q2. Square Numbers
# Create a list of numbers.
# Use map() and lambda to find the square of every number.
# Convert the result into a list and print it.
# number = [1, 2, 3, 4, 5]

# result = map(lambda a: a * a, number)
# print(list(result))

# Q3. Add 5
# Create a list of numbers.
# Use map() and lambda to add 5 to every number.
# Convert the result into a list and print it.

# number = [1, 2, 3, 4, 5]

# result = map(lambda a: a + 5,number)
# print(list(result))

# Q4. Convert to Uppercase
# Create a list of names.
# Use map() and lambda to convert every name to uppercase.
# Convert the result into a list and print it.
# names = ["vikash", "rohit", "mohit", "zen" ]

# result = map(lambda name: name.upper(), names)
# print(list(result))


# Q5. Calculate Final Price
# Create a list of prices.
# Use map() and lambda to add 100 delivery charge to every price.
# Convert the result into a list and print it.

# prices = [20, 30 , 40 , 50] 

# result = map(lambda price: price + 50, prices)
# print(list(result))
#-------------------------------------------------------------------------------------------

# ==========================================
# Python Lambda — filter() Practice
# ==========================================


# Q1. Even Numbers
# Create a list of numbers.
# Use filter() and lambda to select only even numbers.
# Convert the result into a list and print it.

# number = [1, 2, 3, 4, 5]

# result = filter(lambda a: a % 2==0, number)
# print(list(result))


# Q2. Numbers Greater Than 10
# Create a list of numbers.
# Use filter() and lambda to select numbers greater than 10.
# Convert the result into a list and print it.

# numbers = [1, 2, 3, 4, 5,12]

# result = filter(lambda number:number > 10, numbers )
# print(list(result))

# Q3. Positive Numbers
# Create a list containing positive and negative numbers.
# Use filter() and lambda to select only positive numbers.
# Convert the result into a list and print it.

# numbers = [1, 2, -3, 4, -5]

# result = filter(lambda number: number > 0, numbers)
# print(list(result))

# Q4. Passing_Marks
# Create a list of marks.
# Use filter() and lambda to select marks that are 50 or above.
# Convert the result into a list and print it.

# Passing_Marks = [30, 40, 20 ,70,80]

# result = filter(lambda marks: marks >= 50, Passing_Marks )
# print(list(result))


# Q5. Salary_Filter
# Create a list of salaries.
# Use filter() and lambda to select salaries that are 30000 or above.
# Convert the result into a list and print it.

# Salary_Filter = [38800, 20000, 15000]

# result = filter(lambda salary: salary >= 30000, Salary_Filter)
# print(list(result))
#-----------------------------------------------------------------------------------------------------

# ==========================================
# Python Lambda — reduce() Practice
# ==========================================


# Q1. Sum of Numbers
# Import reduce from functools.
# Create a list of numbers.
# Use reduce() and lambda to calculate the total.
# Print the result.

# from functools import reduce
# numbers = [1, 2, 3, 4]

# result = reduce(lambda a, b: a + b, numbers)

# print(result)

# Q2. Multiplication
# Import reduce from functools.
# Create a list of numbers.
# Use reduce() and lambda to multiply all numbers.
# Print the result.

# from functools import reduce
# numbers = [1, 2, 3, 4]

# result = reduce(lambda a, b: a * b, numbers)
# print(result)


# Q3. Find the Largest Number
# Import reduce from functools.
# Create a list of numbers.
# Use reduce() and lambda to find the largest number.
# Print the result.

# from functools import reduce
# numbers = [1, 2, 3, 4]

# result = reduce(lambda a, b:a if a>b else b, numbers  )
# print(result)

# Q4. Calculate Total Salary
# Import reduce from functools.
# Create a list of salaries.
# Use reduce() and lambda to calculate the total salary.
# Print the result.

# from functools import reduce
# salary = [38800, 20000, 15000]

# result = reduce(lambda a , b: a + b, salary )
# print(result)