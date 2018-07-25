#Nome: Matriz Quadrada III
#Resultado: Accepted
#Data: 25/07/18 22:08:31
#Linguagem: Python 3
import math
while 1:
    entrada = int(input())
    if entrada == 0:
        quit()
    caracteres = 1
    x = 4 ** (entrada-1)
    car = entrada
    while x >= 10:
        x/=10
        caracteres+=1
    for i in range(0, entrada):
        for j in range(0, entrada):
            valor = 2**(j+i)
            print("{0:>{x}}".format(valor, x=caracteres), end="")
            if(j!=entrada-1):
                print(" ", end="")
        print()
    print()
