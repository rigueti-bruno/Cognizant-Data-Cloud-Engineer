# Contar as letras das palavras de uma lista:
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    m = 0
    for i in contador:
        m += i
    return m

if __name__ == "__main__":
    a = ['batman','super', 'frodo']
    b = contador_letras(a)
    print(b)