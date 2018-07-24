#Nome: Troca em Vetor I
#Resultado: Accepted
#Data: 24/07/18 23:12:53
#Linguagem: Python 3
vetor = []
for i in range(0,20):
    valor = int(input())
    vetor.append(valor)
vetor.reverse()
for i in range(0,20):
    print("N[{}] = {}".format(i, vetor[i]))
