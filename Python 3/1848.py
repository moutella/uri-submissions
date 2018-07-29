#Nome: Corvo Contador
#Resultado: Accepted
#Data: 29/07/18 19:11:01
#Linguagem: Python 3
count = 0
soma = 0
while count < 3:
    momento = input()
    if momento == "caw caw":
        count+=1
        print(soma)
        soma = 0
    else:
        if(momento == "---"):
            soma +=0
        elif(momento == "--*"):
            soma+=1
        elif (momento == "-*-"):
            soma += 2
        elif (momento == "-**"):
            soma += 3
        elif (momento == "*--"):
            soma += 4
        elif (momento == "*-*"):
            soma += 5
        elif (momento == "**-"):
            soma += 6
        elif (momento == "***"):
            soma += 7
