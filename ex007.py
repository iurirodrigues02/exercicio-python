import colorama

colorama.init()

nome = str(input('Digite um nome: '))

nota1 = float(input('Digite a primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))

if (nota1 + nota2)/2 > 5.9:

    print('\033[1;36mAluno(a) \033[1;37m{}\033[1;36m, teve a primeira nota {} e a segunda {}, portanto sua média é --> {:.1f}'.format(nome, nota1, nota2, (nota1 + nota2)/2))
    
else:

    print('\033[1;31mAluno(a) \033[1;37m{}\033[1;31m, teve a primeira nota {} e a segunda {}, portanto sua média é --> {:.1f}'.format(nome, nota1, nota2, (nota1 + nota2)/2))