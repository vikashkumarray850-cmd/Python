# ========================================
# CODE NUMBERING BY:-

#  Single Column            [14 TO 92]
#  Multiple Columns         [96 TO 139]
#  loc[]                    [143 TO 245] 
#  iloc[]                   [249 TO 363]
#  Row Selection            [366 TO PASS] TO BE UPDATE SOON
#  Column Selection         [376 TO 459]
#  Specific Cell Selection  [463 TO 552]
# ==========================================

#==============================
# Topic 1 — Single Column
#==============================

# 1. Single Column kya hota hai?

# Maan lo hamare paas sales.xlsx ka DataFrame hai:

# SaleID	Product	Quantity	Amount
# 101	Laptop	2	80000
# 102	Mouse	5	2500
# 103	Keyboard	3	4500
# 104	Monitor	2	30000

# Agar humein sirf Product column chahiye, 
# toh poora DataFrame print karne ki zaroorat nahi hai.

# Pandas mein single column select karne ke liye 
# hum column ka naam use karte hain.

# 2. Syntax
# df["column_name"]
# df → DataFrame ka variable
# "column_name" → Us column ka naam jo select karna hai
# 3. Example
# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df["Product"])

# Output:

# 0      Laptop
# 1       Mouse
# 2    Keyboard
# 3     Monitor
# Name: Product, dtype: object

# Yahan sirf Product column ki values dikhengi.

# Ek important baat: sales_df["Product"] ka result Pandas Series hota hai, DataFrame nahi.

# Isi tarah:

# print(sales_df["Amount"])

# Sirf Amount column ki values dikhengi.

# Practice Questions — Single Column

# Tumhari preferred comment-based practice format mein 3 questions:

# ==========================================
# Pandas — Single Column Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display only the "Salary" column.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df["Salary"])
#------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display only the "Product" column.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df["Product"])
#---------------------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Display only the "Price" column.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df["Price"])
#_________________________________________________________________________________________________

#==============================
# Topic 2: Multiple Columns
#==============================

# 1. Multiple Columns kya hote hain?

# Jab ek hi DataFrame se do ya usse zyada columns chahiye hon, toh column names ki list use karte hain.

# Example:

# print(sales_df[["Product", "Amount"]])

# Yahan double square brackets [[...]] hain:

# Bahar ke brackets DataFrame se columns select karte hain.
# Andar ki list mein selected column names hain.

# Isse Product aur Amount dono columns milenge, aur result ek DataFrame hoga.

# Practice Questions — Multiple Columns
# ==========================================
# Pandas — Multiple Columns Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display only the "Employee" and "Salary" columns.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df[["Employee", "Salary"]])
#------------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display only the "Product" and "Amount" columns.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df[["Product", "Amount"]])
#-----------------------------------------
# Q3. Read "products.xlsx" into products_df.
# Display only the "ProductName", "Price" and "Stock" columns.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df[["ProductName", "Price", "Stock"]])
#_______________________________________________________________________________________________

#==============================
# Topic 3: loc[]
#==============================

# 1. loc[] kya hota hai?

# Pandas mein loc[] ka use index labels ke basis par rows select karne ke liye hota hai. 
# Isse hum specific rows, columns ya dono select kar sakte hain.

# Abhi hum pehle row selection samjhenge.

# 2. Example DataFrame

# Maan lo employees.xlsx mein yeh data hai:

# Index	Employee	Department	Salary
# 0	Amit	IT	25000
# 1	Neha	HR	32000
# 2	Rahul	Sales	28000
# 3	Priya	IT	35000

# Is DataFrame ko read karte hain:

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df)
# 3. Ek row select karna

# Agar humein index label 1 wali row chahiye:

# print(employees_df.loc[1])

# Output kuch aisa hoga:

# Employee       Neha
# Department       HR
# Salary        32000
# Name: 1, dtype: object

# Yahan loc[1] index label 1 wali row select karta hai.

# 4. Multiple rows select karna

# Agar humein index labels 0, 1 aur 2 wali rows chahiye:

# print(employees_df.loc[[0, 1, 2]])

# Yahan [0, 1, 2] index labels ki list hai.

# 5. Range of rows select karna

# Agar humein index label 0 se 2 tak ki rows chahiye:

# print(employees_df.loc[0:2])

# Important: loc[] mein range ka last label bhi include hota hai. 
# Isliye loc[0:2] mein labels 0, 1 aur 2 aayenge.

