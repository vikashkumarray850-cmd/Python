# 📝 Practice — Lists Basics

# Q1. Create a list containing "Apple", "Mango", and "Banana" and print the list.
# fruits = ["Apple", "Mango", "Banana"]
# print(fruits)

# Q2. Create a list of 5 numbers and print the first number.
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])

# Q3. Create a list of 5 fruits and print the last fruit using negative indexing.
# fruits = ["mango", "orange", "banana", "coconut", "papaya"]
# print(fruits[-1])

# Q4. Create a list of 5 numbers and print the third number.
# number= [10, 20, 30 ,40 , 50]
# print(number[2])

# Q5. Create a list of 5 fruits and print the first 3 fruits using slicing.
# fruits = ["mango", "orange", "banana", "coconut", "papaya"]
# print(fruits[0:3])

# Q6. Create a list of 5 numbers and print the last 2 numbers using slicing.
# number= [10, 20, 30 ,40 , 50]
# print(number[-2:])

# Q7. Create a list ["Python", "SQL", "Excel"] and change "SQL" to "Power BI".
# text = ["Python", "SQL", "Excel"]
# text[1] = "Power BI"
# print(text)

# Q8. Create a list of 4 fruits and change the second fruit to "Orange".
# fruits = ["mango", "lichi", "banana", "coconut",]
# fruits[1] = "orange"
# print(fruits)

# Q9. Create a list containing your name, age, and city, then print the name using indexing.
# data = ["vikash", "25", "kolkata"]
# print(data[0])

# Q10. Create a list of 5 numbers and change the third number to 100.
# numbers = [200, 300, 300, 400, 500]
# numbers[2] = 100
# print(numbers)
# ----------------------------------------------------------------------------------------------------------

# Q1. Create a list ["Apple", "Mango"] and add "Banana" at the end using append().
# fruits = ["Apple", "Mango"]
# fruits.append("Banana")
# print(fruits)

# Q2. Create a list ["Apple", "Banana"] and add "Mango" at index 1 using insert().
# fruits = ["Apple", "Mango"]
# fruits.insert(1, "Apple")
# print(fruits)

# Q3. Create a list ["Apple", "Mango"] and add ["Banana", "Orange"] using extend().
# fruits = ["Apple", "Mango"]
# fruits.extend(["Banana", "Orange"])
# print(fruits)

# Q4. Create a list ["Apple", "Mango", "Banana"] and remove "Mango" using remove().
# fruits = ["Apple", "Mango", "Banana"]
# fruits.remove("Mango")
# print(fruits)

# Q5. Create a list ["Apple", "Mango", "Banana"] and remove the second element using pop().
# fruits = ["Apple", "Mango", "Banana"]
# fruits.pop(1)
# print(fruits)

# Q6. Create a list ["Apple", "Mango", "Banana"] and remove the last element using pop().
# fruits = ["Apple", "Mango", "Banana"]
# fruits.pop(2)
# print(fruits)

# Q7. Create a list of 4 fruits and remove all elements using clear().
# fruits = ["mango", "orange", "banana", "coconut", "papaya"]
# fruits.clear()
# print(fruits)

# Q8. Create a list of 3 numbers and add another number at the end using append().
# number = [10, 20, 30]
# number. append(40)
# print(number)

# Q9. Create a list ["Python", "SQL"] and add ["Excel", "Power BI"] using extend().
# text = ["Python", "SQL"]
# text.extend(["Excel", "Power BI"])
# print(text)

# Q10. Create a list ["Python", "SQL", "Excel"] and remove "SQL" using remove().
# text = ["Python", "SQL", "Excel"]
# text.remove("SQL")
# print(text)

# Q1. Create a list [40, 10, 30, 20] and arrange it in ascending order using sort().
# number = [40, 10, 30, 20]
# number.sort()
# print(number)

# Q2. Create a list [5, 2, 8, 1, 9] and sort it using sort().
# number = [5, 2, 8, 1, 9]
# number.sort()
# print(number)

# Q3. Create a list [10, 20, 30, 40] and reverse its order using reverse().
# number = [10, 20, 30, 40]
# number.reverse()
# print(number)

# Q4. Create a list ["Apple", "Mango", "Banana"] and find the index of "Banana" using index().
# fruit = ["Apple", "Mango", "Banana"]
# print(fruit.index("Banana"))

# Q5. Create a list ["Python", "SQL", "Excel"] and find the index of "SQL" using index().
# text = ["Python", "SQL", "Excel"]
# print(text.index("SQL"))

