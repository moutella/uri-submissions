#Nome: Matriz Quadrada II
#Resultado: Accepted
#Data: 25/07/18 16:32:25
#Linguagem: Python 3
while 1:
    tamanho = int(input())
    if tamanho == 0:
        break
    tamanho+=1
    o=tamanho
    for i in range(1, tamanho):
        for j in range(1, tamanho):
            valor = abs(i-j) +1
            #valor = min(i,j,abs(j-o), abs(i-o))
            string = "{:>3}".format(valor)
            print(string, end="")
            if(j!=tamanho-1):
                print(" ", end="")
        print()
    print()