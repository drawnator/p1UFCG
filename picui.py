# Prog1 aula miniteste1 - UFCG
# guilherme Silva Toledo
# programa que calcula se um determinado candidato quebrou ou não o recorde de quantidade comida de carne de sol do festival.

recorde = float(input())
atual = float(input())

if (atual > recorde):
    print(f"recorde quebrado ({atual} kg)")
elif(atual == recorde):
    print("recorde empatado")
else:
    print("recorde mantido")

