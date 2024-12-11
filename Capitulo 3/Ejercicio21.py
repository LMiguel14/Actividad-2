import math

def confirmar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:

      perimetro = calcular_perimetro(a, b, c)
      semiperimetro = calcular_semiperimetro(a, b, c)
      area = round(calcular_area(a, b, c),3)
      print(f"Perímetro: {perimetro}")
      print(f"Semiperímetro: {semiperimetro}")
      print(f"Área: {area}")

    else:
        print("Los lados no pueden formar un triangulo")

def calcular_perimetro(a, b, c):
    return a + b + c

def calcular_semiperimetro(a, b, c):
    perimetro = calcular_perimetro(a, b, c)
    return perimetro / 2

def calcular_area(a, b, c):
    s = calcular_semiperimetro(a, b, c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Introduce el lado a: "))
b = float(input("Introduce el lado b: "))
c = float(input("Introduce el lado c: "))

confirmar_triangulo(a, b, c)
