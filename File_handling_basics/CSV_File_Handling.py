import csv

# Write data to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Sahil", 19, "Pune"])
    writer.writerow(["Sai", 21, "Delhi"])

# Read data from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("Student Details:")
    for row in reader:
        print(row)

# Output - 
# Student Details:
# ['Name', 'Age', 'City']
# ['Sahil', '19', 'Pune']
# ['Sai', '21', 'Delhi']