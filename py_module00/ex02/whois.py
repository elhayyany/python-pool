import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 2:
    try:
        int(sys.argv[1])
        if (int(sys.argv[1]) == 0):
            print("I'm Zero")
        elif (int(sys.argv[1]) % 2):
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError:
        print("AssertionError: argument is not an integer")


