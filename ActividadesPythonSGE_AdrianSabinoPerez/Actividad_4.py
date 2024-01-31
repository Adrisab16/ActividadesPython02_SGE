# Actividad 4:
def Palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra_input = input("Ingrese una palabra: ")
if Palindromo(palabra_input):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
