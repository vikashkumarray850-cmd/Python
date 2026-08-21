# Chapter 5: Loops

# 1. for loop
# 2. range()
# 3. while loop
# 4. break
# 5. continue
# 6. pass
# 7. Nested loops
# ======================================
# FOR LOOP - LEVEL 1
# ======================================

# Q1.
# Print "Python" 5 times using a for loop.

# for i in range(5):
#     print("Python")
#----------------------------------------------------------------
# Q2.
# Print your name 10 times using a for loop.

# for i in range(10):
#     print("vikash")
#---------------------------------------------------------------
# Q3.
# Print numbers from 1 to 10.

# Q4.
# Print numbers from 1 to 20


# for i in range(1,21):
#     print(i)

#----------------------------------------------------------------------

# Q5.
# Print numbers from 10 to 1.

# for i in range(10,0,-1):
#     print(i)
#---------------------------------------------------------------------

# Q6.
# Print all even numbers from 1 to 20.

# for i in range(2,21,2):
#     print(i)
#----------------------------------------------------------------------

# Q7.
# Print all odd numbers from 1 to 20.

# for i in range(1,21,2):
#     print(i)
#-------------------------------------------------------------

# Q8.
# Print numbers from 1 to 50 that are divisible by 5.

# for i in range(5, 51, 5):
#     print(i)
#-----------------------------------------------------------------

# Q9.
# Print the square of numbers from 1 to 10.

# Example:
# 1 -> 1
# 2 -> 4
# 3 -> 9

# for i in range(1, 11):
#     print(i ** 2)
#----------------------------------------------------------------------

# Q10.
# Print the cube of numbers from 1 to 10.

# Example:
# 1 -> 1
# 2 -> 8
# 3 -> 27

# for i in range(1, 11):
#     print(i ** 3)
#-----------------------------------------------------------------------

# Q11.
# Find the sum of numbers from 1 to 10.

# total = 0

# for i in range(1, 11):
#     total = total + i

# print("Sum =", total)
#-------------------------------------------------------------------------

# Q12.
# Find the sum of numbers from 1 to 100.

# total = 0

# for i in range(1, 101):
#     total = total + i

# print("Sum=", total)
#-----------------------------------------------------------------------

# Q13.
# Find the sum of all even numbers from 1 to 100.

# total = 0

# for i in range(2, 101, 2):
#     total = total + i
# print("Sum=", total)
#------------------------------------------------------------------------

# Find the sum of all odd numbers from 1 to 100.

# total = 0

# for i in range(1, 101, 2):
#     total= total+ i
# print("Sum=", total)
#----------------------------------------------------------------------

# Q15.
# Count how many even numbers are present from 1 to 100.

# count = 0

# for i in range(2, 101, 2):
#     count = count + 1

# print("total even number", count )
#-------------------------------------------------------------------

# Q16.
# Count how many odd numbers are present from 1 to 100.

# count = 0

# for i in range(1, 101, 2):
#     count = count + 1

# print("total odd number" , count)
#------------------------------------------------------------------------

# Q17.
# Print the multiplication table of 7.

# for i in range(1, 11):
#     print(f"{7} * {i} = {7 * i} ")
#------------------------------------------------------------------------

# Q18.
# Print the multiplication table of any number using input().

# num = int(input("Enter Your Number:"))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
#-----------------------------------------------------------------------

# Q19.
# Print all numbers from 1 to 100 except numbers divisible by 3.

# for i in range(1,101):
#     if i % 3 != 0:
#         print(i)
#-------------------------------------------------------------------------

# Q20.
# Print all numbers from 1 to 100 that are divisible by both 3 and 5.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# both are same 👇👇

# for i in range(1, 101):
#     if i % 15 == 0:
#         print(i)


# ======================================
# WHILE LOOP - LEVEL 1
# ======================================

# Q1.
# Print numbers from 1 to 10 using a while loop.

# i = 1

# while i <= 10:
#     print(i)

#     i = i + 1

#------------------------------------------------------------------------------------

# Q2.
# Print numbers from 10 to 1 using a while loop.

# i = 10

# while i >= 1:
#     print(i)