# Q6. Create a list [10, 20, 10, 30, 10] and count how many times 10 appears using count().
# number = [10, 20, 10, 30, 10]
# print(number.count(10))

# Q7. Create a list ["Apple", "Mango", "Apple", "Banana", "Apple"] and count how many times "Apple" appears.
# fruits = ["Apple", "Mango", "Apple", "Banana", "Apple"]
# print(fruits.count("Apple"))

# Q8. Create a list [50, 20, 40, 10, 30], sort it first and then reverse it.
# number = [50, 20, 40, 10, 30]
# number.sort()
# number.reverse()
# print(number)
# ----------------------------------------------------------------------------------------------------------

# 🐍 Tuples — Part 1: Basics

# Q1. Create a tuple containing "Apple", "Mango", and "Banana" and print the tuple.
# fruits = ("Apple", "Mango", "Banana")
# print(fruits)

# Q2. Create a tuple of 5 numbers and print the first number.
# number = (1, 2, 3, 4, 5)
# print(number[0])

# Q3. Create a tuple of 5 fruits and print the last fruit using negative indexing.
# fruits = ["mango", "orange", "banana", "coconut", "papaya"]
# print(fruits[-1])

# Q4. Create a tuple of 5 numbers and print the third number.
# fruits = (10, 20, 30, 40, 50)
# print(fruits[2])

# Q5. Create a tuple of 5 fruits and print the first 3 fruits using slicing.
# fruits = ["mango", "orange", "banana", "coconut", "papaya"]
# print(fruits[0:3])

# Q6. Create a tuple of 5 numbers and print the last 2 numbers using slicing.
# numbers = (10, 20, 30, 40, 50)
# print(numbers[-2:])

# Q7. Create a tuple ("Python", "SQL", "Excel") and try to change "SQL" to "Power BI".
# Observe what happens.
# text = ("Python", "SQL", "Excel")
# text[1] = "Power BI"
# print(text)

# Q8. Create a tuple containing your name, age, and city, then print your name using indexing.
# data = ("vikash", "25", "kolkata")
# print(data[0])
# ------------------------------------------------------------------------------------------------------------

# ✅ Tuple Basics complete.

# Ab Tuple ke important methods sirf 2 hain:

# count()
# index()

# Phir 5–6 practice questions karke Tuples complete ✅ kar denge.

# Q1. Create a tuple (10, 20, 10, 30, 10) and count how many times 10 appears.
# number = (10, 20, 10, 30, 10)
# print(number.count(10))

# Q2. Create a tuple ("Apple", "Mango", "Banana") and find the index of "Banana".
# fruits = ("Apple", "Mango", "Banana")
# print(fruits.index("Banana"))

# # Q3. Create a tuple ("Python", "SQL", "Python", "Excel") and count how many times "Python" appears.
# text = ("Python", "SQL", "Python", "Excel")
# print(text.count("Python"))

# Q4. Create a tuple (5, 10, 15, 20, 25) and find the index of 20.
# number = (5, 10, 15, 20, 25)
# print(number.index(20))

# Q5. Create a tuple ("Red", "Blue", "Green", "Blue") and count how many times "Blue" appears.
# colour = ("Red", "Blue", "Green", "Blue")
# print(colour.count("Blue"))

# Q6. Create a tuple ("Python", "SQL", "Excel", "Power BI") and find the index of "Excel".
# text = ("Python", "SQL", "Excel", "Power BI")
# print(text.index("Excel"))
# -------------------------------------------------------------------------------------------------------------

# 🐍 SETS — BASIC PRACTICE
# 📌 Topic: Set Creation, Duplicates, in, Empty Set & Indexing

# Q1. SET CREATION
# Create a set containing "Apple", "Mango", and "Banana" and print the set.
# fruits = {"Apple", "Mango", "Banana"}
# print(fruits)

# Q2. DUPLICATES
# Create a set containing duplicate numbers 10, 20, 10, 30, 20
# and print the set.
# number = {10, 20, 10, 30, 20}
# print(number)

# Q3. MEMBERSHIP CHECK — in
# Create a set of 5 fruits and check whether "Mango" is present using in.
# fruits = {"Apple", "Mango", "Banana"}
# print("Mango" in fruits)

# Q4. MEMBERSHIP CHECK — in
# Create a set of numbers and check whether 100 is present using in.
# number = {100, 3888, 373, 283}
# print(100 in number)

# Q5. EMPTY SET
# Create an empty set correctly using set().
# empty_set = set()
# print(empty_set)


