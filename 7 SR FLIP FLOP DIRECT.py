#IMPLEMENTATION OF SR FLIP FLOP - DIRECT METHOD

#Take Input
S = int(input('Value for S : '))
R = int(input('Value for R : '))
Qp = int(input('Value for Qp(Previous o/p) : '))
#Calculate Qn = S + R' Qp
Qn=S|(~R+2)&Qp
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
