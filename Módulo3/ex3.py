#
#? EXERCÍCIO 1
#* Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela 
#* Para fins de simplificação, despreze o dia e o mês do ano.
#* Após o cálculo, verifique se a idde é maior a 18 anos e apresente na tela uma mensagem.
#* Informando que já é possível tirar a carteira de motorista caso seja maior.
#

ano_nascimento = int(input('Digite aqui o seu ano de nascimento: '))
ano_atual = int(input('Digite aqui o ano atual: '))

idade = ano_atual - ano_nascimento

print(f'Você possui {idade} anos de idade.')

if(idade >= 18):
    print('Você já pode tirar a sua carteira')
else:
    print('Você é de menor, infelizmente ainda não pode tirar a sua carteira')


