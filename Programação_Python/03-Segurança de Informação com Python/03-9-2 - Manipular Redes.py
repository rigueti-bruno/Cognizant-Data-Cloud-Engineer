import ipaddress

ip = '192.168.0.0/24' # atribui à string uma refencia de rede no formato string

rede = ipaddress.ip_network(ip) # converte a string em uma referência de rede

print(rede) # imprime a referencia de rede

ip2 = '192.168.0.0/24'
rede2 = ipaddress.ip_network(ip2, strict=False) # strict=False - permite que a rede seja identificada de forma correta mesmo se o IP estiver fora do padrão
for ip in rede2: # vai imprimir todos os IPs da Rede 16
    print(ip)