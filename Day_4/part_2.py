# Day 4 Part 1

# Six-digit number
# Value is within the range vien in puzzle input
# Two adjacent digits are the same like 22 in 122345 but three or more are not
# Going from left to right, the digits never decrease

START = 153512 
END   = 630395	
				
def main():
	ans = 0
	for i in range(START, END):
		if isIncr(i):
			if isValidDbl(i):
				ans = ans + 1
	print("Answer is: {}".format(ans))

def isValidDbl(val):
	i = 0
	count = 0
	length = len(str(val))
	while i < length:
		current = str(val)[i]
		i = i + 1
		if (i == length):
			return False
		while current == str(val)[i]:
			count = count + 1
			i = i + 1
			if (i == length):
				return True if (count == 1) else False
		if count == 1:
			return True
		count = 0
	return False

def isIncr(val):
	last = -1
	for digit in str(val):
		if int(digit) < last:
			return False
		last = int(digit)
	return True


if __name__ == "__main__":
	main()