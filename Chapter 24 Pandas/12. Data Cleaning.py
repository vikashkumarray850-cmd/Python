# ========================================
# CODE NUMBERING BY:-

# 1 Duplicates        [34 TO 181]
#   _______________________________
# 2| String Cleaning  [185 TO 409]|    |
#  | strip()                      |
#  | lower()                      |
#  | upper()                      |
#  | replace()                    |
#  -------------------------------|     
# 7 astype()          [413 TO 550]
# 8 pd.to_numeric()   [553 TO 686]
# =========================================

# | No. | Topic             | Kya seekhenge?                                  |
# | --: | ----------------- | ----------------------------------------------- |
# |   1 | Duplicates        | Duplicate records ko identify aur remove karna  |
# |   2 | Missing Values    | Missing data ko analyse aur handle karna        |
# |   3 | String Cleaning   | Text data ko clean aur consistent banana        |
# |   4 | `strip()`         | Text ke starting aur ending spaces remove karna |
# |   5 | `lower()`         | Text ko lowercase mein convert karna            |
# |   6 | `upper()`         | Text ko uppercase mein convert karna            |
# |   7 | `replace()`       | Text ke andar unwanted values ko replace karna  |
# |   8 | `astype()`        | Column ka data type change karna                |
# |   9 | `pd.to_numeric()` | Values ko numeric data mein convert karna       |


#_____________________________________________________________________________________________________

#==============================
# Section 12 — Data Cleaning
#--------------------------
# Topic 1: Duplicates
#==============================

# 1. Duplicate data kya hota hai?

# Jab dataset mein ek hi record ek se zyada baar aa jata hai, toh use duplicate record kehte hain.

# Example:

# import pandas as pd

# sales_df = pd.DataFrame({
#     "OrderID": [101, 102, 103, 101],
#     "Product": ["Laptop", "Mouse", "Keyboard", "Laptop"],
#     "Amount": [45000, 600, 1200, 45000]
# })

# print(sales_df)

# Output:

#    OrderID   Product  Amount
# 0      101    Laptop   45000
# 1      102     Mouse     600
# 2      103  Keyboard    1200
# 3      101    Laptop   45000

# Yahan index 0 aur 3 par same record hai. Isliye index 3 wala record duplicate hai.

# Data Analyst ke liye yeh kyun important hai?

# Maan lo tum company ki sales report bana rahe ho. 
# Agar ek hi order galti se do baar record ho gaya, 
# toh total sales galat calculate ho sakti hai.

# Lekin dhyan rahe: same OrderID ya same Product dikhne ka matlab hamesha duplicate nahi hota. 
# Humein business rules ke hisaab se decide karna hota hai ki kaun-sa record duplicate hai.

# 2. duplicated() ka use

# duplicated() batata hai ki kaun-si rows pehle se maujood records ki duplicates hain.

# print(sales_df.duplicated())

# Output:

# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool

# Iska matlab:

# False → Default comparison mein yeh row pehli baar aayi hai.
# True → Yeh row pehle se maujood complete record ki duplicate hai.

# Default behaviour mein Pandas pehli occurrence ko False rakhta hai aur uske baad aane wali identical rows ko True mark karta hai.

# Sirf duplicate rows dekhna

# Agar tumhe sirf duplicate records dekhne hain, toh Boolean filtering use kar sakte ho:

# duplicate_rows = sales_df[sales_df.duplicated()]

# print(duplicate_rows)

# Output:

#    OrderID Product  Amount
# 3      101  Laptop   45000

# Yahan sales_df.duplicated() ek Boolean Series deta hai, aur usse DataFrame filter karke sirf duplicate rows milti hain.

# 3. keep parameter — Duplicate kaunsi row mark hogi?

# duplicated() mein keep parameter se decide kar sakte hain ki identical records mein kaunsi occurrence ko original maana jaye.

# Maan lo OrderID 101 teen baar hai.

# sales_df.duplicated(keep="first")
# keep="first" — pehli occurrence ko False, baaki ko True.
# keep="last" — aakhri occurrence ko False, usse pehle wali duplicates ko True.
# keep=False — us record ki saari identical occurrences ko True mark karta hai.