# loc[] vs iloc[]

# Abhi sirf itna difference yaad rakho:

# loc[]	iloc[]
# Index label ke basis par selection	Position ke basis par selection
# df.loc[2]	df.iloc[2]

# Agar index labels default 0, 1, 2, 3 hain, 
# toh dono examples mein teesri row select hogi. 
# Lekin custom index hone par result alag ho sakta hai.

# iloc[] ko hum agle topic mein detail se padhenge.

# Practice Questions — loc[]

# Tumhari comment-based practice format mein 3 questions:

# ==========================================
# Pandas — loc[] Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Select the row with index label 2.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.loc[2])
#-------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Select the rows with index labels 0, 2 and 4.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df.loc[[0, 2, 4]])
#----------------------------------------------
# Q3. Read "products.xlsx" into products_df.
# Select all rows from index label 1 to index label 3,
# including index label 3.

# import pandas as pd

# products_df = pd.read_csv("products.csv")
# print(products_df.loc[1:3])
#_____________________________________________________________________________________________________

#==============================
# Topic 4: iloc[]
#==============================

# iloc[] ka use DataFrame mein integer position ke basis par rows select karne ke liye hota hai.

# Simple language mein:

# loc[] → index label se row select karta hai.
# iloc[] → row ki position se select karta hai.

# Example ke liye, maan lo employees_df mein ye data hai:

# Index	Employee	Department	Salary
# 0	Amit	IT	25000
# 1	Neha	HR	32000
# 2	Rahul	Sales	28000
# 3	Priya	IT	35000

# Example 1: Ek row select karna

# print(employees_df.iloc[2])

# Output mein Rahul ki row aayegi, kyunki Rahul position 2 par hai. Counting 0 se start hoti hai.

# Example 2: Multiple rows select karna

# print(employees_df.iloc[[0, 2]])

# Isse position 0 aur position 2 wali rows milengi — Amit aur Rahul.

# Example 3: Slicing se rows select karna

# print(employees_df.iloc[1:3])

# Isse position 1 aur 2 wali rows milengi — Neha aur Rahul.

# Dhyan do: iloc[1:3] mein position 3 include nahi hoti.

# loc[] aur iloc[] ka difference
# Code	Meaning
# df.loc[2]	Index label 2 wali row
# df.iloc[2]	Position 2 wali row
# df.loc[1:3]	Labels 1 se 3 tak, dono included
# df.iloc[1:3]	Positions 1 aur 2; ending position excluded

# Agar index labels badal diye jaayen, toh loc[] aur iloc[] ka result alag ho sakta hai.

# Tumhari baat samajh aa rahi hai 😊 Agar index aur position
# dono ek hi row ki taraf point kar rahe hain, toh answer same hi aayega. 
# Lekin har baar same answer nahi aayega. Ek example dekho.

# Example: Index labels badal gaye
# Position	Index Label	Employee
# 0	10	Amit
# 1	20	Neha
# 2	30	Rahul
# 3	40	Priya

# Ab dono ko compare karo:

# 1. loc[] — Index label se

# print(df.loc[30])

# Output: Rahul, kyunki Rahul ka index label 30 hai.

# 2. iloc[] — Position se

# print(df.iloc[1])

# Output: Neha, kyunki Neha position 1 par hai.

# Dekha? Dono ka answer alag hai.

# Jab index labels 0, 1, 2, 3 hon

# Tab df.loc[2] aur df.iloc[2] dono Rahul ko select karenge. 
# Isliye tumhe lag raha tha ki dono same hain.

# Bas ye yaad rakho:

# loc = index label
# iloc = row ki position

# Dono ka result same bhi ho sakta hai aur alag bhi—ye DataFrame ke index par depend karta hai.

# Practice Questions — iloc[]
# ==========================================
# Pandas — iloc[] Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Select the row at position 3.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.iloc[3])
# -----------------------------------------------

# Q2. Read "sales.csv" into sales_df.
# Select the rows at positions 1, 3 and 5.

# import pandas as pd
# sales_df = pd.read_csv("sales.csv")
# print(sales_df.iloc[[1, 3, 5]])
# -----------------------------------------------

# Q3. Read "products.csv" into products_df.
# Select all rows from position 2 up to position 5,
# excluding position 5.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# print(products_df.iloc[2:5])
#_____________________________________________________________________________________________________

#==============================
# Topic 5: Row Selection
#==============================





