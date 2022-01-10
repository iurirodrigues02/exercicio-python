from datetime import date

ano_nascimento = int(input('Informe o seu ano de nascimento: '))

ano_atual = date.today().year

idade = abs(ano_nascimento - ano_atual)

alistamento = int(18)

if idade < alistamento:

    print('Você irá se alistar daqui {} anos. O Exército lhe espera :)'.format(abs(idade-alistamento)))

elif idade > alistamento:

    print('Já passou da sua hora de alistar, você atrasou - se em {} anos'.format(abs(idade-alistamento)))

else:
    
    print('Esse é o seu ano de alistamento')