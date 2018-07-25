#Nome: Ho Ho Ho
#Resultado: Accepted
#Data: 25/07/18 22:15:44
#Linguagem: Python 3
nVal = int(input())
for i in range(0, nVal):
    print("Ho", end="")
    if(i != nVal-1):
        print(" ", end="")
print("!")