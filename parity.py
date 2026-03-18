def main():
    x = int(input("Enter the value of x : "))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    # Method 1: Full if-else (basic and very clear)
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # Method 2: Short (ternary operator)
    # return True if n % 2 == 0 else False

    # Method 3: Most succinct (Pythonic way)
    return n % 2 == 0

main()
