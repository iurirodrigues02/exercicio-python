reta1 = int(input('Digite o tamanho da reta 1: '))
reta2 = int(input('Digite o tamanho da reta 2: '))
reta3 = int(input('Digite o tamanho da reta 3: '))

if (abs(reta2 - reta3)) < reta1 < (reta2 + reta3) and (abs(reta1 - reta3)) < reta2 < (reta1 + reta3) and (abs(reta1 - reta2)) < reta3 < (reta1 + reta2):
    print('Essas retas formam um triângulo')
else:
    print('Essas retas não formam um triângulo')