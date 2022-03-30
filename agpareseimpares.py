# Prog1 aula 2022-03-10 08:04:19.740335d - UFCG
# guilherme Silva Toledo - 121110792
# função agrupa_pares_impares(seq) que altera uma dada sequência seq de números inteiros não negativos, de forma que todos os valores pares sejam relocados para o início da lista e os ímpares no final. Por exemplo, ao invocar a função para a sequência

def agrupa_pares_impares(seq):
    tam = len(seq)
    quanti = 0
    ordenado = False
    for i in range(tam):
        i -= quanti
        #print(i)
        if seq[i]%2 != 0:
            primeiro = seq[i]
            for j in range(i,tam):
                if j == tam-1:
                    seq[j] = primeiro
                else:
                    seq[j]=seq[j+1]
            quanti += 1
        #print(seq)
        
            
#seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]
#print(seq)
#agrupa_pares_impares(seq)
#print(seq)
