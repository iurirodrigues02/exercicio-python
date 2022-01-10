import math

ang = float(input('Digite o valor de um ângulo: '))

seno = math.sin(math.radians(ang))

cosseno = math.cos(math.radians(ang))

tangente = math.tan(math.radians(ang))

print('O ângulo de {}°, tem seno igual a {:.4f}, cosseno igual a {:.4f} e tangente igual a {:.4f}'.format(ang, seno, cosseno, tangente))

# A tangente do ângulo de 90° é inexistente, porém, o computador devolve um resutaldo inexpressível