#IMPLEMENTATION OF JK FLIP FLOP - DIRECT METHOD
J = int(input('Value for j : '))
K = int(input('Value for k : '))
Qp = int(input('Value for Qp(Previous o/p) : '))

#Qn=J Qp' + K' Qp
#Qn=OR(AND(J,NOT(Qp)),AND(NOT(K),Qp))
Qn=J&(~Qp+2)|(~K+2)&Qp

print('Output Qn : ',Qn)