# Example:

# sales_df.duplicated(keep=False)

# Isse duplicate group ki pehli row bhi identify ho jayegi, sirf baad wali rows nahi.

# Yeh tab useful hai jab tumhe dataset se duplicate records ka poora group inspect karna ho.

# Practice Questions — Duplicates

# Pehle concept samjho, phir ye 3 questions solve karo. Questions mein solutions nahi diye gaye hain.

# ==========================================
# Pandas — Data Cleaning: Duplicates
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: Amit, Neha, Rahul, Amit
# Department: IT, HR, Sales, IT
# Salary: 25000, 32000, 28000, 25000
# Identify all duplicate rows using duplicated().

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Amit"],
#     "Department": ["IT", "HR", "sales", "IT"],
#     "Salary": [25000, 32000, 30000, 25000]
# }
# employees_df = pd.DataFrame(data)
# print(employees_df.duplicated())
#--------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# OrderID: 101, 102, 103, 101, 102
# Product: Laptop, Mouse, Keyboard, Laptop, Mouse
# Amount: 45000, 600, 1200, 45000, 600
# Display every occurrence of records that have duplicates.

# import pandas  as pd
# data = {
#     "OrderID" : [101, 102, 103, 101, 102],
#     "Product" : ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
#     "Amount"  : [45000, 600, 1200, 45000, 600]
# }
# sales_df = pd.DataFrame(data)
# print(sales_df.duplicated())
#---------------------------------------------------------------

# Q3. Using sales_df from Q2, identify duplicate rows while
# keeping the last occurrence as the non-duplicate record.

# import pandas as pd

# data = {
#     "OrderID": [101, 102, 103, 101, 102],
#     "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
#     "Amount": [45000, 600, 1200, 45000, 600]
# }

# sales_df = pd.DataFrame(data)

# print(sales_df.duplicated(keep="last"))
#_____________________________________________________________________________________________________

#==============================
# Topic 2: String Cleaning
#==============================

# 1. String Cleaning kya hoti hai?

# Vikash, DataFrame mein jab hum text data ke saath kaam karte hain, 
# toh kabhi-kabhi text mein extra spaces, 
# capital letters ka difference ya unwanted characters hote hain.

# Aise text ko clean aur consistent banana String Cleaning kehlata hai.

# Data Analyst ke liye ye important hai, 
# kyunki ganda text data filtering, grouping aur 
# analysis mein problems create kar sakta hai.

# 2. Ek practical example dekho

# Maan lo company ke paas employees ka data hai:

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": [" Amit ", "NEHA", "rahul", "Priya "],
#     "Department": ["IT", "hr", "Sales", "IT"]
# })

# print(employees_df)

# Data kuch aisa dikhega:

# Employee	Department
# " Amit "	IT
# "NEHA"	hr
# "rahul"	Sales
# "Priya "	IT

# Is data mein teen tarah ki inconsistencies hain:

# " Amit " mein starting aur ending spaces hain.
# Employee names ka capitalization alag-alag hai.
# Department mein "hr" lowercase hai, jabki "IT" aur "Sales" ka format alag hai.

# Hum in values ko standard format mein la sakte hain.

# 3. String Cleaning mein kaun-se methods use honge?
# Method	Kaam
# .str.strip()	Text ke aage-peeche ke extra spaces remove karna
# .str.lower()	Text ko lowercase mein convert karna
# .str.upper()	Text ko uppercase mein convert karna
# .str.replace()	Text ke andar kisi specific text ko replace karna

# Ek important baat: Pandas mein column ke text par ye methods lagane ke liye hum
#  .str accessor use karte hain.

# Jaise:

# employees_df["Employee"].str.lower()

# Isse Employee column ke saare names lowercase mein milenge.

# Dhyan rahe, jab hum result ko kisi column mein assign nahi karte, 
# toh original column automatically change nahi hota.

# Practice Questions — String Cleaning Basics

# Abhi humne sirf concept samjha hai. Agle topics mein methods ko ek-ek karke detail mein padhenge.

