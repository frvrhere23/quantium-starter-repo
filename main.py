import pandas as pd # 1. Bring in the Pandas robot and call it 'pd' for short.

# 2. Tell the robot where the data file is. 
# We are looking in the 'data' folder for a file named 'daily_sales_data_0.csv'.
# The dot '.' at the start means "start from where we are right now".
file_path = "./data/daily_sales_data_0.csv" 

# 3. Ask the robot to read the file. 
# It reads the file and turns it into a 'DataFrame', which is like a super-powered table.
# Think of 'df' as our "Data Folder" for our table.
df = pd.read_csv(file_path)

# 4. Show the first 5 rows of the table so we can see what's inside!
# 'df.head()' is like saying "Hey robot, show me the 'head' (the top) of the table."
print("--- First 5 rows of our sales data ---")
print(df.head())

# 5. Show some basic info about the data (how many rows, columns, etc.)
# 'df.info()' gives us a summary, like the ingredients on a cereal box!
print("\n--- Basic Info about the data ---")
print(df.info())
