# Prog1 aula 2022-02-10 08:07:21.594007d - UFCG
# guilherme Silva Toledo
# um programa que leia uma série de números inteiros não negativos e conte quantos estão acima da média dos valores pares.

#entrada
Quant = int(input())
numeros = [0] * Quant
somaPar = 0
quantPar = 0
for i in range(Quant):
    numero = int(input())
    if numero%2 == 0:
        somaPar += numero
        quantPar += 1
    numeros[i] = numero


#processamento
acimaMedia = 0
for i in numeros:
    if i > somaPar/quantPar:
        acimaMedia += 1

#saida
print(f"média dos pares: {somaPar/quantPar:.1f}")
print(f"acima da média: {acimaMedia}")
