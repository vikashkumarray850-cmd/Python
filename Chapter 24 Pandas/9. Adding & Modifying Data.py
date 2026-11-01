# ===================================
# CODE NUMBERING BY:-

# 1 Add New Column          [15 TO 98]
# 2 Modify Column           [101 TO 164]
# 3 Create Column________|  [167  TO 229]
# from Existing Columns__|  [167  TO 229]
# 4 Rename Columns          [233 TO 297 ]
# 5 Rename Index            [301 TO 376]
# ==================================

#_____________________________________________________________________________________________________

#==============================
# Topic 1: Add New Column
#==============================

# 1. Naya column kya hota hai?

# Maan lo tumhare paas products.csv hai:

# ProductName	Price	Stock
# Laptop	45000	12
# Mouse	600	40
# Keyboard	1200	25

# Ab tum chahte ho ki har product ke saath uski category ya discount bhi dikhai de.

# Hum DataFrame mein ek naya column add kar sakte hain.

# 2. Naya column kaise add karein?

# Example:

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# products_df["Discount"] = 10

# print(products_df)

# Yahan:

# products_df["Discount"] naye column ka naam hai.
# = 10 ka matlab hai har row mein Discount ki value 10 set karna.
# Agar Discount column pehle se nahi hai, toh Pandas use create kar dega.

# Output mein naya column dikhega:

# ProductName	Price	Stock	Discount
# Laptop	45000	12	10
# Mouse	600	40	10
# Keyboard	1200	25	10

# Important: Naya column add karne ke liye alag se add_column() 
# method ki zaroorat nahi hai. Hum assignment (=) ka use karte hain.

# Practice Questions — Add New Column
# Pandas — Add New Column Practice
# ==========================================
# Pandas — Add New Column Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Add a new column named "Status".
# Set its value to "Available" for every row.

# import pandas as pd

# products_df = pd.read_csv("products.csv")
# products_df["Status"] = "Available"

# print(products_df)
#-------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Add a new column named "Bonus".
# Set its value to 5000 for every employee.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# employees_df["Bonus"] = 5000

# print(employees_df)
#--------------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Add a new column named "Region".
# Set its value to "Kolkata" for every row.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")
# sales_df["Region"] = "Kolkata"
# print(sales_df)
#_____________________________________________________________________________________________________

#=================================
# Topic 2: Modify Existing Column
#=================================

# Ab seekhenge ki kisi existing column ki values ko kaise change karte hain.

# Maan lo products_df mein Price column hai:

# ProductName	Price
# Laptop	45000
# Mouse	600
# Keyboard	1200

# Agar tum sabhi products ki price ko 10% increase karna chahte ho, toh:

# products_df["Price"] = products_df["Price"] * 1.10

# print(products_df)
# Samjho kaise kaam karta hai
# products_df["Price"] existing Price column ko select karta hai.
# * 1.10 har price ko 1.10 se multiply karta hai, yani 10% increase.
# = updated values ko wapas Price column mein store karta hai.

# Example: 1000 ki price badhkar 1100 ho jayegi.

# Important: Is operation se original DataFrame ke Price column ki values modify ho jaati hain.

# Practice Questions — Modify Existing Column
# Pandas — Modify Existing Column Practice
# ==========================================
# Pandas — Modify Existing Column Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Increase every product's Price by 20%.
# Update the existing Price column.

# import pandas as pd
# products_df = pd.read_csv("products.csv")

# products_df["Price"] = products_df["Price"] * 1.20
# print(products_df)
#------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Increase every employee's Salary by 3000.
# Update the existing Salary column.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")

# employees_df["Salary"] = employees_df["Salary"] +  3000
# print(employees_df)
#-----------------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Double the Quantity of every sale.
# Update the existing Quantity column.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# sales_df["Quantity"] =sales_df["Quantity"] * 2

# print(sales_df)
#_____________________________________________________________________________________________________

#==============================================
# topic 3: Create Column from Existing Columns
#==============================================

# Ab hum seekhenge ki existing columns ka use karke naya column kaise banate hain.

# Maan lo sales_df mein Quantity aur Amount columns hain:

# Product	Quantity	Amount
# Laptop	2	80000
# Mouse	5	2500

# Agar humein ek naya column AveragePrice banana ho, jismein Amount ko Quantity se divide kiya jaye:

# sales_df["AveragePrice"] = sales_df["Amount"] / sales_df["Quantity"]

# print(sales_df)

# Yahan:

# Amount total sale amount hai.
# Quantity sold units ki sankhya hai.
# AveragePrice har unit ka average amount calculate karta hai.

