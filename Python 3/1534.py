#Nome: Matriz 123
#Resultado: Presentation error
#Data: 25/07/18 20:33:00
#Linguagem: Python 3
try:
    while 1:
        tamanho = int(input())
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if i == tamanho - 1 - j:
                    print("2", end="")
                elif i==j:
                    print("1", end="")
                else:
                    print("3", end="")
            print()
except EOFError:
    print()