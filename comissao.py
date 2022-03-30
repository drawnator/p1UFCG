# Prog1 aula miniteste1 - UFCG
# guilherme Silva Toledo
# calcula a comição de um trabalhador depois de uma compra

nome = input("Qual é o nome do(a) vendedor(a)? ")
valor = float(input("Qual é o valor da venda? "))

if (valor > 500):
    comissao = valor*10/100
    nome = nome[0] + nome[1] + nome[2] + nome[3] + nome[4]
else:
    comissao = valor*5/100

print(f"O valor da comissão para o(a) vendedor(a) {nome} é R$ {comissao:.2f}.")

