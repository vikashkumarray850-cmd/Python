# ========================================
# CODE NUMBERING BY:-

#  16 TO 153     head()
#  157 TO 286    tail()
#  290 TO 367    info()
#  370 TO 533    describe() 
#  537 TO 669    shape
#  673 TO 807    columns
#                index
#                dtypes
# ========================================

#==============================
# Topic 1 — head()
#==============================

# 1. head() kya hota hai?

# Jab kisi CSV ya Excel file mein bahut saari rows hoti hain, 
# toh poora data print karne ki zaroorat nahi hoti.

# head() ki help se hum DataFrame ki shuru ki rows dekh sakte hain.

# head() → Pehli 5 rows dikhata hai.
# head(3) → Pehli 3 rows dikhata hai.
# head(10) → Pehli 10 rows dikhata hai.
# 2. Example

# Maan lo hamare paas sales.xlsx file hai, jismein 8 rows hain.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df.head())

# Output:

#    SaleID   Product  Quantity  Amount
# 0     101    Laptop         2   80000
# 1     102     Mouse         5    2500
# 2     103  Keyboard         3    4500
# 3     104   Monitor         2   30000
# 4     105    Laptop         1   40000

# Yahan sirf pehli 5 rows dikh rahi hain, jabki file mein 8 rows hain.

# Agar tum likho:

# print(sales_df.head(3))

# Toh sirf pehli 3 rows dikhengi.

# 3. Data Analyst ke liye head() kyun useful hai?

# Jab Data Analyst koi naya dataset load karta hai, toh head() se jaldi pata chal jata hai:

# Data sahi load hua ya nahi.
# Column names sahi hain ya nahi.
# Data ka format kaisa hai.
# Values expected tarah se dikh rahi hain ya nahi.
# Practice Questions — head()
# ==========================================
# Pandas — head() Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display the first 4 rows.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.head(4))
#--------------------------------------------
# Q2. Read "sales.xlsx" into sales_df.
# Display the first 2 rows.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df.head(2))
#-----------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Display the first 6 rows.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df.head(6))
#______________________________________________________________________________________________________

#==============================
# Topic 2 — tail()
#==============================

# tail() DataFrame ki aakhri rows dikhata hai.

# print(products_df.tail())

# Yeh aakhri 5 rows dikhayega.

# print(products_df.tail(2))

# Yeh aakhri 2 rows dikhayega.

# Yaad rakhna:

# head() → shuru ki rows
# tail() → aakhri rows
# Practice Questions — tail()
# ==========================================
# Pandas — tail() Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display the last 3 rows.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.tail(3))
#0--------------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display the last 4 rows.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df.tail(4))
#-------------------------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Display the last 2 rows.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df.tail(2))
#___________________________________________________________________________________---

#==============================
# 4. Topic — info()
#==============================
# 1. info() kya hota hai?

# info() DataFrame ke baare mein important information deta hai:

# Total rows ka index range
# Total columns
# Har column ka naam
# Har column mein non-null values ki sankhya
# Har column ka data type
# Memory usage
# 2. Example
# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# sales_df.info()

# Output kuch is tarah hoga:

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8 entries, 0 to 7
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   SaleID    8 non-null      int64
#  1   Product   8 non-null      object
#  2   Quantity  8 non-null      int64
#  3   Amount    8 non-null      int64

# Output ka exact format Pandas version aur file ke data types ke hisaab se thoda alag ho sakta hai.

# Is output ko kaise samjhein?

# 8 entries → 8 rows hain.
# 4 columns → 4 columns hain.
# 8 non-null → us column mein 8 values missing nahi hain.
# int64 → integer type ka data.
# object → aam taur par text data.

# Ek important baat: info() ka output khud print ho jata hai, 
# isliye print(sales_df.info()) likhne par aakhir mein None bhi dikh sakta hai. 
# Seedha sales_df.info() likhna behtar hai.

# Practice Questions — info()
# ==========================================
# Pandas — info() Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display the DataFrame information.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# employees_df.info()
#-----------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display the DataFrame information.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# sales_df.info()
#--------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Display the DataFrame information.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# products_df.info()
#_________________________________________________________________________________________________

#==============================
# Topic 4 — describe()
#==============================

# 1. describe() kya hota hai?

# describe() numerical columns ka statistical summary deta hai. 
# Data Analyst iska use data ko jaldi samajhne ke liye karta hai.

# Maan lo tumhare paas sales.xlsx hai:

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df.describe())
# 2. Output ko samjho

# Hamare sales dataset mein SaleID, Quantity aur Amount numerical columns hain. 
# describe() inka summary dega.

# Statistic	Meaning
# count	Non-missing numerical values ki sankhya
# mean	Average
# std	Values kitni spread out hain, iska measure
# min	Sabse chhoti value
# 25%	First quartile
# 50%	Median
# 75%	Third quartile
# max	Sabse badi value

# Example: Agar Amount ki values 80000, 2500, 4500, 30000 hain, toh:

# min = 2500
# max = 80000
# count = 4

# Isse humein baar-baar har value check kiye bina data ka overview milta hai.

# 3. Sirf ek column ka summary

# Agar sirf Amount ka statistical summary chahiye:

# print(sales_df["Amount"].describe())
# 4. Important baat

# Default mein describe() numerical columns ka summary deta hai. 
# Text columns ka summary dekhne ke liye:

# print(sales_df.describe(include="object"))

# Isse text columns ke liye count, unique, top aur freq jaise statistics mil sakte hain.

# Practice Questions — describe()
# ==========================================
# Pandas — describe() Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display the statistical summary of numerical columns.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df.describe())
#-------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display the statistical summary of the "Amount" column.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df["Amount"].describe())
#---------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Display the statistical summary of text columns.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df.describe(include="object"))
#________________________________________________________________________________________________

