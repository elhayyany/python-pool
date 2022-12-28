import sys


def is_it(c, l):
	count = 0
	for k in c:
		if  (k not in ('!#$%&()\'*+,.:;-?@[]^_`{|}~')):
			count += 1
	if count > l:
		return 0
	return 1
if (len(sys.argv) is not 3) or (str(sys.argv[2]).isdigit() is False):
	print("erorr")
	sys.exit(1)
strsplt = str(sys.argv[1]).split(' ')
print(strsplt)
ply = []
for c in strsplt:
	if is_it(c, int(sys.argv[2])):
		strsplt.remove(c)
		pass
	else:
		ply.append(c)
print(ply)
