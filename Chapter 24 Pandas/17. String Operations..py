# ========================================
# CODE NUMBERING BY:-

# 1 .str              [33 T0 134] ALL COMBINE 1 SE 3 TAK ]
# 2 str.lower()       []
# 3 str.upper()       []
#----------------------
# 4 str.strip()       [139 TO 225]
# 5 str.replace()     [229 TO 312]
# 6 str.contains()    [316 TO 420]
# 7 str.startswith()  [424 TO 514]
# 8 str.endswith()    [518 TO 614]
# =========================================

#========================================
# Complete Topic Overview
#========================================

# | No. | Topic              | Kya seekhenge?                                                     |
# | --: | ------------------ | ------------------------------------------------------------------ |
# |   1 | `.str`             | Pandas ke poore text column par operations karna                   |
# |   2 | `str.lower()`      | Text ko lowercase mein convert karna                               |
# |   3 | `str.upper()`      | Text ko uppercase mein convert karna                               |
# |   4 | `str.strip()`      | Text ke aage-peeche ke extra spaces hatana                         |
# |   5 | `str.replace()`    | Text ke andar kisi word ya character ko replace karna              |
# |   6 | `str.contains()`   | Column mein kisi word ya text ko search karna                      |
# |   7 | `str.startswith()` | Check karna ki text kisi particular text se start hota hai ya nahi |
# |   8 | `str.endswith()`   | Check karna ki text kisi particular text par end hota hai ya nahi  |


#================================
# Section 17 — String Operations
#--------------------------------
# Topic 1 — .str Accessor
#================================

# 1. .str kya hai?

# Pandas mein jab humein kisi poore text column par string operation karna hota hai, tab hum.
# str ka use karte hain.

# Maan lo hamare paas employees ka DataFrame hai:

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["vikash", "MOHIT", "Ravi"],
#     "City": ["Kolkata", "Delhi", "Mumbai"]
# })

# print(df)

# Output:

#      Name     City
# 0  vikash  Kolkata
# 1   MOHIT    Delhi
# 2    Ravi   Mumbai

# Ab maan lo humein Name column ke sabhi names lowercase mein chahiye.

# df["Name"] = df["Name"].str.lower()

# print(df)

# Output:

#      Name     City
# 0  vikash  Kolkata
# 1   mohit    Delhi
# 2    ravi   Mumbai
# 2. Code ko samjho
# df["Name"].str.lower()
# df["Name"] → Name column select karta hai.
# .str → Column ke text par string operations use karne deta hai.
# .lower() → Har name ko lowercase mein convert karta hai.

# Important: Python mein "VIKASH".lower() ek string par kaam karta hai, 
# jabki Pandas mein df["Name"].str.lower() poore column ke har name par kaam karta hai.

# Isi tarah hum .str.upper(), .str.strip(), .str.contains() aur doosre methods bhi use karenge.

# Practice — .str Basic

# Pehle ye 3 questions khud try karo. Solutions abhi nahi diye hain.

# ==========================================
# Pandas Section 17 — String Operations
# Topic 1: .str Basic
# ==========================================

# Q1.
# Create a DataFrame with a Name column containing
# "vikash", "mohit", and "ravi".
# Convert all names to uppercase using .str.upper().

# import pandas as pd

# df = pd.DataFrame({
#    "Name": ["vikash", "mohit",  "ravi"]  
# })

# df["Name"] = df["Name"].str.upper()
# print(df)
#-------------------------------------

# Q2.
# Create a DataFrame with a City column containing
# "KOLKATA", "DELHI", and "MUMBAI".
# Convert all cities to lowercase using .str.lower().

# import pandas as pd

# df = pd.DataFrame({
#    "City": ["KOLKATA", "DELHI",  "MUMBAI"]  
# })

# df["City"] = df["City"].str.lower()
# print(df)
#--------------------------------------------

# Q3.
# Create a DataFrame with a Product column containing
# "MAGGI", "BREAD", and "MILK".
# Convert the Product column to lowercase using .str.lower().
# Print the updated DataFrame.

# import pandas as pd

# df = pd.DataFrame({
#    "Product": ["MAGGI", "BREAD",  "MILK"]  
# })

# df["Product"] = df["Product"].str.lower()
# print(df)
#_____________________________________________________________________________________________________

