import colorama

colorama.init()

r1 = int(input('Digite o tamanho da reta 1: '))

r2 = int(input('Digite o tamanho da reta 2: '))

r3 = int(input('Digite o tamanho da reta 3: '))

if (abs(r2 - r3)) < r1 < (r2 + r3) and (abs(r1 - r3)) < r2 < (r1 + r3) and (abs(r1 - r2)) < r3 < (r1 + r2):

    print('\nEssas retas formam um triângulo\n')

    if r1 == r2 and r1 == r3 and r2 == r3:

        print('Esse triângulo é \033[1;31mEQUILÁTERO\n')

    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:

        print('Esse triângulo é \033[1;33mISÓSCELES\n')

    elif r1 != r2 and r1 != r3 and r2 != r3: 

        print('Esse triângulo é \033[1;36mESCALENO\n')

else:
    
    print('\nEssas retas não formam um triângulo\n')