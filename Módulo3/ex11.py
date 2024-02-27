#
#? Exercício 8
#* Escreva um algoritimo que leia dois valores númericos e que pergunte ao usuário qual operação ele deseja realizar:
#* Adição (+), subtração (-), multiplicação (*) ou divisão. Exiba na tela o resultado da operação desejada.
#


print('CALCULADORA')
print('+ Soma')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite outra tecla para sair: ')

op = input('Qual operação deseja realizar? ')
x1 = float(input('Digite o primeiro número: '))
y2 = float(input('Digite o segundo valor: '))

if(op == '+' ):
    res = x1 + y2
    print(f'Resultado de {x1} + {y2} = {res:.2f}')
elif(op == '-'):
    res = x1 - y2
    print(f'Resultado de {x1} - {y2} = {res:.2f}')
elif(op == '*'):
    res = x1 * y2
    print(f'Resultado de {x1} * {y2} = {res:.2f}')
elif(op == '/'):
    res = x1 / y2
    print(f'Resultado de {x1} / {y2} = {res:.2f}')
else:
    print('Finalizando cálculos')