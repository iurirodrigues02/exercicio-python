import colorama

colorama.init()

produto = float(input('Digite o valor do produto: '))

print('O valor do produto é \033[1;36mR${:.2f}\033[1;37m. Seu preço com desconto de 5% é \033[1;32mR${:.2f}'.format(produto, produto*0.95))