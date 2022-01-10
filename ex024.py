cidade = str(input('Digite o nome de uma cidade: ')).strip().upper().split()

print("\nEssa cidade começa com SANTO?", 'SANTO' in cidade[0])

print('\n')

print((' ').join(cidade).title())
