# Prog1 aula 2022-03-17 08:22:07.732046d - UFCG
# guilherme Silva Toledo - 121110792
# Escreva a função cobrinha(M) que monta uma lista de inteiros ímpares gerada a partir do caminhamento em vai e vem de uma matriz de inteiros. O caminhamento em vai e vem incia na primeira linha do sentido da esquerda pra direita e inverte na linha seguinte. A lista de ímpares mantem a ordem em que os inteiros ímapres da matriz original foram visitados.

def cobrinha(M):
    listanova = []
    for i in range(len(M)):
        if i%2 == 0:
            for j in range(len(M[i])):
                if M[i][j]%2 != 0: listanova.append(M[i][j])
        else:
            for j in range(len(M[i])-1,-1,-1):
                if M[i][j]%2 != 0: listanova.append(M[i][j])
    return listanova

#M = [[1,2,3],[4,5,6],[7,8,9]]

#print(cobrinha(M))
            
