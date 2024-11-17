print('Digite o valor das três retas')
r1 = input('Reta 1:')
r2 = input('Reta 2:')
r3 = input('Reta 3:')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
