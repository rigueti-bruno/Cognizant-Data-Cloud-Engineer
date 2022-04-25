import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url): # define o web crawler - recebe a URL do site
    wordlist = [] # receberá o conteúdo da URL
    
    source_code = requests.get(url).text # faz a requisição do conteúdo do site
    
    soup = BeautifulSoup(source_code, features="html.parser") # converte a requisição em conteúdo HTML
    
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text # vai transformar o conteúdo HTML em string onde houver a tag div
        
        words = content.lower().split() # vai colocar o conteúdo em letras minúsculas e vai quebrá-lo em linhas
        
        for each_word in words:
            wordlist.append(each_word) # incluí o conteúdo extraído na wordlist
            
        clean_wordlist(wordlist) # remove os símbolos do conteúdo da wordlist
        

def clean_wordlist(wordlist):
    clean_list = [] # receberá o conteúdo limpo da wordlist
    
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={}[]|\;:"<>/., ' # indica os símbolos que serão buscados
        
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '') # troca os símbolos por espaços vazios ''
            
        if len(word) > 0:
            clean_list.append(word) # adiciona a palavra à clean_list se ela não for um espaço vazio
            
    create_dictionary(clean_list) # cria um dicionário com as palavras da clean_list
    

def create_dictionary(clean_list):
    word_count = {} # receberá o dicionário com as palavras e suas contagens
    
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1 # incrementa em 1 a contagem da palavra caso ela seja encontrada novamente na clean_list
        else:
            word_count[word] = 1 # se for a primeira vez que a palavra for encontrada, conta 1
            
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print('%s : %s' %(key, value)) # constrói o dicionário com as palavras encontradas (key) e suas contagens (value)
        
    c = Counter(word_count) # conta as palavras e as ordena
    
    top = c.most_common(10) # armazena as 10 palavras que mais são encontradas no dicionário
    
    print(top) # imprime as 10 palavras que aparecem mais
    

if __name__ == '__main__':
    url = input('Insira a URL do site: ')
    start(url)