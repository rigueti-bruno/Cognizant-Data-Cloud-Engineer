import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

host = 'localhost'
porta = 5432

s.bind((host, porta)) # liga o servidor ao client UDP - sendo bem sucedida, retorna True

mensagem = '\nServidor: Olá cliente.' # mensagem a ser enviada ao cliente

while 1: # conexão do bind bem sucedida: True = 1
    dados, endereco = s.recvfrom(4096) # solicita 4096 bytes ao cliente
    if dados: # caso a variável dados receba os bytes do cliente
        s.sendto(dados + (mensagem.encode()), end) # envia a mensagem para o cliente