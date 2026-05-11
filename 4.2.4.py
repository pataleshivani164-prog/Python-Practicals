import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code


# Output the most frequent product pairs
grouped = df.groupby('Date')['Product'].apply(list)
# Create list of product combinations
product_combinations = []
for products in grouped:
    product_combinations.extend(combinations(sorted(set(products)), 2))

# Count the frequency of each product pair
combinations_count = Counter(product_combinations)

# Find the most frequently sold product pair(s)
max_count = combinations_count.most_common(1)[0][1]

# Output the most frequent product pair(s)
for combo, count in combinations_count.items():
    if count == max_count:
        print(f"{combo[0]} and {combo[1]}: {count} times")