# Q6. MEMBERSHIP CHECK — in
# Create a set containing "Python", "SQL", and "Excel".
# Check whether "Power BI" is present using in.
# text = {"Python", "SQL", "Excel"}
# print("Power BI" in text)

# Q7. DUPLICATES
# Create a set with duplicate values and observe how Python removes duplicates.
# number = {100, 100, 400, 400, 600, 200, 200}
# print(number)

# Q8. INDEXING
# Create a set of 5 numbers and try to access its first element using indexing.
# Observe what happens.
# number = { 5, 2, 8, 1, 9}
# print(number[0])
# -----------------------------------------------------------------------------------------------------------

# 🐍 SETS — METHODS PRACTICE
# 📌 Topic: add(), update(), remove(), discard(), pop(), clear()

# Q1. ADD
# Create a set {"Apple", "Mango"} and add "Banana" using add().
# fruit = {"Apple", "Mango"}
# fruit.add("Banana")
# print(fruit)

# Q2. UPDATE
# Create a set {"Python", "SQL"} and add "Excel" and "Power BI" using update().
# text = {"Python", "SQL"}
# text.update(["Excel", "Power BI"])
# print(text)

# Q3. REMOVE
# Create a set {"Apple", "Mango", "Banana"} and remove "Mango" using remove().
# fruits = {"Apple", "Mango", "Banana"}
# fruits.remove("Mango")
# print(fruits)

# Q4. DISCARD
# Create a set {"Apple", "Mango", "Banana"} and remove "Orange" using discard().
# Observe what happens.
# fruits = {"Apple", "Mango", "Banana"}
# fruits.discard("Orange")
# print(fruits)

# Q5. POP
# Create a set of 4 fruits and remove one element using pop().
# Observe which element gets removed.
# fruits = {"Apple", "Mango", "Banana", "Orange"}
# fruits.pop()
# print(fruits)

# Q6. CLEAR
# Create a set {"Python", "SQL", "Excel"} and remove all elements using clear()
# Tool = {"Python", "SQL", "Excel"}
# Tool.clear()
# print(Tool)

# Q7. ADD + UPDATE
# Create a set {10, 20, 30}.
# Add 40 using add().
# Then add 50 and 60 using update().
# number = {10, 20, 30}
# number.add(40)
# print(number)
# number.update([50,60])
# print(number)

# Q8. DISCARD
# Create a set {"Python", "SQL", "Excel"} and remove "SQL" using discard().
# text = {"Python", "SQL", "Excel"}
# text.discard("SQL")
# print(text)
#------------------------------------------------------------------------------------------------------------

#📝 Practice — Set Operations

# Q1. UNION
#Find the union of A and B.
#Create two sets:
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.union(B))

# Q2. INTERSECTION
# Find the common elements.
# Create two sets:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A.intersection(B))


# Q3. DIFFERENCE
# Find the elements that are in A but not in B.
# Create two sets:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A.difference(B))

# Q4. DIFFERENCE
# Using the same sets, find the elements that are in B but not in A.
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(B.difference(A))

# Q5. SYMMETRIC DIFFERENCE
# Find the elements that are present in only one of the two sets.
# Create:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A.symmetric_difference(B))

# Q6. UNION
# Find all unique skills.
# A = {"Python", "SQL"}
# B = {"Excel", "SQL"}
# print(A.union(B))

# Q7. INTERSECTION
# Find the common skills.
# A = {"Python", "SQL", "Excel"}
# B = {"SQL", "Power BI", "Excel"}
# print(A.intersection(B))

# Q8. DIFFERENCE
# Find the skills that A has but B does not have.
# A = {"Python", "SQL", "Excel"}
# B = {"SQL", "Power BI"}
# print(A.difference(B))
#--------------------------------------------------------------------------------------------------------

#🐍 DICTIONARIES — PART 1: BASICS

# Q1. DICTIONARY CREATION
# Create a dictionary containing your name, age, and city.
# Print the dictionary.
# student = {
#     "name": "Vikash",
#     "age" : 25,
#     "city": "Kolkata"
# }

# print(student)

# Q2. KEY-VALUE ACCESS
# Create a dictionary containing "name", "age", and "city".
# Print the value of "name" using its key.
# student = {
#     "name": "Vikash",
#     "age" : 25,
#     "city": "Kolkata"
# }

# print(student["name"])

# Q3. KEY-VALUE ACCESS
# Create a dictionary containing "name", "age", and "city".
# Print the value of "city" using its key.
# student = {
#     "name": "Vikash",
#     "age" : 25,
#     "city": "Kolkata"
# }
# print(student["city"])

