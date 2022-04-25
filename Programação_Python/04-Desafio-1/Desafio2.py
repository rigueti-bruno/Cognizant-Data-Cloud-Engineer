lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
    #TODO Preencha a formula do perímeto do triangulo (soma de todos os lados).
    perimetro = round((a + b + c), 1)
    print(f"Perimetro = {perimetro}")
else:
    #TODO Preencha a formula da área do trapézio: AREA = ((A + B) x C) / 2
    trapezio = round((((a + b) * c) / 2), 1)
    print(f"Area = {trapezio}")