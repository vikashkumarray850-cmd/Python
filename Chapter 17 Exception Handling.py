# ==========================================
# Python Exception Handling — Basic try-except
# ==========================================

# Exception Handling — Basic

# Sabse pehle samjho exception hota kya hai.

# Program normally chale:

# a = 10
# b = 2

# print(a / b)

# Output:

# 5.0

# Lekin agar:

# a = 10
# b = 0

# print(a / b)

# to Python error dega:

# ZeroDivisionError

# Aise runtime errors ko handle karne ke liye Exception Handling use karte hain.

# try aur except

# Basic structure:

# try:
#     # risky code
# except:
#     # error hone par ye code chalega

# Example:

# try:
#     a = 10
#     b = 0
#     print(a / b)

# except:
#     print("Something went wrong")

# Output:

# Something went wrong

# Yahan kya hua?

# try
#  ↓
# Python ne code run kiya
#  ↓
# 10 / 0
#  ↓
# Error mila
#  ↓
# except
#  ↓
# "Something went wrong"

# Program crash hone ke bajay except ke andar chala gaya.

# Sabse important baat

# try mein hum wo code rakhte hain jisme error aa sakta hai.

# except mein hum error aane par kya karna hai wo likhte hain.

# Ek aur example
# try:
#     number = int("hello")
#     print(number)

# except:
#     print("Invalid number")

# "hello" ko integer mein convert nahi kar sakte, isliye except chalega.

# Output:

# Invalid number
#=======================================
# QUESTION STARTED NOW
#=======================================


# Q1. Write a program that divides 10 by 0.
# Use try-except to handle the error.
# If an error occurs, print a suitable message.

# try:
#     a = 10
#     b = 0
#     print(a / b)
# except:
#     print("Cannot divide by zero")

# Q2. Write a program that converts the string "hello"
# into an integer using int().
# Use try-except to handle the error.
# If an error occurs, print a suitable message.

# try:
#     number = int("Hello")
#     print(number)
# except:
#     print("it's not possible")

# Q3. Write a program that takes a number from the user
# and prints the result of 100 divided by that number.
# Use try-except to handle any error.


# try:
#     number = int(input("Enter Your Number:"))
#     result = 100 / number
#     print(result)
# except:
#     print("Cannot divide by zero")

# Q4. Take two numbers from the user.
# Divide the first number by the second number.
# Use try-except to handle any error.
# Print the result if there is no error.

# try:
#     a = int(input("Enter first Number:"))
#     b = int(input("Enter second Number:"))

#     result = a/ b
#     print(result)
# except:
#     print("An error occurred")


# Q5. Take a number from the user.
# Convert it into an integer using int().
# Print the number multiplied by 10.
# Use try-except to handle any error.

# try:
#     number = int(input("enter a number:"))
#     print(number * 10)

# except:
#     print("Invild Number")

#---------------------------------------------------------------------------------------
# ==========================================
# Python Exception Handling — ZeroDivisionError
# ==========================================

# Basic except: mein hum kisi bhi error ko catch kar rahe the:

# try:
#     print(10 / 0)

# except:
#     print("Something went wrong")

# Lekin problem ye hai ki humein exactly pata nahi chal raha kaunsa error hua.

# Isliye hum specific exception ka naam likhte hain.

# 1. ZeroDivisionError

# Jab kisi number ko 0 se divide karte hain:

# try:
#     print(10 / 0)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# Yahan Python ko pata hai:

# 10 / 0
#    ↓
# ZeroDivisionError
#    ↓
# except ZeroDivisionError

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1. Divide 20 by 0.
# Use try-except with ZeroDivisionError.
# Print a suitable message when the error occurs.

# try:
#     a = 20
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print("invalid")

# Q2. Take two numbers from the user.
# Divide the first number by the second number.
# Use ZeroDivisionError to handle division by zero.
# Print the result if there is no error.

# try:
#     a = int(input("Enter First Number:"))
#     b = int(input("Enter Second Number:"))
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("not valid")


