# Actividad 8:

num_palabras = int(input("Ingrese el número de palabras que va a tener la lista: "))
lista_palabras = []

for _ in range(num_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

print("Lista de palabras:", lista_palabras)
