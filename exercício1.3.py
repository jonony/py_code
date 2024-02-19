#
#? Exercício 3
#* Desenvolva um algoritmo que solicite ao usuário o preço de um produto
#* e um percentual de desconto a ser aplicado a ele
#* Calcule e exiba esse valor do desconto e o preço final do produto
#

preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o perventual a ser aplicado (0/100%): '))

p = preco * (percentual/100)
total = preco - p

print(f'O preço do produto é R$ {preco}. Desconto a ser aplicado é {percentual}')
print(f'O valor do desconto cálculado foi {p}%')
print(f'O total a ser pago será de R${total}')
