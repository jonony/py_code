init = int(input('Digie um número para se iniciar: '))
final = int(input('Digite um número para finalizar: '))

i = init
while(i <= final):
    if(i % 2 == 0):
        print(i)
    i = i + 1

