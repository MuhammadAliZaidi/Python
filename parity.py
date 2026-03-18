def main():
    x=int(input("Enter the value of x : "))
    if is_even(x):
        print('Even')
    else:
        print('Odd')
def is_even(n):
   # if n%2==0:
    #    return True
    # else:
      #  return False
    return True if n%2==0 else False
main()
