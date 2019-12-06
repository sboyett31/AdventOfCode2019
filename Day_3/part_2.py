# Day 3 part 2
# Wire 1 will have a list of tuples that contains the points it occupies
# Wire 2 will create a list of tuples that contains the points it intersects with Wire 1
# List of intersections will be looped over to find the shortest steps
import time 
def main():
	path1, path2 = get_paths()
	intersections = get_intersections(path1, path2)
	point, min_steps = get_min_steps(intersections)
	print("Point with min steps: {}, steps: {}".format(point, min_steps))

def get_min_steps(intersections):
	min_step = float('inf')
	for i in intersections:
		if i[1] < min_step:
			point = i[0]
			min_step = i[1]
	return point, min_step		


def get_intersections(path1, path2):
	wire1 = {}
	rc = []
	xy = (0,0)
	steps = 0
	for instr in path1:
		for _ in range(0,int(instr[1:])):
			if xy not in wire1.keys():
				wire1[xy] = steps
			xy = update_xy(xy,instr[:1])
			steps = steps + 1
	xy = (0,0)
	steps = -1
	for instr in path2:
		for _ in range(0, int(instr[1:])):
			steps = steps + 1
			if xy in wire1.keys() and xy != (0,0):
				rc.append((xy,steps+wire1[xy]))
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