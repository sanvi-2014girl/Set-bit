def setOrNot(number, n):
    if number & (1 << (n-1)):
        print("\nSet")
    else:
        print("\nNot SET")
number = int(input("Enter number: "))
n = int(input("enter bit number: "))
setOrNot(number, n)