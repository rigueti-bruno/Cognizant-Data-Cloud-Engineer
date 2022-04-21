import itertools # biblioteca que fornece condições para fazer iterações com caracteres, como combinações e permutações

string = input('Digite a palavra a ser permutada: ')

resultado = itertools.permutations(string, len(string)) # recebe o método que fará as permutações dos caracteres das strings informadas (string) pelo número de permutações (len(string))

for i in resultado:
    print(''.join(i)) # gerará e imprimirá cada palavra gerada pela permutação, recebendo cada caracter e adicionando até formar as palavras na quantidade de permutações informadas