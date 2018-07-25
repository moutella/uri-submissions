#Nome: Matriz Quadrada I
#Resultado: Presentation error
#Data: 25/07/18 16:06:22
#Linguagem: Python 3
while 1:
    tamanho = int(input())
    if tamanho == 0:
        break
    tamanho+=1
    o=tamanho
    for i in range(1, tamanho):
        for j in range(1, tamanho):
            valor = min(i,j,abs(j-o), abs(i-o))
            if(valor>9):
                print("", valor, "",end="")
            else:
                print(" ", valor, "", end="")
        print()
    print()
