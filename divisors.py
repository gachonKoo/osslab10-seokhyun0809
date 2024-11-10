import sys

number = int(sys.argv[1])

for i in range(1, number+1):
	if (number % i == 0) :      # loop between 1 and number
 		print(i, end=" ")   # check if remainder is 0

print()
