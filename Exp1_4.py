# Exp1_4 WAP to demonstrate use of break,pass and continue in a while loop 


for i in range(0,10,1):
    while(i>0):
        if (i==4):
            continue
        elif(i==5):
            break
        else:
            pass
print(i)