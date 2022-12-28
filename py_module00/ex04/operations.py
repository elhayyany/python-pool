import sys


if len(sys.argv) == 3:
    if str(sys.argv[1]).isdigit() and str(sys.argv[2]).isdigit():
        print("Sum: "+ str(int(sys.argv[1]) + int(sys.argv[2])))
        print("difference: "+ str(int(sys.argv[1]) - int(sys.argv[2])))
        print("Product: "+ str(int(sys.argv[1]) * int(sys.argv[2])))
        if int(sys.argv[2]) is not 0:
            print("Quotient: "+ str(int(sys.argv[1]) / int(sys.argv[2])))
            print("Remainder: "+ str(int(sys.argv[1]) % int(sys.argv[2])))
        else:
            print("Quotient:   ERROR (division by zero)\nRemainder:  ERROR (modulo by zero)")
    else:
        print("AssertionError: only integers")
elif len(sys.argv) != 1:
    print("AssertionError: too many arguments")
else:
    print("Usage: python operations.py <num1> <num2>")
    print("Example:\n\tpython operations 10 2")


