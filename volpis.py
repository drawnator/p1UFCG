# Prog1 aula miniteste1 - UFCG
# guilherme Silva Toledo
# recebe uma largura comprimento e profundidade e retorna o volume em litros da piscina

comprimento = float(input())
largura = float(input())
profundidade = float(input())

volm3 = 1000 * comprimento * largura * profundidade

print(f"A piscina comporta {volm3:.2f} litros de água.")
