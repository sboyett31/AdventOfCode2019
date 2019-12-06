#Day 2 Part 1

# list of integers seperated by commas (1,0,0,3,99)

# Look at first integer (position 0) Here is opcode (either 1, 2 or 99)

# 99 - Program is finished and should immediately halt 
# 1 - adds together numbers read from two positions and stores the result in third position
#   - Three integers immediately after the opcode tell you the three positions 
#   - First two indicate the positions whcih you should read the input values
#   - Third indicates the position at which the output should be stored.  
# 2 - Works exactly like opcode 1 except it performs multiplication


a = [int(_) for _ in open("input.txt", "r").read().split(",")]
a[1] = 12
a[2] = 2 
for x in range(0, len(a)-1, 4):
	a[a[x+3]] = a[a[x+1]] + a[a[x+2]] if a[x]==1 else a[a[x+1]]*a[a[x+2]]

print("a[0]: {}".format(a[0]))