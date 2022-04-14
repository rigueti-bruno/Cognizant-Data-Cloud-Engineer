# Classe que simula o botão de ligar/desligar de uma televisão:
class Televisao:
    def __init__(self):
        self.ligada = False # inicia como a televisao estivesse desligada
        self.canal = 2 # inicia a televisao no canal 2
    def power (self):
        if self.ligada:
            self.ligada = False # se a televisão estiver liga, desliga
        else:
            self.ligada = True # se a televisão estiver desligada, liga
    
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1 # incrementa o número do canal em 1, se a televisão estiver ligada
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1 # decrementa o número do canal em 1, se a televisão estiver ligada
    
# Prevenção para os testes não serem importados por outros códigos:        
if __name__ == '__main__':
    # Teste do código:
                
    televisao = Televisao() # instancia a classe criada a uma variável

    print(f'Televisão ligada: {televisao.ligada}') # verifica o status - desligada: False
    televisao.power() # aperta o botão power
    print(f'Televisão ligada: {televisao.ligada}') # verifica o status - ligada: True
    televisao.power() # aperta o botão power
    print(f'Televisão ligada: {televisao.ligada}') # verifica o status - desligada: False

    print('...')

    print(f'Canal: {televisao.canal}') # verifica o canal atual
    televisao.power()
    televisao.aumenta_canal() # aumenta 1 canal
    televisao.aumenta_canal() # aumenta 1 canal
    print(f'Canal: {televisao.canal}') # verifica o canal atual
    televisao.diminui_canal() # diminui 1 canal
    print(f'Canal: {televisao.canal}') # verifica o canal atual