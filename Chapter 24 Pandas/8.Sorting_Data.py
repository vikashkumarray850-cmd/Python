# ===================================
# CODE NUMBERING BY:-

# 1 sort_values()            [14 TO 103]
# 2 Ascending Sorting   --|  [107 TO 215]
# 3 Descending Sorting  --# ==================================|  [108 TO 241]
# 4 Multiple Column Sorting  [245 TO 315]
# 5 sort_index()             [319 TO 369]


#_____________________________________________________________________________________________________

#==============================
# Topic 1: sort_values()
#==============================

# 1. Sorting kya hoti hai?

# Sorting ka matlab data ko kisi order mein arrange karna hai.

# Example:

# Price ko lowest se highest arrange karna.
# Salary ko highest se lowest arrange karna.
# Sales amount ko ascending ya descending order mein arrange karna.

# Data Analyst ke liye sorting useful hai jab humein highest salary, 
# expensive products ya top sales dekhni hoti hain.

# 2. sort_values() ka use

# Maan lo tumhare paas products.csv hai:

# ProductName	Price
# Laptop	45000
# Mouse	600
# Keyboard	1200
# Monitor	16000

# Agar tum Price ko lowest se highest arrange karna chahte ho:

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df.sort_values(by="Price")

# print(result)

# Output ka order:

# ProductName	Price
# Mouse	600
# Keyboard	1200
# Monitor	16000
# Laptop	45000

# Notice karo: Price ke according rows ka order change ho gaya hai.

# 3. Important baatein
# sort_values() rows ko sort karta hai.
# by="Price" batata hai ki kis column ke according sorting karni hai.
# Default sorting ascending hoti hai, yani chhoti value se badi value.
# Is example mein original DataFrame ko directly change nahi kiya; 
# sorted result ko result mein store kiya hai.

# Practice Questions — sort_values()

# Pandas — sort_values() Practice
# ==========================================
# Pandas — sort_values() Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Sort all products by Price from lowest to highest.

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df.sort_values(by = "Price")
# print(result)
#-----------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Sort all employees by Salary from lowest to highest.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# result = employees_df.sort_values(by = "Salary")

# print(result)
#---------------------------------------------------

# # Q3. Read "sales.xlsx" into sales_df.
# # Sort all sales by Amount from lowest to highest.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")
# result = sales_df.sort_values(by = "Amount")
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 2 Ascending Sorting
# Topic 3 Descending Sorting
#==============================

# 1. Ascending Sorting

# Ascending ka matlab smallest se largest.

# result = products_df.sort_values(
#     by="Price",
#     ascending=True
# )

# print(result)

# Example: 600, 1200, 2500, 16000, 45000

# Yahan ascending=True explicitly batata hai ki values chhoti se badi honi chahiye.

# 2. Descending Sorting

# Descending ka matlab largest se smallest.

# result = products_df.sort_values(
#     by="Price",
#     ascending=False
# )

# print(result)

# Example: 45000, 16000, 2500, 1200, 600

# Yahan ascending=False ka matlab hai badi se chhoti value.

# Yaad rakhne ka easy trick
# Parameter	Order	Example
# ascending=True	Chhoti → Badi	10, 20, 30, 40
# ascending=False	Badi → Chhoti	40, 30, 20, 10

# sort_values(by="Price") aur sort_values(by="Price", ascending=True) dono ka result same hoga.

# Example
# # Method 1
# result = products_df.sort_values(by="Price")

# # Method 2
# result = products_df.sort_values(by="Price", ascending=True)

# Dono mein Price lowest se highest sort hoga, kyunki ascending=True default hota hai.

# Phir ascending=False kab use karenge?
# result = products_df.sort_values(by="Price", ascending=False)

# Ismein Price highest se lowest sort hoga.

# Code	Sorting order
# sort_values(by="Price")	Lowest → Highest
# sort_values(by="Price", ascending=True)	Lowest → Highest
# sort_values(by="Price", ascending=False)	Highest → Lowest

