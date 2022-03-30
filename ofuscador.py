# Prog1 aula 2022-03-21 10:44:00.250564d - UFCG
# guilherme Silva Toledo - 121110792
# programa que ofusca um código seguindo 3 regras:
# 1. 
# 2.
# 3.

def ofuscador(linha):
    # mapa para trocar maiusculas por minusculas
    mapa_letras = {}
    for i in range(26):
        mapa_letras[65+i] = chr(97+i) 
        mapa_letras[97+i] = chr(65+i)

    # mapa para trocar as letras por numeros e
    mapa_transforma ={
    ord('a'): '4',ord('A'): '4',ord('4'): 'A',
    ord('b'): '8',ord('B'): '8',ord('8'): 'B',
    ord('e'): '3',ord('E'): '3',ord('3'): 'E',
    ord('g'): '6',ord('G'): '6',ord('6'): 'G',
    ord('i'): '1',ord('I'): '1',ord('1'): 'I',
    ord('l'): '7',ord('L'): '7',ord('7'): 'L',
    ord('s'): '5',ord('S'): '5',ord('5'): 'S',
    ord('o'): '0',ord('O'): '0',ord('0'): 'O'
    }
    
    #juntar os dois mapas
    for indice in mapa_transforma:
        mapa_letras[indice] = mapa_transforma[indice]
    
    #tratamento de texto
    saida = ''
    tamanho_palavra = 0
    for letra in linha:
        ocorreu_troca = 0
        #adiciona espaços
        if letra == ' ':
            ocorreu_troca = 1
            for i in range(tamanho_palavra):
                saida += '*'
            tamanho_palavra = 0
        else:
            tamanho_palavra +=1

        #troca caracteres
        ordletra = ord(letra)
        for indice in mapa_letras:
            if indice == ordletra:
                saida += mapa_letras[indice]
                ocorreu_troca = 1

        #insere o caractere caso não tenha ocorrido trocas
        if ocorreu_troca == 0:
            saida += letra

    return saida

def test_1():
    assert ofuscador('teste') == 'T35T3'
def test_2():
    assert ofuscador('!@#$% !@#$%') == '!@#$%*****!@#$%'
def test_3():
    linha = "I love Pythonnnnnn!"
    assert ofuscador(linha) == "1*70V3****pYTH0NNNNNN!"




