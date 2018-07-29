#Nome: Notação Científica
#Resultado: Wrong answer (100%)
#Data: 29/07/18 20:50:38
#Linguagem: Python 3
valor = input()
sinal = valor[0]
valor = float(valor)
contador = 0
if valor == 0:
    if(sinal=="-"):
        print("-0.0000E+00")
    else:
        print("+0.0000E+00")
while not 1 <= abs(valor) < 10:
    print(valor)
    if abs(valor) < 1:
        valor *= 10
        contador -= 1
    else:
        valor /= 10
        contador += 1
if(valor > 0):
    print("+{:.4f}".format(valor), end="")
else:
    print("{:.4f}".format(valor), end="")
if(contador >= 0):
    print("E+{:>2}".format(contador).replace(" ", "0"))
else:
    print("E-{:>2}".format(abs(contador)).replace(" ", "0"))