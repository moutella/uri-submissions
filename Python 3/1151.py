#Nome: Fibonacci Fácil
#Resultado: Accepted
#Data: 24/07/18 21:36:26
#Linguagem: Python 3
nValores = int(input())
temp = 0
nAnt = 0
nAtual = 1
print("0 1", end =" ")
nAtual = nAtual + nAnt
for i in range(0, nValores - 3):
    temp = nAnt
    nAnt = nAtual
    nAtual = nAtual + temp
    print(nAtual, end = " ")
print(nAtual + nAnt)