# UNIESP - CENTRO UNIVERSITARIO
# CURSO : SISTEMAS PARA INTERNET | PI-B | NOITE
# ALUNO : Miguel Rodrigues Carneiro

from random import randint

numero_clientes = 1000
lista_de_resposta = [randint]

while numero_clientes > 0:
    lista_de_resposta.append(randint(1, 5))
    numero_clientes -= 1

resposta_1 = lista_de_resposta.count(1)
resposta_2 = lista_de_resposta.count(2)
resposta_3 = lista_de_resposta.count(3)
resposta_4 = lista_de_resposta.count(4)
resposta_5 = lista_de_resposta.count(5)

print(f'Quantidade de resposta 1: {resposta_1}')
print(f'Quantidade de resposta 2: {resposta_2}')
print(f'Quantidade de resposta 3: {resposta_3}')
print(f'Quantidade de resposta 4: {resposta_4}')
print(f'Quantidade de resposta 5: {resposta_5}')
