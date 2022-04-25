import webbrowser
from tkinter import * # carrega todos os métodos e classes do Tkinter

root = Tk( ) # cria o objeto que representará a tela em si, deve ter um espaço no meio dos () e não tem nome

root.title('Abrir Browser') # define o título da janela
root.geometry('300x200') # define as dimensões da janela

def google(): # define a função que será executada pela janela
    webbrowser.open('www.google.com.br') # abre a url especificada

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20) # cria um botão na janela onde root = janela, text = título do botão, command = função que será executada, pack(pady=) = posição do botão

root.mainloop() # método que abre a janela para ser utilizada