#============================================
# ADVANCED PYTHON — *ARGS / **KWARGS REVISION
#============================================

# Ye dono hum pehle Functions chapter mein kar chuke hain. 
# Ab Advanced Python mein quick revision + practical use karenge.

# 1. *args

# Jab function mein pata nahi ho ki kitne positional arguments aayenge, 
# tab *args use karte hain.

# def total(*numbers):
#     print(numbers)
# total(10, 20, 30)

# Output:
# (10, 20, 30)

# args ke andar values tuple ke form mein aati hain.
# Isliye loop bhi laga sakte hain:

# def total(*numbers):
#     result = 0

#     for number in numbers:
#         result += number

#     return result

# print(total(10, 20, 30, 40))

# Output:
# 100

# 2. **kwargs

# Jab function mein pata nahi ho ki kitne keyword arguments aayenge, 
# tab **kwargs use karte hain.

# def details(**info):
#     print(info)

# details(name="Vikash", age=25, city="Kolkata")

# Output:
# {'name': 'Vikash', 'age': 25, 'city': 'Kolkata'}

# kwargs ke andar values dictionary ke form mein aati hain.

# Isliye:

# for key, value in info.items():
#     print(key, value)
# 3. Dono saath
# def data(*args, **kwargs):
#     print(args)
#     print(kwargs)

# data(10, 20, 30, name="Vikash", city="Kolkata")

# Output:

# (10, 20, 30)
# {'name': 'Vikash', 'city': 'Kolkata'}

# Yaad rakhne ka simple rule:

# *args    → positional values → tuple
# **kwargs → keyword values    → dictionary

# Ab isi revision par 3 focused practice questions karte hain.

# ==========================================
# Advanced Python — *args / **kwargs Revision
# ==========================================

# Q1. Create a function using *args.
# Accept multiple numbers and calculate their total.

# def total(*numbers):
#     result = 0

#     for number in numbers:
#         result += number

#     return result

# print(total(10, 20, 30, 40))
    

# Q2. Create a function using **kwargs.
# Accept employee details such as name, age and salary.
# Print each key and value.

# def employee_details(**info):
#     for key, value in info.items():
#         print(key, value)

# employee_details(
#     name="Vikash",
#     age=25,
#     salary=30000
# )

# Q3. Create a function using both *args and **kwargs.
# Accept multiple numbers using *args.
# Accept employee details using **kwargs.
# Print the numbers and employee details.

def data(*numbers, **info):
    print("Numbers:")

    for number in numbers:
        print(number)

    print("Employee Details:")

    for key, value in info.items():
        print(key, value)


data(
    10, 20, 30,
    name="Vikash",
    age=25,
    salary=30000
)