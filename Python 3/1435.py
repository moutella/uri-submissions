#Nome: Matriz Quadrada I
#Resultado: Presentation error
#Data: 25/07/18 15:42:55
#Linguagem: Python 3
while 1:
    tamanho = int(input())
    if tamanho == 0:
        break
    tamanho+=1
    o=tamanho
    for i in range(1, tamanho):
        for j in range(1, tamanho):
            print(" ", min(i,j,abs(j-o), abs(i-o)),end="")
            if(j<tamanho-1):
                print(" ", end="")
        print()
    print()
