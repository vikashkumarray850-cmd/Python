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


# (Lekin TypeError nahi aayega.

# Python mein:

# 10 * "5"

# ka matlab hai "5" ko 10 times repeat karna.

# Output:

# 5555555555

# Isliye except TypeError execute nahi hoga.

# 👉 Tumne actually ek useful point discover kiya: int × string valid hai, jabki int + string invalid hai.

# So tumhara code syntactically correct hai, bas TypeError test nahi ho raha.)
#--------------------------------------------------------------------------------------------------------------------

# ================================================
# Python Exception Handling — Multiple Exceptions
# =================================================

# Yahan ek hi program mein alag-alag errors ko alag tarike se handle karna seekhenge.

# Example:

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(result)

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# Isme kya ho raha hai?

# Agar user 10 dale:

# 100 / 10 = 10.0

# Agar user hello dale:

# ValueError
# ↓
# except ValueError

# Agar user 0 dale:

# ZeroDivisionError
# ↓
# except ZeroDivisionError

# Simple rule:

# ValueError        → invalid value
# ZeroDivisionError → 0 se division

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1. Take a number from the user.
# Convert it into an integer.
# Divide 100 by that number.
# Handle ValueError and ZeroDivisionError separately.

# try:
#     number = int(input("Enter Your Number:"))
#     result = 100 / number
#     print(result)

# except ValueError:
#     print("invalid value")

# except ZeroDivisionError:
#     print("Can't divide by zero")



# Q2. Take two numbers from the user.
# Divide the first number by the second number.
# Handle invalid input using ValueError.
# Handle division by zero using ZeroDivisionError.

# try:
#     a = int(input("Enter First Number:"))
#     b = int(input("Enter Second Number:"))
#     result = a / b
#     print(result)

# except ValueError:
#     print("Value Invalid")

# except ZeroDivisionError:
#     print("Can't Divide By Zero ")

# Q3. Take a number from the user.
# Calculate 50 divided by that number.
# Handle ValueError and ZeroDivisionError separately.
# Print a different message for each error.


# try:
#     number = int(input("enter a number:"))
#     print(50 / number)

# except ValueError:
#     print("Value Not Found")

# except ZeroDivisionError:
#     print("Can't Divide By Zero")
#-----------------------------------------------------------------------------------------------------

# ==========================================
# Python Exception Handling — try-except-else
# ==========================================

# else kya karta hai?

# else tabhi run hota hai jab try mein koi error nahi aata.

# try:
#     number = int(input("Enter a number: "))
#     print(100 / number)

# except ValueError:
#     print("Please enter a number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Calculation successful")
# Flow samjho

# Agar input 10:

# try → successfully run
#      ↓
# else → run

# Output:

# 10.0
# Calculation successful

# Agar input 0:

# try → error
#      ↓
# except ZeroDivisionError → run
#      ↓
# else → run nahi hoga
# Simple rule
# try     → code try karo
# except  → error aaye toh
# else    → error NA aaye toh

# Important: else ka matlab "otherwise" nahi hai jaise if-else mein. Yahan iska specific meaning hai: try successful hua toh else chalega.

# TRY
#  ↓
# Kya error aaya?
#  ↓
#  ├── Haan → EXCEPT
#  │
#  └── Nahi → ELSE

# ==========================================
# Python Exception Handling — try-except-else
# ==========================================


# Q1. Take a number from the user.
# Convert it into an integer.
# Use try-except to handle ValueError.
# Use else to print the number if the conversion is successful.

# try:
#     number = int(input("enter a number:"))
#     print(number)

# except ValueError:
#     print("invalid value")

# else:
#     print("Conversion successful")

# Q2. Take two numbers from the user.
# Divide the first number by the second number.
# Handle ValueError and ZeroDivisionError separately.
# Use else to print "Division successful" when there is no error.

# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second Number:"))
#     print(a / b )

# except ValueError:
#     print("Invalid Value")

# except ZeroDivisionError:
#     print("Can't Divide By Zero")

# else:
#     print("Division Successful")

# Q3. Take a number from the user.
# Calculate 100 divided by that number.
# Handle ValueError and ZeroDivisionError separately.
# Use else to print the result only when no error occurs.

# try:
#     number = int(input("Enter a number:"))
#     result =  100 / number

# except ValueError:
#     print("Invalid Value")

# except ZeroDivisionError:
#     print("Can't Divide By Zero")

# else:
#     print(result)
#-------------------------------------------------------------------------------------------

# ==========================================
# Python Exception Handling — finally
# ==========================================

# finally kya hota hai?

# finally chahe error aaye ya na aaye, normally hamesha run hota hai.

# try:
#     number = int(input("Enter a number:"))
#     print(100 / number)

# except ValueError:
#     print("Invalid value")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program finished")
# 2 situations dekho:

# Input 10:

# try ✅
# ↓
# 10.0
# ↓
# finally ✅
# Program finished

# Input 0:

# try ❌
# ↓
# except ZeroDivisionError ✅
# ↓
# finally ✅
# Program finished

# Matlab:

