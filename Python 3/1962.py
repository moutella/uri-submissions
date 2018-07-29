#Nome: Há Muito, Muito Tempo Atrás
#Resultado: Accepted
#Data: 29/07/18 21:33:18
#Linguagem: Python 3
nvals = int(input())
for i in range(nvals):
    x = int(input())
    y = 2015 - x
    if y <= 0:
        y -= 1
        print("{} A.C.".format(abs(y)))
    else:
        print("{} D.C.".format(y))