#==============================
# Topic 4 — str.strip()
#==============================

# 1. str.strip() kya karta hai?

# Jab kisi text ke aage ya peeche extra spaces hote hain, toh .
# str.strip() unhe remove karta hai.

# Data Analyst ke liye ye useful hai, kyunki CSV ya Excel 
# se data import karte waqt text mein extra spaces ho sakte hain.

# 2. Example
# import pandas as pd

# df = pd.DataFrame({
#     "Name": [" Vikash ", " Mohit", "Ravi "]
# })

# df["Name"] = df["Name"].str.strip()

# print(df)

# Output:

#      Name
# 0  Vikash
# 1   Mohit
# 2    Ravi

# Samjho:

# " Vikash " → "Vikash"
# " Mohit" → "Mohit"
# "Ravi " → "Ravi"

# Yaad rakho: .str.strip() sirf aage aur peeche ke spaces hatata hai. 
# Text ke beech ke spaces nahi hatata.

# 3. Practice Questions
# Pandas — str.strip() Practice
# ==========================================
# Pandas Section 17 — String Operations
# Topic: str.strip()
# ==========================================

# Q1.
# Create a DataFrame with a Name column containing
# " Vikash ", " Mohit ", and " Ravi ".
# Remove leading and trailing spaces using .str.strip().

# import pandas as pd

# df = pd.DataFrame({
#    "Name": [" Vikash  ", "  Mohit",  "  Ravi"]  
# })

# df["Name"] = df["Name"].str.strip()
# print(df)
#----------------------------------------------

# Q2.
# Create a DataFrame with a City column containing
# " Kolkata", "Delhi ", and " Mumbai ".
# Remove leading and trailing spaces from the City column.

# import pandas as pd

# df = pd.DataFrame({
#    "City": ["  KOLKATA  ", "  DELHI  ",  "  MUMBAI  "]  
# })
# df["City"] = df["City"].str.strip()
# print(df)
#-----------------------------------------------

# Q3.
# Create a DataFrame with an Employee column containing
# " Amit ", " Rahul", and "Priya ".
# Apply .str.strip() and print the updated DataFrame.

# import pandas as pd

# df = pd.DataFrame({
#    "Employee": [" Amit ", " Rahul", "Priya "]  
# })

# df["Employee"] = df["Employee"].str.strip()
# print(df)
#_____________________________________________________________________________________________________

#==============================
# Topic 5 — str.replace()
#==============================

# 1. str.replace() kya karta hai?

# Ye text ke andar kisi character ya word ko doosre character ya word se replace karta hai.

# Maan lo City column mein Kol-kata likha hai aur humein hyphen (-) hatana hai.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kol-kata", "New-Delhi", "Mum-bai"]
# })

# df["City"] = df["City"].str.replace("-", "")

# print(df)

# Output:

#         City
# 0    Kolkata
# 1   NewDelhi
# 2     Mumbai
# 2. Code samjho
# df["City"].str.replace("-", "")
# Pehla "-" → jis text ko replace karna hai.
# Doosra "" → uski jagah kya rakhna hai; empty string dene se hyphen remove ho jata hai.

# Data Analyst use case: Text columns mein unwanted symbols ya inconsistent text ko clean karna.

# Practice Questions — str.replace()
# Pandas — str.replace() Practice
# ==========================================
# Pandas Section 17 — String Operations
# Topic: str.replace()
# ==========================================

# Q1.
# Create a DataFrame with a City column containing
# "Kol-kata", "New-Delhi", and "Mum-bai".
# Remove all hyphens using .str.replace().

import pandas as pd

df = pd.DataFrame({
   "City": ["Kol-kata", "New-Delhi", "Mum-bai"]  
})

df["City"] = df["City"].str.replace("-", "")
print(df)
#-----------------------------------------------

# Q2.
# Create a DataFrame with a Product column containing
# "Maggi123", "Bread456", and "Milk789".
# Remove the digits 123, 456, and 789 from the values
# using .str.replace().

import pandas as pd

df = pd.DataFrame({
    "Product": ["Maggi123", "Bread456", "Milk789"]
})

df["Product"] = df["Product"].str.replace("123", "")
df["Product"] = df["Product"].str.replace("456", "")
df["Product"] = df["Product"].str.replace("789", "")