#     i = i - 1
#------------------------------------------------------------------------------------

# Q3.
# Print all even numbers from 1 to 20.

# i = 2

# while i <= 20:
#     print(i)
#     i = i + 2
#----------------------------------------------------------------------------------

# Q4.
# Print all odd numbers from 1 to 20.

# i = 1

# while i <= 20:
#     print(i)
#     i = i + 2

#--------------------------------------------------------------------------

# Q5.
# Print numbers from 1 to 50 that are divisible by 5.

# i = 1

# while i <= 50:
#    if i % 5 == 0:
#     print(i)
#    i = i + 1
#--------------------------------------------------------------------------

# Q6.
# Find the sum of numbers from 1 to 10.

# total = 0
# i = 1

# while i <= 10:
#     total = total + i
#     i = i + 1

# print("Sum =", total)

#--------------------------------------------------------------------

# Q7.
# Find the sum of numbers from 1 to 100.

# total = 0
# i = 1

# while i <= 100:
#     total = total + i
#     i = i + 1
# print("Sum=", total)
#---------------------------------------------------------------------

# Q8.
# Find the sum of all even numbers from 1 to 100.

# total = 0
# i = 2

# while i <= 100:
#     total = total + i
#     i = i + 2
# print("Sum =", total)

#-----------------------------------------------------------------------

# Q9.
# Find the sum of all odd numbers from 1 to 100.

# total = 0
# i = 1

# while i <= 100:
#     total = total + i
#     i = i + 2
# print("Sum =", total)
#---------------------------------------------------------------------------

# Q10.
# Count how many even numbers are present from 1 to 100.

# count = 0
# i = 2

# while i <= 100:
#     count = count + 1
#     i = i + 2
# print("total even number", count)

#-------------------------------------------------------------------------------

# Q11.
# Count how many odd numbers are present from 1 to 100.

# count = 0
# i = 1

# while i <= 100:
#     count = count + 1
#     i = i + 2

# print("Total Odd Number", count)
#--------------------------------------------------------------------------------

# Q12.
# Print the multiplication table of 7.

# i = 1

# while i <= 10:
#     print(f"{7} * {i} = {7 * i}")
#     i = i + 1
#-------------------------------------------------------------------------------

# Q13.
# Take a number using input()
# and print its multiplication table from 1 to 10.

# num = int(input("Enter Your Number:"))

# i = 1

# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i = i + 1
#------------------------------------------------------------------------------

# Q14.
# Print all numbers from 1 to 100
# that are divisible by both 3 and 5
# using a while loop.
# i = 1

# while i <= 100:
#     if i % 15 == 0:
#         print(i)
#     i = i + 1
#-----------------------------------------------------------------------------
# ======================================
# FACTORIAL PRACTICE
# ======================================
# Q16.
# Find the factorial of a number using a while loop.
#
# Example:
# Input: 5
# Output: 120
#
# Because:
# 5 × 4 × 3 × 2 × 1 = 120

# num = int(input("Enter Your Number:"))

# result = 1

# while num >= 1:
#     result = result * num
#     num = num - 1

# print("factorial =", result)
#----------------------------------------------------------------------------------------

# Q1.
# Take a number using input()
# and find its factorial using a while loop.
#
# Example:
# Input: 4
# Output: 24
#
# Because:
# 4 × 3 × 2 × 1 = 24

# num = int(input("Enter Your Number:"))
# result = 1

# while num >= 1:
#     result = result * num
#     num = num - 1

# print("factorial=", result)

#----------------------------------------------------------------------------\

# Q2.
# Take a number using input()
# and find its factorial using a while loop.
#
# Example:
# Input: 6
# Output: 720
#
# Because:
# 6 × 5 × 4 × 3 × 2 × 1 = 720

# num = int(input("Enter Your Number:"))

# result = 1

# while num >= 1:
#     result = result * num
#     num = num - 1

# print(result)
#------------------------------------------------------------------------------

# Q17.
# Take a number using input()
# and print its reverse.
#
# Example:
# Input: 12345
# Output: 54321

# num = int(input("Enter Your Number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse =", reverse)
#------------------------------------------------------------------------
# ======================================
# DIGIT EXTRACTION - WHILE LOOP
# ======================================

