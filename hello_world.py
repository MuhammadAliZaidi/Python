# Ask the user to enter their name and store it in the variable 'name'
name = input("What's ur name? ")

# Print Hello and the name by joining the strings using +
# Note: this will not add a space automatically
print("Hello," + name)

# Print Hello and the name using a comma
# Python automatically adds a space between them
print("Hello,", name)

# Print "Hello," only
print("Hello,")

# Print the name on the next line
print(name)

# Print "Hello," but do not move to the next line
# end="" removes the default newline
print("Hello,", end="")

# This will print the name on the same line
print(name)

# This prints the text exactly as written
# The variable name will NOT be replaced
print("Hello, {name}")

# This is an f-string (formatted string)
# Python replaces {name} with the value stored in the variable
print(f"Hello, {name}")

# Remove extra whitespace (spaces before and after the name)
name = name.strip()

# Capitalizing only first letter
name= name.capitalize()
print(f"Hello, {name}")


#Capitalizing first letter of every word
name= name.title()

print(f"Hello, {name}")
