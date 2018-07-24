#Nome: Imposto de Renda
#Resultado: Accepted
#Data: 24/07/18 17:40:08
#Linguagem: Python 3
sal = float(input())
if sal <= 2000:
    print("Isento")
elif sal <= 3000:
    print("R$ {:.2f}".format(((sal - 2000) * 0.08)))
elif sal <= 4500:
    print("R$ {:.2f}".format(((sal - 3000) * 0.18) + (1000 * 0.08)))
else:
    print("R$ {:.2f}".format(((sal - 4500) * 0.28 + (1500 * 0.18) + 1000 * 0.08)))
