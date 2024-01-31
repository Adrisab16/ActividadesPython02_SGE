# Actividad 9:

numeros = []
entrada = input("Ingrese un número (o algo que no sea un número para finalizar): ")

while entrada.isdigit():
    numeros.append(int(entrada))
    entrada = input("Ingrese otro número: ")

num_buscado = int(input("Ingrese un número que haya introducido: "))

if num_buscado in numeros:
    print(f"El número {num_buscado} está en la posición {numeros.index(num_buscado) + 1}")
else:
    print("El número no está en la lista.")
