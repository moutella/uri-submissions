#Nome: Média 3
#Resultado: Wrong answer (20%)
#Data: 24/07/18 17:20:46
#Linguagem: Python 3
entradas = input()
entrada = entradas.split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
D = float(entrada[3])
media = (A*2+B*3+C*4+D*1)/10
print("Media: {:.1f}".format(media))
if(media > 7):
    print("Aluno aprovado.")
elif(media < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    mediafinal = exame+media/2
    if(media > 5):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediafinal))
    else:
        print("Aluno reprovado.")