# .

# 📦 Package kya hota hai?

# Simple language mein:

# Package = ek folder jisme multiple Python .py files (modules) rakhe ja sakte hain.

# Example:

# my_package/
# │
# ├── math_tools.py
# ├── user_tools.py
# └── data_tools.py

# Yahan:

# my_package → Package
# math_tools.py → Module
# user_tools.py → Module
# data_tools.py → Module

# Matlab:

# Module = ek .py file
# Package = multiple modules ka folder

# Data Analyst ke liye bas itna concept abhi important hai. 👍

#---------------------------------------------------------------------------------------------

# Package Structure — Practical

# Ab VS Code mein C:\PYTHON 37 ke andar ek folder banao:

# my_package

# Uske andar ek Python file banao:

# my_package/
# └── calculator.py

# calculator.py ke andar abhi sirf ye likho:

# def add(a, b):
#     return a + b
#----------------------------------

# from my_package.calculator import add

# result = add(10, 20)

# print(result)

# Expected output
# 30

# Yahan:

# my_package → package
# calculator → module
# add → function

# Ye Package ka basic import hai.

#--------------------------------------------------------------------------

# Perfect 👍 30 aa gaya matlab package se import successfully ho gaya. ✅

# Ab Package ka last small concept:

import my_package.calculator
result = my_package.calculator.add(5, 7)
print(result)


# Output:

# 12

# Isse tumhe ye samajhna hai ki package → module → function kaise access hota hai.


# MODULES & PACKAGES — COMPLETE ✅