# ============================================================
# Pandas — Section 12: Data Cleaning
# Topic: String Cleaning Practice
# ============================================================


# Q1. lower()
# Create a DataFrame named employees_df with these columns:
# Employee: ["AMIT", "NEHA", "RAHUL", "PRIYA"]
# Department: ["IT", "HR", "SALES", "IT"]
# Convert all Employee names into lowercase and save the
# result in the Employee column.

# import pandas as pd

# data = {
#     "Employee": ["AMIT", "NEHA", "RAHUL", "PRIYA"],
#     "Department": ["IT", "HR", "SALES", "IT"]
# }
# employees_df = pd.DataFrame(data)
# employees_df["Employee"] = employees_df["Employee"].str.lower()
# print(employees_df)
#--------------------------------------------------------------

# Q2. lower()
# Create a DataFrame named customers_df with these columns:
# Customer: ["KOLKATA", "DELHI", "MUMBAI", "CHENNAI"]
# CityCode: [101, 102, 103, 104]
# Convert all Customer names into lowercase and display
# the complete DataFrame.

# import pandas as pd

# data = {
#     "Customer": ["KOLKATA", "DELHI", "MUMBAI", "CHENNAI"],
#     "CityCode": [101, 102, 103, 104]
# }

# customers_df = pd.DataFrame(data)
# customers_df["Customer"] = customers_df["Customer"].str.lower()
# print(customers_df)
#-----------------------------------------------------
# Q3. upper()
# Create a DataFrame named products_df with these columns:
# Product: ["laptop", "mouse", "keyboard", "monitor"]
# Category: ["electronics", "accessories", "accessories", "electronics"]
# Convert all Product names into uppercase and save the
# result in the Product column.

# import pandas as pd

# data = {
#     "Product": ["laptop", "mouse", "keyboard", "monitor"],
#     "Category": ["electronics", "accessories", "accessories", "electronics"]
# }
# products_df = pd.DataFrame(data)
# products_df["Product"] = products_df["Product"].str.upper()
# print(products_df)
#-----------------------------------------------------------

# Q4. upper()
# Create a DataFrame named employees_df with these columns:
# Employee: ["amit", "neha", "rahul", "priya"]
# Department: ["it", "hr", "sales", "it"]
# Convert all Department values into uppercase and display
# the complete DataFrame.

# import pandas as pd

# data = {
#     "Employee": ["amit", "neha", "rahul", "priya"],
#     "Department": ["it", "hr", "sales", "it"]
# }
# employees_df = pd.DataFrame(data)
# employees_df["Department"] = employees_df["Department"].str.upper()
# print(employees_df)
#--------------------------------------------------------

# Q5. replace()
# Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul", "Priya"]
# Department: ["IT", "HR", "IT", "Sales"]
# Replace every occurrence of "IT" with "Technology" in
# the Department column and display the complete DataFrame.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "Sales"]
# }

# employees_df = pd.DataFrame(data)

# employees_df["Department"] = employees_df["Department"].str.replace("IT", "Technology")

# print(employees_df)
#---------------------------------------------------------------

# Q6. replace()
# Create a DataFrame named products_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Mouse"]
# Category: ["Electronics", "Old", "Accessories", "Old"]
# Replace every occurrence of "Old" with "Accessories" in
# the Category column and display the complete DataFrame.

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Mouse"],
#     "Category": ["Electronics", "Old", "Accessories", "Old"]
# }
# products_df = pd.DataFrame(data)
# products_df["Category"] = products_df["Category"].str.replace("Old" , "Accessories")
# print(products_df)
#----------------------------------------------------------

# Q7. strip()
# Create a DataFrame named employees_df with these columns:
# Employee: [" Amit ", " Neha", "Rahul ", " Priya "]
# Department: [" IT", "HR ", " Sales ", "IT"]
# Remove extra spaces from the beginning and end of every
# Employee name and save the cleaned values in the Employee column.
# Display the complete DataFrame.

# import pandas as pd

