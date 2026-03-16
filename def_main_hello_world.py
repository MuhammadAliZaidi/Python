def main():
    hello()
    name=input("What's your name? ")
    hello(name)
def hello(to="World"):
    print("Hello, ",to)
    
main()
