#IMPLEMENTATION OF JK FLIP FLOP - DIRECT METHOD

#Take Input
J = int(input('Value for J : '))
K = int(input('Value for K : '))
Qp = int(input('Value for Qp(Previous o/p) : '))
#Calculate Qn=J Qp' + K' Qp
Qn=J&(~Qp+2)|(~K+2)&Qp
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
