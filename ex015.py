from time import sleep

import colorama

colorama.init()

km = float(input('Quantos quilômetros o carro rodou? '))

dias = int(input('Quantos dias o carro rodou? '))

print('''\n\033[1;32mA cada quilômetro rodado é cobrado R$0.15
A cada dia rodado é cobrado R$60.00\n''')

sleep(1)

print('\033[1;33mO carro rodou {} quilômetros, durante {} dias, portanto o valor do aluguel a pagar é R${:.2f}\n'.format(km, dias, (dias*60+0.15*km)))