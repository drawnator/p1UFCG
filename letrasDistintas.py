# Prog1 aula 2022-02-14 10:08:07.590514d - UFCG
# guilherme Silva Toledo - 121110792
# um programa que determina quantas letras distintas estão na primeira palavra em relação à segunda.

#entrada
pPrimaria = input()
pSecundaria = input()

#processamento
diferenca = len(pPrimaria)

for letraPrimaria in pPrimaria:
    for letraTirar in pSecundaria:
        if letraTirar == letraPrimaria:
            diferenca -= 1
            break


#saida
print(diferenca)
