# Prog1 aula 2022-03-17 08:58:09.111954d - UFCG
# guilherme Silva Toledo - 121110792
# implemente a função soma_matrizes_esparsas(m1, m2) que recebe duas matrizes esparsas com as mesmas dimensões e que produz uma nova matriz esparsa, contendo a soma das duas matrizes passadas como parâmetro.

def soma_matrizes_esparsas(m1, m2):
    x = m1[0]
    y = m2[1]
    novoDic = {}
    for i in m1[2]:
        if i in novoDic:
            novoDic[i] += m1[2][i]
        else:
            novoDic[i] = m1[2][i]
    for i in m2[2]:
        if i in novoDic:
            novoDic[i] += m2[2][i]
        else:
            novoDic[i] = m2[2][i]
    return((x,y,novoDic))

#M1 = (120, 200, {(115, 64): -5})
#M2 = (120, 200, {(20, 55): 5})

#SOMA1 = soma_matrizes_esparsas(M1, M2)
#assert SOMA1 == (120, 200, {(115, 64): -5, (20, 55): 5})
