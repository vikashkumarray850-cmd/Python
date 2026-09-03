
#----------------------------------------------------------------------------

#🐍 Strings — Practice Questions

# Q1. Create a string "Vikash" and print its first character.

# name = "Vikash"
# print(name[0])

# Q2. Create a string "Vikash" and print its last character using negative indexing.

# name = "Vikash"
# print(name[-1])

# Q3. Create a string "Kolkata" and print its third character.
# city = "Kolkata"
# print(city[2])

# Q4. Create a string "Python" and print "Pyt" using slicing.
# name = "Python"
# print(name[0:3])

# Q5. Create a string "Python" and print "hon" using slicing.
# name = "Python"
# print(name[3:6])

# Q6. Create a string "Programming" and print "Program" using slicing.
# name = "Programming"
# print(name[0:7])

# Q7. Create a string "Programming" and print the last 3 characters using negative slicing.
# name = "Programming"
# print(name[-3:])

# Q8. Create a string "Vikash Kumar" and print only "Vikash" using slicing.
# name ="Vikash kumar"
# print(name[0:6])

# Q9. Create a string "Vikash Kumar" and print only "Kumar" using slicing.
# name ="Vikash kumar"
# print(name[7:])

# Q10. Create a string "Data Analyst" and print "Data" and "Analyst" separately using slicing.
# text = "Data Analyst"
# print(text[0:4], text[5:])

# Q11. Create a string "Computer" and print its first 5 characters using slicing.
# name = "Computer" 
# print(name[0:5])

# Q12. Create a string "Computer" and print its last 4 characters using negative slicing.
# name = "Computer"
# print(name[-4:])

# Q13. Create a string "Python" and print "thon" using slicing.
# name = "Python"
# print(name[2:])

# Q14. Create a string "Programming" and print "gram" using slicing.
# name = "Programming"
# print(name[3:7])
#-----------------------------------------------------------------------------------------

#🐍 Strings — Part 2: String Operations


# Q1. Create two strings "Vikash" and "Kumar" and join them with a space using +.
# first_name = "Vikash"
# last_name = "Kumar"

# Full_name = first_name + " " + last_name
# print(Full_name)

# Q2. Create two strings "Data" and "Analyst" and join them using +.
# first_text = "Data"
# last_text = "Analyst"

# full_text = first_text + " " + last_text
# print(full_text)

# Q3. Create a string "Python" and print it 3 times using *.
# word = "Python"
# print(word * 3)

# Q4. Create a string "Hi " and print it 5 times using *.
# name = "Hi "
# print(name * 5)

# Q5. Create a string "Vikash" and find its length using len().
# Name = "Vikash"
# print(len(Name))

# Q6. Create a string "Data Analyst" and find its total length using len().
# text = "Data Analyst"
# print(len(text))

# Q7. Create a string "Python Programming" and check whether "Python" is present using in.
# name = "Python Programming" 
# print("Python" in name)

# Q8. Create a string "Python Programming" and check whether "Java" is not present using not in.
# name = "Python Programming" 
# print("Java" not in name)

#--------------------------------------------------------------------------------------------------------
#🐍 String Methods — Practice

# Q1. Create a string "python" and convert it into uppercase using upper().
# name = "python"
# print(name.upper())

# Q2. Create a string "PYTHON" and convert it into lowercase using lower().
# name = "PYTHON"
# print(name.lower())

# Q3. Create a string "python programming" and convert the first character to uppercase using capitalize().
# name = "python programming"
# print(name.capitalize())

# Q4. Create a string "python programming language" and convert every word's first character to uppercase using title().
# name = "python programming"
# print(name.title())

# Q5. Create a string with extra spaces around "Vikash" and remove the extra spaces using strip().
# name = "    Vikash     "
# print(name.strip())

# Q6. Create a string "I like Python" and replace "Python" with "SQL" using replace().
# name = "I like Python"
# print(name.replace("Python", "SQL"))

# Q7. Create a string "banana" and count how many times "a" appears using count().
# NAME = "banana"
# print(NAME. count("a"))

# Q8. Create a string "Python" and find the index of "t" using find().
# name = "Python"
# print(name.find("t"))

# Q9. Create a string "Python Programming" and check whether it starts with "Python" using startswith().
# name = "python programming"
# print(name.startswith("Python"))

# Q10. Create a string "Python Programming" and check whether it ends with "Programming" using endswith().
# name = "python programming"
# print(name.endswith("programming"))

#-----------------------------------------------------------------------------------------------------
#🐍 String Methods — Part 2

# Q1. Create a string "I love Python" and split it into separate words using split().
# text = "I love Python" 
# print(text.split())


# Q2. Create a list ["Data", "Analyst"] and join the words with a space using join().
# word = ["Data", "Analyst"]
# print(" ".join(word))

# Q3. Create a string "Python" and check whether it contains only alphabets using isalpha().
# text = "Python"
# print(text. isalpha())

# Q4. Create a string "Python123" and check whether it contains only alphabets using isalpha().
# text= "Python123"
# print(text.isalpha())

# Q5. Create a string "12345" and check whether it contains only digits using isdigit().
# number="12345"
# print(number. isdigit())

# Q6. Create a string "Python123" and check whether it contains only alphabets and numbers using isalnum().
# number="Python123"
# print(number. isalnum())

# Q7. Create a string "Python 123" and check whether it contains only alphabets and numbers using isalnum().
# number="Python 123"
# print(number. isalnum())

# Q8. Create a string containing only spaces and check it using isspace().
# text = "   "

# print(text.isspace())

# Q9. Create a list ["Python", "SQL", "Excel"] and join all elements using " - " as the separator.
# languages = ["Python", "SQL", "Excel"]

# print(" - ".join(languages))

# Q10. Create a string "Data Analyst Python" and split it into separate words using split().
# text = "Data Analyst Python"

# print(text.split())

#------------------------------------------------------------------------------------------------------------
# 🐍 String Methods — Part 3

# Q1. Create a string "Python" and find the index of "t" using index().
# text=  "Python"
# print(text.index("t"))

# Q2. Create a string "Programming" and find the index of "g" using index().
# text=  "Programming"
# print(text.index("g"))

# Q3. Create a string "banana" and find the last occurrence of "a" using rfind().
# name = "banana"
# print(name.rfind("a"))

# Q4. Create a string "Programming" and find the last occurrence of "m" using rfind().
# name = "Programming"
# print(name.rfind("m"))

# Q5. Create a string with spaces before "Python" and remove the left-side spaces using lstrip().
# text = "   Python"

# print(text.lstrip())

# Q6. Create a string with spaces after "Python" and remove the right-side spaces using rstrip().
# text = "Python   "

# print(text.rstrip())

# Q7. Create a string with spaces on both sides of "Data Analyst" and remove only the left-side spaces using lstrip().
# text = "   Data Analyst   "

# print(text.lstrip())

# Q8. Create a string with spaces on both sides of "Data Analyst" and remove only the right-side spaces using rstrip().

# text = "   Data Analyst   "

# print(text.rstrip())
