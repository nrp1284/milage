#
# A much better example which can handle any number of people and
# rows in the CSV file.
# 

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join(".","Resources", "mileage.csv")

# Create a dictionary to keep track of each person's miles
# and another one to keep track of the number of records per user.
names = []
mile_counts = {}
num_records = {}

# Open the CSV file. Any lines indented after this while statement
# have access to the CSV data from the file.
with open(file_to_load) as mile_data:

    # Create a new variabe "reader" which is used to access the CSV
    # data line by line.
    reader = csv.reader(mile_data)

    # Read the header, print it out, but we don't use it
    header = next(reader)
    print(header)

    # Use a for loop to loop through the remainder of the rows
    row_num = 0
    for row in reader:

        # Create variables that contain the name and miles in this row
        name = row[0]
        miles = float(row[2])

        # If this is the first time we have encountered this person's name
        # 1) Append it to the names list
        # 2) Create an entry for this person in the mile_counts dict
        # 3) Create an entry for this person in the num_records dict
        if name not in names:
            names.append(name)
            mile_counts[name] = 0.0
            num_records[name] = 0

        # In the 2 dicts update the values for this person
        mile_counts[name] = mile_counts[name] + miles
        num_records[name] = num_records[name] + 1

        # For debugging, print out the liost and dicts to view our progress
        row_num = row_num + 1
        print(f"\nRow {row_num}: {name}")
        print(f"names: {names}")
        print(f"mile_counts: {mile_counts}")
        print(f"num_records: {num_records}")

# We are now finished reading the rows of data from the CSV file.

print("\n********\nResults:")

# Keep track of the person with the best average
best_avg_name = ""
best_avg = 0.0

# Calculate and print the mile averages for each person
# Use a for loop.
for name,total_miles in mile_counts.items():
    # Calculate the average
    records_count = num_records[name]
    avg_miles = total_miles / records_count

    # If this person has the best average so far...
    if avg_miles > best_avg:
        best_avg = avg_miles
        best_avg_name = name

    # Print
    print(f"{name}'s average miles was: {avg_miles}")

print(f"Person with best average: {best_avg_name}")
    
print("********\n\n\n\n\n")
    