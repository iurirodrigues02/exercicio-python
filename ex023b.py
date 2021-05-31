from time import sleep

num = int(input('Digite um número de 0 à 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('\nAnalisando o número {}'.format(num))

sleep(1)

print('\nEle possui:\nUnidades: {}\nDezenas: {}\nCentenas: {}\nMilhares: {}'.format(u, d, c, m))