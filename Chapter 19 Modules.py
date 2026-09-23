# ==========================================
# Modules & Packages — import Basic
# ==========================================

# Module kya hota hai?

# Python mein module ek .py file hoti hai jisme functions, variables ya classes ho sakte hain.

# Example:

# math

# Python ka ek built-in module hai.

# Agar hume math module use karna hai:

# import math

# Ab hum math ke functions use kar sakte hain:

# import math

# print(math.sqrt(25))

# Output:

# 5.0

# Yahan:

# import math → math module ko program mein laaya
# math.sqrt() → math module ka sqrt() function
# 25 → jis number ka square root chahiye
# Ek important pattern
# import module_name

# module_name.function_name()

# Example:

# import math

# print(math.factorial(5))

# Output:

# 120

# Bas abhi ke liye import ka basic concept itna hi. Pehle practice karte hain, phir next built-in modules par jayenge.

# Practice


# ==========================================
# Modules & Packages — import Basic [MATH]
# ==========================================

# Q1. Import the math module.
# Find and print the square root of 64.

# import math

# print(math.sqrt(64))


# Q2. Import the math module.
# Find and print the factorial of 5.

# import math

# print(math.factorial(5))

# Q3. Import the math module.
# Find and print the value of 2 raised to the power of 5.

# import math

# print(math.pow(2,5))


# Q4. Import the math module.
# Use ceil() with 6.3.
# Print the result.

# import math

# print(math.ceil(6.3))

# Q5. Import the math module.
# Use floor() with 6.8.
# Print the result.

# import math

# print(math.floor(6.8))

#--------------------------------------------------------------------------------------------------

# ==========================================
# random Module — randrange()[RANDOM]
# ==========================================

# Q1. Import the random module.
# Generate a random number from 1 to 9.
# Print the result.

# import random

# print(random.randrange(1, 10))


# Q2. Import the random module.
# Generate a random number from 10 to 19.
# Print the result.

# import random

# number = random.randrange(10, 20)

# print(number)

#-------------------------------------------------------------------------------------

# ==========================================
# random Module — random()
# ==========================================


# Next hai random.random().

# random.random()

# Ye 0 se 1 ke beech random decimal number deta hai.

# ==========================================
# random Module — random()
# ==========================================

# Q1. Import the random module.
# Generate a random decimal number.
# Print the result.

# import random

# number = random.random()
# print(number)

# Q2. Import the random module.
# Generate two random decimal numbers.
# Print both results.

# import random

# number1 = random.random()
# number2 = random.random()

# print(number1)
# print(number2)
#--------------------------------------------------------------------------------------

# ==========================================
# random Module — choice()
# ==========================================

# random.choice()

# Iska use list ya string mein se randomly ek item select karne ke liye hota hai.

# Example:

# import random

# names = ["Vikash", "Rahul", "Amit", "Ravi"]

# print(random.choice(names))

# Output har baar alag ho sakta hai:

# Amit

# ya

# Vikash

# Yahan:

# names → list
# random.choice(names) → list mein se 1 random item
# Practice — 2 questions

# ==========================================
# random Module — choice()
# ==========================================

# Q1. Create a list containing five student names.
# Select one random name from the list.
# Print the selected name.

# import random

# names = ["Vikash", "Rahul", "Amit", "Ravi"]

# print(random.choice(names))

# Q2. Create a list containing five cities.
# Select one random city from the list.
# Print the selected city.

# import random

# name = ["kolkata", "delhi", "mumbai", "chennai", "pune" ]
# print(random.choice(name))


#----------------------------------------------------------------------------------------------------

# ==========================================
# random Module — choices()
# ==========================================
# choice() se sirf 1 item select hota tha:

# random.choice(names)

# choices() se multiple random items select kar sakte hain.

# Example:

# import random

# names = ["Vikash", "Rahul", "Amit", "Ravi"]

# print(random.choices(names, k=2))

# Possible output:

# ['Amit', 'Vikash']

