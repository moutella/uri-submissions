#Nome: Sequência S
#Resultado: Accepted
#Data: 24/07/18 21:49:57
#Linguagem: Python 3
S = 0
for i in range(1,101):
    S += 1/i
print("{:.2f}".format(S))