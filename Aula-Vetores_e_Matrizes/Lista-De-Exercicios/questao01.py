from random import randint
vetor_q = []

for numero in range(20):
    vetor_q.append(randint(1, 100))

print(vetor_q)

# Variavel de controle
maior = -1
menor = 101

for item_da_lista in vetor_q:
    if maior < item_da_lista:
        maior = item_da_lista

    if menor > item_da_lista:
        menor = item_da_lista

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

print("____________________________________")
