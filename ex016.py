from math import trunc

import random

num1 = float(input('Digite um número com casa decimal: '))

num2 = random.uniform(2.0, 105.2)

print('O seu número digitado é {} e tem parte inteira {}'.format(num1, trunc(num1)))

print('O número escolhido pelo computador é {}, e tem parte inteira {}'.format(num2, trunc(num2)))