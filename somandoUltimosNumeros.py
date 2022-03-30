# Prog1 aula 2022-02-14 10:34:41.614550d - UFCG
# guilherme Silva Toledo - 121110792
# um programa que recebe uma sequência de números inteiros, determina a média deles e calcula a soma dos últimos números da sequência até encontrar o primeiro valor maior ou igual à média calculada.

#entrada
entradasTotal = int(input())
lista = [0] * entradasTotal
for ciclo in range(entradasTotal):
    lista[ciclo] = int(input())

#processamento

#media
somaNumerosTotal = 0
for numero in lista:
    somaNumerosTotal += numero
media = somaNumerosTotal/entradasTotal

#soma dos ultimos
somaUltimos = 0
for posicao in range(entradasTotal):
    somaUltimos += lista[(-1 * posicao)-1]
    if lista[(-1* posicao)-1] >= media:
        break

print(somaUltimos)