# Yahan:

# names → list
# k=2 → 2 items select karo
# Same item dobara bhi aa sakta hai

# Example:

# ['Ravi', 'Ravi']

# Ye bhi possible hai.

# choice() vs choices()
# choice()   → 1 item
# choices()  → multiple items
# Practice — 2 questions

# ==========================================
# random Module — choices()
# ==========================================

# Q1. Create a list containing five student names.
# Select three random names from the list.
# Print the selected names.

# import random 
# names = ["Vikash", "Rahul", "Amit", "Ravi"]
# print(random.choices(names, k=2))


# Q2. Create a list containing five cities.
# Select two random cities from the list.
# Print the selected cities.

# import random

# name = ["kolkata", "delhi", "mumbai", "chennai", "pune" ]
# print(random.choices(name, k=3))
#--------------------------------------------------------------------------------------------------------

# ==========================================
# random Module — shuffle()
# ==========================================

# shuffle()

# shuffle() ka kaam hai list ke items ko randomly rearrange karna.

# Example:

# import random

# names = ["Vikash", "Rahul", "Amit", "Ravi"]

# random.shuffle(names)

# print(names)

# Pehle:

# ["Vikash", "Rahul", "Amit", "Ravi"]

# Shuffle ke baad possible output:

# ["Amit", "Vikash", "Ravi", "Rahul"]

# Har baar order alag ho sakta hai.

# Important difference
# choice()   → list se 1 item
# choices()  → list se multiple items
# shuffle()  → poori list ka order change

# Aur ek important baat:

# random.shuffle(names)

# Ye original list ka order change karta hai. Isliye isko 
# print(random.shuffle(names)) mat karna — shuffle() khud list return nahi karta.

# Practice — 2 questions

# ==========================================
# random Module — shuffle()
# ==========================================

# Q1. Create a list containing five student names.
# Shuffle the list randomly.
# Print the list after shuffling.

# import random

# names = ["Vikash", "Rahul", "Amit", "Ravi", "Mohit"]

# random.shuffle(names)
# print(names)

# Q2. Create a list containing five cities.
# Shuffle the list randomly.
# Print the list after shuffling.

# import random

# name = ["kolkata", "delhi", "mumbai", "chennai", "pune" ]

# random.shuffle(name)
# print(name)

#----------------------------------------------------------------------------------------------

#==========================================
# datetime Module — Basic Practice
# ==========================================

# datetime module — Basic

# datetime Python ka built-in module hai jo date aur time ke saath kaam karne ke liye use hota hai.

# Sabse basic:

# import datetime

# now = datetime.datetime.now()

# print(now)

# Output kuch aisa ho sakta hai:

# 2026-09-19 12:30:45.123456

# Yahan:

# 2026-09-19 → Date
# 12:30:45 → Time

# Sirf date chahiye

# import datetime

# today = datetime.date.today()

# print(today)

# Output:

# 2026-09-19
# Sirf current time
# import datetime

# current_time = datetime.datetime.now().time()

# print(current_time)

# Bas abhi ke liye datetime.now(), date.today() aur .time() samajhna hai.


# ==========================================
# datetime Module — Basic Practice
# ==========================================

# Q1. Import the datetime module.
# Print the current date and time.

# import datetime

# now = datetime.datetime.now()
# print(now)

# Q2. Import the datetime module.
# Print today's date.
# Print the current time.

# import datetime

# today = datetime.date.today()
# curtime = datetime.datetime.now().time()
# print(today)
# print(curtime)


# Q3. Import the datetime module.
# Store the current date and time in a variable.
# Print the variable.

# import datetime

# now = datetime.datetime.now()

# print(now)
#---------------------------------------------------------------------------------------------

# ==========================================
# datetime Module — Date & Time Parts
# ==========================================


# datetime ke important parts — year, month, day, hour, minute, second.

# Example:

# import datetime

