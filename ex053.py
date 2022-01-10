import colorama

colorama.init()

frase = str(input('Digite uma palavra ou frase: ')).upper().replace(' ','')

invertida = ''.join(palavra[::-1]for palavra in frase.split())

print(invertida)

if invertida == frase:

    print('Essa frase ou palavra é um \033[1;32mpalíndromo')

else:
    
    print('Essa frase não é um \033[1;31mpalíndromo')
