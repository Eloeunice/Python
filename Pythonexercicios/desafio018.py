import math
ang = int(input('Digite o valor do ângulo:'))
rad = math.radians(ang)
sin = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)
print('O ângulo {} tem seno {:.2f},cosseno {:.2f} e tangente {:.2f}'.format(ang, sin, cos, tang))
