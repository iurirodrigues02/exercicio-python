import random
from time import sleep

pc_numero = random.randint(0, 5)

print('-=-'*20)

print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR...')

print('-=-'*20)

seu_numero = int(input('Digite um número entre 0 e 5: '))

print('\nPROCESSANDO...\n')

sleep(2)

if seu_numero == pc_numero:

    print('PARABÉNS!! Você adivinhou eu pensei no número {}'.format(pc_numero))

else:
    
    print('GANHEI!! Eu pensei no número {} e não no {}'.format(pc_numero, seu_numero))