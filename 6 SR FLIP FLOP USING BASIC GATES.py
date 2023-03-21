#IMPLEMENTATION OF SR FLIP FLOP USING BASIC LOGIC GATES IN PYTHON

#Basic Gates
def NOT(A):
    return ~A+2
def OR(A,B):
    return A|B
def AND(A,B):
    return A&B
#Take Input
S = int(input('Value for S : '))
R = int(input('Value for R : '))
Qp = int(input('Value for Qp(Previous o/p) : '))
#Calculate Qn = S + R' Qp
Qn=OR(S,AND(NOT(R),Qp))
#Print Output (Next State)
print()
print('Output Qn : ',Qn)
#Print State
if S==0 and R==0 :
    print('Hold State')
elif S==0 and R==1 :
    print('Reset State')
elif S==1 and R==0 :
    print('Set State')
elif S==1 and R==1 :
    print('Indeterminate State')
