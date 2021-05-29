from time import sleep

num = int(input('Digite um número inteiro de 0 a 9999: '))
num2 = str(int(10000 + num))

print('\nAnalisando número\n')

sleep(2)

print('O número {}.\nPossui:\n{} unidade\n{} dezenas\n{} centenas\n{} milhares'. format(num, num2[-1], num2[-2], num2[-3], num2[-4]))