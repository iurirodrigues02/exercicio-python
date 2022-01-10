import colorama

colorama.init()

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

print('\033[1;32mA soma enteo o número: \033[1;36m{} \033[1;32me o número: \033[1;36m{} \033[1;32m é igual a: \033[1;36m{}'.format(n1,n2,n1+n2))
