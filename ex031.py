import colorama
colorama.init()

distancia = float(input('Digite a distância à ser viajada: '))

print('\nVocê estar preste a fazer sua viagem de {:.2f}km\n'.format(distancia))

if distancia <= 200:
    print('\033[1;32mO preço de sua passagem será: R${:.2f}\n'.format(distancia*0.50))
else:
    print('\033[1;33mO preço de sua passagem será: R${:.2f}\n'.format(distancia*0.45))