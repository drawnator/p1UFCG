# Prog1 aula P08 - UFCG
# guilherme Silva Toledo
# recebe 3 numeros e ordena eles apenas com if

primeiro = int(input())
segundo = int(input())
terceiro = int(input())


PS = (primeiro < segundo)
PT = (primeiro < terceiro)
ST = (segundo < terceiro)

resposta = ""



if PS and PT:
    resposta = f"{primeiro}"
    if ST:
        resposta = f"{resposta} {segundo} {terceiro}"
    else:
        resposta = f"{resposta} {terceiro} {segundo}"
elif ST and not PS:
    resposta = f"{segundo}"
    if PT:
        resposta = f"{resposta} {primeiro} {terceiro}"
    else:
        resposta = f"{resposta} {terceiro} {primeiro}"
else:
    resposta = f"{terceiro}"
    if PS:
        resposta = f"{resposta} {primeiro} {segundo}"
    else:
        resposta = f"{resposta} {segundo} {primeiro}"


print (resposta)
