print('Qual fruta deseja comprar? ')
print('1 - Banana')
print('2 - Laranja')
print('3 - Melancia')
produto = int(input('Qual a sua ecolha? '))
qtd     = int(input('Quantas unidades deseja comprar? '))

if(produto == 1):
    pagar = qtd * 2.30
    print(f'Você selecionou {qtd} maçãs e irá pagar R${pagar:.2f}')
else:
    if(produto == 2):
        pagar = qtd * 1.75
        print(f'Você selecionou {qtd} laranjas e irá pagar R${pagar:.2f}')
    else:
         if(produto == 3):
            pagar = qtd * 2.70
            print(f'Você selecionou {qtd} melancias e irá pagar R${pagar:.2f}')
         else:
             print('Produto inexistente')