# data = {
#     "Employee": [" Amit ", " Neha", "Rahul ", " Priya "],
#     "Department": [" IT", "HR ", " Sales ", "IT"]
# }

# employees_df = pd.DataFrame(data)
# employees_df["Employee"] = employees_df["Employee"].str.strip()
# print(employees_df)
#-------------------------------------------------------------
# Q8. strip()
# Create a DataFrame named customers_df with these columns:
# Customer: [" Vikash ", " Mohit", "Ravi ", " Parmeshwar "]
# City: [" Kolkata ", " Delhi", "Mumbai ", " Chennai "]
# Remove extra spaces from the beginning and end of every
# value in both columns.
# Display the complete DataFrame.


# import pandas as pd

# data = {
#     "Customer": [" Vikash ", " Mohit", "Ravi ", " Parmeshwar "],
#     "City": [" Kolkata ", " Delhi", "Mumbai ", " Chennai "]
# }

# customers_df = pd.DataFrame(data)

# customers_df["Customer"] = customers_df["Customer"].str.strip()
# customers_df["City"] = customers_df["City"].str.strip()

# print(customers_df)
#_____________________________________________________________________________________________________

#==============================
# Topic 3: astype()
#==============================

# 1. astype() kya hai?

# Pandas mein astype() ka use kisi column ya Series ka data type change karne ke liye hota hai.

# Maan lo kisi dataset mein Product ID numbers ke roop mein hain, 
# lekin tum unhe text ke roop mein store karna chahte ho.

# Example:

# import pandas as pd

# products_df = pd.DataFrame({
#     "ProductID": [101, 102, 103],
#     "Product": ["Laptop", "Mouse", "Keyboard"]
# })

# print(products_df.dtypes)

# Output:

# ProductID     int64
# Product      object
# dtype: object

# Yahan ProductID ka data type int64 hai, jo integer numbers ko represent karta hai.

# 2. Integer ko String mein convert karna

# Ab maan lo Product ID ko text ke roop mein store karna hai.

# products_df["ProductID"] = products_df["ProductID"].astype(str)

# print(products_df.dtypes)

# Output:

# ProductID    object
# Product      object
# dtype: object

# Ab ProductID ka data type object ho gaya hai, 
# jo is example mein strings ko represent karta hai.

# Dhyan do: "101" aur 101 dikhne mein similar hain, lekin dono alag hain:

# 101 ek integer hai.
# "101" ek string hai.

# String ke roop mein Product ID ko display, 
# match ya text identifier ke roop mein use karna useful ho sakta hai.

# 3. String ko Integer mein convert karna

# Maan lo Quantity column mein numbers text ke roop mein store hain.

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Quantity": ["2", "5", "3"]
# })

# print(sales_df.dtypes)

# Ab Quantity ko integer mein convert karte hain:

# sales_df["Quantity"] = sales_df["Quantity"].astype(int)

# print(sales_df.dtypes)

# Ab Quantity ka data type int64 hoga.

# Isse tum Quantity par mathematical calculations kar sakte ho, 
# jaise total quantity ya quantity-based analysis.

# Important: astype(int) tabhi kaam karega jab values valid integers mein convert ho sakti hon. 
# Agar column mein "five" ya "unknown" jaisi values hain, toh conversion error de sakta hai.

# Practice Questions — astype()

# Pehle ye 3 questions khud solve karo. Solutions abhi nahi diye gaye hain.

# ==========================================
# Pandas — Data Cleaning: astype()
# ==========================================

# Q1. Create a DataFrame named products_df with these columns:
# ProductID: [101, 102, 103, 104]
# Product: ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Convert ProductID into a string data type.
# Print the data types of all columns.

# import pandas as pd
# products_df = pd.DataFrame({
# "ProductID":   [101, 102, 103, 104],
# "Product"  :   ["Laptop", "Mouse", "Keyboard", "Monitor"]
# })

# products_df["ProductID"] = products_df["ProductID"].astype(str)
# print(sales_df)
# print(products_df.dtypes)
#-----------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Quantity: ["2", "5", "3", "4"]
# Convert Quantity into an integer data type.
# Print the complete DataFrame and its data types.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Quantity": ["2", "5", "3", "4"]
# })

