#Nome: Matriz Quadrada IV
#Resultado: Time limit exceeded
#Data: 29/07/18 16:53:57
#Linguagem: Python 3
while 1:
    try:
        x = int(input())
        for i in range(x):
            for j in range(x):
                print(i, end="")
                print(j, "", end="")
            print()
        print(x // 3)
        for i in range(x):
            for j in range(x):
                if i == j == ((x // 2)):
                    print(4, end="")
                elif (x) // 3 <= i < (2 * x) // 3 and ((x) // 3) <= j < (2 * x) // 3:
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
