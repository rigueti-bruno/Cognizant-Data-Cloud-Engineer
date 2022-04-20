import socket # cria a conexão com o sistema e a placa de rede

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria o objeto de conexão com a família "socket.AF_INET" e tipo "socket.SOCK_DGRAM" - Datagrama

print('Cliente Socket criado com sucesso.')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432)) # empacota (encode) e envia (sendto) a mensagem para o servidor
    
    dados, servidor = s.recvfrom(4096) # solicita 4096 bytes ao servidor e armazena nas variaveis dados e servidor
    dados = dados.decode() # desempacota os bytes recebidos do servidor
    print(f'Cliente: {dados}') # exibe os dados recebidos e enviados para o servidor
finally:
    print('Cliente: fechando a conexão.')
    s.close() # finaliza a conexão com o servidor para que não fique em loop