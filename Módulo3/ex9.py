#
#? EXERCÍCIO 2
#* Uma empresa concedeu um bônus de 20% para todos os seus funcionários que possuem 5 anos de empresa
#* Ainda, funcionários com mais de 10 anos de empresa ganham uma bonificação de 30%
#* Todos os outros com menos tempo, receberam uma bonificaçõ de 10% somente
#* Escreva um algoritmo que leia o sálario do funcionario e o seu tempo de empresa,
#* E apresente  bonificção de cada funcionário na tela.
#

salario      = float(input('Digite aqui o seu sálario: '))
ano_admissao = int(input('Digite aqui o seu ano de admissão: '))
ano_atual    = int(input('Digite aqui o ano atual: '))

tempo = ano_atual - ano_admissao

if(tempo > 10):
    bonus = salario * 0.3
else:
    if(tempo > 5):
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

print(f'Você tem {tempo} anos de empresa')
print(f'O salário é de R$ {salario}')
print(f'A sua bonificação será de {bonus}')
print(f'Seu salário final será de R$ {salario + bonus}')