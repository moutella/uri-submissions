#Nome: Crescimento Populacional
#Resultado: Accepted
#Data: 24/07/18 22:47:18
#Linguagem: Python 3
nTestes = int(input())

for i in range(0, nTestes):
    valores = input().split()
    APop = float(valores[0])
    ACresc = float(valores[2])
    BPop = float(valores[1])
    BCresc = float(valores[3])
    anos = 0
    while BPop >= APop:
        APop += int(ACresc * 0.01 *APop)
        BPop += int(BCresc * 0.01 * BPop)
        anos+=1
        if anos > 100:
            BPop = 0
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(anos, "anos.")