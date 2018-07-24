#Nome: Soma de Ímpares Consecutivos II
#Resultado: Wrong answer (60%)
#Data: 24/07/18 19:25:18
#Linguagem: Python 3
nTestes = int(input())

for i in range(0,nTestes):
    valores = input().split()
    A = int(valores[0])
    B = int(valores[1])

    if A > B:
        temp = A
        A = B
        B = temp

    if not A%2:
        A+=1
    conta = 0
    for j in range(A+2, B, 2):
        conta+=j
    print(conta)