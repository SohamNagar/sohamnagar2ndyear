import csv

# Open the CSV file
file_name = "data.csv"
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    row_count = 0

    # Count rows
    for row in reader:
        row_count += 1

print("Total number of rows in the CSV file:", row_count)