# Q1.
# Take a number using input()
# and print each digit separately.
#
# Example:
# Input: 1234
# Output:
# 4
# 3
# 2
# 1

# num = int(input("Enter Your Number: "))

# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10
#--------------------------------------------------------------

# Q2.
# Take a number using input()
# and print each digit separately.
#
# Example:
# Input: 5678
# Output:
# 8
# 7
# 6
# 5

# num = int(input("Enter your number:"))

# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10
#----------------------------------------------------------------

# Q3.
# Take a number using input()
# and print the last digit of the number.
#
# Example:
# Input: 12345
# Output:
# 5

# num = int(input("Enter Your Number: "))

# digit = num % 10

# print(digit)
#-----------------------------------------------------------------------

# Q4.
# Take a number using input()
# and print the last two digits separately.
#
# Example:
# Input: 12345
# Output:
# 5
# 4

# num = int(input("enter your number:"))

# digit = num % 10
# print(digit)

# num = num // 10

# digit = num % 10
# print(digit)

#----------------------------------------------------------------------

# Q5.
# Take a number using input()
# and print all digits one by one.
#
# Example:
# Input: 90876
# Output:
# 6
# 7
# 8
# 0
# 9

# num = int(input("enter your number:"))

# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10
#-------------------------------------------------------------------------------------

# Q6.
# Take a number using input()
# and print its reverse using a while loop.
#
# Example:
# Input: 12345
# Output:
# 54321

# num = int(input("enter your number:"))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("reverse=", reverse)
#----------------------------------------------------------------------

# Q2.
# Take a number using input()
# and print its reverse.
#
# Example:
# Input: 6789
# Output: 9876

# num = int(input("enter your number:"))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num  // 10

# print(reverse)
#-----------------------------------------------------------------------------

# Q3.
# Take a number using input()
# and print its reverse.
#
# Example:
# Input: 1205
# Output: 5021

# num = int(input("enter your number:"))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)
#-------------------------------------------------------------------------

# Q4.
# Take a number using input()
# and print its reverse.
#
# Example:
# Input: 9087
# Output: 7809

# num = int(input("enter your number:"))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)
#-----------------------------------------------------------------------------

# Q5.
# Take a number using input()
# and print its reverse.
#
# Example:
# Input: 45678
# Output: 87654 

# num = int(input(" enter your name :"))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)
#---------------------------------------------------------------------
# ======================================
# PALINDROME - PRACTICE
# ======================================

# Q1.
# Take a number using input()
# and check whether it is a palindrome.
#
# Example:
# Input: 121
# Output: Palindrome

# num = int(input("enter your number:"))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome")
# else :
#     ("Not Palindrome")
#--------------------------------------------------------------------------

# Q5.
# Take a number using input()
# and check whether it is a palindrome.
#
# Example:
# Input: 4567
# Output: Not Palindrome

# num = int(input("Enter Your Number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#-------------------------------------------------------------------------------

# Q2.
# Take a number using input()
# and check whether it is a palindrome.
#
# Example:
# Input: 12321
# Output: Palindrome

# num = int(input("enter your number:"))

# original = num 
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome")

# else :
#     print("Not Palindrome")

#---------------------------------------------------------------------------

#Digit Count

# Q1.
# Take a number using input()
# and count how many digits it has.
#
# Example:
# Input: 9876
# Output:
# Total Digits = 4

# num = int(input("enter your number :"))
# count = 0

# while num > 0:
#     digit = num % 10
#     count = count + 1
#     num = num // 10

# print(count)
#-------------------------------------------------------------------------------

# Q2.
# Take a number using input()
# and count how many digits it has.
#
# Example:
# Input: 123456789
# Output:
# 9

# num = int(input("enter your number :"))
# count = 0

# while num > 0:
#     digit = num % 10
#     count = count + 1
#     num = num // 10

# print(count)
#----------------------------------------------------------------
# Q3.
# Take a number using input()
# and find the sum of all its digits.
#
# Example:
# Input: 12345
# Output:
# Sum = 15
#
# Because:
# 1 + 2 + 3 + 4 + 5 = 15

