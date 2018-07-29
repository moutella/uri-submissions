#Nome: Notação Científica
#Resultado: Wrong answer (100%)
#Data: 29/07/18 20:10:38
#Linguagem: Python 3
valor = float(input())
contador = 0
while -1 < valor < 1 or valor < -10 or valor > 10:
    if(0 < abs(valor) < 1):
        valor*=10
        contador-=1
    else:
        valor /= 10
        contador += 1
if(valor>0):
    print("+", end ="")
print("{:.4f}".format(valor), end="")
if(contador >=0):
    print("+E{:2d}".format(contador).replace(" ", "0"))
else:
    print("E{:2d}".format(contador).replace(" ", "0"))