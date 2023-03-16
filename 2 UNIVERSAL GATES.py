#IMPLEMENTATION OF UNIVERSAL LOGIC GATES IN PYTHON

#NAND GATE -> NOT GATE + AND GATE
def NAND(A,B):
	return ~(A&B)+2
print()
print("Output of 0 NAND 0 is", NAND(0, 0))
print("Output of 0 NAND 1 is", NAND(0, 1))
print("Output of 1 NAND 0 is", NAND(1, 0))
print("Output of 1 NAND 1 is", NAND(1, 1))

#NOR GATE -> NOT GATE + OR GATE
def NOR(A,B):
	return ~(A|B)+2
print()
print("Output of 0 NOR 0 is", NOR(0, 0))
print("Output of 0 NOR 1 is", NOR(0, 1))
print("Output of 1 NOR 0 is", NOR(1, 0))
print("Output of 1 NOR 1 is", NOR(1, 1))
