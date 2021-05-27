import math
import colorama
colorama.init()

n1 = int(input('Digite um número inteiro: '))

print('\033[33;40mO dobro de \033[35m{}\033[33;40m é \033[35m{}\033[33;40m, seu triplo é \033[35m{}\033[33;40m e sua raiz é aproximadamente \033[35m{:.2f}'.format(n1, n1*2, n1*3, math.sqrt(n1)))