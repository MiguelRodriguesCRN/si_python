# UNIESP - CENTRO UNIVERSITARIO
# CURSO : SISTEMAS PARA INTERNET | PI-B | NOITE
# ALUNO : Miguel Rodrigues Carneiro

compras_total = float(input('Digite o valor da compra: '))

if compras_total >= 100:
    compras_total = compras_total - (compras_total * 10) / 100
    print(f'Vc recebeu um desconte de 10%, com isso o valor total a ser pago é de {compras_total} R$')

elif compras_total >= 50 < 100:
    compras_total = compras_total - (compras_total * 5) / 100
    print(f'Vc recebeu um desconte de 5%, com isso o valor total a ser pago é de {compras_total} R$')

elif compras_total < 50:
    compras_total
    print(f'Vc não recebeu desconto e o valor total a ser pago é de: {compras_total} R$')

