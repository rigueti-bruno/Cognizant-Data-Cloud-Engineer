def mover(nome_arquivo):
    import shutil # importa a biblioteca com as funções de movimentação de arquivos "shutil"
    shutil.move(nome_arquivo, 'C:\Github\Cognizant-Data-Cloud-Engineer\Programação_Python\Introdução à Programação com Python/')
    
a = input('Nome do arquivo: ')
mover(a)