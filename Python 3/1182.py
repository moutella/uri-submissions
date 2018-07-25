#Nome: Coluna na Matriz
#Resultado: Accepted
#Data: 25/07/18 13:32:36
#Linguagem: Python 3
linha = int(input())
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(0, 12):
    soma += matriz[k][linha]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/12))
