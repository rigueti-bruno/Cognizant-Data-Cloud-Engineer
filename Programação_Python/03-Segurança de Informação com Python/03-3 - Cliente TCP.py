def main():
    import socket # cria a relação com o sistema e a placa de rede
    import sys # fornece o acesso a algumas variáveis e funções relacionadas ao interpretador python
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # cria o objeto com a família (socket.AF_INET), tipo (socket.SOCK_STREAM) e protocolo de conexão (0 - TCP)
    except socket.error as e: # tratamento de erro
        print('A conexão falhou')
        print(f'Erro: {e}')
        sys.exit()
    
    print('Socket criado com sucesso.')
    
    hostalvo = input('Informe o host ou IP a ser conectado: ')
    portaalvo = input('Informe a porta a ser conectada: ')
    
    try:
        s.connect((hostalvo, int(portaalvo))) # cria a conexão com o host informado na porta informada
        print(f'Cliente TCP conectado com sucesso no host {hostalvo} e na porta {portaalvo}.') # mensagem para conexão bem sucedida no host
        s.shutdown(2) # finaliza a conexão após 2 segundos para que ela não fique em loop
    except socket.error as e: # tratamento de falha de conexão no host
        print(f'A conexão com o host {hostalvo} na porta {portaalvo} falhou.')
        print(f'Erro: {e}')
        sys.exit()

if __name__ == "__main__":
    main() # executa a função do Cliente TCP
    # Caso a conexão ao TCP seja bem sucedida, será solicitado o Host e a Porta para conexão