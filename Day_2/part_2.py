# Day 2 Part 2

# Find inputs into "computer system" that result in the output 19690720

# First input (a[1]) = noun
# Second input (a[2]) = verb
# Answer is 100*noun + verb
TARGET = 19690720
def main():
	n, v = find_inputs(TARGET)
	ans = 100*n + v
	print("Answer is: {}".format(ans))

def find_inputs(TARGET): 
	for n in range(0, 99):
		for v in range(0, 99):
			a = [int(_) for _ in open("input.txt", "r").read().split(',')]
			a[1] = n
			a[2] = v
			for x in range(0, len(a)-1, 4):
				a[a[x+3]] = a[a[x+1]] + a[a[x+2]] if a[x]==1 else a[a[x+1]]*a[a[x+2]]

			if a[0] == TARGET:
				return n, v

if __name__ == "__main__":
	main()