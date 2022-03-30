# Prog1 aula 2022-02-03 11:44:19.762761d - UFCG
# guilherme Silva Toledo
# um programa que seleciona as palavras que possuem letras dobradas em um conjunto de palavras lidas da entrada.

#entrada
quantidade = int(input())
palavras = [''] * quantidade
for i in range(quantidade):
    palavras[i] = input()
    
#processo
comDobras = 0
semDobras = 0
dobradas = []
normais = []
vp = 0
for i in range(quantidade):
    vp = 0
    for j in range(1,len(palavras[i])):
        if palavras[i][j] == palavras[i][j-1]:
            if vp == 0:
                dobradas.append(palavras[i])
                vp = 1
    if dobradas != []:
        if palavras[i] != dobradas[-1]:
            normais.append(palavras[i])
    else:
        normais.append(palavras[i])

#saida
print(f"{len(dobradas)} palavra(s) com letras dobradas:")
for i in dobradas:
    print(i)
print('---')
print(f"{len(normais)} palavra(s) sem letras dobradas:")
for i in normais:
    print(i)
