#Nome: A Lenda de Flavious Josephus
#Resultado: Time limit exceeded
#Data: 22/07/18 02:13:36
#Linguagem: Python 3
nCasos = input()
for x in range(0, int(nCasos)):
	casoAtual = input().split()
	nPessoas = int(casoAtual[0])
	nPulo = int(casoAtual[1])
	pessoas = [1] * nPessoas
	indiceAtual = 0
	indiceExiste = -1
	contaExist = 0
	while pessoas.count(1)>1:
		if(pessoas[indiceAtual]==1):
			contaExist += 1
		if(contaExist == nPulo):
			pessoas[indiceAtual]=0
			contaExist = 0
		indiceAtual+=1
		if(indiceAtual >= nPessoas):
			indiceAtual = 0
	print(pessoas.index(1)+1)