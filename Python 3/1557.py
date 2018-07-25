#Nome: Matriz Quadrada III
#Resultado: Wrong answer (100%)
#Data: 25/07/18 21:43:26
#Linguagem: Python 3
import math
while 1:
    try:
        entrada = int(input())
        if entrada == "0":
            break
        caracteres = 1
        x = 2 ** (entrada - 1)
        car = entrada
        while x >= 10:
            x /= 10
            caracteres += 1
        for i in range(0, entrada):
            for j in range(0, entrada):
                valor = min(2 ** j, 2 ** i)

                print("{0:>{x}}".format(valor, x=caracteres), end="")
                if (j != entrada - 1):
                    print(" ", end="")
            print()
        print()
    except EOFError:
        break
    except ValueError:
        entrada = ""