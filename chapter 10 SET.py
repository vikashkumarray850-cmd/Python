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