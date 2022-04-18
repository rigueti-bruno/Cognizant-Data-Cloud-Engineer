# Importar as Bibliotecas "os" e "time":
import os
import time

# Abrir o arquivo de texto:
with open('host.txt') as file:
    dump = file.read() # carrega o arquivo em uma variável
    dump = dump.splitlines() # quebra os registros do arquivo por linha em um array
    for ip in dump:
        print(ip) # imprime cada registro do arquivo
        
    for ip in dump:
        os.system(f'ping -n 2 {ip}') # faz o Ping em cada registro do arquivo
        time.sleep(5) # coloca um tempo de espera entre o Ping em cada registro