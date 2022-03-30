# Prog1 aula 2022-02-10 08:20:51.432233d - UFCG
# guilherme Silva Toledo
# um programa que leia 3 palavras indicadas pelos pais de um récem-nascido de Ordenópolis e que imprime o nome completo do novo Ordenopolitano (pessoa que nasce em Ordenópolis).

nomeInvalido = 1

while nomeInvalido == 1:
    #input
    nome1 = input("nome 1? ")
    nome2 = input("nome 2? ")
    nome3 = input("nome 3? ")

    #processo
    if nome1 < nome2:
        if nome2 < nome3:
            nomeInvalido = 0
    #saida
    if nomeInvalido == 1:
        print("nomes inválidos: tente novamente")

#fim
print(nome1, nome2,'de', nome3)

