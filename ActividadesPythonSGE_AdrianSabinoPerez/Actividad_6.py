# Actividad 6:
def longitud_palabras(frase):
    palabras = frase.split()
    diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}
    return diccionario_longitudes

frase_input = input("Ingrese una frase: ")
resultado = longitud_palabras(frase_input)
print(resultado)