# Q4. MODIFY VALUE
# Create a dictionary with "name" and "age".
# Change the age to 26 and print the dictionary.
# student = {
#     "name": "Vikash",
#     "age" : 25,
#     "city": "Kolkata"
# }
# student["age"] = 26

# print(student)

# Q5. UNIQUE KEYS
# Create a dictionary with "name" and "age".
# Try using the same key twice with different values.
# Observe which value Python keeps.

# student = {
#     "name": "Vikash",
#     "age": 25,
#     "age": 30
# }

# print(student)
#Output:
# {'name': 'Vikash', 'age': 30}
# Python keep last value.

# "age" : 25  ❌
# "age" : 30  ✅

# Q6. DUPLICATE VALUES
# Create a dictionary where two different keys have the same value.
# Print the dictionary.


# Q7. MULTIPLE DATA TYPES
# Create a dictionary containing:
# name → string
# age → integer
# salary → number
# Print the dictionary.
# student = {
#     "name": "Vikash",
#     "age": 25,
#     "salary": 30000
# }

# print(student)

# Q8. ACCESS MULTIPLE VALUES
# Create a dictionary containing name, age, and city.
# Print the name and city separately using their keys.
# student = {
#     "name": "Vikash",
#     "age": 25,
#     "city": "Kolkata"
# }

# print(student["name"])
# print(student["city"])
#---------------------------------------------------------------------------------------------------

# 🐍 DICTIONARY — ADD NEW KEY-VALUE
# Q1. ADD NEW KEY
# Create a dictionary with "name" and "age".
# Add a new key "city" with value "Kolkata".
# Print the dictionary.

# student = {
#     "name": "Vikash",
#     "age": 25
# }

# student["city"] = "kolkata"
# print(student)


# Q2. ADD NEW KEY
# Create a dictionary with "name" and "city".
# Add a new key "age" with value 25.
# Print the dictionary.
# student = {
#     "name": "Vikash",
#     "city": "kolkata"
# }

# student["age"] = 25
# print(student)

# Q3. ADD NEW KEY
# Create a dictionary with "name" and "age".
# Add a new key "job" with value "Data Analyst".
# Print the dictionary.
# student = {
#     "name": "Vikash",
#     "age": 25
# }

# student["job"] = "Data Analyst"
# print(student)

# Q4. ADD NEW KEY
# Create a dictionary with "name", "age", and "city".
# Add a new key "salary" with value 30000.
# Print the dictionary.
# student = {
#     "name": "Vikash",
#     "age": 25,
#     "city": "Delhi"
# }

# student["salary"] = 30000
# print(student)

# Q5. ADD MULTIPLE KEYS
# Create a dictionary with "name" only.
# Add "age" and "city" as new key-value pairs.
# Print the dictionary.
# student = {
#     "name": "vikash"
# }

# student["age"] = 25
# student["city"] = "Delhi"
# print(student)
#--------------------------------------------------------------------------

# 🐍 DICTIONARY — DELETE PRACTICE

# Q1. DELETE KEY
# Create a dictionary with "name", "age", and "city".
# Delete the "age" key using del.
# Print the dictionary.
# student = {
#     "name": "vikash",
#     "age": 25,
#     "city":"Chennai"
# }

# del student["age"]
# print(student)

# Q2. DELETE KEY
# Create a dictionary with "name", "age", and "city".
# Delete the "city" key using del.
# Print the dictionary.
# student = {
#     "name": "vikash",
#     "age": 25,
#     "city":"Chennai"
# }

# del student["city"]
# print(student)

# Q3. DELETE MULTIPLE KEYS
# Create a dictionary with "name", "age", "city", and "salary".
# Delete "age" and "salary".
# Print the dictionary.
# student = {
#     "name": "vikash",
#     "age": 25,
#     "city":"Chennai",
#     "salary": 100000
# }
# del student["salary"]
# del student["age"]
# print(student)
#----------------------------------------------------------------------

# 🐍 DICTIONARY — keys() PRACTICE

# Q1. Create a dictionary with "name", "age", and "city".
# Print all keys using keys().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai"
# }
# print(student.keys())

# Q2. Create a dictionary with "name", "age", "city", and "salary".
# Print all keys using keys().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai",
#     "salary": 37777
# }
# print(student.keys())
#-------------------------------------------------------------------------------------

# Q1. keys()
# Create a dictionary with name, age and city.
# Print all keys using keys().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai"
# }
# print(student.keys())

