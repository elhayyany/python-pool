import random
import sys

r1 = random.randint(0, 99)


print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType'exit'to end the game.\nGood luck!")
u = -1
num = 0
while True:
    print("What's your guess between 1 and 99?")
    j = input(">>")
    if not j.isdigit():
        if j is "exit":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("That's not a number")
    elif int(j) > 99 or int(j) < 0:
        print("jjlsb nxciu vmncxvdi hdj vdihvd ")
    else:
        if (int(j) > r1):
            print("too high")
        elif int(j) < r1:
            print("too low")
        else: break
    num += 1


if (r1 == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if num == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!You won in " + str(num) + " attempts!")


