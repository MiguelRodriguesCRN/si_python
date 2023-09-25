# UNIESP - CENTRO UNIVERSITARIO
# CURSO : SISTEMAS PARA INTERNET | PI-B | NOITE
# ALUNO : Miguel Rodrigues Carneiro


horas_extras = int(input('Digite o numero exato de horas extras: '))

horas_faltas = int(input('Digite o numero exato de horas faltas: '))

horas_faltas_final = horas_faltas + (horas_faltas/2)

if horas_extras > horas_faltas_final:
    print('Você recebeu um bonus de R$ 500.00 esse mês')
    
else:
    print('Você não recebeu bônus esse mês')