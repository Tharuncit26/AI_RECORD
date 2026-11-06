# Pandas Series and DataFrame

import pandas as pd

marks = pd.Series([76, 89, 92, 81, 95],
                  index=["A", "B", "C", "D", "E"])

print("--- Pandas Series ---")
print(marks)

data = {
    "RollNo": [201, 202, 203, 204, 205],
    "Name": ["Arun", "Bharath", "Deepa", "Kavya", "Manoj"],
    "Department": ["ECE", "CSE", "IT", "CSE", "ECE"],
    "Mark": [76, 89, 92, 81, 95]
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