#_____________________________________________________________________________________________________

#==============================
# Topic 6: Column Selection
#==============================

# Column Selection ka matlab hai DataFrame mein se ek ya ek se zyada columns ko select karna.

# Single Column aur Multiple Columns hum pehle padh chuke hain. 
# Isliye unhe repeat nahi karenge. 
# Ab hum seekhenge ki loc[] aur iloc[] ki madad se columns kaise select karte hain.

# 1. loc[] se column select karna

# Maan lo employees_df mein ye data hai:

# Employee	Department	Salary
# Amit	IT	25000
# Neha	HR	32000
# Rahul	Sales	28000

# Agar tumhe sabhi employees ke naam chahiye:

# print(employees_df.loc[:, "Employee"])

# Samjho:

# : ka matlab hai sabhi rows.
# "Employee" ka matlab hai Employee column select karna.

# Agar tumhe Employee aur Salary dono columns chahiye:

# print(employees_df.loc[:, ["Employee", "Salary"]])

# Yahan : sabhi rows select karta hai aur list mein diye gaye columns select hote hain.

# 2. iloc[] se column select karna

# iloc[] mein column ki integer position use kar sakte ho.

# Position	Column
# 0	Employee
# 1	Department
# 2	Salary

# Sirf Salary column:

# print(employees_df.iloc[:, 2])

# Employee aur Salary columns:

# print(employees_df.iloc[:, [0, 2]])

# Yaad rakho: loc[] mein column ka naam use kar sakte ho, jabki iloc[] mein uski position.

# Practice Questions — Column Selection
# ==========================================
# Pandas — Column Selection Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Use loc[] to select all rows and the Department column.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.loc[:,"Department"])
#--------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Use iloc[] to select all rows and the columns
# at positions 0 and 3.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df.iloc[:, [0, 3]])
#------------------------------------------------

# Q3. Read "products.csv" into products_df.
# Use loc[] to select all rows and the ProductName
# and Price columns.

# import pandas as pd

# products_df = pd.read_csv("products.csv")
# print(products_df.loc[:,["ProductName","Price" ]])
#________________________________________________________________________________________________

#==================================
# Topic 7: Specific Cell Selection.
#==================================

# 1. Specific Cell Selection kya hai?

# Jab humein DataFrame ke andar se sirf ek particular
# row aur ek particular column ki value chahiye,
# tab hum Specific Cell Selection karte hain.

# Maan lo products_df mein ye data hai:

# Index	ProductName	Price	Stock
# 0	Laptop	45000	12
# 1	Mouse	600	40
# 2	Keyboard	1200	25
# 3	Monitor	16000	18

# Humein sirf Mouse ki price 600 nikalni hai.

# 2. loc[] se ek cell select karna
# print(products_df.loc[1, "Price"])

# Output:

# 600

# Samjho:

# 1 → row ka index label
# "Price" → column ka naam
# Dono ke intersection par value 600 hai.
# 3. iloc[] se ek cell select karna
# print(products_df.iloc[1, 2])

# Yahan:

# Pehla 1 → row ki position
# Doosra 2 → column ki position

# Is example mein column positions hain:

# Position	Column
# 0	ProductID
# 1	ProductName
# 2	Category
# 3	Price
# 4	Stock

# Dhyan do: Agar tumhe Mouse ki price chahiye, 
# toh iloc[1, 3] likhna hoga, kyunki Price ki position 3 hai.

# print(products_df.iloc[1, 3])

# Output:

# 600

# Yaad rakho: loc[] mein label aur column name use karte hain, 
# jabki iloc[] mein row aur column ki integer positions use karte hain.

# Practice Questions — Specific Cell Selection
# ==========================================
# Pandas — Specific Cell Selection
# ==========================================

# Q1. Read "products.csv" into products_df.
# Use loc[] to print the Price of the Laptop.

# import pandas as pd
# products_df =pd.read_csv("products.csv")
# print(products_df.loc[0,"Price"])
#------------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Use iloc[] to print the Salary of Rahul.
# Use the actual row and column positions.

# import pandas as pd
# employees_df =pd.read_excel("employees.xlsx")
# print(employees_df.iloc[2,2])
#------------------------------------------------
# Q3. Read "sales.xlsx" into sales_df.
# Use loc[] to print the Amount for SaleID 104.
# Assume the DataFrame index is the default integer index.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df.loc[3, "Amount"])
##_____________________________________________________________________________________________________
