# ========================================
# CODE NUMBERING BY:-

# 1 drop()                   [15 TO 100]
# 2 Drop Columns             [103 TO 160]
# 3 Drop Rows                [103 TO 160]
# 4 drop_duplicates()        [244 TO 340]
# =========================================

#_____________________________________________________________________________________________________

#==============================
# Section 10: Removing Data
#--------------------------
# Topic 1: drop() in Pandas
#==============================

# drop() kya karta hai?

# Pandas mein drop() method ka use DataFrame se unwanted 
# rows ya columns ko remove karne ke liye hota hai.

# Maan lo hamare paas products.csv ka DataFrame hai.

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# print(products_df)

# DataFrame mein ye columns hain:

# Index	ProductID	ProductName	Category	Price	Stock
# 0	301	Laptop	Electronics	45000	12
# 1	302	Mouse	Accessories	600	40
# 2	303	Keyboard	Accessories	1200	25
# 3	304	Monitor	Electronics	16000	18

# Ab maan lo humein index 2 wali row remove karni hai.

# new_df = products_df.drop(index=2)

# print(new_df)

# Kya hoga?

# Keyboard wali row remove ho jayegi.
# Baaki rows DataFrame mein rahengi.
# Original products_df by default change nahi hoga; 
# removed row wala result new_df mein milega.

# Dhyan do: index=2 ka matlab hai index label 2 wali row remove karna.

# Ek important baat

# drop() se column remove karne ke liye bhi use hota hai. 
# Lekin filhaal basic concept samjho; 
# agle topic mein columns ko detail mein remove karenge.

# Practice Questions — drop() Basic

# In questions ko apni Python file mein solve karo. Abhi solutions nahi diye gaye hain.

# ==========================================
# Pandas — Removing Data: drop() Basic
# ==========================================

# Q1. Load products.csv into a DataFrame.
# Remove the row whose index label is 3.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd
# product_df = pd.read_csv("products.csv")

# new_df = product_df.drop(index=3)
# print(new_df)
#-------------------------------------------

# Q2. Load sales.xlsx into a DataFrame.
# Remove the row whose index label is 5.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# result = new_df = sales_df.drop(index=5)
# print(result)
#--------------------------------------------

# Q3. Load employees.xlsx into a DataFrame.
# Remove the row whose index label is 1.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd
# employees_df  = pd.read_excel("employees.xlsx")
# result = new_df = employees_df.drop(index=1)
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 2: Drop Columns
#==============================

# Ab hum seekhenge ki DataFrame se unwanted column kaise remove karte hain.

# Maan lo products_df mein ye columns hain:

# ProductID, ProductName, Category, Price, Stock

# Agar humein Stock column remove karna ho, to:

# new_df = products_df.drop(columns=["Stock"])

# print(new_df)

# Yahan columns=["Stock"] ka matlab hai ki Stock column remove karna hai.

# Dhyan do: Row remove karte waqt humne index=3 use kiya tha; 
# column remove karte waqt columns=["Stock"] use kar rahe hain.

# ==========================================
# Pandas — Removing Data: Drop Columns
# ==========================================

# Q1. Load products.csv into a DataFrame.
# Remove the Stock column.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd
# product_df = pd.read_csv("products.csv")
# result = product_df.drop(columns=["Stock"])
# print(result)
#----------------------------------------------

# Q2. Load employees.xlsx into a DataFrame.
# Remove the Department column.
# Store the result in a new_df  DataFrame.
# Print the new DataFrame.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df.drop(columns=["Department"])
# print(result)
#----------------------------------------------------

# Q3. Load sales.xlsx into a DataFrame.
# Remove both the Quantity and Amount columns.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# result = sales_df.drop(columns=["Quantity", "Amount" ])
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 3: Drop Rows
#==============================

# Pehle hum ek row remove kar chuke hain. Ab samjhenge ki ek 
# saath multiple rows kaise remove karte hain.

# 1. Multiple Rows Remove Karna

