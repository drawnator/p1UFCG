# Prog1 aula 2022-02-17 08:49:17.430665d - UFCG
# guilherme Silva Toledo - 121110792
# Escreva a função elemento_faltando(lista1, lista2) que compara as duas listas e retorna qual elemento está faltando na primeira lista.

def elemento_faltando(lista1, lista2):
    if lista1 == []:
        return lista2[0]
    for elemento1 in lista2:
        numeroNalista = 0
        for elemento2 in lista1:
            if elemento1 == elemento2:
                numeroNalista = 1
            if elemento2 == lista1[-1] and numeroNalista == 0:
                return elemento1

lista1 = []
lista2 = [4]
print(elemento_faltando(lista1, lista2))
