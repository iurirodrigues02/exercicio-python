frase = str(input('Digite uma frase: ')).strip().upper()

print('\nA letra (''A'') aparece: {} vezes'.format(frase.count('A')))
print('\nA letra ''A'' aparece primeiramente na posição {}'.format(frase.find('A')+1))
print('\nA letra ''A'' aparece a ultima vez na posição {}\n'.format(frase.rfind('A')+1)) 