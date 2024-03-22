#cateto oposto   cateto adjacente    hipotenusa= ca**2 + co**2== h**2
from math import sqrt
co = float(input('Qual o valor do cateto oposto:'))
ca = float(input('Qual o valor do cateto adjacente:'))
h = (sqrt(ca**2 + co**2))
print('O valor da hipotenusa é: {}'.format(h))
#h = math.hypot(co, ca)
