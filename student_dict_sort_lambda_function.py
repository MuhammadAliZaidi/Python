# Create an empty list to store student dictionaries
students = []

# Open the CSV file
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        # Create dictionary for each student
        student = {"name": name, "house": house}

        # Add dictionary to list
        students.append(student)

# Sort using lambda function
for student in sorted(students, key=lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']}")
