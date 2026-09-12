
# Recursion ka simple meaning hai:

# Ek function apne aap ko hi call karta hai.

# Example:

# def count(n):
#     if n == 0:
#         return

#     print(n)
#     count(n - 1)

# count(5)

# Output:

# 5
# 4
# 3
# 2
# 1

# Yahan:

# count(5)
#    ↓
# count(4)
#    ↓
# count(3)
#    ↓
# count(2)
#    ↓
# count(1)
#    ↓
# count(0) → stop
# Recursion mein 2 cheezein important hain

# 1. Base Condition
# Function ko batati hai kab rukna hai.

# if n == 0:
#     return

# 2. Recursive Call
# Function apne aap ko call karta hai.

# count(n - 1)

# Agar base condition nahi hogi, function continuously khud ko call karta rahega.

# ============================================
# RECURSION PRACTICE SET - 1
# Rules: Sirf recursion use karna hai, loop (for/while) nahi
# Har function mein base case zaroor hona chahiye

# ============================================
# RECURSION PRACTICE - Set 1 (Q2 se Q5)
# Tareeka: Har function mein teen cheezein socho
#   A) Base case - kab rukna hai?
#   B) Rukne se pehle kya kaam karna hai?
#   C) Khud ko chhote input ke saath kaise call karna hai?

# ============================================


# Q1. Ek function banao print_hi(n) jo n baar "Hi" print kare
# Example: print_hi(4)
# Output:
# Hi
# Hi
# Hi
# Hi

# def print_hi(n):
#     if n == 0:
#         return
#     print("hi")
#     print_hi(n - 1)

# print_hi(4)


# Q2. Ek function banao count_down(n) jo n se 1 tak numbers print kare (ulta)
# phir last mein "Liftoff!" print kare
# Example: count_down(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!

# def count_down(n):
#     if n == 0:
#         print("Liftoff!")
#         return
#     print(n)
#     count_down(n - 1)

# count_down(5)

    
# Q3. Ek function banao count_up(n) jo 1 se n tak numbers print kare (seedha order)
# Example: count_up(4)
# Output:
# 1
# 2
# 3
# 4
# Hint: print aur recursive call ka order badalna padega

# def count_up(n):
#     if n == 0:
#         return
#     count_up(n - 1)    # PEHLE call karo
#     print(n)            # BAAD mein print karo
# count_up(4)


# Q4. Ek function banao print_even(n) jo 1 se n tak sirf EVEN numbers print kare
# Example: print_even(10)
# Output:
# 2
# 4
# 6
# 8
# 10

# def print_even(n):
#     if n == 0:          # base case - poori tarah rukna
#         return
#     print_even(n - 1)    # pehle chhote number ka kaam karo
#     if n % 2 == 0:        # phir check karo - yeh number even hai?
#         print(n)          # agar haan, to print karo

# print_even(10)



# Q5. (Thoda tricky) Ek function banao star_pattern(n) jo yeh pattern print kare
# Example: star_pattern(4)
# Output:
# *
# **
# ***
# ****

# def star_pattern(n):
#     if n==0:
#         return
#     star_pattern(n -1)
#     print("*" * n)

# star_pattern(4)
#----------------------------------------------------------------------------------

#Theek hai, sirf sum_n wale pattern pe focused practice karte hain — same style ke 3 questions.

# Pattern (sum_n jaisa hi):
# def func(n):
#     if n == 0:
#         return <base value>
#     return n <operation> func(n - 1)


# Q1. product_n(n) — 1 se n tak sabka product (multiply)
# Example: product_n(4) → 4*3*2*1 = 24
# Hint: sum_n mein tha "n + sum_n(n-1)", yahan "+" ki jagah "*" use karo
#       base case mein return 1 hoga (0 nahi, warna sab 0 ho jayega)

# def product_n(n):
#     if n == 0:
#         return 1
#     return n * product_n(n - 1)

# print(product_n(4))


# Q2. sum_even(n) — 1 se n tak sirf even numbers ka sum
# Example: sum_even(6) → 2+4+6 = 12
# Hint: sum_n jaisa hi hai, bas check add karo -
#       agar n even hai to n add karo, warna sirf sum_even(n-1) return karo

# def sum_even(n):
#     if n == 0:
#         return 0
#     if n % 2 == 0:              # agar n even hai
#         return n + sum_even(n - 1)   # to add karo
#     else:
#         return sum_even(n - 1)        # warna skip karo, bas aage badho

# print(sum_even(6))   # expect 12


# Q3. sum_squares(n) — 1 se n tak numbers ke squares ka sum
# Example: sum_squares(3) → 1*1 + 2*2 + 3*3 = 1+4+9 = 14
# Hint: sum_n jaisa hi, bas "n" ki jagah "n*n" add karo

# def sum_squares(n):
#     if n == 0:
#         return 0          # base case bhi 0 honi chahiye (sum ke liye), 1 nahi
#     return (n * n) + sum_squares(n - 1)

# print(sum_squares(3))
#--------------------------------------------------------------------------------------------

#Step 4 — Practice (Return Value Recursion)

