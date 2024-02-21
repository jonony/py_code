#
#? Exercício 3
#* Desenvolva um algoritmo que converta a temparatura em Celsius para Fahrenheit
#* equação de conversão é:
#! 9 x Celsius, tudo dividido por 5, e somando 32
#

C = float(input('Digite uma temperatura em Celsius: '))
F = (9 * C) / 5 + 32

print(f'Valor em Celsius: {C}. Fahrenheit: {F} ')
