#Nome: Médias Ponderadas
#Resultado: Accepted
#Data: 24/07/18 19:03:30
#Linguagem: Python 3
num = int(input())
for i in range(0, num):
    entradas = input()
    entrada = entradas.split()
    A = float(entrada[0])
    B = float(entrada[1])
    C = float(entrada[2])
    print("{:.1f}".format((A*2+B*3+C*5)/10))