num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
if num1 > num2 and num1 > num3:
    print('\nO primeiro número é maior\n')
if num2 > num1 and num2 > num3:
    print('\nO segundo número é maior\n')
if num3 > num1 and num3 > num2:
    print('\nO terceiro número é maior\n')
else:
    print('\nTodos os números são iguais\n')