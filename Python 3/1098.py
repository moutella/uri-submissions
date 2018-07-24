#Nome: Sequencia IJ 4
#Resultado: Wrong answer (10%)
#Data: 24/07/18 19:17:20
#Linguagem: Python 3
for i in range(0,11):
    for j in range(1,4):
        if(float(i*0.2)%1):
            print("I={:.1f} J={}".format(i*0.2,j + i * 0.2))
        else:
            print("I={} J={}".format(int(i * 0.2), j + int(i*0.2)))