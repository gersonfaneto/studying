def convValorMod(valorLista, valorMod):
    if valorLista < 0:
        return ((valorLista * -1) % valorMod) * -1
    return valorLista % valorMod

def SelectionSort(Lista, Mod):
    for i in range(len(Lista) - 1):
        menor, menorIndex = Lista[i], i
        valorModI = convValorMod(Lista[i], Mod)
        for j in range(i, len(Lista)):
            valorModJ = convValorMod(Lista[j], Mod)
            if valorModJ < valorModI:
                menor, menorIndex = Lista[j], j
            elif valorModJ == valorModI:
                if Lista[j] % 2 != 0 and menor % 2 == 0:
                    menor, menorIndex = Lista[j], j
                elif Lista[j] % 2 != 0 and menor % 2 != 0:
                    if Lista[j] > menor:
                        menor, menorIndex = Lista[j], j
                elif Lista[j] % 2 == 0 and menor % 2 == 0:
                    if Lista[j] < menor:
                        menor, menorIndex = Lista[j], j
            valorModI = convValorMod(menor, Mod)
        Lista[i], Lista[menorIndex] = Lista[menorIndex], Lista[i]
    return Lista

def main():
    quantNumeros, valorMod = 1, 1
    Saida = {}

    while quantNumeros != 0 and valorMod != 0:
        quantNumeros, valorMod = map(int, input().split())
        Lista = []

        for i in range(quantNumeros):
            num = int(input())
            Lista.append(num)

        Lista = SelectionSort(Lista, valorMod)
        Saida[(quantNumeros, valorMod)] = Lista

    for chave, valor in Saida.items():
        print(chave[0], chave[1])
        if not chave[0] and not chave[1]:
            print()
        for num in valor:
            print(num)

if __name__ == '__main__':
    main()
