# Exp1_3_c - WAP to print the following pattern
""" *
    **
    ***
    **
    *"""
for i in range(0,3):
    for j in range(0,i+1):
        print("* ",end="")
    print("")
for i in range(2,0,-1):
    for j in range(1,i+1):
        print("* ",end ="")
    print("")



