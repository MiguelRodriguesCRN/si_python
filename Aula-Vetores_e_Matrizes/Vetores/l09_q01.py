# CENTRO UNIVERSITARIO UNIESP
# ALUNO: MIGUEL RODRIGUES CARNEIRO


# Criar uma lista Com 5 Clubes
clubes_de_futebol = [
    'ibis',
    'flamengo',
    'perilima',
    'volta redonda',
    'nacilnal de patos'
]

#perguntar qual o clube oo usuario vai verificar

clube_pesquisado = input('Digite o clube: ')

for clube in clubes_de_futebol:

    if clube == clube_pesquisado:
        print('ACHEI!!')
    else:
        print('Ainda Não achei!!')