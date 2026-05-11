import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df['Total_Sales'] = df['Quantity'] * df['Price']
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
total = df.groupby('Month')['Total_Sales'].sum()

# Find the month with the highest total sales
best_month =total.idxmax()
highest_sales =  total.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
