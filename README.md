# RETO_09
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.
## 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
Este programa calcula el promedio de una lista de números reales. Es útil cuando se necesita obtener un valor representativo del conjunto, como en promedios académicos, resultados de mediciones o estadísticas. El algoritmo recorre los elementos, los suma y divide el total por la cantidad de datos presentes.


```
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
```

## 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
Este programa realiza el cálculo del producto punto entre dos listas de números reales del mismo tamaño. Esta operación consiste en multiplicar los elementos que ocupan la misma posición en ambas listas y luego sumar los resultados. Es una operación común en álgebra lineal, física y análisis de datos.
```
def producto_punto(a: list, b: list) -> float:
    if len(a) != len(b):
        print("Error: Los arreglos deben tener el mismo tamaño.")
        return 0

    producto: float = 0
    for i in range(len(a)):
        producto += a[i] * b[i]
    return producto

# Ejemplo de uso
a = [1.5, 2.0, 3.5]
b = [4.0, 0.5, 2.0]
print("Producto punto:", producto_punto(a, b))
```
## 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
Este programa reorganiza los elementos de una lista de números enteros para que todos los ceros se ubiquen al final, sin modificar el orden de los demás valores. Es útil en tareas de limpieza de datos o procesos donde los ceros representan ausencia de información y deben apartarse para facilitar operaciones posteriores.
```
    def mover_ceros_al_final(arreglo: list) -> list:
        resultado: list = []
        contador_ceros: int = 0

    for numero in arreglo:
        if numero != 0:
            resultado.append(numero)
        else:
            contador_ceros += 1

    for i in range(contador_ceros):
        resultado.append(0)

    return resultado

    # Ejemplo de uso
    arreglo = [0, 3, 0, 5, 7, 0, 2]
    print("Resultado:", mover_ceros_al_final(arreglo))
```
## 4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).
Este programa implementa el algoritmo de ordenamiento Bubble Sort. Ordena una lista de números enteros de menor a mayor, comparando elementos adyacentes e intercambiándolos si están en el orden incorrecto. Aunque no es el método más eficiente, es una herramienta educativa muy útil para entender los fundamentos de los algoritmos de ordenamiento.
```
  def bubble_sort(lista: list) -> None:
      n: int = len(lista)
      for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

  # Ejemplo
datos = [5, 3, 8, 4, 2]
bubble_sort(datos)
print("Ordenado:", datos)
```
