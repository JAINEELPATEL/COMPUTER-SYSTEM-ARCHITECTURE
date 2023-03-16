#IMPLEMENTATION OF SPECIAL PURPOSE GATES IN PYTHON

#XOR
def XOR(A, B):
	return A ^ B
print()
print("Output of 0 XOR 0 is", XOR(0, 0))
print("Output of 0 XOR 1 is", XOR(0, 1))
print("Output of 1 XOR 0 is", XOR(1, 0))
print("Output of 1 XOR 1 is", XOR(1, 1))

#XNOR
def XNOR(A, B):
	return ~(A ^ B)+2
print()
print("Output of 0 XNOR 0 is", XNOR(0, 0))
print("Output of 0 XNOR 1 is", XNOR(0, 1))
print("Output of 1 XNOR 0 is", XNOR(1, 0))
print("Output of 1 XNOR 1 is", XNOR(1, 1))
