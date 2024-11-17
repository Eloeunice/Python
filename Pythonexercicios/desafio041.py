from datetime import date
data = date.today().year
birth = int(input('Digite o ano de seu nascimento:'))
t = data - birth
if t <= 9:
    print('Você tem {} anos.Sua categoria é MIRIM.'.format(t))
elif 9 < t <= 14:
    print('Você tem {} anos.Sua categoria é INFANTIL.'.format(t))
elif 14 < t <= 19:
    print('Você tem {} anos.Sua categoria é JÚNIOR.'.format(t))
elif 19 < t <= 20:
    print('Você tem {} anos.Sua categoria é SÊNIOR.'.format(t))
elif t > 20:
    print('Você tem {} anos.Sua categoria é MASTER.'.format(t))