print(df)
#--------------------------------------------

# Q3.
# Create a DataFrame with a Phone column containing
# "987-654", "876-543", and "765-432".
# Remove the hyphen from every phone number.

# import pandas as pd 
# df = pd.DataFrame({ 
#     "Phone": ["987-654", "876-543", "765-432"] 
# }) 
# df["Phone"] = df["Phone"].str.replace("-", "") 
# print(df)
#_____________________________________________________________________________________________________

#==============================
# 6 str.contains()
#==============================

# Pandas mein .str.contains() ka use kisi text column mein specific 
# word ya text ko search karne ke liye hota hai.

# Example: Humein products mein se "Milk" wale products find karne hain.

# import pandas as pd

# df = pd.DataFrame({
#     "Product": ["Milk", "Bread", "Milk Powder", "Butter"]
# })

# result = df["Product"].str.contains("Milk")

# print(result)

# Output:

# 0     True
# 1    False
# 2     True
# 3    False
# Name: Product, dtype: bool

# Yahan:

# "Milk" → True
# "Bread" → False
# "Milk Powder" → True
# "Butter" → False

# Kyunki "Milk" aur "Milk Powder" dono mein "Milk" present hai.

# 2. Matching rows filter karna

# Agar humein sirf Milk wale products chahiye:

# filtered_df = df[df["Product"].str.contains("Milk")]

# print(filtered_df)

# Output:

#        Product
# 0         Milk
# 2  Milk Powder

# Yaad rakho:

# .str.contains("Milk") → True/False deta hai.
# df[...] → sirf matching rows select karta hai.
# Default mein search case-sensitive hota hai. "milk" aur "Milk" alag ho sakte hain.
# Practice Questions — str.contains()
# Pandas — str.contains() Practice

# ==========================================
# Pandas Section 17 — String Operations
# Topic 6: str.contains()
# ==========================================

# Q1.
# Create a DataFrame with a Product column containing
# "Milk", "Bread", "Milk Powder", and "Butter".
# Filter and display rows where Product contains "Milk".

# import pandas as pd

# df = pd.DataFrame({
#     "Product" : ["Milk", "Bread", "Milk Powder",  "Butter"]
# })

# filter_df = df[df["Product"].str.contains("Milk")]
# print(filter_df)
#--------------------------------------------------

# Q2.
# Create a DataFrame with an Email column containing
# "user@gmail.com", "admin@yahoo.com", and "sales@gmail.com".
# Filter and display rows where Email contains "gmail".

# import pandas as pd

# df = pd.DataFrame({
#     "Email" : ["user@gmail.com", "admin@yahoo.com", "sales@gmail.com"]
# })

# filter_df = df[df["Email"].str.contains("gmail")]
# print(filter_df)
#------------------------------------------------

# Q3.
# Create a DataFrame with an Employee column containing
# "Amit Sharma", "Rahul Verma", and "Amit Kumar".
# Filter and display rows where Employee contains "Amit".

# import pandas as pd

# df = pd.DataFrame({
#     "Employee" : ["Amit Sharma", "Rahul Verma",  "Amit Kumar"]
# })

# filter_df = df[df["Employee"].str.contains("Amit")]
# print(filter_df)
#_____________________________________________________________________________________________________

#==============================
# Topic 7 — str.startswith()
#==============================

# 1. str.startswith() kya karta hai?

# Ye check karta hai ki kisi text ki value kisi particular word ya character se start (shuru) hoti hai ya nahi.

# Example:

# import pandas as pd

# df = pd.DataFrame({
#     "Employee": ["Amit Sharma", "Rahul Verma", "Amit Kumar", "Priya Singh"]
# })

# result = df["Employee"].str.startswith("Amit")

# print(result)

# Output:

# 0     True
# 1    False
# 2     True
# 3    False
# Name: Employee, dtype: bool
# 2. Matching rows filter karna
# filtered_df = df[df["Employee"].str.startswith("Amit")]

# print(filtered_df)

# Output:

#        Employee
# 0   Amit Sharma
# 2     Amit Kumar

# Important difference:

