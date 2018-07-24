#Nome: Quadrado de Pares
#Resultado: Accepted
#Data: 24/07/18 18:57:53
#Linguagem: Python 3
num = int(input())
num = num // 2
for i in range(0, num):
    n = 2 + i*2
    print("{}^2 = {}".format(n, n*n))