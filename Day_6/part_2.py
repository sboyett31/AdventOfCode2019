# Day 6 part 2

orbits = {}
path1 = []
path2 = []
transfers = 0
with open("input.txt", "r") as fp:
	# p1)p2
	orbit = fp.readline()
	while orbit:
		p1 = orbit.split(")")[0].replace("\n", "")
		p2 = orbit.split(")")[1].replace("\n", "")
		if p2 not in orbits.keys():
			orbits[p2] = p1
		orbit = fp.readline()

obj1 = orbits['YOU']
obj2 = orbits['SAN']

planet = obj1

while planet in orbits.keys():
	path1.append(planet)  # save path of object 1 to base orbit
	planet = orbits[planet]

planet = obj2
while planet in orbits.keys():
	if planet in path1:
		match = planet
		break;
	planet = orbits[planet]
	transfers = transfers + 1

transfers = transfers + path1.index(match)

print("total transfers: {}".format(transfers))

