#Nome: Sequência S II
#Resultado: Accepted
#Data: 24/07/18 21:53:58
#Linguagem: Python 3
S = 0
frac = 1
for i in range(1, 39, 2):
    S += i / frac
    frac*=2

print("{:.2f}".format(S))