#Nome: Preenchimento de Vetor II
#Resultado: Accepted
#Data: 24/07/18 23:32:29
#Linguagem: Python 3
valor = int(input())
for i in range(0,1000):
    print("N[{}] = {}".format(i, i%valor))