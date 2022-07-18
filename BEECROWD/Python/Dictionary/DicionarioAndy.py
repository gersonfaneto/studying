import sys
from unidecode import unidecode

Dicionario = set()
for line in sys.stdin:
    linha = line.rstrip("\n")
    for char in linha:
        if not char.isalpha():
            linha = linha.replace(char, " ")
    linha = linha.split(" ")
    for palavra in linha:
        Dicionario.add(unidecode(palavra).lower())

for item in sorted(Dicionario):
    if len(item) > 0:
        print(item)
