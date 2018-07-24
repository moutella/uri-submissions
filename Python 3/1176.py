#Nome: Fibonacci em Vetor
#Resultado: Runtime error
#Data: 24/07/18 23:29:26
#Linguagem: Python 3
nValores = int(input())
temp = 0
nAnt = 0
nAtual = 1

nAtual = nAtual + nAnt

fib = []
fib.append(0)
fib.append(1)
for i in range(3, 61):
    temp = nAnt
    nAnt = nAtual
    nAtual = nAtual + temp
    fib.append(nAtual)
for j in range(0, nValores):
    indice = int(input())
    print("Fib({}) = {}".format(indice, fib[indice]))