# now = datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# Yahan now ek datetime object hai, aur .year, .month etc. se uska particular part nikal sakte hain.

# ==========================================
# datetime Module — Date & Time Parts
# ==========================================

# Q1. Import the datetime module.
# Store the current date and time in a variable.
# Print the year, month, and day.

# import datetime

# now = datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)

# Q2. Import the datetime module.
# Store the current date and time in a variable.
# Print the hour, minute, and second.

# import datetime

# now = datetime.datetime.now()

# print(now.hour)
# print(now.minute)
# print(now.second)

# Q3. Import the datetime module.
# Store the current date and time in a variable.
# Print the year, month, day, hour, minute, and second.

# import datetime

# now = datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

#------------------------------------------------------------------------------------------------------

#==========================================
# datetime Module — Custom Date Practice
# ==========================================

# datetime — Custom Date

# Ab hum khud ki specific date banana seekhenge.

# Syntax:

# import datetime

# my_date = datetime.date(2025, 12, 25)

# print(my_date)

# Output:

# 2025-12-25

# Yahan:

# datetime.date(year, month, day)

# Matlab:

# 2025 → year
# 12 → month
# 25 → day

# Agar date + time dono khud banana ho:

# import datetime

# my_datetime = datetime.datetime(2025, 12, 25, 10, 30, 0)

# print(my_datetime)

# Yahan order hai:

# year, month, day, hour, minute, second

# Ab iske 3 practice questions karte hain.

# ok
# ==========================================
# datetime Module — Custom Date Practice
# ==========================================

# Q1. Import the datetime module.
# Create a date for 15 August 2025.
# Print the date.

# import datetime

# my_datetime = datetime.datetime(2025, 8, 15)
# print(my_datetime)

# Q2. Import the datetime module.
# Create a date for 1 January 2026.
# Print the date.

# import datetime

# my_datetime = datetime.date(2026, 1, 1)
# print(my_datetime)


# Q3. Import the datetime module.
# Create a date and time for 25 December 2025 at 10:30:00.
# Print the date and time.

# import datetime

# my_datetime = datetime.datetime(2025, 12, 25, 10,30,00)
# print(my_datetime)
#-----------------------------------------------------------------------------------------------------

# ==========================================
# datetime Module — Date Difference Practice
# ==========================================

# datetime — Date Difference

# Do dates ke beech difference nikalne ke liye hum dates ko subtract kar sakte hain.

# import datetime

# date1 = datetime.date(2025, 1, 1)
# date2 = datetime.date(2025, 1, 10)

# difference = date2 - date1

# print(difference)
# print(difference.days)

# Output:

# 9 days, 0:00:00
# 9

# Yahan:

# difference = date2 - date1

# ne dono dates ka difference nikala.

# Aur:

# difference.days

# se sirf number of days mila.


# ==========================================
# datetime Module — Date Difference Practice
# ==========================================

# Q1. Import the datetime module.
# Create two dates: 1 January 2026 and 15 January 2026.
# Find the difference between the two dates.
# Print the difference in days.

# import datetime

# date1 = datetime.date(2026, 1, 1)
# date2 = datetime.date(2026, 1, 15)

# difference =  date2 - date1

# print(difference)
# print(difference.days)

# Q2. Import the datetime module.
# Create two dates: 10 March 2026 and 25 March 2026.
# Find the difference between the two dates.
# Print the difference in days.

# import datetime

# date1 = datetime.date(2026, 3, 10)
# date2 = datetime.date(2026, 3, 25)

# difference =  date2 - date1

# print(difference)
# print(difference.days)

#-----------------------------------------------------------------------------------------

# ==========================================
# datetime Module — Date Formatting Practice
# ==========================================

# datetime — Date Formatting with strftime()

# strftime() ka use date/time ko apne desired format mein convert karke display karne ke liye hota hai.

# Example:

# import datetime

# now = datetime.datetime.now()

# formatted_date = now.strftime("%d-%m-%Y")

# print(formatted_date)

