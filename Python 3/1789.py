#Nome: A Corrida de Lesmas
#Resultado: Accepted
#Data: 25/07/18 22:19:42
#Linguagem: Python 3
try:
    while 1:
        nVal = int(input())
        vels = input().split()
        maior = 0
        for vel in vels:
            if(int(vel)>maior):
                maior = int(vel)
        if(maior < 10):
            print("1")
        elif(maior<20):
            print("2")
        else:
            print("3")
except EOFError:
    pass