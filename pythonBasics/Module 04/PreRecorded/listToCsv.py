import csv
""" 
data = [
    ["Name", "Salary", "Designation", "Department", "Location"],
    ["Alice", 70000, "Software Engineer", "IT", "New York"],
    ["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
    ["Charlie", 60000, "System Administrator", "IT", "New Heaven"],
    ["Al Hasan", 98000, "Product Manager", "Product", "New Heaven"]
]


with open("hello.csv", "w", newline='') as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)
    print("Successful...")
"""
data = []
with open("hello.csv", "r") as file:
    content = csv.reader(file)
    for row in content:
        data.append(row)
print(data)