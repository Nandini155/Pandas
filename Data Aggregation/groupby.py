#sing groupby() for Data Aggregation: Demonstrate how to calculate the average sales per category for a given dataset using the groupby() function in Pandas?

import pandas as pd

# Creating a DataFrame with sales data
data = {
    'category': ['Electronics', 'Clothing', 'Electronics', 'Toys', 'Clothing', 'Toys'],
    'sales': [400, 150, 300, 100, 200, 150]
}

df = pd.DataFrame(data)
df_grouped= df.groupby("category")["sales"].mean()