# Q3. Take a number from the user.
# Calculate 100 divided by that number.
# Use ZeroDivisionError to handle division by zero.
# Print "Cannot divide by zero" if the user enters 0.

# try:
#     number = int(input("Enter a Number:"))
#     print(100 / number)

# except ZeroDivisionError:
#     print("Can't difine")
#--------------------------------------------------------------------------------

# ==========================================
# Python Exception Handling — ValueError
# ==========================================

# Without try-except
# number = int("hello")
# print(number)

# print("Program continues")

# Output:

# ValueError

# Aur "Program continues" print nahi hoga.

# With ValueError
# try:
#     number = int("hello")
#     print(number)

# except ValueError:
#     print("Please enter a valid number")

# print("Program continues")

# Output:

# Please enter a valid number
# Program continues
# Toh use kyu karte hain?

# Real program mein user galat input de sakta hai.

# age = int(input("Enter your age: "))

# Agar user 25 dale → sab theek.

# Agar user abc dale → program crash ho sakta hai.

# ValueError use karke hum bolte hain:

# "Galat value aayi toh program band mat karo, us situation ko handle karo."

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1. Convert the string "hello" into an integer.
# Use try-except with ValueError.
# Print "Invalid value" when the error occurs.

# try:
#     number = int("Hello")
#     print("Hello")
# except ValueError:
#     print("Invalid value")

# Q2. Take a number from the user using input().
# Convert the input into an integer.
# Use ValueError to handle invalid input.
# Print the number if the conversion is successful.

# try:
#    numbers = int(input("Enter Your number:"))
#     print(number)
# except ValueError:
#     print("invalid")

# Q3. Take the user's age as input.
# Convert it into an integer.
# Print the age.
# Use ValueError to handle a non-numeric value.
# Print "Please enter a valid age" if the input is invalid.

# try:
#     age = int(input("Enter Your Age:"))
#     print(age)

# except ValueError:
#     print("invalid")
#----------------------------------------------------------------------------------------

# ==========================================
# Python Exception Handling — TypeError
# ==========================================

# TypeError kya hota hai?

# Jab hum do incompatible data types ke saath koi operation karne ki koshish karte hain, tab TypeError aata hai.

# Example:

# try:
#     result = 10 + "20"
#     print(result)

# except TypeError:
#     print("Invalid data types")

# Yahan:

# 10 → int
# "20" → str

# Python normally int + str nahi kar sakta.

# Isliye:

# 10 + "20"
#    ↓
# TypeError
#    ↓
# except TypeError
# Ek aur example
# try:
#     name = "Vikash"
#     result = name + 10
#     print(result)

# except TypeError:
#     print("Cannot add string and integer")

# Yahan bhi string + integer hai, isliye TypeError.

# Important difference

# ValueError:

# int("hello")

# Type conversion kar rahe hain, value problem hai.

# TypeError:

# "hello" + 10

# Yahan types hi compatible nahi hain.

# Simple yaad rakho:

# ValueError → value galat
# TypeError → type galat/incompatible

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1. Add the integer 10 and the string "20".
# Use try-except with TypeError.
# Print a suitable message when the error occurs.

# try:
#     result = 10 + "20"
#     print(result)

# except TypeError:
#     print("invaild info")


# Q2. Create a string variable containing your name.
# Try to add the number 10 to the string.
# Use TypeError to handle the error.

# try:
#     name = "vikash"
#     result = name + 10
#     print(result)

# except TypeError:
#     print("invalid input")


# Q3. Create a number and a string.
# Try to multiply them using the + operator.
# Use TypeError to handle the error.

# try:
#     number = 10
#     text = "5"

#     result = number * text
#     print(result)

# except TypeError:
#     print("value ERROR") 
# 
# 
# (Lekin TypeError nahi aayega.

# Python mein:

# 10 * "5"

# ka matlab hai "5" ko 10 times repeat karna.

# Output:

# 5555555555

# Isliye except TypeError execute nahi hoga.

# 👉 Tumne actually ek useful point discover kiya: int × string valid hai, jabki int + string invalid hai.

# So tumhara code syntactically correct hai, bas TypeError test nahi ho raha.)



