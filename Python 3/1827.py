#Nome: Matriz Quadrada IV
#Resultado: Accepted
#Data: 29/07/18 17:19:56
#Linguagem: Python 3
while 1:
    try:
        x = int(input())
        meio = x//2
        offset = x // 3
        offsetM = meio-offset
        for i in range(x):
            for j in range(x):
                if i == j == (meio):
                    print(4, end="")
                elif j >= offset and i >= offset and j <= meio+offsetM and i <= meio+offsetM:
                    print(1, end="")
                elif i == j:
                    print(2, end="")
                elif x - i == j + 1 or x - j == i + 1:
                    print(3, end="")
                else:
                    print("0", end="")
            print()
        print()
    except EOFError:
        exit()
