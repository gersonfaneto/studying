nPalavrasChave, nFuncionarios = map(int, input().split(" "))
HayPoints = {}
for i in range(nPalavrasChave):
    palavraChave, valorAtribuido = input().split(" ")
    HayPoints[palavraChave] = int(valorAtribuido)

valorFuncionarios = []
for i in range(nFuncionarios):
    linha = ""
    valor = 0
    while linha != ["."]:
        linha = input().split(" ")
        for palavra in linha:
            if palavra in HayPoints.keys():
                valor += HayPoints[palavra]
    valorFuncionarios.append(valor)

for valor in valorFuncionarios:
    print(valor)
