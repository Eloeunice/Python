sal = float(input('Qual o valor do seu salário: R$'))
if sal > 1249:
    a = (sal * 0.10) + sal
    print('O valor atualizado do seu salário é:R${}'.format(a))
else:
    a2 = (sal * 0.15) + sal
    print('O valor atualizado do seu salário é:R${}'.format(a2))
