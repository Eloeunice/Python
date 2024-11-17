from datetime import date
birth = int(input('Em qual ano você nasceu:'))
data = date.today().year
t = data - birth
f = 18 - t
p = t - 18
if t < 18:
    print('Você tem {} anos em 2024.Falta {} anos para você se alistar.'.format(t,f))
elif t == 18:
    print('Você tem 18 anos. Está na hora de se alistar.')
elif t > 18:
    print('Você tem {} anos. Já passou {} anos para você se alistar.'.format(t, p))
