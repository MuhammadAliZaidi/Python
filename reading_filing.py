# in this code with (with keyword) we don't need to close the file
# at the end
string=input("What's your name? ")
with open("string.txt",'a') as file:
    file.write(f"{string} \n")

# Now reading from the file
with open('string.txt','r') as file:
    lines=file.readlines()
for line in lines:
    print("Hello, ",line.rstrip())
