import calendar
ano = int(input('Digite o ano:'))
r = calendar.isleap(ano)
print('O ano {} é bissexto? {}'.format(ano, r))
#from datetime import date
#if ano == 0:
# ano = date.today().year
#parar pegar o ano atual da máquina