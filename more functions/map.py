"""
Problem Description
You have a dataset of employee records, and each employee's role is labeled as "Manager", "Developer", or "Intern". Your task is to adjust their base salary according to their role with the following criteria:

"Manager" should receive a 20% increase.
"Developer" should receive a 10% increase.
"Intern" receives no increase.
"""

#Create a function that takes the role and base salary as inputs and returns the new salary after applying the appropriate increase. 
#Use .map() to apply this function across the DataFrame to update the salaries

import pandas as pd

# Creating a DataFrame with employee data
data = {
    'employee_id': [101, 102, 103, 104, 105],
    'role': ['Developer', 'Manager', 'Intern', 'Developer', 'Manager'],
    'base_salary': [50000, 60000, 30000, 50000, 65000]
}

df_employees = pd.DataFrame(data)

# Mapping roles to their respective salary increases
salary_adjustments = {
    'Manager': 1.20,  # 20% increase
    'Developer': 1.10,  # 10% increase
    'Intern': 1.00  # No increase
}

# Create a multiplier column based on role
df_employees['multiplier'] = df_employees['role'].map(salary_adjustments)

# Calculate the adjusted salary
df_employees['adjusted_salary'] = df_employees['base_salary'] * df_employees['multiplier']

# Display the result
print(df_employees)
