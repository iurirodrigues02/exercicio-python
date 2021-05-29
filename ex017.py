from math import hypot

cta = float(input('Digite o valor do cateto adjacente: '))
cto = float(input('Digite o valor do cateto oposto: '))

print('A hipotenusa é {:.2f}'.format(hypot(cta, cto)))
