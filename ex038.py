import colorama
colorama.init()

n1 = float(input('Digite um número decimal qualquer: '))
n2 = float(input('\nDigite um número decimal qualquer: '))

if n1 > n2:
    print('O \033[1;33mprimeiro valor é \033[1;34mmaior')
elif n2 > n1:
    print('O \033[1;33msegundo valor é \033[1;34mmaior')
else:
     print('\033[1;33mNão existe valor maior, os dois são \033[1;34miguais')