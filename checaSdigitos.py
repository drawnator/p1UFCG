# Prog1 prova 2022-03-21 10:09:08.136418 - UFCG
# guilherme Silva Toledo - 121110792
# recebe uma string que representa uma sequência de dígitos não iniciados por 0 e com pelo menos um dígito, e um valor limite que será usado na checagem na linha seguinte
# o programa imprime a soma dos valores lidos a quantidade de valores lidos e o criterio de parada do codigo, sendo possiveis tais criterios:
# checagem de 6 digitos pares
# a somar ofr igual ou maior ao valor limite
# final da sequencia ser atingido
# extra: a string deve ser lida da esquerda para a direita

#entrada
sequencia_digitos = input()
limite_soma_digitos = int(input())

#processamento
quantidade_num_impar = 0
soma_atual = 0
criterio_de_parada = 'final da sequência'
indice_numero = 0

while indice_numero < len(sequencia_digitos):
    #somas e contagens
    numero_atual_string = sequencia_digitos[indice_numero]
    numero_atual_int = int(numero_atual_string)
    if numero_atual_int%2 != 0:
        quantidade_num_impar += 1
    soma_atual += numero_atual_int
    indice_numero += 1
    #verificações
    if quantidade_num_impar == 6:
        criterio_de_parada = '6 ímpares'
        break
    if soma_atual >= limite_soma_digitos:
        criterio_de_parada = 'limite'
        break


#saida
print(f'soma: {soma_atual}')
print(f'números lidos: {indice_numero} de {len(sequencia_digitos)}')
print(f'critério de parada: {criterio_de_parada}')

