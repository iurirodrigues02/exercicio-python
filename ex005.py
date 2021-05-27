import colorama
colorama.init()

n1 = int(input('Digite um número inteiro: '))

print('\033[1;36mO número \033[1;31m{}\033[1;36m, tem sucessor \033[1;31m{}\033[1;36m e antecesor \033[1;31m{}'.format(n1, n1+1, n1-1))