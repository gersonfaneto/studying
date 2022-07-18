Matrizes = {}
quantMatrizes = int(input())
for i in range(quantMatrizes):
    Matriz = []
    tamanhoMatriz = int(input())
    for j in range(tamanhoMatriz):
        linha = input().split(" ")
        Matriz.append(linha)
    for k in range(len(Matriz)):
        for l in range(len(Matriz[k])):
            Matriz[k][l] = int(Matriz[k][l]) ** 2
    Matrizes[i] = Matriz

X = 4
for n, Matriz in enumerate(Matrizes.values()):
    tamanhoColunas = []
    for i in range(len(Matriz)):
        maior = 0
        for j in range(len(Matriz[i])):
            if len(str(Matriz[j][i])) > maior:
                maior = len(str(Matriz[j][i]))
        tamanhoColunas.append(maior)

    print("Quadrado da matriz #{}:".format(X))
    X += 1
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            quantEspaco = tamanhoColunas[j] - len(str(Matriz[i][j]))
            print("{}{}".format(" "*quantEspaco, Matriz[i][j]), end=" ")
        if i != len(Matriz) - 1:
            print()
    if n + 1 != len(Matrizes):
        print("\n")
