#===============================
# ADVANCED PYTHON
# └── ITERATORS & ITERABLES
#===============================

# 1. Iterable kya hota hai?

# Simple language mein:

# Iterable = jis object ke andar se hum ek-ek value nikal sakte hain.

# Examples:

# numbers = [10, 20, 30, 40]

# List ek iterable hai.

# String bhi iterable hai:

# name = "Vikash"

# Tuple, Set, Dictionary bhi iterable hain.

# list
# tuple
# set
# dictionary
# string

# Isliye hum inpar for loop chala sakte hain:

# numbers = [10, 20, 30]

# for number in numbers:
#     print(number)

# Output:

# 10
# 20
# 30

# Yahan numbers ek iterable hai.

# 2. Iterator kya hota hai?

# Iterator woh object hai jo iterable ke elements ko one by one provide karta hai.

# Python mein hum iter() se iterable ko iterator bana sakte hain:

# numbers = [10, 20, 30]

# my_iterator = iter(numbers)

# Ab my_iterator ek iterator hai.

# Values ek-ek karke lene ke liye next() use karte hain:

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# Output:

# 10
# 20
# 30

# Phir agar dobara:

# print(next(my_iterator))

# karoge, to:

# StopIteration

# aayega, kyunki iterator ke andar ab koi value remaining nahi hai.

# 3. Iterable vs Iterator

# Is difference ko abhi achhe se samjho:

# Iterable
#    ↓
# iter()
#    ↓
# Iterator
#    ↓
# next()
#    ↓
# Value
#    ↓
# next()
#    ↓
# Next Value

# Example:

# numbers = [10, 20, 30]   # Iterable

# my_iterator = iter(numbers)   # Iterator

# print(next(my_iterator))      # 10
# print(next(my_iterator))      # 20
# print(next(my_iterator))      # 30
# Ek important point

# for loop internally iterator ka concept use karta hai.

# Jab hum:

# for number in numbers:
#     print(number)

# likhte hain, Python internally values ko one-by-one retrieve karta hai.

# Abhi custom iterator class ya __iter__() / __next__() nahi karenge. Pehle basic concept strong karenge.

# Practice — Iterators & Iterables

# ==========================================
# Advanced Python — Iterators & Iterables
# ==========================================

# Q1. Create a list containing 5 numbers.
# Convert the list into an iterator using iter().
# Use next() three times and print the values.

# numbers = [10, 20, 30]

# my_iterator = iter(numbers)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#-----------------------------------

# Q2. Create a string containing your name.
# Convert the string into an iterator.
# Use next() to print each character one by one.

# name = "vikash"

# my_iterator = iter(name)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#-----------------------------------

# Q3. Create a tuple containing 4 city names.
# Convert the tuple into an iterator.
# Use next() to retrieve all four city names one by one.

# city = ("Kolkata", "mumbai", "delhi", "chennai" )

# my_iterator = iter(city)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# --------------------------------------

#===============================
#(Iterables)
#===============================

# Q4. Create a list of 5 numbers.
# Use a for loop to print all values.
# Identify whether the list is an iterable or an iterator.

# numbers = [10,20 ,30, 40, 50]

# for number in numbers:
#     print(number)
#----------------------------


# Q5. Create a list containing 5 fruits.
# Use a for loop to print each fruit one by one.
# Then state whether the list is an iterable or an iterator.

# fruits = ("kela", "aam", "angur", "nariyal", "papita")

# for fruit in fruits:
#     print(fruit)

#_____________________________________________________________


# Q6. Create a dictionary containing 3 student names as keys
# and their marks as values.
# Use a for loop to print each key one by one.
# Then state whether the dictionary is an iterable or an iterator.



