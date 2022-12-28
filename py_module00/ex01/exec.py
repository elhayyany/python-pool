import sys

for n in range(len(sys.argv) - 1, 0, -1):
    print("".join(c.upper() if c.islower() else c.lower() for c in str(sys.argv[n])[::-1]), end=" ")
print()



# l = "kkk;lll;ooo"
# l.split(';')
# print(len(l))