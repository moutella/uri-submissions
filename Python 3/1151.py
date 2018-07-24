#Nome: Fibonacci Fácil
#Resultado: Presentation error
#Data: 24/07/18 21:35:45
#Linguagem: Python 3
nValores = int(input())
temp = 0
nAnt = 0
nAtual = 1
print("0 1", end =" ")
nAtual = nAtual + nAnt
for i in range(0, nValores - 2):
    temp = nAnt
    nAnt = nAtual
    nAtual = nAtual + temp
    print(nAtual, end = " ")