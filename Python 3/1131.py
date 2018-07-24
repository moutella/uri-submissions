#Nome: Grenais
#Resultado: Wrong answer (100%)
#Data: 24/07/18 20:30:06
#Linguagem: Python 3
continua = 1
interVit = 0
greVit = 0
empt = 0
while(continua==1):
    grenalstr = input().split()
    intGol = int(grenalstr[0])
    greGol = int(grenalstr[1])
    if(greGol==intGol):
        empt+=1
    else:
        if(intGol>greGol):
            interVit+=1
        else:
            greVit+=1
    print("Novo grenal (1-sim 2-nao)")
    continua = int(input())

if(interVit>greVit):
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")