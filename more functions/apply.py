#problem statement

#use the .apply() method to convert all the sales numbers in the dataset to another currency, assuming an exchange rate of 1 USD to 0.9 EUR? 
import pandas as pd

# Creating a DataFrame with sales data
data = {
    'category': ['Electronics', 'Clothing', 'Electronics', 'Toys', 'Clothing', 'Toys'],
    'sales': [400, 150, 300, 100, 200, 150]
}

df = pd.DataFrame(data)

df["sales"] = df["sales"].apply(lambda x: x * 0.9)

#--------------------------------------------------------------------
#Example 2
import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
# Add 5 to each age
df['Age'] = df['Age'].apply(lambda x: x + 5)
print(df)

#-------------------------------------------------
# Example 3
import pandas as pd
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [10, 20, 30, 40]
})
# Group and apply aggregation
result = df.groupby('Category')['Values'].apply(lambda x: x.sum())
print(result)

