#IMPLEMENTATION OF JK FLIP FLOP USING BASIC LOGIC GATES IN PYTHON

#Basic Gates
def NOT(A):
    return ~A+2
def OR(A,B):
    return A|B
def AND(A,B):
    return A&B
#Take Input
J = int(input('Value for J : '))
K = int(input('Value for K : '))
Qp = int(input('Value for Qp(Previous o/p) : '))
#Calculate Qn=J Qp' + K' Qp
Qn=OR(AND(J,NOT(Qp)),AND(NOT(K),Qp))
#Print Output (Next State)
print()
print('Output Qn : ',Qn)
#Print State
if J==0 and K==0 :
    print('Hold State')
elif J==0 and K==1 :
    print('Reset State')
elif J==1 and K==0 :
    print('Set State')
elif J==1 and K==1 :
    print('Toggle State')