# Q2. values()
# Create a dictionary with name, age and city.
# Print all values using values().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai"
# }
# print(student.values())

# Q3. items()
# Create a dictionary with name, age and city.
# Print all key-value pairs using items().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai"
# }
# print(student.items())

# Q4. get()
# Create a dictionary with name, age and city.
# Get the value of "city" using get().
# student = {
#     "name": "vikash",
#     "age": 24,
#     "city": "mumbai"
# }
# print(student.get("city"))

# Q5. update()
# Create a dictionary with name and age.
# Update age to 26 using update().
# student = {
#     "name": "vikash",
#     "city":"mumbai",
#     "age": 25
# }
# student.update({"age": 26, "city": "kolkata"} )
# print(student)

# Q6. pop()
# Create a dictionary with name, age and city.
# Remove "age" using pop().
# student = {
#     "name": "vikash",
#     "city":"mumbai",
#     "age": 25
# }
# student.pop("age")
# print(student)


# Q7. popitem()
# Create a dictionary with name, age and city.
# Remove the last key-value pair using popitem().
# student = {
#     "name": "vikash",
#     "city":"mumbai",
#     "age": 25
# }
# student.popitem()
# print(student)


# Q8. clear()
# Create a dictionary with name, age and city.
# Remove all elements using clear().
# student = {
#     "name": "vikash",
#     "city":"mumbai",
#     "age": 25
# }
# student.clear()
# print(student)
#------------------------------------------------------------------------------------------

#📝 Practice — Nested Dictionary
# Q1. NESTED DICTIONARY
# Create a dictionary containing two students.
# Each student should have name and age.
# Print the complete dictionary.

# student = {
#     "student1":{
#     "name": "vikash",
#     "age": 24
#   },

#     "student2":{
#         "name": "rahul",
#         "age": 25
#     }

# }

# print(student)


# Q2. ACCESS NESTED VALUE
# Using the same type of dictionary,
# print the name of the first student.
# student = {
#     "student1":{
#     "name": "vikash",
#     "age": 24
#   },

#     "student2":{
#         "name": "rahul",
#         "age": 25
#     }

# }

# print(student["student1"] ["name"])


# Q3. ACCESS NESTED VALUE
# Using the same type of dictionary,
# print the age of the second student.

# student = {
#     "student1": {
#         "name": "vikash",
#         "age": 25
#     },

#     "student2" : {
#         "name": "rahul",
#         "age": 26
#     }
# }

# print(student["student2"]["age"])
#-----------------------------------------------------------------------------------

#Nested Dictionary — Change Value

# Q4. CHANGE VALUE
# Create a nested dictionary with two students.
# Change the age of the first student to 26.
# Print the dictionary.

# student = {
#     "student1": {
#         "name": "vikash",
#         "age": 24
#     },

#     "student2": {
#         "name": "vikash",
#         "age": 25
#     }
# }
# student["student1"]["age"] = 26
# print(student)

# Q5. CHANGE VALUE
# Create a nested dictionary with two students.
# Change the name of the second student to "Amit".
# Print the dictionary.

# student = {
#     "student": {
#         "name": "sumit"
#     },

#     "student2":{
#         "name": "vinit"
#     }
# }

# student["student2"]["name"] = "amit"

# print(student)
#--------------------------------------------------------------------------------------------

#🐍 Nested Dictionary — Add New Key

# Q6. ADD NEW KEY
# Create a nested dictionary with two students.
# Add "city" to the first student with value "Kolkata".
# Print the dictionary.

# student = {
#     "student1": {
#         "name": "Vikash",
#         "age": 24
#     },
#     "student2": {
#         "name": "Rahul",
#         "age": 25
#     }
# }

# student["student1"]["city"] = "Kolkata"

# print(student)

# Q7. ADD NEW KEY
# Create a nested dictionary with two students.
# Add "city" to the second student with value "Delhi".
# Print the dictionary.

# student = {
#     "student1": {
#         "name": "Vikash",
#         "age": 24,
#     },
#     "student2": {
#         "name": "Rahul",
#         "age": 25,
#     }
# }
# student["student2"]["city"] = "Delhi"
# print(student)
#------------------------------------------------------------------------------------

#🐍 Nested Dictionary — Delete
# Q8. DELETE NESTED KEY
# Create a nested dictionary with two students.
# Delete the "age" key from the first student.
# Print the dictionary.

student = {
    "student1": {
        "name": "Vikash",
        "age": 24,
    },
    "student2": {
        "name": "Rahul",
        "age": 25,
    }
}
del student["student1"]["age"]
print(student)
