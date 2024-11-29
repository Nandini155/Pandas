#join(), concat(), and merge()

import pandas as pd

# Creating DataFrame df1
data1 = {'customer_id': [1, 2, 3, 4],
         'customer_name': ['Alice', 'Bob', 'Charlie', 'David']}
df1 = pd.DataFrame(data1).set_index('customer_id')


# Creating DataFrame df2
data2 = {'customer_id': [2, 4, 1, 5],
         'order_date': ['2021-06-05', '2021-07-15', '2021-08-01', '2021-08-02']}
df2 = pd.DataFrame(data2)


# Creating DataFrame df3
data3 = {'month': ['January', 'February', 'March'],
         'sales': [234, 456, 678]}
df3 = pd.DataFrame(data3)


##  Using join()
#Scenario: Combine customer information with their order dates based on customer IDs.
#Preparation: Since join() works on indices, let's set the index of df2 to customer_id

df2 = df2.set_index('customer_id')
joined_df = df1.join(df2)
print(joined_df)


# Using concat()
#Scenario: You need to add monthly sales data from a new month to an existing dataset.

# New month data
new_month = pd.DataFrame({'month': ['April'], 'sales': [789]})
concatenated_df = pd.concat([df3, new_month], axis=0)
print(concatenated_df)


#Using merge()
#Scenario: Merge customer names with their respective order dates using their customer ID, suitable for cases where not all customer IDs match.

merged_df = pd.merge(df1.reset_index(), df2, on='customer_id', how='inner')
print(merged_df)
