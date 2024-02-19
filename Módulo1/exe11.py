nome = input('Digite aqui o seu nome: ')
idade = input('Qual a sua idade? ')

frase = f'Olá {nome}! Como vai? Você possui {idade} anos de idade, seja bem vindo :)'
print(frase)



# O python em si identifica quaalquer número digitado como uma string, para isso devemos tratr esse dado para que ele possa ser tratado como realmente um número, para realizar cálculos maatemáticos
# Se usassemos o seguinte código:

'''

num1 = input('Digite aqui um número: 5')
num2 = input('Digite aqui outro número 1')

print(n1 + n2)

-> Esse resultado seria 51 pois estamos somando uma String na outra, para corrigirmos esse problema, devemos usar o seguinte código para conversão:
Lembrando;

int de número inteiro e float de ponto flutuante

'''



num1 = int(input('Digite aqui um número: '))
num2 = int(input('Digite aqui outro número: '))
soma = num1 + num2
print(f'A soma de {num1} e {num2} é: {soma}')

