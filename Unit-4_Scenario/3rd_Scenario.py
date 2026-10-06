#3. Mobile Price Analysis System
import numpy as np
import pandas as pd

# Create NumPy array of mobile prices
prices = np.array([15000, 22000, 35000, 28000, 45000, 18000, 32000])

# Calculate price statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create Pandas DataFrame
mobiles = pd.DataFrame({
    "Mobile Price": prices
})

print("\nMobile Data:")
print(mobiles)

# Display mobiles costing more than 30000
print("\nMobiles costing more than ₹30,000:")
print(mobiles[mobiles["Mobile Price"] > 30000])


'''
Output

Mean Price: 27857.14285714286
Median Price: 28000.0
Maximum Price: 45000
Minimum Price: 15000

Mobile Data:
   Mobile Price
0         15000
1         22000
2         35000
3         28000
4         45000
5         18000
6         32000

Mobiles costing more than ₹30,000:
   Mobile Price
2         35000
4         45000
6         32000
'''