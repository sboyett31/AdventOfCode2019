# Day 3 part 1
# Wire 1 will have a list of tuples that contains the points it occupies
# Wire 2 will create a list of tuples that contains the points it intersects with Wire 1
# List of intersections will be looped over to find the shortest manhattan distance from center

def main():
	path1, path2 = get_paths()
	intersections = get_intersections(path1, path2)
	print("Intersections are: {}".format(intersections))
	min_dist = get_minimum_distance(intersections)

def get_minimum_distance(intersections):
	min_dist = float('inf')
	for xy in intersections:
		dist = abs(xy[0]) + abs(xy[1])
		min_dist = dist if dist < min_dist else min_dist

def get_intersections(path1, path2):
	wire1 = []
	rc = []
	xy = (0,0)
	for instr in path1:
		print("instr is: {}".format(instr))
		for _ in range(0,int(instr[1:])-1):
			wire1.append(xy)
			xy = update_xy(xy,instr[:1])
	xy = (0,0)
	for instr in path2:
		print("instr2 is: {}".format(instr))
		for _ in range(0, int(instr[1:])-1):
			if xy in wire1 and xy != (0,0):
				print("Intersection found! ({})".format(xy))
				rc.append(xy)
			xy = update_xy(xy,instr[:1])
	return rc

def get_paths():
	# Return wire paths 
	with open("input.txt", "r") as fp:
		return fp.readline().split(','), fp.readline().split(',')

def update_xy(xy, direction):
	#Move current position of wire
	if direction == 'U':
		return (xy[0], xy[1]+1)
	elif direction == 'D':
		return (xy[0], xy[1]-1)
	elif direction == 'R':
		return (xy[0]+1, xy[1])
	else:
		return (xy[0]-1, xy[1])

if __name__ == "__main__":
	main()