import re

# Ask the user to enter email and remove extra spaces
email = input("What's your email? ").strip()
# Check if @ and . are present in the email
if '@'in email and '.' in email:
    print("Valid")
else:
    print("Invalid")

# Split email into username and domain using @
username, domain = email.split('@')

# Check if username exists and domain ends with .com
if username and domain.endswith('.com'):
    print("Valid")
else:
    print("Invalid")

# Check email format using regular expression
if re.search('.+@.+', email):
    print("Valid")
else:
    print("Invalid")
