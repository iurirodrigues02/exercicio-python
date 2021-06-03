import colorama
colorama.init()

velocidade = int(input('A velocidade do carro registrada no RADAR foi: '))

if velocidade > 80:
    print('\033[1;33mMULTADO. Você excedeu o limite permitido da rodovia de 80km/h')
    print('Você deve pagar uma multa de: \033[1;31mR${:.2f}'.format((velocidade-80)*7))