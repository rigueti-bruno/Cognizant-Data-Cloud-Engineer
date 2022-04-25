import phonenumbers # biblioteca que permite a manipulação de números de telefone
from phonenumbers import geocoder # método que busca a localização do telefone

phone = input('Digite o número no formato +5599999999999: ') # recebe o número de telefone desejado

phone_number = phonenumbers.parse(phone) # converte o número recebido em número de telefone

print(geocoder.description_for_number(phone_number, 'pt-br')) # imprime a localização do telefone com o idioma indicado (pt-br)