print('PAGAMENTO')
print('1 - a vista')
print('2 - parcelamento em 3x')
print('3 - parcelamento em 5x')
print('4 - parcelamento em 10x')
print('precisone outra tecla para sair...')

op = int(input('Qual a forma de pagamento deseja fazer? '))
valor = float(input('Qual foi o valor da compra? '))

if(op == 1):
    valor_final = valor * 0.95
    print(f'Produto comprado à vista. Total a pagar: R${valor_final}')
elif(op == 2):
    valor_final = valor 
    parcela = valor_final / 3
    print(f'Produto comprado parcelado em 3x. Total a pagar: R${valor_final:.2f} / Total da parcela R${parcela:.2f}')
elif(op == 3):
    valor_final = valor * 1.02
    parcela = valor_final / 5
    print(f'Produto comprado parcelado em 5x. Total a pagar: R${valor_final:.2f} / Total da parcela R${parcela:.2f}')
elif(op == 4):
    valor_final = valor * 1.08
    parcela = valor_final / 10
    print(f'Produto comprado parcelado em 10x. Total a pagar: R${valor_final:.2f} / Total da parcela R${parcela:.2f}')
else:
    print('Essa opção está inválida')