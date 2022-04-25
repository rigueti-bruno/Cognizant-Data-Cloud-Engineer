# Cálculo de Média Ponderada de Notas:

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
        
while True:
    try:
        a = float(input('Nota 1: Insira um valor entre 0 e 10: '))
        if a > 10: 
            raise InputError('Nota não pode ser maior que 10.')
        elif a < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números')
    except InputError as ex:
        print(ex)
        
while True:
    try:
        b = float(input('Nota 2: Insira um valor entre 0 e 10: '))
        if b > 10: 
            raise InputError('Nota não pode ser maior que 10.')
        elif b < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números')
    except InputError as ex:
        print(ex)
        
media = round(((a * 3.5 + b * 7.5) / 11), 5)

print(f'MEDIA = {media}', end='')