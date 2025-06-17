import os
lista_analisados = []
for raiz, pastas, arquivos in os.walk("arquivos/organizados"):
    for arquivo in arquivos:
        lista_analisados.append(arquivo.rsplit('.',1)[0])

for raiz, pastas, arquivos in os.walk("arquivos/brutos"):

    for arquivo in arquivos:
        if arquivo.rsplit('.',1)[0] not in lista_analisados:
            print(arquivo)

print(lista_analisados)