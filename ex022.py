nome = str(input('Digite o seu nome completo: ')).strip()

print('\nSeu nome em maiúsculo é:',nome.upper())

print('\nSeu nome em minúscilo é:', nome.lower())

print('\nSeu nome tem ao todo {} letras'.format(len(nome.replace(' ',''))))

nome1 = nome.split()

print('\nSeu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))