# Agar date 19 September 2026 hai, output hoga:

# 19-09-2026

# Kuch important format codes:

# %d  → Day
# %m  → Month
# %Y  → 4-digit Year
# %y  → 2-digit Year
# %H  → Hour
# %M  → Minute
# %S  → Second

# Example:

# print(now.strftime("%d/%m/%Y"))
# print(now.strftime("%d-%m-%Y %H:%M:%S"))

# Matlab hum decide kar sakte hain ki date/time kis format mein dikhana hai.

# ==========================================
# datetime Module — Date Formatting Practice
# ==========================================

# Q1. Import the datetime module.
# Create a date for 25 December 2025.
# Print the date in the format: 25-12-2025.

# import datetime

# my_datetime = datetime.date(2025, 12, 25)
# formatted = my_datetime.strftime("%d-%m-%Y")

# print(formatted)

# Q2. Import the datetime module.
# Create a date and time for 1 January 2026 at 09:30:00.
# Print the date and time in the format: 01/01/2026 09:30:00.

# import datetime

# my_datetime = datetime.datetime(2026, 1, 1, 9, 30, 00)
# formatted = my_datetime.strftime("%d-%m-%y %H:%M:%S")

# print(formatted)
#=-------------------------------------------------------------------------------------------

# ==========================================
# os Module — getcwd() Practice
# ==========================================

# os module — Basic

# os Python ka built-in module hai.

# Iska use Python se computer ke operating system aur folders/files ke saath kaam karne ke liye hota hai.

# Sabse pehle:

# import os

# Yahan os module ko program mein import kiya.

# 1. os.getcwd()

# getcwd() ka full meaning hai Get Current Working Directory.

# Ye batata hai ki Python abhi kis folder mein kaam kar raha hai.

# import os

# print(os.getcwd())

# Example output:

# C:\Users\Vikash\Documents\Python

# Bas abhi sirf import os aur os.getcwd() samjho.

# ==========================================
# os Module — getcwd() Practice
# ==========================================

# Q1. Import the os module.
# Print the current working directory.

# import os

# print(os.getcwd())


# Q2. Import the os module.
# Store the current working directory in a variable.
# Print the variable.

# import os

# result = os.getcwd()
# print(result)
#--------------------------------------------------------------------------------
#==========================================
# os Module — listdir() Practice
# ==========================================

# os.listdir() — Basic

# os.listdir() current working folder ke andar ki files aur folders ke naam list mein deta hai.

# import os

# items = os.listdir()

# print(items)

# Yahan:

# os.listdir() → files/folders ki list banata hai
# items → us list ko store karta hai
# print(items) → list ko display karta hai

# Ab iski 2 practice questions karo:

# ==========================================
# os Module — listdir() Practice
# ==========================================

# Q1. Import the os module.
# Print the names of all files and folders
# in the current working directory.

# import os

# print(os.listdir())

# Q2. Import the os module.
# Store the list of files and folders in a variable.
# Print the variable.

# import os

# items = os.listdir()
# print(items)
#-----------------------------------------------------------------------------------------------------

# ==========================================
# os Module — listdir() Specific Folder Practice
# ==========================================

# os.listdir("folder_path")

# Abhi tak humne:

# os.listdir()

# use kiya tha, jo current folder ki files/folders dikhata hai.

# Agar kisi specific folder ke andar ki files/folders dekhni ho, to folder ka path de sakte hain:

# import os

# print(os.listdir("folder_name"))

# Example:

# import os

# print(os.listdir("data"))

# Isse data folder ke andar jo files aur folders hain, unki list milegi.

# Important: folder_name ki jagah tumhare computer mein actually existing 
# folder ka naam/path hona chahiye.

# Practice
# ==========================================
# os Module — listdir() Specific Folder Practice
# ==========================================

# Q1. Import the os module.
# Print the files and folders inside a specific folder.

# import os

# print(os.listdir("students.csv"))

