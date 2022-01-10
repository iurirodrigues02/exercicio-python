import colorama
colorama.init()

kelvin = float(input('\033[1;33mTemperatura em K: '))

print('\033[1;37m=='*25)

print('\033[1;35mA temperatura de {}K, corresponde a {:.2f}°C'.format(kelvin, kelvin-273.15))

print('A temperatura de {}K, corresponde a {:.2f}°F'.format(kelvin, (kelvin*1.8)-459.67))

print('\033[1;37m=='*25)
