import hashlib # importa a biblioteca hashlib

arquivo1 = 'a.txt'
                    # Carrega nas variáveis os arquivos a serem comparados
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') # cria a primeira hash informando o algoritmo de criação dela - ripemd160 (algoritmo hash de 160 bits)

hash1.update(open(arquivo1, 'rb').read()) # atribui o primeiro arquivo à hash criada

hash2 = hashlib.new('ripemd160') # cria a hash para o segundo arquivo - deve ser do mesmo algoritmo da primeira

hash2.update(open(arquivo2, 'rb').read()) # atribui o segundo arquivo à segunda hash criada

# Estrutura que irá comparar as Hashes:

if hash1.digest() != hash2.digest(): # o método digest() resume os valores gerados pelo método update() nas hashes
    print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2}.')
else:
    print(f'O arquivo {arquivo1} é igual ao arquivo {arquivo2}.')