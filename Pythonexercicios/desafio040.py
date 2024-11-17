# Calcule a média do aluno e mostre a mensagem no final de acordo com a média
print('Vamos ver como você se saiu nesse bimestre:')
n1 = float(input('Sua primeira nota:'))
n2 = float(input('Sua segunda nota:'))
m = (n1 + n2)/2
#abaixo de 5.0: reprovado
if m < 5.0:
    print('Sua média é {}.Você foi reprovado.'.format(m))
#entre 5.0 e 6.9: recuperação
elif 5.0 <= m < 6.9:
    print('Sua média é {}. Você está de recuperação.'.format(m))
#7.0 ou superior: aprovado
else:
    print('Sua média é {}. Parabéns! Você foi aprovado.'.format(m))
