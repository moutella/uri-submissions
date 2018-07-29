#Nome: Numeração Romana para Números de Página
#Resultado: Wrong answer (100%)
#Data: 29/07/18 21:16:48
#Linguagem: Python 3
for valor in range(1000):
    #valor = int(input())
    x = valor // 100
    if x > 8:
        print("CM", end="")
    elif x >= 5:
        print("D", end="")
        for i in range(x-5):
            print("C", end="")
    elif x > 3:
        print("CD", end="")
    elif x > 0:
        for i in range(x):
            print("C", end="")
    valor %= 100
    y = valor//10
    if y > 8:
        print("XC", end="")
    elif y >= 5:
        print("L", end="")
        for i in range(y-5):
            print("X", end="")
    elif y > 3:
        print("XL", end="")
    elif y > 0:
        for i in range(y):
            print("X", end="")
    valor%=10
    if valor > 8:
        print("IX", end="")
    elif valor >= 5:
        print("V", end="")
        for i in range(valor-5):
            print("I", end="")
    elif valor > 3:
        print("IV", end="")
    elif valor > 0:
        for i in range(valor):
            print("I", end="")
    print()