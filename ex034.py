salario = float(input('Digite o valor do salário: '))

if salario <= 1250.00:
    print('\nO aumento de seu salário é de 10%, portanto seu novo valor é {:.2f}\n'.format(salario*1.10))
else:
    print('\nO aumento de seu salário é de 15%, portanto seu novo valor é {:.2f}\n'.format(salario*1.15))