#Nome: Dividindo X por Y
#Resultado: Accepted
#Data: 24/07/18 20:08:27
#Linguagem: Python 3
nDiv = int(input())

for i in range(0, nDiv):
    valoresSTR = input().split()
    A  = int(valoresSTR[0])
    B = int(valoresSTR[1])
    if(B == 0):
        print("divisao impossivel")
    else:
        print("{:.1f}".format(A/B))