# Day 5 Part 1 & 2
# For Part 1 -> input '1'
# For Part 2 -> input '5'

from IntComputer import IntComputer

def main():
	computer = IntComputer([int(_) for _ in open("input.txt", "r").read().split(",")])	
	computer.run()

if __name__ == "__main__":
	main()