# Q2. Import the os module.
# Store the files and folders of a specific folder in a variable.
# Print the variable.

# import os

# items = os.listdir()
# print(items)
#-----------------------------------------------------------------------------------------------

# ==========================================
# os Module — path.exists() Practice
# ==========================================

# os.path.exists()

# Ye check karta hai ki koi file ya folder exist karta hai ya nahi.

# import os

# print(os.path.exists("data.txt"))

# Agar data.txt exist karta hai → True

# Agar nahi karta → False

# Ab isko practice karenge.

# OK

# Chalo 👍 ab os.path.exists() practice karte hain.

# ==========================================
# os Module — path.exists() Practice
# ==========================================

# Q1. Import the os module.
# Check whether "data.txt" exists in the current working directory.
# Print the result.

# import os

# print(os.path.exists("data.txt"))

# Q2. Import the os module.
# Store the result of checking whether "employees.csv" exists
# in a variable.
# Print the variable.

# import os 

# items = (os.path.exists("employees.csv"))
# print(items)

#------------------------------------------------------------------------------------------------

# ==========================================
# os Module — isfile() Practice
# ==========================================

# os.path.isfile() start karte hain.

# os.path.isfile()

# Iska kaam hai check karna ki diya gaya path file hai ya nahi.

# Example:

# import os

# print(os.path.isfile("data.txt"))

# Tumhare folder mein data.txt hai, isliye output:

# True

# Agar hum aisa likhen:

# print(os.path.isfile("hello.txt"))

# aur hello.txt exist nahi karti, to:

# False
# Yaad rakho
# os.path.exists()  → path exist karta hai?
# os.path.isfile()  → path ek file hai?

# Ab 2 practice questions:

# ==========================================
# os Module — isfile() Practice
# ==========================================

# Q1. Import the os module.
# Check whether "data.txt" is a file.
# Print the result.

# import os

# print(os.path.isfile("data.txt"))


# Q2. Import the os module.
# Check whether "employees.csv" is a file.
# Print the result.

# import os 

# result = (os.path.isfile("labour.csv"))
# print(result)

#--------------------------------------------------------------------------------------------

# ==========================================
# os Module — isdir() Practice
# ==========================================

# os.path.isdir() start karte hain.

# os.path.isdir()

# isdir() ka full meaning is directory? hota hai.

# Ye check karta hai ki diya gaya path folder/directory hai ya nahi.

# Example:

# import os

# print(os.path.isdir("my_folder"))

# Agar my_folder ek folder hai:

# True

# Agar folder nahi hai ya exist nahi karta:

# False
# Difference yaad rakho:
# os.path.exists()  → path exist karta hai?
# os.path.isfile()  → path file hai?
# os.path.isdir()   → path folder hai?

# Ab 2 practice:

# ==========================================
# os Module — isdir() Practice
# ==========================================

# Q1. Import the os module.
# Check whether "PYTHON 37" is a directory.
# Print the result.

# import os

# print(os.path.isdir("PYTHON 37"))


# Q2. Import the os module.
# Check whether "data.txt" is a directory.
# Print the result.

# import os 

# result = (os.path.isdir("data.txt"))
# print(result)
#-------------------------------------------------------------------------------------------

# ==========================================
# os Module — mkdir() Practice
# ==========================================

# os.mkdir()

# os.mkdir() ka use Python se naya folder create karne ke liye hota hai.

# Syntax:

# import os

# os.mkdir("folder_name")

# Example:

# import os

# os.mkdir("Practice")

# Isse current working directory ke andar Practice naam ka naya folder ban jayega.

# Agar folder pehle se bana hua hai aur dobara same naam se mkdir() karoge, to error aayega.

# Practice
# ==========================================
# os Module — mkdir() Practice
# ==========================================

# Q1. Import the os module.
# Create a new folder named "Chapter 20 Package".

# import os

# os.mkdir("Chapter 20 Package")

# Q2. Import the os module.
# Create a new folder named "cita file".

