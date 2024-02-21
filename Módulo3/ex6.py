#
#? EXERCÍCIO 3
#* Um aluno, para passar de ano, precisa estar aprovado em todas maatérias que ele está cursando.
#* Assuma que média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
#* Escreva um algoritmo que leia a nota final do aluno em cada matérias, e informe na tela se ele possou de ano, ou não.
#

nota1 = float(input('Digite aqui a sua primeira nota do semestre: '))
nota2 = float(input('Digite aqui a sua segunda nota do semestre: '))
nota3 = float(input('Digite aqui a sua terceira nota do semestre: '))

if(nota1 >= 7) and (nota2 >= 7) and (nota3 >= 7):
    print('Aluno aprovado de ano')
else:
    print('Aluno reprovado')
    
