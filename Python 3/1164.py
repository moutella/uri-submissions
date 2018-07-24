#Nome: Número Perfeito
#Resultado: Accepted
#Data: 24/07/18 22:51:30
#Linguagem: Python 3
nTestes = int(input())

for i in range(0, nTestes):
    valor = int(input())
    divisores = []
    soma = 0
    for i in range(1, int(valor/2)+1):
        if not valor % i:
            divisores.append(i)
    for val in divisores:
        soma += val
    if soma == valor:
        print("{} eh perfeito".format(valor))
    else:
        print("{} nao eh perfeito".format(valor))