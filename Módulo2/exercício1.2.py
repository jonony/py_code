#
#? Exercício 2
#* Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias
#* de horas, de minutos e de segundos 
#* Calcule o total de segundos resultantes e imprima na tela para o usuário
#

d = int(input('Quantos dias? '))
h = int(input('Quantas horas? '))
m = int(input('Quantos minutos? '))
s = int(input('Quantos segundos? '))

#! 1 dia = a 24 h / 1 hora = 60 min / 1 min = 60 s

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
res = f'O total de segundos resultantes é: {total}'

print(res)
