import colorama

colorama.init()

nome = str(input('Digite o seu nome completo: '))

print('\033[1;34mÉ um prazer lhe conhecer, {}'.format(nome))
