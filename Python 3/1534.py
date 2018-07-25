#Nome: Matriz 123
#Resultado: Wrong answer (10%)
#Data: 25/07/18 20:31:23
#Linguagem: Python 3
try:
    while 1:
        tamanho = int(input())
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if i==j:
                    print("1", end="")
                elif i == tamanho-1-j:
                    print("2", end="")
                else:
                    print("3", end="")
            print()
except EOFError:
    print()