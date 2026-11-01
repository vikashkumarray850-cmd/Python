#===============================
# ADVANCED PYTHON
# └── GENERATORS
#===============================

# Generator kya hota hai?

# Simple language mein:

# Generator ek special type ka function hai jo values ko ek-ek karke generate karta hai, instead of saari values ek saath memory mein rakhne ke.

# Normal function mein hum return use karte hain:

# def numbers():
#     return [1, 2, 3, 4, 5]

# Ye poori list ek saath return karega.

# Generator mein hum yield use karte hain:

# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# Ab ye function values ko one by one deta hai.

# 2. Generator function ko call karne par
# my_generator = numbers()

# Yahan important baat:

# numbers() turant 1, 2, 3, 4, 5 nahi deta.

# Ye ek generator object banata hai.

# Phir:

# print(next(my_generator))

# Output:

# 1

# Dobara:

# print(next(my_generator))

# Output:

# 2

# Phir:

# 3

# Aur isi tarah.

# 3. yield ka basic idea
# Generator Function
#        ↓
#      yield 1
#        ↓
#      next()
#        ↓
#        1

#      yield 2
#        ↓
#      next()
#        ↓
#        2

# Yani generator ek value deta hai aur wahi se pause ho jata hai. Agli next() call par wahi se continue karta hai.

# 4. Data Analyst ke liye useful kyun?

# Agar data bahut bada ho, jaise:

# 10 lakh rows
# 50 lakh rows
# 1 crore records

# toh har value ko ek saath memory mein rakhna expensive ho sakta hai.

# Generator data ko one-by-one process karne ka concept deta hai.

# Abhi hum sirf basic generator samjhenge. yield ko alag se next topic mein detail mein karenge.

# Practice — Generators

# ==========================================
# Advanced Python — Generators
# ==========================================

# Q1. Create a generator function that generates
# the numbers 1, 2, and 3 using yield.
# Create a generator object.
# Use next() three times to print the values.

# def numbers():
#     yield 1
#     yield 2
#     yield 3

# my_generator = numbers()

# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
#---------------------------------

# Q2. Create a generator function that generates
# three city names using yield.
# Create a generator object.
# Use next() to print each city name one by one.

# def city():
#     yield "Kolkata"
#     yield "Mumbai"
#     yield "Delhi"

# my_generator = city()

# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

# Q3. Create a generator function that generates
# the numbers 10, 20, 30, 40, and 50 using yield.
# Use a for loop to print all generated values.

# def numbers():
#     yield 10
#     yield 20
#     yield 30
#     yield 40
#     yield 50

# for number in numbers():
#     print(number)

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
#-----------------------------------------------------------------------------------------------------------

