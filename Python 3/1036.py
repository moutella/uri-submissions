#Nome: Fórmula de Bhaskara
#Resultado: Accepted
#Data: 24/07/18 17:11:38
#Linguagem: Python 3
import math
entradas = input()
entrada = entradas.split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
raiz = B*B-4*A*C
if(raiz < 0 or A==0):
    print("Impossivel calcular")
else:
    print("R1 = {:.5f}".format((-B + math.sqrt(raiz))/(2*A)))
    print("R2 = {:.5f}".format((-B - math.sqrt(raiz) )/ (2 * A)))