import colorama

colorama.init()

valor_da_casa = int(input('QUAL O VALOR DA CASA A SER COMPRADA? R$'))

salário = float(input('QUAL O VALOR DO SEU SALÁRIO? R$'))

quantos_anos = float(input('EM QUANTOS ANOS VOCÊ QUER PAGAR O EMPRÉSTIMO? '))

parcelas_mensais = quantos_anos*12

valor_do_empréstimo = (valor_da_casa/parcelas_mensais)*1.03

if valor_do_empréstimo <= salário*0.30:

    print('\n\033[1;32mSEU EMPRÉSTIMO FOI APROVADO!!')

    print('\033[1;33mO VALOR DO EMPRÉSTIMO FICOU R${:.2f} DE {:.0f} PARCELAS\n'.format(valor_do_empréstimo, parcelas_mensais))

elif valor_do_empréstimo > salário*0.30:

    print('\n\033[1;31mSEU EMPRÉSTIMO FOI REPROVADO!!')
    
    print('\033[1;33mFOI REPROVADO PORQUE O VALOR DO EMPRÉSTIMO É MAIOR DO QUE 30% DO SEU SALÁRIO. Valor do empréstimo R${:.2f} e 30% do seu salario é R${:.2f}\n'.format(valor_do_empréstimo, salário*0.30))