# sales_df["Quantity"] = sales_df["Quantity"].astype(int)
# print(sales_df.dtypes)
#----------------------------------------------------------------------

# Q3. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul"]
# Salary: [25000, 32000, 28000]
# Convert Salary into a float data type.
# Print the complete DataFrame and its data types.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": [25000, 32000, 28000]
# })

# employees_df["Salary"] = employees_df["Salary"].astype(float)
# print(employees_df)
# print(employees_df.dtypes)
#_____________________________________________________________________________________________________

#==============================
# topic 4: pd.to_numeric()
#==============================

# 1. pd.to_numeric() kya hai?

# Data Analysis mein kabhi-kabhi numbers kisi column mein 
# text (string) ke roop mein store hote hain. 
# Humein unhe numeric data mein convert karna padta hai.

# Example: "25000" ek string hai, jabki 25000 ek integer hai.

# pd.to_numeric() ka use text values ko numbers mein convert karne ke liye hota hai.

# Example 1: Normal conversion
# import pandas as pd

# df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": ["25000", "32000", "28000"]
# })

# df["Salary"] = pd.to_numeric(df["Salary"])

# print(df)
# print(df.dtypes)

# Yahan Salary column ke numbers text se numeric data type mein convert ho jayenge.

# Data Analyst use: Jab CSV ya Excel se numeric columns text ke roop mein aate hain, 
# toh unhe calculations aur analysis ke liye convert kar sakte hain.

# 2. Agar column mein invalid value ho toh?

# Maan lo Salary column mein ek value "Unknown" hai.

# import pandas as pd

# df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": ["25000", "Unknown", "28000"]
# })

# df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# print(df)

# Output:

#   Employee   Salary
# 0     Amit  25000.0
# 1     Neha      NaN
# 2    Rahul  28000.0

# Yahan errors="coerce" ka matlab hai:

# Valid numeric value → number mein convert hogi.
# Invalid value, jaise "Unknown" → NaN ban jayegi.
# NaN ka matlab hai missing numeric value.

# Dhyan rahe: errors="coerce" invalid data ko chupchaap NaN mein badal deta hai. 
# Isliye real analysis mein aisi values ko baad mein check karna chahiye.

# 3. astype() aur pd.to_numeric() mein difference
# Feature	astype()	pd.to_numeric()
# Main use	Data type convert karna	Values ko numeric banana
# String mein convert	astype(str)	Iska primary use nahi
# Integer mein convert	astype(int)	pd.to_numeric()
# Invalid values ko NaN banana	Direct option nahi	errors="coerce"
# Practice Questions — pd.to_numeric()

# Pehle examples samajh lo, phir ye 3 questions solve karo.

# ==========================================
# Pandas — Data Cleaning: pd.to_numeric()
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul"]
# Salary: ["25000", "32000", "28000"]
# Convert Salary into a numeric data type.
# Print the complete DataFrame and its data types.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": ["25000", "32000", "28000"]
# })
# employees_df["Salary"]= pd.to_numeric(employees_df["Salary"])
# print(employees_df)
# print(employees_df.dtypes)
#-----------------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Amount: ["45000", "600", "Invalid", "16000"]
# Convert Amount into numeric values.
# Handle invalid values using errors="coerce".
# Print the complete DataFrame.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Amount": ["45000", "600", "Invalid", "16000"]
# })
# sales_df["Amount"]= pd.to_numeric(sales_df["Amount"])
# print(sales_df)
# print(sales_df.dtypes)
#----------------------------------------------------------------

# Q3. Create a DataFrame named products_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Monitor"]
# Price: ["45000", "600", "1200", "Invalid"]
# Convert Price into numeric values.
# Handle invalid values using errors="coerce".
# Count the missing values in each column.

import pandas as pd

products_df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": ["45000", "600", "1200", "Invalid"]
})

products_df["Price"] = pd.to_numeric(
    products_df["Price"],
    errors="coerce"
)

print(products_df)

print("\nMissing Values:")
print(products_df.isna().sum())