# .str.contains("Amit") → text ke kisi bhi part mein Amit search karta hai.
# .str.startswith("Amit") → sirf check karta hai ki text Amit se shuru ho raha hai ya nahi.
# Practice Questions — str.startswith()
# Pandas — str.startswith() Practice
# ==========================================
# Pandas Section 17 — String Operations
# Topic 7: str.startswith()
# ==========================================

# Q1.
# Create a DataFrame with an Employee column containing
# "Amit Sharma", "Rahul Verma", "Amit Kumar", and "Priya Singh".
# Filter and display employees whose names start with "Amit".

# import pandas as pd

# df = pd.DataFrame({
#     "Employee" : ["Amit Sharma", "Rahul Verma", "Amit Kumar","Priya Singh"]
# })

# result = df[df["Employee"].str.startswith("Amit")]
# print(result)
#------------------------------------

# Q2.
# Create a DataFrame with a Product column containing
# "Milk", "Milk Powder", "Bread", and "Butter".
# Filter and display products that start with "Milk".

# import pandas as pd

# df = pd.DataFrame({
#     "Product" : ["Milk", "Milk Powder", "Bread", "Butter"]
# })

# result = df[df["Product"].str.startswith("Milk")]
# print(result)
#----------------------------

# Q3.
# Create a DataFrame with an Email column containing
# "admin@gmail.com", "user@yahoo.com", and "amit@gmail.com".
# Filter and display emails that start with "amit".

# import pandas as pd

# df = pd.DataFrame({
#     "Email" : ["admin@gmail.com", "user@yahoo.com", "amit@gmail.com"]
# })

# result = df[df["Email"].str.startswith("amit")]
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 8 — str.endswith()
#==============================

# 1. str.endswith() kya karta hai?

# Ye check karta hai ki kisi text ki value kisi particular 
# word ya character par end (khatam) hoti hai ya nahi.

# Example
# import pandas as pd

# df = pd.DataFrame({
#     "Email": [
#         "user@gmail.com",
#         "admin@yahoo.com",
#         "sales@gmail.com",
#         "info@outlook.com"
#     ]
# })

# result = df["Email"].str.endswith(".com")

# print(result)

# Output:

# 0    True
# 1    True
# 2    True
# 3    True
# Name: Email, dtype: bool

# Sabhi emails .com par end ho rahe hain, isliye sabhi ka result True hai.

# 2. Matching rows filter karna

# Maan lo humein sirf Gmail addresses chahiye:

# filtered_df = df[df["Email"].str.endswith("@gmail.com")]

# print(filtered_df)

# Output:

#              Email
# 0   user@gmail.com
# 2  sales@gmail.com
# Important Difference
# Method	Kaam
# .str.contains()	Text ke andar search karta hai
# .str.startswith()	Text ki shuruaat check karta hai
# .str.endswith()	Text ka ending check karta hai
# Practice Questions — str.endswith()
# Pandas — str.endswith() Practice
# ==========================================
# Pandas Section 17 — String Operations
# Topic 8: str.endswith()
# ==========================================

# Q1.
# Create a DataFrame with an Email column containing
# "user@gmail.com", "admin@yahoo.com", and "sales@gmail.com".
# Filter and display emails that end with "@gmail.com".

# import pandas as pd

# df = pd.DataFrame({
#     "Email" : [
#         "user@gmail.com", 
#         "admin@yahoo.com", 
#         "sales@gmail.com"
#     ]
# })

# result = df[df["Email"].str.endswith("@gmail.com")]
# print(result)

#----------------------------------------------------

# Q2.
# Create a DataFrame with a File column containing
# "sales.csv", "report.xlsx", and "employee.csv".
# Filter and display files that end with ".csv".

# import pandas as pd

# df = pd.DataFrame({
#    "File" : ["sales.csv", "report.xlsx", "employee.csv"] 
# })

# fillter_data = df[df["File"].str.endswith(".csv")]
# print(fillter_data)
#--------------------------------------------

# Q3.
# Create a DataFrame with a Product column containing
# "Apple Juice", "Orange Juice", and "Fresh Milk".
# Filter and display products that end with "Juice".

import pandas as pd

df = pd.DataFrame({
   "Product" : ["Apple Juice", "Orange Juice", "Fresh Milk"] 
})

fillter_data = df[df["Product"].str.endswith("Juice")]
print(fillter_data)