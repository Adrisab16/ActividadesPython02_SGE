# Actividad 3:

modulos = ["SGE", "AD", "EIE", "PMDM"]
notas = {}

for modulo in modulos:
    nota = float(input(f"Ingrese la nota para {modulo}: "))
    notas[modulo] = nota

for modulo, nota in notas.items():
    if nota >= 5:
        modulos.remove(modulo)

print("Módulos a repetir:")
for modulo in modulos:
    print(modulo)
