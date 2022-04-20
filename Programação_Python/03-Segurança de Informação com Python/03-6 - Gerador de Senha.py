import random # importa a biblioteca que numeros, letras e simbolos aleatorios
import string # importa a biblioteca que viabliza operações com strings

tamanho = int(input('digite o tamanho da senha: ')) # define o tamanho da senha a ser criada - as boas práticas recomendam 16

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+.' # especifica a estrutura da senha a ser criada com letras (string.ascii_letters), numeros (string.digits) e simbolos ('!@#$%&*()-=+.')

rnd = random.SystemRandom() # gera códigos aleatórios a partir de fontes fornecidas pelo sistema

print(''.join(rnd.choice(chars) for i in range(tamanho))) # gera e imprime uma senha aleatória com os critérios especificados