# Q1. sum_of_digits(n) — sum of all digits of a number
# Example: sum_of_digits(123) → 1+2+3 = 6
# Hint: n % 10 gives the last digit, n // 10 removes the last digit

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_of_digits(n // 10)
# print(sum_of_digits(123))     # expect 6

# Q2. count_digits(n) — count how many digits a number has
# Example: count_digits(12345) → 5

# def count_digits(n):
#     if n == 0:
#         return 0
#     return 1 + count_digits(n // 10)
# print(count_digits(12345))     # expect 5

# Q3. power(base, exp) — raise base to the power exp (don't use **)
# Example: power(2, 3) → 8

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)
# print(power(2, 3))              # expect 8

# print(sum_of_digits(123))     # expect 6
# print(count_digits(12345))     # expect 5
# print(power(2, 3))              # expect 8
#-----------------------------------------------------------------------------------------

#Step 5: Fibonacci — Function Calls Itself TWICE

# Rule samjho: Har number, apne pehle do numbers ka sum hota hai.

# Dekho:

# Position 0: 0
# Position 1: 1
# Position 2: 0 + 1 = 1
# Position 3: 1 + 1 = 2
# Position 4: 1 + 2 = 3
# Position 5: 2 + 3 = 5
# Position 6: 3 + 5 = 8

# Matlab agar tumhe position n ka number chahiye, to formula hai:

# fib(n) = fib(n-1) + fib(n-2)

# Yaani, current number = pichle wale + uske bhi pichle wale

#------------------------------------------------------------------------------

# ==========================================
# Python Recursion — Base Condition Practice
# ==========================================


# Q1.
# Create a recursive function named count().
# The function should print the value of n.
# Add a condition that stops the recursion when n becomes 0.
# Call the function with 3.

# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n - 1)
# count(3)
# Q2.
# Create a recursive function named show().
# The function should print the value of n.
# Add a condition that stops the function when n becomes 1.
# Call the function with 5.

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n - 1)
# show(5)

# Q3.
# Create a recursive function named number().
# The function should print the value of n.
# Add a condition that stops the recursion when n becomes 0.
# Call the function with 4.

# def number(n):
#     if n == 0:
#         return
#     print(n)
#     number(n - 1)
# number(4)

# Q4.
# Create a recursive function named test().
# The function should stop immediately when n is equal to 0.
# Otherwise, print n and continue the recursive process.
# Call the function with 5.

# def test(n):
#     if n == 0:
#         return
#     print(n)
#     test(n - 1)
# test(5)

#-----------------------------------------------------------------------------------------

# ==========================================
# Python Recursion — Recursive Call Practice
# ==========================================


# Q1.
# Create a recursive function named count().
# Start with 1 and print numbers up to 5.
# Use a recursive call to move to the next number.
# Stop the recursion after printing 5.

# def count(n):
#     if n > 5:
#         return
#     print(n)
#     count(n + 1)
# count(1)

# Q2.
# Create a recursive function named show().
# Start with 10 and print every second number in decreasing order.
# Continue using a recursive call.
# Stop when the number becomes 0 or below.
# def show(n):
#     if n <= 0:
#         return
#     print(n)
#     show(n - 2)
# show(10)

# Q3.
# Create a recursive function named numbers().
# Take a number as a parameter.
# Print the number before making the recursive call.
# Then reduce the number by 1 and call the function again.
# Stop when the number reaches 1.
# Call the function with 4.

# def numbers(n):

#     if n == 1:
#         print(n)
#         return

#     print(n)
#     numbers(n - 1)

# numbers(4)
#-------------------------------------------------------------------------------------


# ==========================================
# Python Recursion — Countdown & Count Up Practice
# ==========================================

# Q1. Countdown
# Create a recursive function named countdown().
# Start with 7.
# Print the numbers in decreasing order.
# Stop after reaching 1.
# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n - 1)
# # countdown(7)
    


# Q2. Count Up
# Create a recursive function named count_up().
# Start with 2.
# Print the numbers in increasing order.
# Stop after reaching 7.

# def count_up(n):

#     if n > 7:
#         return

#     print(n)
#     count_up(n + 1)

# count_up(2)

# Q3. Countdown by 2
# Create a recursive function named countdown().
# Start with 10.
# Print the numbers in decreasing order with a gap of 2.
# Stop when the next value reaches 0 or below.

# def countdown(n):
#     if n <= 0:
#         return
#     print(n)
#     countdown(n - 2)
# countdown(10)
#------------------------------------------------------------------------------------


# ==========================================
# Python Recursion — Sum of Numbers Practice
# ==========================================


# Q1.
# Create a recursive function named total().
# Take a positive integer as a parameter.
# Calculate the sum from 1 up to that number.
# Return the final result.
# Call the function with 5 and print the result.

# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)
# result = total(5)
# print(result)
    

# Q2.
# Create a recursive function named add_numbers().
# Take a positive integer as a parameter.
# Calculate the sum from 1 up to that number using recursion.
# Return the final result.
# Call the function with 7 and print the result.

# def add_numbers(n):
#     if n == 0:
#         return 0
#     return n + add_numbers(n - 1)
# result = add_numbers(7)
# print(result)