# try     → code run karo
# except  → error aaye toh handle karo
# else    → error na aaye toh run karo
# finally → dono situation mein run karo

# Important: finally ka use aksar cleanup ke liye hota hai, jaise file/database connection ko close karna.

# ==========================================
# Python Exception Handling — finally
# ==========================================


# Q1. Take a number from the user.
# Divide 100 by that number.
# Handle ZeroDivisionError.
# Use finally to print "Program finished".

# try:
#     number = int(input("Enter a number:"))
#     result = 100 / number
#     print(result)

# except ZeroDivisionError:
#     print("Can't Divide by Zero")

# finally:
#     print("Program finished")


# Q2. Ask the user to enter a number.
# Try to convert it into an integer.
# If the user enters invalid text, handle ValueError.
# If the number is valid, print it.
# Always print "Input process completed" using finally.

# try :
#     number = int(input("Enter A number:"))
#     print(number)

# except ValueError:
#     print("Invalid values")

# finally:
#     print("Input process completed")


# Q3. Take a number from the user.
# Divide 50 by that number.
# Handle ValueError and ZeroDivisionError separately.
# Use finally to print "Program ended" in both cases.

# try:
#     number = int(input("Enter a Number:"))
#     result = 50 / number
#     print(result)

# except ValueError:
#     print("Invalid Values")

# except ZeroDivisionError:
#     print("Can't Divide by zero")

# finally:
#     print("Program ended")

#-----------------------------------------------------------------------------------------------------

# ==========================================
# Exception Handling — raise Basic Practice
# ==========================================

# raise kya karta hai?

# Normally Python khud error deta hai.
# raise se hum khud apni condition par exception generate kar sakte hain.

# Simple example:

# age = 15

# if age < 18:
#     raise ValueError("Age must be 18 or above")

# print("You can vote")

# Yahan:

# age < 18 → condition true
# raise ValueError(...) → humne khud ValueError raise kiya
# "Age must be 18 or above" → error message

# Agar age = 20 hota, raise nahi chalta aur print() execute hota.

# Important difference
# int("hello")

# → Python automatically ValueError deta hai.

# raise ValueError("Invalid age")

# → Hum khud ValueError create kar rahe hain.

# ==========================================
# Exception Handling — raise Basic Practice
# ==========================================


# Q1. Create a variable named age and store an age in it.
# If the age is less than 18, raise a ValueError
# with the message "Age must be 18 or above".
# Otherwise, print "Eligible".

# age = 15

# if age < 18:
#     raise ValueError("Age must be 18 or above")

# print("Eligible")

# Q2. Create a variable named number and store a number in it.
# If the number is negative, raise a ValueError
# with the message "Number cannot be negative".
# Otherwise, print the number.

# number = -1

# if number < 0:
#     raise ValueError("Number cannot be negative")

# print(number)

# Q3. Create a variable named password and store a password in it.
# If the password length is less than 6 characters,
# raise a ValueError with the message "Password is too short".
# Otherwise, print "Valid password".

# password = "abc"

# if len(password) < 6:
#     raise ValueError("Password is too short")

# print("Valid password")

# FLOW:
# password = "abc" → length 3
# 3 < 6 → True
# raise ValueError execute hoga
# "Valid password" print nahi hoga

# Agar password "python123" hota, toh raise nahi chalta aur "Valid password" print hota.
#-------------------------------------------------------------------------------------------------------------

# ==========================================
# Exception Handling — raise + try-except
# ==========================================

# Ab raise ko try-except ke saath use karna seekhenge.

# Example:

# try:
#     age = 15

#     if age < 18:
#         raise ValueError("Age must be 18 or above")

# except ValueError as e:
#     print(e)

# Yahan:

# raise → hum khud error create kar rahe hain
# except → us error ko handle kar raha hai
# as e → error ka message e me store hota hai\

# ==========================================
# Exception Handling — raise + try-except
# ==========================================


# Q1. Create a variable named age and store an age in it.
# Inside try, check whether age is less than 18.
# If it is less than 18, raise a ValueError.
# Handle the ValueError using except.
# Print the error message.

# try:
#     age = 20

#     if age < 18:
#         raise ValueError("age must be above 18")

# except ValueError as e:
#     print(e)


# {Agar tum chahte ho ki 18+ hone par message aaye, toh try ke andar:

# print("Eligible")

# add kar sakte ho.}


# Q2. Create a variable named marks and store marks in it.
# Inside try, check whether marks are outside the range 0 to 100.
# If they are outside the range, raise a ValueError.
# Handle the ValueError using except.
# Print the error message.

# try:   
#     marks = 105

#     if marks < 0 or marks > 100:
#         raise ValueError("Marks must be between 0 and 100")
    
# except ValueError as e:
#     print(e)

# else :
#     print("Valid marks")

    
# Q3. Create a variable named balance and store an amount in it.
# Inside try, check whether balance is negative.
# If it is negative, raise a ValueError.
# Handle the ValueError using except.
# Otherwise, print the balance.

# try :

#     balance = -2
#     if balance < 0 :
#         raise ValueError("balance must be positive")
    
# except ValueError as e:
#     print(e)

# else:
#     print(balance)

