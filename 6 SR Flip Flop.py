# initialize inputs and outputs
s = 0
r = 0
q = 0
q_bar = 0

# define function for SR flip-flop
def sr_flip_flop(s, r):
    global q, q_bar
    if s == 1 and r == 0:
        q = 1
        q_bar = 0
        print("Q is Set to 1 and Q_bar is reset to 0")
    elif s == 0 and r == 1:
        q = 0
        q_bar = 1
        print("Q_bar is Set to 1 and Q is reset to 0")
    elif s == 0 and r == 0:
        pass # no change
        print("No change hold condition")
    else: # s == 1 and r == 1
        print("Invalid input: s and r cannot be both 1")

# test the function with different inputs
S=int(input("Enter the value of S: "))
R=int(input("Enter the value of R: "))
sr_flip_flop(S, R)
if(S==0 and R==0):
    print("q =", q, "q_bar =", q_bar)
elif(S==1 and R==0):
    print("q =", q, "q_bar =", q_bar)
elif(S==0 and R==1):
    print("q =", q, "q_bar =", q_bar)
elif(S==1 and R==1): # this will print an error message
    print("")