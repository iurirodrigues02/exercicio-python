from datetime import date

ano = int(input('Digite ''0'' para usar o ano atual: '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('ANO {}, É BISSEXTO'.format(ano))
else:
    print('O ANO {}, NÃO É BISSEXTO'.format(ano))
