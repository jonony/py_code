#
#? EXERCÍCIO 2
#* Uma empresa concedeu um bônus de 20% para todos os seus funcionários que possuem 5 anos de empresa
#* Todos os outros com menos tempo, receberam uma bonificaçõ de 10% somente
#* Escreva um algoritmo que leia o sálario do funcionario e o seu tempo de empresa,
#* E apresente  bonificção de cada funcionário na tela.
#

salario      = float(input('Digite aqui o seu sálario: '))
ano_admissao = int(input('Digite aqui o seu ano de admissão: '))
ano_atual    = int(input('Digite aqui o ano atual: '))

tempo = ano_atual - ano_admissao

if(tempo > 5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1

print(f'O seu salário é de R$ {salario:.2f}')
print(f'Você tem {tempo} anos de empresa')
print(f'Você possui a bonificação de R$ {bonus:.2f}')
print(f'O seu salário final é de R$ {salario + bonus:.2f}')
