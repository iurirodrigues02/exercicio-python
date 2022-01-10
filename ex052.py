primos = int(input('Digite um número inteiro: '))

cont = 0

for i in range(1, primos + 1):

    if primos % i == 0:

        cont +=1

if cont == 2:

    print('O número {} é primo'.format(primos))

else:
    
    print('O número {} não é primo'.format(primos))
