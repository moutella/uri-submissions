#Nome: Número Primo
#Resultado: Accepted
#Data: 24/07/18 22:54:21
#Linguagem: Python 3
nTestes = int(input())

for i in range(0, nTestes):
    valor = int(input())
    divisores = []
    soma = 0
    for i in range(1, int(valor/2)+1):
        if not valor % i:
            divisores.append(i)
    divisores.append(valor)

    if (len(divisores) == 2):
        print("{} eh primo".format(valor))
    else:
        print("{} nao eh primo".format(valor))