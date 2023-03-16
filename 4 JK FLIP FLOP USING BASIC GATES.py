#IMPLEMENTATION OF JK FLIP FLOP USING BASIC LOGIC GATES IN PYTHON

def NOT(A):
    return ~A+2
    
def OR(A,B):
    return A|B

def AND(A,B):
    return A&B

J = int(input('Value for j : '))
K = int(input('Value for k : '))
Qp = int(input('Value for Qp(Previous o/p) : '))

#Qn=J Qp' + K' Qp
Qn=OR(AND(J,NOT(Qp)),AND(NOT(K),Qp))

print('Output Qn : ',Qn)
