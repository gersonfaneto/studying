FelizNatal = {}

quantIdiomas = int(input())
for i in range(quantIdiomas):
    idioma = input()
    felizNatalIdioma = input()
    FelizNatal[idioma] = felizNatalIdioma

quantCriancas = int(input())
for i in range(quantCriancas):
    nomeCrianca = input()
    idiomaCrianca = input()
    print(nomeCrianca)
    print(FelizNatal[idiomaCrianca])
    print()