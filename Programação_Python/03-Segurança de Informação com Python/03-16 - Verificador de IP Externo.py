import re # biblioteca que permite a utilização de expressões regulares - regex
import json # biblioteca que permite a manipulação de arquivos .json
from urllib.request import urlopen # classe que permite o carregamento de URLs no código

url = 'https://ipinfo.io/json' # recebe a string da URL

resposta = urlopen(url) # abre a URL no código

dados = json.load(resposta) # carrega os dados em javascript da URL

# Extração dos dados da URL - indica a [key], armazena o value na variável
ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP Externo:')
print(f'IP: {ip} \nEstado: {regiao} \nPaís: {pais} \nCidade: {cid} \nOrganização: {org}')