#
#? Exercicio 4
#* Escreva um algoritmo que lê um valor inteiro qualquer.
#* Após verifique se este valor está contido dentro dos seguintes intervalos: -100 < x < -1 ou 1 < x < 100.
#* Imprima na tela caso ele esteja em um dos intervalos.
#

x = int(input('Digite aqui um número inteiro: '))

if((x > 1) and (x < 100)) or ((x < -1) and (x > -100)):
    print('Um dos critérios foi atingido')

    