#Nome: A Lenda de Flavious Josephus
#Resultado: Runtime error
#Data: 22/07/18 16:10:58
#Linguagem: Python 3
nCasos = input()
casos = []
for x in range(0, int(nCasos)):
	casos.append(input().split())
	
for j in range(0, len(casos)):
	nPessoas = int(casos[j][0])
	nPulo = int(casos[j][1])
	pessoas = []
	for i in range(0, nPessoas):
		pessoas.append(i+1)
	atual = -1	+ nPulo
	
	while len(pessoas)>1:
		del pessoas[atual]
		nPessoas-=1
		atual+=nPulo-1
		while atual >= nPessoas:
			atual -= nPessoas
	print("Case " +  str(j+1) + ":", pessoas[0])