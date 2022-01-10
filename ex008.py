medida = float(input('Digite um valor: ')) # A variavel medida estar representando o valor em metros

print('--'*18)

print('O valor em Quilômetro é {:.3f}. \nO valor em Hectômetro é {:.3f}. \nO valor em Decâmetro é {:.3f}'.format(medida/1000, medida/100, medida/10))

print('=='*18)

print('O valor em decímetro é {:.3f}. \nO valor em centímetro é {:.3f}. \nO valor em milímetro é {:.3f}'.format(medida*10, medida*100, medida*1000))

print('--'*18)