# Prog1 aula 2022-03-17 08:31:32.239020d - UFCG
# guilherme Silva Toledo - 121110792
# Um cientista precisa de uma maneira automática para calcular a massa de várias moléculas com o intuito de agilizar suas pesquisas. Para ajudá-lo, você precisa desenvolver um programa que realize esse cálculo. O seu programa deve usar os dados da tabela acima.

tE = {'H':1,
'S':32,
'O':16,
'C':12,
'Ca':40,
'Na':23,
'P':31}

entrada = input().split()
saidas = []

while(entrada[0] != 'fim'):
    #print(entrada[0])
    massaMolar = 0
    for i in range(len(entrada)):
        if entrada[i].isdigit():
            massaMolar += tE[entrada[i-1]] * (int(entrada[i])-1)
        else:
            massaMolar += tE[entrada[i]]
    saidas.append(massaMolar)
    entrada = input().split()

for i in range(len(saidas)):
    print(saidas[i])
