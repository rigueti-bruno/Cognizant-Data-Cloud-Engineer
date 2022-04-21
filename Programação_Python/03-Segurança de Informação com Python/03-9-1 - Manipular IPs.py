import ipaddress # biblioteca que permite manipular e realizar cálculos com IPs e redes

ip = '192.168.0.1' # a variável recebe um IP no formato string

endereco = ipaddress.ip_address(ip) # converte a string em um endereço IP

print(endereco) # imprime o IP informado

print(endereco + 256) # adiciona 256 ao IP e gera um número de IP novo