#Nome: Grenais
#Resultado: Accepted
#Data: 24/07/18 20:31:45
#Linguagem: Python 3
continua = 1
interVit = 0
greVit = 0
empt = 0
nGrenais = 0
while(continua==1):
    nGrenais +=1
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

print("{} grenais".format(nGrenais))
print("Inter:{}".format(interVit))
print("Gremio:{}".format(greVit))
print("Empates:{}".format(empt))
if(interVit>greVit):
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")