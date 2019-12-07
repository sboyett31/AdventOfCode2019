class IntComputer:

	def __init__(self, data):
		self.mem = data
		self.PC = 0
		self.instr = 0
		self.opCode = 0
		self.instr_type = "none"
		self.op1 = 0
		self.op2 = 0
		self.op3 = 0


	def run(self): 
		while (self.PC != -1):
			self.IF()	#instruction fetch
			self.ID()	#instruction decode
			self.EX()   #instruction execute

	def IF(self):
		# fetches current instruction and updates program counter
		self.opCode = self.mem[self.PC]

	def ID(self):
		if (self.opCode == 99):
			self.instr = "exit"
			self.PC = -1
		else:
			l = len(str(self.opCode))
			opCode = [int(_) for _ in str(self.opCode)]

			# Get instruction/instruction type
			if opCode[l-1] == 1:
				self.instr = "add"
				self.instr_type  = "3R"
			elif opCode[l-1] == 2:
				self.instr = "mul"
				self.instr_type  = "3R"
			elif opCode[l-1] == 3:
				self.instr = "input"
				self.instr_type  = "I"
			elif opCode[l-1] == 4:
				self.instr = "output"
				self.instr_type  = "1R"
			elif opCode[l-1] == 5:
				self.instr = "jt"
				self.instr_type  = "J"
			elif opCode[l-1] == 6:
				self.instr = "jf"
				self.instr_type  = "J"
			elif opCode[l-1] == 7:
				self.instr = "lt"
				self.instr_type = "3R"
			elif opCode[l-1] == 8:
				self.instr = "eq"
				self.instr_type = "3R"

			# Get Parameter Modes
			if l == 5:
				mode = [opCode[0], opCode[1], opCode[2]]
			elif l == 4:
				mode = [0, opCode[0], opCode[1]]
			elif l == 3:
				mode = [0, 0, opCode[0]]
			else:
				mode = [0, 0, 0]

			# Get Parameters
			if self.instr_type == "3R":
				self.op1 = self.mem[self.mem[self.PC+1]] if mode[2] == 0 else self.mem[self.PC+1]
				self.op2 = self.mem[self.mem[self.PC+2]] if mode[1] == 0 else self.mem[self.PC+2]
				self.op3 = self.mem[self.PC+3] #storing value, always positional

			elif self.instr_type == "I":
				self.op1 = self.mem[self.PC+1]  # storing value, always postiional

			elif self.instr_type == "1R":
				self.op1 = self.mem[self.mem[self.PC+1]] if mode[2] == 0 else self.mem[self.PC+1]

			elif self.instr_type == "J":
				self.op1 = self.mem[self.mem[self.PC+1]] if mode[2] == 0 else self.mem[self.PC+1]
				self.op2 = self.mem[self.mem[self.PC+2]] if mode[1] == 0 else self.mem[self.PC+2]


	def EX(self):
		self.op1 = int(self.op1)
		self.op2 = int(self.op2)
		self.op3 = int(self.op3)

		if self.instr == "input":
			user_in = input("Please provide input: ")
			self.mem[self.op1] = int(user_in)
			self.PC = self.PC + 2
		elif self.instr == "output":
			print("Test output: {}".format(self.op1))
			self.PC = self.PC + 2
		elif self.instr == "add":
			self.mem[self.op3] = self.op1 + self.op2
			self.PC = self.PC + 4
		elif self.instr == "mul":
			self.mem[self.op3] = self.op1 * self.op2
			self.PC = self.PC + 4
		elif self.instr == "jt":
			self.PC = self.op2 if self.op1 != 0 else self.PC+3
		elif self.instr == "jf":
			self.PC = self.op2 if self.op1 == 0 else self.PC+3
		elif self.instr == "lt":
			self.mem[self.op3] = 1 if (self.op1 < self.op2) else 0
			self.PC = self.PC + 4
		elif self.instr == "eq":
			self.mem[self.op3] = 1 if (self.op1 == self.op2) else 0
			self.PC = self.PC + 4