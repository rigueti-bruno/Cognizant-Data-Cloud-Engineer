# Importa o módulo de outro arquivo:
import aula7

# Instancia uma classe do modulo importado:
televisao = aula7.Televisao()

# Executa métodos/funções da Classe importada:
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

# Importar apenas uma classe específica de um módulo:

from aula7_1 import Calculadora

calc = Calculadora()

print(calc.soma(20, 45))

# Importando um método de outro módulo:

from aula8_letras import contador_letras as cl

a = ['ovo', 'galinha']
b = cl(a)
print(f'Total de letras da lista: {b}')

