# Ask user for a name to save
new_name = input("Enter a name: ")

# Open file in append mode to add the new name
# 'a' means append (adds to end, does not erase old data)
with open("names.txt", "a") as file:
    file.write(new_name + "\n")

# Create an empty list to store names
names = []

# Open file in read mode (default mode is 'r')
with open("names.txt") as file:
    # Read file line by line
    for line in file:
        # Remove newline character and store clean name
        names.append(line.rstrip())

# Sort names alphabetically and print greeting
for name in sorted(names):
    print(f"hello, {name}")
