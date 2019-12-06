# Bring santa 50 stars to save christmas

# Fuel for a module = floor(mass/3) - 2
import math 

fuel = 0
with open("input.txt") as fp:
	line = fp.readline()
	while line:
		fuel += (math.floor(int(line)/3) - 2)
		line = fp.readline()

print("Fuel required is: {}".format(fuel))