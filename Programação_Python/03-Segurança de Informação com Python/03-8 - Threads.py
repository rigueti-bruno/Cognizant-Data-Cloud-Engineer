# As funções são executadas simultâneamente:

from threading import Thread # importação da classe Thread da biblioteca threading
import time # importação da biblioteca time

def carro(velocidade, piloto): # uma única função a ser executada
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5) # diferencia as execuções simultâneas
        print(f'Piloto: {piloto} KM: {trajeto} \n')
        
t_carro1 = Thread(target=carro, args=[1, 'Bruno']) # thread da primeira execução da função
t_carro2 = Thread(target=carro, args=[2, 'Python']) # thread da segunda execução da função

t_carro1.start()
                    # Execuções da função simultâneas - quando o Piloto de velocidade maior chegar a 100, ele pára e só o outro executa
t_carro2.start()