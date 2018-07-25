#Nome: Área Direita
#Resultado: Accepted
#Data: 25/07/18 14:21:56
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(0,6):
    for j in range(0,k):
        soma += matriz[k][j-k]
        soma += matriz[11-k][j-k]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/30))
