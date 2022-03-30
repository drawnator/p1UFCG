# Prog1 aula 2022-02-03 09:08:25.870131d - UFCG
# guilherme Silva Toledo
# um programa que receba um ângulo maior ou igual a zero e informa qual é o quadrante do ciclo trigonométrico em que ele se encontra ou se encontra-se sobre os eixos.

angulo = int(input())

quadrante = 1+ (angulo//90)%4
eixo = angulo%90

if eixo == 0:
    print("Sobre eixos")
else:
    print(f"Quadrante {quadrante}")
