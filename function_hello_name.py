def hello():
    print("Hello, ")

name = input("What is your name? ")
hello()
print(name)
# passing name to the hello function
def hello2(name):
    print("Hello, ",name)
name2=input("Whats your name? ")
hello2(name2)
