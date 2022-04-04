# Podemos não instanciar os parâmetros de valor na função __init__ para informá-los diretamente nas funções:
class Calculadora:
    def __init__ (self): # instancia só o self
        pass # passa só o parâmetro pass
    def soma (self, a, b): # função soma
        return a + b
    def sub (self, a, b): # função sub
        return a - b
    def mult (self, a, b): # função mult
        return a * b
    def div (self, a, b): # função div
        return a / b
    
# Prevenção para os testes não serem importados por outros códigos:
if __name__ == '__main__':
    calc = Calculadora() # atribuição apenas da classe a uma variável

    print(calc.soma(10, 2)) # informando os valores na função soma para executá-la
    print(calc.sub(10, 2)) # informando os valores na função sub para executá-la
    print(calc.mult(10, 2)) # informando os valores na função mult para executá-la
    print(calc.div(10, 2)) # informando os valores na função div para executá-la