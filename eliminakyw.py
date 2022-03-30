# Prog1 aula 2022-02-17 08:28:09.066837d - UFCG
# guilherme Silva Toledo - 121110792
# Escreva a função elimina_kyw(sentenca) que recebe uma string e retorna uma nova string baseada na sentença recebida apenas removendo as ocorrências das 3 letras: k, y e w. Por simplificação, assumir que todas as letras são minúsculas.

def elimina_kyw(sentenca):
    nova_sentenca = ""
    for letra in sentenca:
        if letra == k or letra == w or letra == y:
            pass
        else:
            nova_sentenca = f"{nova_sentenca}{letra}"

    return nova_sentenca
