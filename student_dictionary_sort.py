# Create an empty list to store student dictionaries
students = []

# Open the CSV file
with open("students.csv") as file:
    # Read file line by line
    for line in file:
        # Split each line into name and house
        name, house = line.rstrip().split(",")

        # Create a dictionary for each student
        student = {"name": name, "house": house}

        # Add dictionary to the list
        students.append(student)


# Function used for sorting by house
def get_house(student):
    return student["house"]


# Sort students by house and print them
for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")
