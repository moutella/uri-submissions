#Nome: Área
#Resultado: Accepted
#Data: 24/07/18 16:28:39
#Linguagem: Python 3
entradas = input()
entrada = entradas.split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

print("TRIANGULO: {:.3f}".format(A*C/2))
print("CIRCULO: {:.3f}".format(3.14159*C*C))
print("TRAPEZIO: {:.3f}".format((A+B)*C/2))
print("QUADRADO: {:.3f}".format(B*B))
print("RETANGULO: {:.3f}".format(A*B))
