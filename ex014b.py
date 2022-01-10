import colorama
colorama.init()

fahrenheit = float(input('\033[1;33mTemperatura em °F: '))

print('\033[1;37m=='*25)

print('\033[1;32mA temperatura de {}°F, corresponde a {:.2f}°C'.format(fahrenheit, (fahrenheit-32)/1.8))

print('A temperatura de {}°F, corresponde a {:.2f}K'.format(fahrenheit, (fahrenheit-32)/1.8+273.15))

print('\033[1;37m=='*25)
