def valid(pergunta, min, max):
    """
    Função que verifica se o número é positivo
    :param pergunta: 
    :param min: 
    :param max: 
    :return: 
    """""
    x = int(input(pergunta))
    while((x < min)) or (x > max):
        x = int(input(pergunta))
    return x

def fatorial(num):
   """
   Função que calcula o fatorial de um número
   :param num:
   :return:
   """

    fat: int = 1
    if num == 0:
        return fat
    for n in range(1, num + 1, 1):
        fat *= n #var acumuladora que vai multiplicando os valores de n
    return fat

x = valid(input("Digite um número:", 0, 9999))
print(f'{x}! = {fatorial(x)}')
 #validação dos dados: somente valores positivos devem ser aceitos

