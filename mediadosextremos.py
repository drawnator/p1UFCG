# Prog1 aula 2022-02-03 09:25:18.434644d - UFCG
# guilherme Silva Toledo
# um programa que utiliza a média dos extremos para classificar um conjunto de números inteiros. 

#entrada
total = int(input())
entradas = [0] * total
entradas[0] = int(input())
for i in range(1,total):
    entradas[i] = int(input())

#tratamento    
maior = menor = entradas[0]
for i in range(total):
    if entradas[i] > maior:
        maior = entradas[i]
    elif entradas[i] < menor:
        menor = entradas[i]
media = (maior + menor)/2

acima = 0
abaixo = 0
for i in range(total):
    if entradas[i] > media:
        acima += 1
    elif entradas[i] < media:
        abaixo += 1
#output    
print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Média dos extremos: {media:.2f}")
print(f"{abaixo} número(s) abaixo da média")
print(f"{acima} número(s) acima da média")