# Yaad rakho: ascending=True likhna optional hai, lekin ascending=False 
# likhna zaroori hai jab descending order chahiye.

# Practice Questions — Ascending & Descending
# Pandas — Ascending & Descending Practice

# ==========================================
# Pandas — Ascending & Descending Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Sort products by Price from highest to lowest.

# import pandas as pd
# products_df = pd.read_csv("products.csv")

# result = products_df.sort_values(
#     by = "Price",
#     ascending = False
# )
# print(result)
#------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Sort employees by Salary from highest to lowest.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx" )

# result = employees_df.sort_values(
#     by = "Salary",
#     ascending = False
# )
# print(result)
#--------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Sort sales by Amount from highest to lowest.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx" )

# result = sales_df.sort_values(
#     by = "Amount",
#     ascending = False
# )
# print(result)
#------------------------------------------

# Q1. Read "products.csv" into products_df.
# Sort all products by Price from highest to lowest.

# import pandas as pd
# products_df = pd.read_csv("products.csv")

# result = products_df.sort_values(
#     by = "Price",
#     ascending = True
# )
# print(result)
#-------------------------------------------
# Q2. Read "employees.xlsx" into employees_df.
# Sort all employees by Salary from lowest to highest.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx" )

# result = employees_df.sort_values(
#     by = "Salary",
#     ascending = True
# )
# print(result)
#_____________________________________________________________________________________________________

#=================================
# topic 4: Multiple Column Sorting
#=================================

# Ab hum seekhenge ki ek DataFrame ko ek se zyada columns ke according kaise sort karte hain.

# Maan lo employees ka data hai:

# Employee	Department	Salary
# Amit	IT	25000
# Neha	HR	32000
# Rahul	Sales	28000
# Priya	IT	35000
# Mohit	HR	30000

# Agar pehle Department ke according aur phir har department ke andar 
# Salary ke according sort karna ho, toh:

# result = employees_df.sort_values(
#     by=["Department", "Salary"]
# )

# print(result)

# Kaise kaam karta hai?

# Pehle departments alphabetical order mein arrange honge.
# Phir har department ke employees ki salary lowest se highest arrange hogi.

# Yahan by mein ek column ke bajay columns ki list di gayi hai.

# Practice Questions — Multiple Column Sorting
# Pandas — Multiple Column Sorting Practice
# ==========================================
# Pandas — Multiple Column Sorting Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Sort employees first by Department and then by Salary.

# import pandas  as pd
# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df.sort_values(
#     by = ["Department","Salary"],
#     ascending = True
# )
# print(result)
#------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Sort sales first by Product and then by Amount.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")

# result = sales_df.sort_values(
#     by = ["Product", "Amount"]   
# )
# print(result)
#----------------------------------------

# Q3. Read "products.csv" into products_df.
# Sort products first by Category and then by Price.

# import pandas as pd
# products_df = pd.read_csv("products.csv")

# result = products_df.sort_values(
#     by = ["Price", "Category"]
# )
# print(result)
#_____________________________________________________________________________________________________

#==============================
# topic 5: sort_index()
#==============================

# Ab hum Section 8 ka agla topic shuru karenge: sort_index().

# sort_values() → column ki values ke according sorting.
# sort_index() → DataFrame ke index ke according sorting.

# Example:

# result = employees_df.sort_index()
# print(result)

# Agar index 0, 1, 2, 3 hai, toh rows index ke ascending order mein arrange hongi.

# Practice Questions — sort_index()
# Pandas — sort_index() Practice
# ==========================================
# Pandas — sort_index() Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Sort the DataFrame by its index in descending order.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx" )

# result = employees_df.sort_index(ascending = False)
# print(result)
#--------------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Sort the DataFrame by its index in ascending order.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx" )

# result = sales_df.sort_index(ascending = True)
# print(result)
#------------------------------------------------------

# Q3. Read "products.csv" into products_df.
# Sort the DataFrame by its index in descending order.

import pandas as pd
products_df = pd.read_csv("products.csv")

result = products_df.sort_index()
print(result)