# Actividad 5:
preciosFrutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta = input("Ingrese una fruta: ")

if fruta in preciosFrutas:
    kilos = float(input(f"Ingrese el número de kilos de {fruta}: "))
    precio_total = preciosFrutas[fruta] * kilos
    print(f"El precio de {fruta} por {kilos} kilos es: {precio_total} euros")
else:
    print(f"{fruta} no está en el diccionario de precios.")
