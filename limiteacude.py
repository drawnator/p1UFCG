# Prog1 aula 2022-02-17 08:07:38.765600d - UFCG
# guilherme Silva Toledo - 121110792
# # Prog1 aula 2022-02-17 08:07:38.765600d - UFCG
# guilherme Silva Toledo - 121110792
# um programa que leia o limite de um açude, o seu nível de água atual e uma série de eventos que registram o aumento ou a diminuição do nível de água.

limiteMax = int(input())
atual = float(input())

while atual < limiteMax:
    entrada = input().split()
    evento = entrada[0]
    quantidade = float(entrada[1])
    if (evento == "demanda"):
        if atual >= quantidade:
            atual -= quantidade
    else:
        atual += quantidade

print("Açude passou a liberar água.")
print(f"Nível: {atual:.2f}")
