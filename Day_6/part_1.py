# Day 6 part 1

orbits = {}
total_orbits = 0

with open("input.txt", "r") as fp:
	# p1)p2
	orbit = fp.readline()
	while orbit:
		p1 = orbit.split(")")[0].replace("\n", "")
		p2 = orbit.split(")")[1].replace("\n", "")
		if p2 not in orbits.keys():
			orbits[p2] = p1
		orbit = fp.readline()

for planet in orbits.keys():
	p = planet
	while p in orbits.keys():
		total_orbits = total_orbits + 1
		p = orbits[p]
			 
print("Total sum of orbits is: {}".format(total_orbits))