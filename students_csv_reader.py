# Create an empty list to store student messages
students = []

# Open the CSV file in read mode
with open("students.csv") as file:
    # Read the file line by line
    for line in file:
        # Remove newline and split by comma
        row = line.rstrip().split(",")

        # Print directly using list indexing
        print(f"{row[0]} is in {row[1]} house")

        # Another way: unpack values into variables
        name, house = line.rstrip().split(",")

        # Add formatted string to the students list
        students.append(f"{name} is in {house}'s house")

# Sort the list alphabetically and print each entry
for student in sorted(students):
    print(student)
