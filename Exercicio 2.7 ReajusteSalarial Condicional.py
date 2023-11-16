# Reajuste salarial
'''
A empresa iTalents resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que
calculará os reajustes.

Faça um programa que solicita o salário atual do colaborador e calcule o
reajuste salarial com base nas seguintes faixas salariais:
• Salários até R$ 280,00 (incluindo): aumento de 20%.
• Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
• Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
• Salários de R$ 1500,00 em diante: aumento de 5%.
Ao final, o programa deverá imprimir na tela as seguintes informações:
• Salário antes do reajuste.
• Percentual de aumento aplicado.
• Valor do aumento.
• Novo salário após o reajuste.
'''
print ('.'*40)
salario = float (input('Salário Atual do Colaborador R$ '))
if salario < 280:
    aumento = salario + (salario * 20 / 100)
    print ('Salario inicial era de R$ {}.\nCom aumento de 20 % seu novo salario será de R$ {}'. format (salario ,aumento))
    print('*'*35)

elif salario <= 780:
    aumento = salario + (salario * 15/100)
    print ('Seu salário atual é de R$ {}.\nSeu novo salário será de R$ {} com 15% de aumento'.format (salario, aumento))

elif salario <= 1500:
    aumento = salario + (salario * 10/100)
    print ('Seu salário atual é de R$ {}.\nSeu novo salário será de R$ {} com 10% de aumento'.format (salario, aumento))

elif salario > 1500:
    aumento = salario + (salario * 5/100)
    print ('Seu salário atual é de R$ {:.2f}.\nSeu novo salário será de R$ {:.2f} com 5% de aumento'.format (salario, aumento))

print ('.'*40)