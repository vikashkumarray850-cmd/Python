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
