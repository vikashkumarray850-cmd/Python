#===============================
# RETURN VS YIELD
#===============================

# Normal function mein return function ko completely stop kar deta hai:

# def number():
#     return 10
#     return 20

# Yahan sirf 10 milega. 20 kabhi execute nahi hoga.

# yield alag hai:

# def number():
#     yield 10
#     yield 20

# Yahan function pehli yield par pause hota hai. Next next() call par wahi se continue hota hai.

# my_generator = number()

# print(next(my_generator))  # 10
# print(next(my_generator))  # 20

# Output:

# 10
# 20
# Sabse important baat
# return → value do → function finish

# yield  → value do → pause → next() par continue

# Isi wajah se generator large data ko one-by-one process karne mein useful hota hai.

# Ab yield ka ye difference practice karte hain:

# ==========================================
# Advanced Python — yield Practice
# ==========================================

# Q1. Create a function using yield.
# Generate the numbers 5, 10, and 15.
# Create a generator object.
# Use next() to get all three values.

# def numbers():
#     yield 5
#     yield 10
#     yield 15

# my_generator = numbers()

# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
#____________________________________________________

# Q2. Create a generator function.
# Generate the names "Vikash", "Ravi", and "Mohit".
# Use a for loop to print each name.

# def names():
#     yield "Vikash"
#     yield "Ravi"
#     yield "Mohit"

# for name in names():
#     print(name)
# #_________________________________________

# Q3. Create a generator function.
# Generate the numbers 100, 200, and 300.
# Store the generator object in a variable.
# Print the first value using next().
# Then print the remaining values using a for loop.

# def numbers():
#     yield 100
#     yield 200
#     yield 300

# my_generator = numbers()

# print(next(my_generator))

# for number in my_generator:
#     print(number)

# Teeno karo. Is baar focus yield pause/resume behavior par rakhenge.