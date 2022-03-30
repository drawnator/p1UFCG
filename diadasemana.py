# Prog1 miniteste2 - UFCG
# guilherme Silva Toledo
# um programa que a partir do dia da semana que corresponde ao dia 1 do ano (ou seja 01 de janeiro) e de um determinado dia que desejamos identificar o dia da semana que cai, ele retorna o nome do dia da semana correspondente

diaD = input()
numeroN = int(input())

if diaD == 'domingo':
    diaAtual = 0
elif diaD == 'segunda':
    diaAtual = 1
elif diaD == 'terca':
    diaAtual = 2
elif diaD == 'quarta':
    diaAtual = 3
elif diaD == 'quinta':
    diaAtual = 4
elif diaD == 'sexta':
    diaAtual = 5
else:
    diaAtual = 6

numeroN = (numeroN + diaAtual - 1)%7

if numeroN == 0:
    print('domingo')
elif numeroN == 1:
    print('segunda')
elif numeroN == 2:
    print('terca')
elif numeroN == 3:
    print('quarta')
elif numeroN ==  4:
    print('quinta')
elif numeroN == 5:
    print('sexta')
else:
    print('sabado')

