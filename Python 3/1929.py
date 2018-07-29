#Nome: Triângulo
#Resultado: Wrong answer (10%)
#Data: 29/07/18 19:39:55
#Linguagem: Python 3
valores = input().split()
vals = []
for n in valores:
    vals.append(int(n))
vals.sort()
if(vals[3] > vals[2] + vals[1]) and (vals[2] > vals[1]+vals[0]):
    print("N")
else:
    print("S")