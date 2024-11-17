print('Vamos ver como está seu IMC. Coloque suas informações abaixo:')
peso = float(input('Informe seu peso em kg:'))
alt = float(input('Informe sua altura em m:'))
imc = peso / (alt**2)
if imc < 18.5:
    print('Seu IMC é : {:.2f}.Você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25.0:
    print('Seu IMC é: {:.2f}.Você está no PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é: {:.2f}. Você está no SOBREPESO.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é: {:.2f}.Você está em OBESIDADE.'.format(imc))
elif imc > 40:
    print('Seu IMC é: {:.2f}.Você está em OBESIDADE MÓRBIDA.'.format(imc))
