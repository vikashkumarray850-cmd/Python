#📝 Practice — Lists Basics

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
#----------------------------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------------------------

#🐍 Tuples — Part 1: Basics

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
