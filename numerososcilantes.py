# Prog1 miniteste2 - UFCG
# guilherme Silva Toledo
# um programa que receba um código gerado para acesso a um formulário online e verifica se ele é "verdadeiro" ou "falso".
senha = input()
contador = 0
primeironumero = int(senha[1])%2
validador = 0
for digito in senha:
    if int(digito)%2 == primeironumero:
        validador = 1
    primeironumero = int(digito)%2
    contador += 1

if validador == 1:
    print(f'falso: {contador} algarismos.')
else:
    print(f'verdadeiro: {contador} algarismos.')
