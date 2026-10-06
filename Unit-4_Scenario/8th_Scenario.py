# 8. Grocery Store Analysis System

import numpy as np
import pandas as pd

# Create NumPy arrays
prices = np.array([50, 120, 80, 200, 150, 90])
quantity = np.array([15, 8, 5, 12, 7, 9])

# Calculate price statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create Pandas DataFrame
grocery = pd.DataFrame({
    "Product Price": prices,
    "Quantity": quantity
})

print("\nGrocery Data:")
print(grocery)

# Display items having quantity less than 10
print("\nItems with quantity less than 10:")
print(grocery[grocery["Quantity"] < 10])


'''
Output

Mean Price: 115.0
Median Price: 105.0
Maximum Price: 200
Minimum Price: 50

Grocery Data:
   Product Price  Quantity
0             50        15
1            120         8
2             80         5
3            200        12
4            150         7
5             90         9

Items with quantity less than 10:
   Product Price  Quantity
1            120         8
2             80         5
4            150         7
5             90         9
'''