# Q3.
# Create a recursive function named sum_numbers().
# Take a positive integer as a parameter.
# Calculate the sum of all numbers from 1 up to that number.
# Use a base condition to stop the recursion.
# Return the final result.
# Call the function with 10 and print the result.

# def sum_numbers(n):
#     if n == 0:
#         return 0
#     return n + sum_numbers(n - 1)
# result = sum_numbers(10)
# print(result)
#------------------------------------------------------------------------------------

# ==========================================
# Python Recursion — Factorial Practice
# ==========================================


# Q1.
# Create a recursive function named factorial().
# Take a positive integer as a parameter.
# Use a base condition to stop the recursion.
# Calculate the factorial using recursion.
# Call the function with 4 and print the result.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))

# Q2.
# Create a recursive function named fact().
# Take a positive integer as a parameter.
# Calculate its factorial using recursion.
# Call the function with 5 and print the result.

# def fact(n):
#     if n == 0:
#         return 1
#     return n * factorial( n - 1)
# print(factorial(5))


# Q3.
# Create a recursive function named calculate_factorial().
# Take a positive integer as a parameter.
# Use a base condition.
# Calculate the factorial using recursion.
# Call the function with 6 and print the result.

# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     return n * calculate_factorial(n - 1)

# print(calculate_factorial(6))


# ==========================================
# Python Recursion — Factorial Variation
# ==========================================


# Q1.
# Create a recursive function named factorial().
# Take a number as a parameter.
# Use a base condition to stop the recursion.
# Calculate the factorial using recursion.
# Take a number from the user using input().
# Call the function with the entered number.
# Print the factorial result.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# num = int(input("ENTER YOUR NUMBER:"))

# print(factorial(num))
#-----------------------------------------------------------------------------------

# ==========================================
# Python Recursion — Power of a Number
# ==========================================


# Q1.
# Create a recursive function named power().
# Take base and exponent as parameters.
# Calculate base raised to the exponent using recursion.
# Use a base condition to stop the recursion.
# Call the function with base = 2 and exponent = 4.
# Print the result.
# def power(base, exponent):
#     if exponent == 0:
#         return 1

#     return base* power(base, exponent - 1)
# print(power(2, 4))

# Q2.
# Create a recursive function named calculate_power().
# Take base and exponent as parameters.
# Calculate the power using recursion.
# Call the function with base = 3 and exponent = 3.
# Print the result.

# def calculate_power(base, exponent):
#     if exponent== 0:
#         return 1
#     return base * calculate_power(base, exponent - 1)

# print(calculate_power(3, 3))


# Q3.
# Create a recursive function named power_number().
# Take base and exponent as parameters.
# Use recursion to calculate the power.
# Call the function with base = 5 and exponent = 2.
# Print the result.

# def power_number(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power_number(base, exponent - 1)

# print(power_number(5,2))

#----------------------------------------------------------------------------------------------------

# ==========================================
# Python Recursion — Reverse String Practice
# ==========================================


# Q1.
# Create a recursive function named reverse_string().
# Take a string as a parameter.
# Reverse the string using recursion.
# Use a base condition to stop the recursion.
# Call the function with "hello".
# Print the result.

# def reverse_string(text):
#     if len(text) <= 1:
#         return text

#     return reverse_string(text[1:]) + text[0]

# print(reverse_string("hello"))

# Q2.
# Create a recursive function named reverse_text().
# Take a string as a parameter.
# Reverse the string using recursion.
# Use a base condition.
# Call the function with "python".
# Print the result.

# def reverse_text(text):
#     if len(text) <= 1:
#         return text

#     return reverse_text(text[1:]) + text [0]

# print(reverse_text("python")) 

# Q3.
# Create a recursive function named reverse_word().
# Take a string as a parameter.
# Reverse the string using recursion.
# Use a base condition to stop the recursion.
# Call the function with "data".
# Print the result.

# def reverse_word(text):
#     if len(text) <= 1:
#         return text

#     return reverse_word(text[1:]) + text[0]

# print(reverse_word("data"))
#-----------------------------------------------------------------------------

# ==========================================
# Python Recursion — Fibonacci Practice
# ==========================================


# Q1.
# Create a recursive function named fibonacci().
# Take a number n as a parameter.
# Use a base condition for n <= 1.
# Return the sum of the previous two Fibonacci values.
# Call the function with 5.
# Print the result.

# def fibonacci(n):
#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(5))

# Q2.
# Create a recursive function named fib().
# Take a number n as a parameter.
# Use recursion to calculate the Fibonacci value.
# Use a base condition to stop the recursion.
# Call the function with 6.
# Print the result.

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n -1) + fibonacci(n -2)   

# print(fibonacci(6))

# Q3.
# Create a recursive function named fibonacci_number().
# Take a number n as a parameter.
# Calculate the Fibonacci value using recursion.
# Use both previous Fibonacci values in the recursive call.
# Call the function with 7.
# Print the result.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n -1) + fibonacci(n -2)   

print(fibonacci(7))







def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num // 10)


count = count_digits(num)

print(count)




