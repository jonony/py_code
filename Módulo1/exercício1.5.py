#
#? Exercício 5
#* Desenvolva um algoritmo que seja capaz de calcular a soma e a subtração entre 2 valores com vírgula.
#* Crie duas variáveis de teste. Uma que testa se a soma é maior que 10
#* Outra que testa se a subtração é menor que 0. Imprima tudo na tela
#

x = float(input('Digite aqui um número com vírgula: '))
y = float(input('Digite aqui outro número com vírgula: '))

s = x + y
sb = x - y

testeA = s > 10
testeB = s < 0

print(f'Soma: {x:.2f}. Subtração: {y:.2f}')
print(f'A soma é maior que 10? {testeA}')
print(f'A subtração é menor que 0? {testeB}')

# É utilizado -> :.2f  para definir o número de casas decimais terá após o número inteiro

