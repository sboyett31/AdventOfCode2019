# Day 4 Part 1

# Six-digit number
# Value is within the range vien in puzzle input
# Two adjacent digits are the same like 22 in 122345
# Going from left to right, the digits never decrease

START = 153512 
END   = 630395	
				
def main():
	count = 0
	for i in range(START, END):
		if isValid(i):
			count = count + 1
	print("Number of valid passwords is: {}".format(count))

def isValid(val):
	last = -1
	double = False
	for digit in str(val):
		if int(digit) < last:
			return False
		if int(digit) == last:
			double = True
		last = int(digit)
	return True if double else False

if __name__ == "__main__":
	main()