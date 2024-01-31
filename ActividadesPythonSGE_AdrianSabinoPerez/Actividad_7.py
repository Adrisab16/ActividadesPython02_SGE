# Actividad 7:
def dibujar_triangulo(anchura):
    for i in range(1, anchura + 1):
        print('*' * i)

anchura_input = int(input("Ingrese la anchura del triángulo: "))
dibujar_triangulo(anchura_input)
