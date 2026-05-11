import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
city_wise_sell = df.groupby('City')['Quantity'].sum().reset_index()
best_city = city_wise_sell.loc[city_wise_sell['Quantity'].idxmax()]
"""
# write the code..

# Display the result
print(f"City sold the most products: {best_city}")
"""
print(f"City sold the most products: {best_city['City']}")4.