# Example: Laptop ke liye ₹80,000 ÷ 2 = ₹40,000 per unit.

# Difference yaad rakho:

# Modify Existing Column → purane column ki values change hoti hain.
# Create Column from Existing Columns → existing columns se naya column banta hai.
# Practice Questions — Create Column from Existing Columns
# Pandas — Create Column from Existing Columns Practice
# ==========================================
# Pandas — Create Column from Existing Columns
# ==========================================

# Q1. Read "products.csv" into products_df.
# Create a new column named "TotalValue".
# Calculate it using Price multiplied by Stock.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# products_df["TotalValue"] = products_df["Price"] * products_df["Stock"]
# print(products_df)
#--------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Create a new column named "AnnualSalary".
# Calculate it using Salary multiplied by 12.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# employees_df["AnnualSalary"] = employees_df["Salary"] * 12
# print(employees_df)
#----------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Create a new column named "AverageAmount".
# Calculate it by dividing Amount by Quantity.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# sales_df["AverageAmount"] = sales_df["Amount"] / sales_df["Quantity"]
# print(sales_df)
#_____________________________________________________________________________________________________

#==============================
# topic 4: Rename Columns
#==============================

# Kabhi-kabhi dataset mein column names bade ya confusing hote hain. 
# Pandas mein hum rename() se unka naam change kar sakte hain.

# Maan lo DataFrame mein ye columns hain:

# ProductName	Price	Stock
# Laptop	45000	12
# Mouse	600	40

# Agar ProductName ko Product karna hai:

# products_df = products_df.rename(
#     columns={"ProductName": "Product"}
# )

# print(products_df)
# Samjho kaise kaam karta hai
# rename() column ya index ke labels change karne ke liye use hota hai.
# columns= batata hai ki hum column names rename kar rahe hain.
# Dictionary mein "old_name": "new_name" likhte hain.
# Yahan ProductName ka naam Product ho jayega; baaki columns waise hi rahenge.

# Dhyan do: rename() by default naya DataFrame return karta hai. 
# Isliye humne result ko wapas products_df mein store kiya hai.

# Practice Questions — Rename Columns
# Pandas — Rename Columns Practice
# ==========================================
# Pandas — Rename Columns Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Rename the "ProductName" column to "Product".

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# products_df = products_df.rename(
#     columns= {"ProductName": "Product"}
# )
# print(products_df)
#----------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Rename the "Employee" column to "EmployeeName".

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# employees_df = employees_df.rename(
#     columns= {"Employee": "EmployeeName"}
# )
# print(employees_df)
#-----------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Rename the "Amount" column to "SalesAmount".

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# sales_df =sales_df.rename(
#     columns={"Amount": "SalesAmount" }
# )
# print(sales_df)
#_____________________________________________________________________________________________________

#==============================
# topic 5: Rename Index
#==============================

# 1. Index kya hota hai?

# DataFrame mein har row ka ek index label hota hai. By default, ye 0, 1, 2, 3... hota hai.

# Example:

# Index	Employee	Salary
# 0	Amit	25000
# 1	Neha	32000
# 2	Rahul	28000

# Hum rename() ke index parameter se index labels change kar sakte hain.

# 2. Index rename karna
# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# employees_df = employees_df.rename(
#     index={0: "First", 1: "Second"}
# )

# print(employees_df)

# Is example mein:

# Index 0 ka label "First" ho jayega.
# Index 1 ka label "Second" ho jayega.
# Baaki index labels unchanged rahenge.

# Important difference:

# columns={...} → column names change karta hai.
# index={...} → row index labels change karta hai.

# Practice Questions — Rename Index

# Pandas — Rename Index Practice
# ==========================================
# Pandas — Rename Index Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Rename index 0 to "First" and index 1 to "Second".

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# employees_df = employees_df.rename(
#     index = {0: "First", 1: "Second"}
# )
# print(employees_df)
#--------------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Rename index 0 to "FirstSale" and index 1 to "SecondSale".

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# sales_df = sales_df.rename(
#     index= {0: "FirstSale", 1: "SecondSale"}
# )
# print(sales_df)
#----------------------------------------------------------

# Q3. Read "products.csv" into products_df.
# Rename index 0 to "FirstProduct" and index 2 to "ThirdProduct".

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# products_df = products_df.rename(
#     index= {0: "FirstProduct", 2: "ThirdProduct"}
# )
# print(products_df)
#_____________________________________________________________________________________________________

#==============================
# 
#==============================