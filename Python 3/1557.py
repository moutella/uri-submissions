#Nome: Matriz Quadrada III
#Resultado: Wrong answer (100%)
#Data: 25/07/18 21:53:34
#Linguagem: Python 3
import math
try:
    while 1:
        entrada = int(input())
        if entrada == "0":
            break
        caracteres = 1
        x = 2 ** (entrada+1)
        print(x)
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
except EOFError:
    pass