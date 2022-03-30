# Prog1 aula \d - UFCG
# guilherme Silva Toledo
# um programa que codifica palavras usando um sistema simples de criptografia que consiste na substituição das letras de uma palavra por números considerando o seguinte mapeamento:

senha = input()
senhanova = ""

letras = "aeioAEIO"
trocas = "43104310"
contador = 0
contador2 = 0
contador3 = 0
for i in senha:
    if contador == 0:
        senhanova = f"{i}"

    else:
        for j in letras:
            if j == i:
                senhanova = f"{senhanova}{trocas[contador2]}"
                contador2 = -20
                contador3 += 1
            contador2 += 1
            if contador2 == 8:
                senhanova = f"{senhanova}{i}"

        contador2 = 0
    contador = contador + 1

print(f"{senhanova} ({contador3} troca(s))")