# import os

# os.mkdir("cita file")
#-----------------------------------------------------------------------------------

# ==========================================
# os Module — rmdir() Practice
# ==========================================

# os.rmdir()

# os.rmdir() ka use empty folder ko delete/remove karne ke liye hota hai.

# Syntax:

# import os

# os.rmdir("folder_name")

# Example:

# import os

# os.rmdir("DataFiles")

# Isse DataFiles folder delete ho jayega, agar folder empty hai.

# ⚠️ Agar folder ke andar koi file/folder hai, to os.rmdir() error dega.

# Practice
# ==========================================
# os Module — rmdir() Practice
# ==========================================

# Q1. Import the os module.
# Remove the "Chapter 20 Package" folder.

# import os

# os.rmdir("Chapter 20 Package")

# Q2. Import the os module.
# Create a folder named "TempFolder".
# Then remove the "cita file" folder.

# import os

# os.rmdir("cita file")

#----------------------------------------------------------------------------------------------

# ==========================================
# os Module — path.join() Practice
# ==========================================

# os.path.join()

# Iska use folder aur file ke path ko properly combine karne ke liye hota hai.

# Example:

# import os

# path = os.path.join("DataFiles", "data.txt")

# print(path)

# Windows par output kuch aisa hoga:

# DataFiles\data.txt

# Yahan:

# "DataFiles" → folder
# "data.txt"  → file

# os.path.join() dono ko correct path mein combine kar deta hai.

# Ek aur example
# import os

# path = os.path.join("C:\\PYTHON 37", "data.txt")

# print(path)

# Iska matlab hai:

# C:\PYTHON 37 folder ke andar data.txt file ka path.

# Yaad rakho
# os.path.join("folder", "file")
#           ↓
# folder + file ka proper path

# Ab 2 practice questions:

# ==========================================
# os Module — path.join() Practice
# ==========================================

# Q1. Import the os module.
# Join the folder name "DataFiles" and the file name "data.txt".
# Print the resulting path.

# import os

# print(os.path.join("DataFiles", "data.txt" ))

# Q2. Import the os module.
# Join the folder name "DataFiles" and the file name "employees.csv".
# Store the resulting path in a variable.
# Print the variable.

# import os

# path = os.path.join("DataFiles", "employees.csv" )

# print(path)
#----------------------------------------------------------------------------------------------

# ==========================================
# os Module — abspath() Practice
# ==========================================

# os.path.abspath()

# abspath() ka use kisi path ka complete/absolute path nikalne ke liye hota hai.

# Example:

# import os

# path = os.path.abspath("data.txt")

# print(path)

# Tumhare system mein output kuch aisa hoga:

# C:\PYTHON 37\data.txt

# Yahan:

# data.txt
#    ↓
# relative path

# C:\PYTHON 37\data.txt
#    ↓
# absolute path
# Simple difference
# "data.txt"                 → short/relative path
# "C:\PYTHON 37\data.txt"   → complete/absolute path

# abspath() file create nahi karta. Sirf uska complete path banakar deta hai.

# Practice
# ==========================================
# os Module — abspath() Practice
# ==========================================

# Q1. Import the os module.
# Get the absolute path of "data.txt".
# Print the result.

# import os

# print(os.path.abspath("data.txt"))

# Q2. Import the os module.
# Get the absolute path of "employees.csv".
# Store the result in a variable.
# Print the variable.

# import os

# path = os.path.abspath("employees.csv")
# print(path)
#---------------------------------------------------------------------------------------------

# ==========================================
# os Module — rename() Practice
# ==========================================
# OS.RENAME()

# os.rename() ka use file ya folder ka naam change karne ke liye hota hai.


# Syntax:

# import os

# os.rename("old_name", "new_name")

# Example:

# import os

# os.rename("data.txt", "new_data.txt")

# Isse:

# data.txt
#    ↓
# new_data.txt

# Naam change ho jayega.

