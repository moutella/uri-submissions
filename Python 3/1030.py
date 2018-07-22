#Nome: A Lenda de Flavious Josephus
#Resultado: Time limit exceeded
#Data: 22/07/18 02:43:03
#Linguagem: Python 3
nCasos = input()
casos = []
for x in range(0, int(nCasos)):
	casos.append(input().split())
	
for j in range(0, len(casos)):
	nPessoas = int(casos[j][0])
	nPulo = int(casos[j][1])
	pessoas = []
	pessoasBack = []
	for i in range(0, nPessoas):
		pessoas.append(i+1)
		pessoasBack.append(i+1)
	indiceExiste = -1
	atual = 0
	contador = 0
	while len(pessoas)>1:
		contador+=1
		if (atual >= len(pessoas)):
			atual = 0
		if(contador == nPulo):
			del pessoas[atual]
			contador = 0
		else:
			atual+=1
	print("Case " +  str(j+1) + ":", pessoasBack.index(pessoas[0])+1)