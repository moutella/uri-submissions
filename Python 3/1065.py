#Nome: Pares entre Cinco Números
#Resultado: Accepted
#Data: 24/07/18 18:51:41
#Linguagem: Python 3
valores = []
nPar = 0
for i in range(0, 5):
    x = int(input())
    if not (x % 2):
        nPar+=1
        valores.append(x)
print("{} valores pares".format(nPar))
