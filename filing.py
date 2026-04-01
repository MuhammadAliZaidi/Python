names=[]
for _ in range(3):
    names.append(input("What's your name? "))
    
for name in sorted(names):
    print(f"Hello, {name}")
# we have written this code but unfortunately we don't saved the names for saving the 
# name we would use filing
string=input("What's your name? ")
file=open("string.txt",'a')
file.write(f"{string} \n")
file.close()
