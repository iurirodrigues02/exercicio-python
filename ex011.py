largura = float(input('Digite o valor da largura: '))
altura = float(input('Digite o valor da altura: '))

print('A parede tem uma largura de {} metros, e uma altura de {} metros, possuindo uma área de {:.2f}m², portanto, são necessaria {:.2f} litros de tinta'.format(largura, altura, largura*altura, (largura*altura/2)))

# Um litro de tinta pinta 2m² de parede