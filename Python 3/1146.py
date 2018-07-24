#Nome: Sequências Crescentes
#Resultado: Accepted
#Data: 24/07/18 21:01:43
#Linguagem: Python 3
seqFim = int(input())
while seqFim:
    for i in range(1, seqFim):
        print(i, end=" ")
    print(seqFim)
    seqFim = int(input())