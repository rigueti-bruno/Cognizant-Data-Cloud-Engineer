# Importa a Biblioteca "os":
import os

# Inicializa uma variável que receberá o IP/Host que será verificado:
x = input('Digite o IP/Host que será verificado: ')

# Carrega o comando Ping do sistema que realizará a verificação:
os.system(f'ping -n 6 {x}')