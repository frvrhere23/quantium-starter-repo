import pandas as pd # Import the pandas library, which is like a super-powered Excel for Python
import glob # Import glob to help us find all the files in a folder

# --- STEP 1: Find and Load the Data ---
# We use glob to find all files in the 'data' folder that end with '.csv'
# It's like telling the computer: "Go to the 'data' room and grab every piece of paper with '.csv' on it."
data_files = glob.glob("data/*.csv")

# We create an empty list to store the data from each file
dataframes = []

# Now we loop through each file we found
for file in data_files:
    # pd.read_csv reads the file and turns it into a 'DataFrame' (think of it as a virtual spreadsheet)
    df = pd.read_csv(file)
    # Put this spreadsheet into our list
    dataframes.append(df)

# We combine all our spreadsheets into one big giant spreadsheet!
# 'pd.concat' is like taping all the papers together into one long scroll.
combined_df = pd.concat(dataframes, ignore_index=True)

# --- STEP 2: Filter for Pink Morsels ---
# Soul Foods only cares about 'Pink Morsels'. 
# This line says: "Keep only the rows where the product name is EXACTLY 'pink morsel'."
# It's like filtering a list to only show your favorite candy.
pink_morsels_only = combined_df[combined_df['product'] == 'pink morsel'].copy()

# --- STEP 3: Clean and Calculate Sales ---
# The price looks like '$3.00', which is text. We need to turn it into a number.
# .str.replace('$', '') removes the dollar sign.
# .astype(float) tells the computer: "Treat this as a decimal number."
pink_morsels_only['price'] = pink_morsels_only['price'].str.replace('$', '', regex=False).astype(float)

# Now we calculate total sales for each row.
# 'Sales' = 'Price' of one candy multiplied by the 'Quantity' (how many were sold).
# It's like saying: "If 1 candy costs $3 and I sell 2, I made $6!"
pink_morsels_only['sales'] = pink_morsels_only['price'] * pink_morsels_only['quantity']

# --- STEP 4: Format the Final Output ---
# We only want three columns: Sales, Date, and Region.
# We pick them out from our big spreadsheet.
final_output = pink_morsels_only[['sales', 'date', 'region']]

# We need to rename the columns to match what Soul Foods asked for (Capitalized names)
# 'sales' becomes 'Sales', 'date' becomes 'Date', and 'region' becomes 'Region'
final_output = final_output.rename(columns={
    'sales': 'Sales',
    'date': 'Date',
    'region': 'Region'
})

# --- STEP 5: Save the Result ---
# We save our clean, combined data into a new file called 'formatted_data.csv'.
# 'index=False' means we don't want to add extra row numbers to the file.
final_output.to_csv("formatted_data.csv", index=False)

# Print a happy message to let us know it worked!
print("Success! The data has been cleaned and saved to 'formatted_data.csv'.")
