#Nome: Soma de Ímpares Consecutivos II
#Resultado: Accepted
#Data: 24/07/18 19:27:14
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
    else:
        A+=2
    conta = 0
    for j in range(A, B, 2):
        conta+=j
    print(conta)