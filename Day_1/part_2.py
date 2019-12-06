#Day 2 -- Part 2
import math 

#Fuel itself now requires fuel - take its mass , divide by three, rownd down and sub 2

fuel_req = 0
with open("input.txt") as fp:
	mass = fp.readline()
	while mass:
		fuel = (math.floor(int(mass)/3) - 2)
		while fuel > 0:
			fuel_req += fuel
			fuel = (math.floor(int(fuel)/3) - 2)
		mass = fp.readline()

print("Fuel requirement is: {}".format(fuel_req))