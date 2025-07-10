def promedio_arreglo(arreglo: list) -> float:
    suma: float = 0
    for numero in arreglo:
        suma += numero
    if len(arreglo) == 0:
        return 0
    return suma / len(arreglo)

# Ejemplo de uso
numeros = [3.5, 4.2, 5.8, 2.1]
print("Promedio:", promedio_arreglo(numeros))
