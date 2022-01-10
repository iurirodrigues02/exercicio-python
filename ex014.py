import colorama
colorama.init()

celsius = float(input('\033[1;33mTemperatura em °C: '))

print('\033[1;37m=='*25)

print('\033[1;36mA temperatura de {}°C, corresponde a {:.2f}°F'.format(celsius, celsius*1.8+32))

print('A temperatura de {}°C, corresponde a {}K'.format(celsius, celsius+273.15))

print('\033[1;37m=='*25)
