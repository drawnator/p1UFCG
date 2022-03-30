# Prog1 aula 2022-02-24 08:05:29.596087d - UFCG
# guilherme Silva Toledo - 121110792
# escreva a função flipmove(lista, k) que deve ter o efeito total especificado pelas operações flipback e move acima descritas. Assuma que k é não negativo e menor ou igual ao número de elementos da lista.

def flipmove(lista, k):
    saida = []
    for i in range(len(lista)-k):
        saida.append(lista[i+k])
    for j in range(k):
        saida.append(lista[k-j-1])
    for i in range(len(lista)):
        lista.pop(0)
        lista.append(saida[i])
    

lista = [5, 8, 3, 7, 1, 6, 4, 9, 2]
flipmove(lista, 4)
print(lista)

lista2 = [5, 8, 3, 7, 1, 6, 4, 9, 2]
flipmove(lista2, 2)
print(lista2)