# Maan lo products_df mein index labels 0 se 7 tak hain.

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# new_df = products_df.drop(index=[1, 3, 5])

# print(new_df)

# Samjho:

# index=[1, 3, 5] ka matlab hai index labels 1, 3 aur 5 wali rows remove karna.
# Square brackets [] ke andar hum multiple index labels dete hain.
# Baaki rows result mein rahengi.
# Original products_df default behaviour mein unchanged rahega.
# 2. Index Labels Important Hain

# Maan lo DataFrame ke index labels hain:

# 0, 2, 4, 6

# Agar tum drop(index=2) likhoge, to label 2 wali row remove hogi, doosri row nahi.

# Yaad rakho: drop(index=...) index labels ke basis par rows remove karta hai.

# Practice Questions — Drop Rows

# Ab ye 3 questions khud solve karo. Solutions abhi nahi diye gaye hain.

# ==========================================
# Pandas — Removing Data: Drop Rows
# ==========================================

# Q1. Load products.csv into a DataFrame.
# Remove the rows whose index labels are 1 and 4.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# product_df = pd.read_csv("products.csv")
# result = product_df.drop(index=[1, 4])
# print(result)
#---------------------------------------------

# Q2. Load sales.xlsx into a DataFrame.
# Remove the rows whose index labels are 0, 3 and 6.
# Store the result in a new DataFrame.
# Print the new DataFrame.

import pandas as pd
sales_df = pd.read_excel("sales.xlsx")
result = sales_df.drop(index=[0,3,6])
print(result)
#------------------------------------------------


# Q3. Load employees.xlsx into a DataFrame.
# Remove the rows whose index labels are 0 and 2.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# result = employees_df.drop(index=[0, 2])
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 4: drop_duplicates()
#==============================

# Ab hum Section 10 ka aakhri topic seekhenge: duplicate rows ko remove karna.

# Maan lo DataFrame mein ye data hai:

# Index	Employee	Department
# 0	Amit	IT
# 1	Neha	HR
# 2	Amit	IT
# 3	Rahul	Sales

# Yahan Amit ki row do baar hai.

# new_df = employees_df.drop_duplicates()

# Isse poori tarah duplicate rows mein se ek row remove ho jayegi. 
# Amit ki ek row rahegi aur Neha aur Rahul ki rows bhi rahengi.

# Dhyan do: drop_duplicates() by default original DataFrame ko modify nahi karta; 
# result ko new_df mein store kiya ja sakta hai.

# ==========================================
# Pandas — Removing Data: drop_duplicates()
# ==========================================

# Q1. Load employees.xlsx into a DataFrame.
# Add a duplicate of the first row to the DataFrame.
# Remove duplicate rows.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# # Add a duplicate of the first row
# duplicate_row = employees_df.iloc[[0]]

# employees_df = pd.concat(
#     [employees_df, duplicate_row],
#     ignore_index=True
# )

# # Remove duplicate rows
# result = employees_df.drop_duplicates()

# print(result)
#----------------------------------------------------

# Q2. Load products.csv into a DataFrame.
# Add a duplicate of the last row to the DataFrame.
# Remove duplicate rows.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# # Add a duplicate of the last row
# duplicate_row = products_df.iloc[[-1]]

# products_df = pd.concat(
#     [products_df, duplicate_row],
#     ignore_index=True
# )

# # Remove duplicate rows
# result = products_df.drop_duplicates()

# print(result)
#--------------------------------------------

# Q3. Create a DataFrame with these records:
# Employee: Amit, Neha, Amit, Rahul
# Department: IT, HR, IT, Sales
# Salary: 25000, 32000, 25000, 28000
# Remove duplicate rows.
# Store the result in a new DataFrame.
# Print the new DataFrame.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Amit", "Rahul"],
#     "Department": ["IT", "HR", "IT", "Sales"],
#     "Salary": [25000, 32000, 25000, 28000]
# }

# employees_df = pd.DataFrame(data)

# # Remove duplicate rows
# result = employees_df.drop_duplicates()

# print(result)