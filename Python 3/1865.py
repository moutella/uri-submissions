#Nome: Mjölnir
#Resultado: Accepted
#Data: 25/07/18 22:23:50
#Linguagem: Python 3
nVal = int(input())
for i in range(nVal):
    pode = input().split()[0] == "Thor"
    if pode:
        print("Y")
    else:
        print("N")
