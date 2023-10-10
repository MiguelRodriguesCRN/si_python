# Lista de Contatos

contatos = [
    ['Mãe', '(83) 99999-9999', '28/05/1951'],
    ['SAMU', '192'],
    ['Marcão Lanches (Podrão)', '83 99999', '18/09/2005'],
    ['Policia', '190']
]

#print(contatos[0][0])#

for contato in contatos:
    print(f'Nome: {contato[0]} | telefone: {contato[1]}')