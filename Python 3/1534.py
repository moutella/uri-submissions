#Nome: Matriz 123
#Resultado: Runtime error
#Data: 25/07/18 20:28:32
#Linguagem: Python 3
while 1:
    tamanho = int(input())
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            if i==j:
                print("1", end="")
            elif i == 3-j:
                print("2", end="")
            else:
                print("3", end="")
        print()