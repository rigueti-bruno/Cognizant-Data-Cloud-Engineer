import ctypes # biblioteca que permite manipularmos objetos nos windows a níveis baixos

atributo_ocultar = 0x02 # valor de atributo que oculta o arquivo/diretório

arq = input('digite o arquivo e extensao:')

retorno = ctypes.windll.Kernel32.SetFileAttributesW(arq, atributo_ocultar) # oculta o arquivo

if retorno: #true
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')