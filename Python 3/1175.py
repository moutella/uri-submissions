#Nome: Troca em Vetor I
#Resultado: Wrong answer (100%)
#Data: 24/07/18 23:10:50
#Linguagem: Python 3
vetor = []
for i in range(19,-1,-1):
    valor = int(input())
    vetor.append(valor)
for i in range(0,20):
    print("N[{}] = {}".format(i, vetor[i]))
