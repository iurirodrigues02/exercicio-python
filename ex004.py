import colorama
colorama.init()

n = input('Digite qualquer coisa: ')

print(n)
print('\033[31mQual o seu tipo primito?', type(n))
print('\033[1;33mÉ um número?', n.isnumeric()); print('\033[1;33mÉ um alfabetico?', n.isalpha())
print('\033[1;33mEstá minúsculo:', n.islower()); print('\033[1;33mEstá maiúsculo?', n.isupper())
print('\033[1;33mSó tem espaço?', n.isspace()); print('\033[1;33mÉ um alfanúmerico?', n.isalnum())