# ⚠️ Ye file ka content delete nahi karta, sirf naam change karta hai.

# PRACTICE
# ==========================================
# OS MODULE — RENAME() PRACTICE
# ==========================================

# Q1. IMPORT THE OS MODULE.
# RENAME "DATA.TXT" TO "MYDATA.TXT".

# import os

# print(os.rename("DATA.TXT", "MYDATA.TXT"))

# Q2. IMPORT THE OS MODULE.
# RENAME "MYDATA.TXT" BACK TO "DATA.TXT".

# import os

# result = os.rename("MYDATA.TXT", "data.txt")

# print(result)
#------------------------------------------------------------------------------------

# ==========================================
# os Module — remove() Practice
# ==========================================

# os.remove()

# os.remove() ka use file delete karne ke liye hota hai.

# Example:

# import os

# os.remove("test.txt")

# Agar test.txt exist karti hai, to file delete ho jayegi.

# ⚠️ Important: os.remove() sirf file delete karta hai, folder nahi.

# Folder ke liye humne pehle:

# os.rmdir("folder_name")

# use kiya tha.

# Safe practice

# Pehle ek temporary file bana sakte ho:

# import os

# with open("temp.txt", "w") as file:
#     file.write("Testing")

# Phir check:

# print(os.path.isfile("temp.txt"))

# Aur finally delete:

# os.remove("temp.txt")

# Practice ke liye actual data.txt, employees.csv etc. ko delete mat karna.

# Practice
# ==========================================
# os Module — remove() Practice
# ==========================================

# Q1. Create a temporary file named "temp.txt".
# Write some text into the file.
# Delete the "temp.txt" file using os.remove().

# import os

# os.remove("temp.txt")


# Q2. Create a file named "delete_me.txt".
# Write some text into the file.
# Delete the file using os.remove().

# import os

# with open("delete_me.txt", "w") as file:
#     file.write("delete hoga tu")

# print(os.path.isfile("delete_me.txt"))

# os.remove("delete_me.txt")
#-------------------------------------------------------------------------------------------

# ==========================================
# os Module — getsize() Practice
# ==========================================


# os.path.getsize()

# Iska use file ka size check karne ke liye hota hai.

# import os

# size = os.path.getsize("data.txt")

# print(size)

# Output example:

# 25

# Yahan 25 ka matlab 25 bytes hai.

# Simple:

# os.path.getsize("file")
#         ↓
# file ka size in bytes

# ⚠️ Ye file ke andar kitne characters hain ye directly nahi batata; ye file ka size bytes mein batata hai.

# Practice
# ==========================================
# os Module — getsize() Practice
# ==========================================

# Q1. Import the os module.
# Get the size of "data.txt".
# Print the result.

# import os

# print(os.path.getsize("data.txt"))

# Q2. Import the os module.
# Get the size of "employees.csv".
# Store the result in a variable.
# Print the variable.

# import os

# size = os.path.getsize("employees.csv")

# print(size)
#----------------------------------------------------------------------------

# ==========================================
# Creating Your Own Module in Python
# ==========================================

# Creating Your Own Module
# ├── .py file banana       ✅
# ├── Function banana       ✅
# └── Doosri file mein import karna ✅

# Apni .py file banana

# Abhi tumhare paas:

# Chapter 19 Modules.py

# hai.

# Isi folder C:\PYTHON 37 mein ek nayi Python file banao:

# my_module.py

# Is file ke andar hum apna function banayenge:

# def greet():
#     print("Hello Vikash")

# Yahan my_module.py hamara own module hai.

# Phir Chapter 19 Modules.py se isko import karenge:

# import my_module

# my_module.greet()

# Output:

# Hello Vikash
# Flow samjho
# my_module.py
#      ↓
# function banaya
#      ↓
# import my_module
#      ↓
# my_module.greet()
#      ↓
# Hello Vikash

# ==========================================
# os Module — getsize() Practice
# ==========================================

# import my_module

# my_module.greet()

