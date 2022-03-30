# Prog1 aula 2022-02-24 08:47:45.422341d - UFCG
# guilherme Silva Toledo - 121110792
# a função remove_duplas(lista) que recebe uma lista de números inteiros como parâmetro e remove dessa lista apenas os números que aparecem duas vezes na lista, ou seja, aparecem em duplas. A lista deve ser modificada de forma a não possuir nenhum número duplicado. A função não tem retorno explícito e produz efeito colateral.

def remove_duplas(lista):
    i = 0
    while i < len(lista):
        numAtual = lista[i]
        posAtual = 0
        posGrupo = []
        for j in range(len(lista)):
            if lista[j] == numAtual:
                posAtual += 1
                posGrupo.append(j)
        if posAtual == 2:
            lista.pop(posGrupo[1])
            lista.pop(posGrupo[0])
            i -= 1
        i += 1

lista = [1,1,2,3,3,2]
remove_duplas(lista)
print(lista)
