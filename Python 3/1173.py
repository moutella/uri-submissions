#Nome: Preenchimento de Vetor I
#Resultado: Runtime error
#Data: 24/07/18 23:11:39
#Linguagem: Python 3
vetor = []
for i in range(19,-1,-1):
    valor = int(input())
    vetor.append(valor)
vetor.reverse()
for i in range(0,20):
    print("N[{}] = {}".format(i, vetor[i]))
