#Nome: Construindo Casas
#Resultado: Accepted
#Data: 25/07/18 20:40:32
#Linguagem: Python 3
import math
while 1:
    entrada = input()
    if entrada == "0":
        break
    valores = entrada.split()
    tamanho = int(valores[0])*int(valores[1])
    proporcao = 100/int(valores[2])
    print(int(math.sqrt(tamanho*proporcao)))
