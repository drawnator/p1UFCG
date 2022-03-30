# Prog1 aula 2022-03-10 09:08:21.318425d - UFCG
# guilherme Silva Toledo - 121110792
# Crie uma função ordena_vpb que recebe como parâmetro uma lista de letras, representando cores, em uma ordem qualquer. Por simplificação, a lista só contém 3 tipos diferentes de letras: v representando a cor vermelha, p representando a cor preta e b representando a cor branca. A função deve modificar a lista recebida organizando todos os vermelhos na parte inicial da lista, pretos na parte central e brancos no final da lista.

def ordena_vpb(lis):
    v = 0
    p = 0
    b = 0
    for i in range(len(lis)):
        if lis[i] == 'v':
            v +=1
        if lis[i] == 'p':
            p +=1
        if lis[i] == 'b':
            b+=1
    #print(v,p,b)
    for i in range(v):
        lis[i] = 'v'
    for i in range(p):
        lis[i+v]= 'p'
    for i in range(b):
        lis[i+v+p] = 'b'

