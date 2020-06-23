from enum import Enum
class Instr_type(Enum):
	ACCEPT = 0
	SPLIT  = 1
	MATCH  = 2
	JMP	   = 3
	END_WITHOUT_ACCEPTING = 4

class Instr:
	def __init__(self, pc, instr_type, data):
		self.pc   = pc
		self.type = instr_type
		self.data = data

	def set_pc(self,aPc):
		self.pc = aPc

	def set_data(self, aData):
		self.data = aData

	def __str__(self):
		return f"@ {self.pc} TYPE: {self.type} DATA: {self.data}"
	
	def dotty_str(self):
		return f"{id(self)} [label=\"unknown\" color=\"black\"  fillcolor=\"gray\"	style=\"filled\" ]\n"

	def code(self):
		assert self.data < 255
		return f"{self.type.value} ; {self.data}\n"

class Accept(Instr):
	def __init__(self, pc):
		super().__init__(pc, Instr_type.ACCEPT, 0)

	def dotty_str(self):
		return f"{self.pc} [label=\"{self.pc} : ✓\" color=\"black\"  fillcolor=\"#1ac0c6\"	style=\"filled\"]\n"


class Split(Instr):
	def __init__(self, pc, data):
		super().__init__(pc, Instr_type.SPLIT, data)

	def dotty_str(self):
		return 	(f"{self.pc} -> {self.data}\n" +
			   	 f"{self.pc} -> {self.pc+1}\n" +
        		 f"{self.pc} [color=\"black\" fillcolor=\"#dee0e6\" style=\"filled\"]\n")

class Match(Instr):
	def __init__(self,pc, char):
		super().__init__(pc, Instr_type.MATCH, char)
	
	def dotty_str(self):
		return (f"{self.pc} -> {self.pc+1}\n"+
				f"{self.pc} [label =\"{self.pc} : {self.data}\" color=\"black\" fillcolor=\"#ffa822\" style=\"filled\"]\n"             )

class Jmp(Instr):
	def __init__(self, pc, data):
		super().__init__(pc, Instr_type.JMP, data)
	
	def dotty_str(self):
		return (f"{self.pc} -> {self.data}\n"+
                f"{self.pc} [color=\"black\" fillcolor=\"#2792ce\" style=\"filled\"]\n")

class End(Instr):
	def __init__(self, pc):
		super().__init__(pc, Instr_type.END_WITHOUT_ACCEPTING, 0 )

	def dotty_str(self):
		return f"{self.pc} [label =\"{self.pc} : ✗\" color=\"black\" fillcolor=\"#ff6150\"	style=\"filled\"]\n"
