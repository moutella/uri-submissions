#Nome: Coordenadas de um Ponto
#Resultado: Accepted
#Data: 24/07/18 17:31:01
#Linguagem: Python 3
import math
entradas = input()
entrada = entradas.split()
A = float(entrada[0])
B = float(entrada[1])

if(A==0 and B ==0):
    print("Origem")
    exit()
if(A==0):
    print("Eixo Y")
    exit()
if(B==0):
    print("Eixo X")
    exit()
if(A>0):
    if(B>0):
        print("Q1")
    else:
        print("Q4")
elif(A<0):
    if(B>0):
        print("Q2")
    else:
        print("Q3")