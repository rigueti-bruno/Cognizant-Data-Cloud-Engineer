from bs4 import BeautifulSoup # biblioteca que permite extrair dados de HTML e XML
import requests # permite o envio de solicitações HTTP

site = requests.get("https://www.climatempo.com.br/").content # conecta ao site (.get) e coleta seu conteúdo (.content)

soup = BeautifulSoup(site) # baixa o conteúdo do site no formato HTML e o armazena na variável

print(soup.prettify()) # formata o html baixado (.prettify) e o imprime