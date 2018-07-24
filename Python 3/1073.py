#Nome: Quadrado de Pares
#Resultado: Wrong answer (100%)
#Data: 24/07/18 18:57:13
#Linguagem: Python 3
num = int(input())
num = 7 // 2
for i in range(0, num):
    n = 2 + i*2
    print("{}^2 = {}".format(n, n*n))