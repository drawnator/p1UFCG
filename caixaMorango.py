morangos = int(input())

caixas = morangos // 400
perda = (morangos%400)/morangos * 100


print(f"{caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{perda:.1f}% dos morangos serão perdidos.")