# num = int(input("enter your number:"))
# total = 0

# while num > 0 :
#     digit = num % 10
#     total = total + digit
#     num =  num // 10

# print(total)
#------------------------------------------------------------------------------------------

# Take a number using input()
# and find the sum of all its digits.
#
# Example:
# Input: 2468
# Output:
# Sum = 20

# num = int(input("enter your number:"))
# total = 0

# while num > 0:
#     digit = num % 10
#     total = total + digit
#     num = num // 10

# print(total)
#-------------------------------------------------------------------------------

# Q6.
# Take a number using input()
# and find the product of all its digits.
#
# Example:
# Input: 1234
# Output:
# Product = 24
#
# Because:
# 1 × 2 × 3 × 4 = 24

# num = int(input("enter yopur number:"))

# product = 1

# while num > 0:
#     digit = num % 10
#     product = product * digit
#     num = num // 10

# print("Product =", product)
#---------------------------------------------------------------------------------

# Q8.
# Take a number using input()
# and find the largest digit in the number.
#
# Example:
# Input: 58321
# Output:
# Largest Digit = 8

# num = int(input("enter your number:"))

# largest = 0

# while num > 0:
#     digit = num % 10

#     if digit > largest:
#       largest = digit

#     num = num // 10

# print("largest digit =", largest)
#-----------------------------------------------------------------------------------

# Take a number using input()
# and find the largest digit in the number.
#
# Example:
# Input: 74621
# Output:
# Largest Digit = 7

# num = int(input("enter your number:"))
# largest = 0

# while num > 0:
#     digit = num % 10

#     if digit > largest :
#         largest = digit

#     num = num // 10

# print("largest number = ", largest)
#-------------------------------------------------------------------------------------

# Take a number using input()
# and find the smallest digit in the number.
#
# Example:
# Input: 58321
# Output:
# Smallest Digit = 1

# num = int(input("enter your number:"))
# smallest = num % 10

# while num > 0:
#     digit = num % 10

#     if digit < smallest :
#         smallest = digit

#     num = num // 10

# print("smallest number = ", smallest)

# ======================================
# BREAK - PRACTICE QUESTIONS
# ======================================

# Q1.
# Print numbers from 1 to 20.
# Stop the loop when the number reaches 8.
#
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# for i in range(1, 21):
#     if i == 8:
#         break
#     print(i)
#----------------------------------------------------------------------------

# Q2.
# Print numbers from 1 to 50.
# Stop the loop when you find the first number
# that is divisible by 7.

# for i in range(1, 51):
#     if i % 7 == 0:
#         break
#     print(i)
#----------------------------------------------------------------------------

# Q3.
# Take a number from the user.
# Search for that number from 1 to 100.
# If the number is found, print "Number Found"
# and stop the loop using break.

# num = int(input("Enter Your Number: "))

# for i in range(1, 101):
#     if i == num:
#         print("Number Found")
#         break

# ======================================
# CONTINUE - PRACTICE QUESTIONS
# ======================================

# Q1.
# Print numbers from 1 to 20.
# Skip the number 10 using continue.
#
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 11
# 12
# ...
# 20

# for i in range(1, 21):
#     if i == 10:
#         continue
#     print(i)

# Q2.
# Print numbers from 1 to 50.
# Skip all numbers that are divisible by 5.
# Use continue.

# for i in range(1, 51):
#     if i % 5 == 0:
#         continue
#     print(i)

# Q3.
# Print only odd numbers from 1 to 100.
# Use continue to skip all even numbers.
#
# Expected Output:
# 1
# 3
# 5
# 7
# ...
# 99

# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     print(i)

# ======================================
# PASS - PRACTICE QUESTIONS
# ======================================

# Q1.
# Print numbers from 1 to 10.
# When the number is 5, use pass.
# Observe whether 5 gets printed or not.

# for i in range(1, 11):
#     if i == 5 :
#         pass
#     print(i)

# Q2.
# Create a for loop from 1 to 10.
# If the number is even, use pass.
# Print every number.
#
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for i in range(1,11):
#     if i % 2 == 0:
#         pass
#     print(i)


