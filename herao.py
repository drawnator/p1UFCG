# Prog1 aula miniteste2 - UFCG
# guilherme Silva Toledo
# programa que calcula a área de uma série de triângulos, bem como a área média dos triângulos maiores. Os triângulos são considerados maiores se sua área for maior que 100.

triangulos = int(input())

contador = 0
somaarea = 0
a100 = 0
for i in range(triangulos):
    contador += 1
    lado1, lado2, lado3 = input().split()
    lado1 = float(lado1)
    lado2 = float(lado2)
    lado3 = float(lado3)
    s = (lado1 + lado2 + lado3)/2
    A = (s * (s-lado1) * (s-lado2) * (s-lado3)) ** (1/2)
    if A > 100:
        somaarea += A
        a100 += 1
    print(f'Área {contador}: {A:.2f}')

if a100 > 0:
    somaarea = somaarea/a100

print(f'Número maiores: {a100}, área média: {somaarea:.2f}')
