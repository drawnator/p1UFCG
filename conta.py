# Prog1 aula 2022-03-17 08:08:26.409566d - UFCG
# guilherme Silva Toledo - 121110792
# escrever uma função calcula_conta(tabela) que calcula a conta de energia. Para saber o consumo de cada equipamento basta multiplicar a quantidade dos equipamentos pela quantidade de horas e depois pela potência. Para indicar o valor da conta considere que um kWh custa R$ 0,28.

def calcula_conta(tabela):
    qEletronicos = len(tabela)
    preco = 0
    for i in range(1,qEletronicos):
        eletronicoI = tabela[i][1] * tabela[i][2] * tabela[i][3]
        preco += eletronicoI
    preco = preco * 0.28 / 1000
    return f"R$ {preco:.2f}"

#tabela = [["Equipamento", "Quantidade", "Tempo de Uso (horas)", "Potencia (Watts)"],["AR-CONDICIONADO",1,240,2000],["COMPUTADOR",2,150,180],["TV",3,150,110]]

#print(calcula_conta(tabela))
