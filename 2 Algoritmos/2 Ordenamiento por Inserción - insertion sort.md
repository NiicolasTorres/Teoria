                    Ordenamiento por Inserción


El Ordenamiento por Inserción (Insertion Sort) es un algoritmo simple y eficiente para ordenar una lista de elementos, especialmente adecuado para listas pequeñas o parcialmente ordenadas. Funciona de manera similar a cómo los humanos ordenan un mazo de cartas en sus manos.

Descripción Técnica del Ordenamiento por Inserción
El ordenamiento por inserción construye la lista ordenada de forma incremental, tomando un elemento de la lista de entrada y ubicándolo en la posición correcta en la lista ordenada, hasta que todos los elementos hayan sido procesados.

                    Algoritmo
1. Inicialización: Considera el primer elemento de la lista como una lista ordenada de un solo elemento.

2. Iteración: Para cada elemento restante de la lista, realiza los siguientes pasos:

- Toma el elemento actual.

- Compara el elemento con los elementos en la lista ordenada, moviéndolos un lugar a la derecha si son mayores que el elemento actual.

- Inserta el elemento en su posición correcta.

3. Repetición: Repite el proceso para todos los elementos hasta que toda la lista esté ordenada.
Ejemplo de Código

Aquí hay un ejemplo en Python:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Mover los elementos del arreglo que son mayores que la clave
        # un lugar adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar la clave en su posición correcta
        arr[j + 1] = key

    return arr

# Ejemplo de uso
lista = [12, 11, 13, 5, 6]
print("Lista original:", lista)
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)


                    Complejidad del Algoritmo

Peor caso: O(n 2) - Ocurre cuando la lista está en orden inverso.
Mejor caso: O(n) - Ocurre cuando la lista ya está ordenada.
Caso promedio: O(n 2).

                    Características

1. Estabilidad: El ordenamiento por inserción es un algoritmo estable, lo que significa que mantiene el orden relativo de los elementos con claves iguales.
2. En su lugar: Es un algoritmo en su lugar (in-place), es decir, no requiere memoria adicional significativa aparte de la lista que se está ordenando.
3. Simplicidad: Es fácil de entender e implementar.
4. Eficiencia: Es eficiente para listas pequeñas y para listas que ya están parcialmente ordenadas.

                    Funcionamiento Paso a Paso
Supongamos que tenemos la lista [12, 11, 13, 5, 6]:

1. Inicialización: [12] | [11, 13, 5, 6]

2. Iteración 1: 11 se inserta antes de 12:
 [11, 12] | [13, 5, 6]

3. Iteración 2: 13 se mantiene en su lugar:
[11, 12, 13] | [5, 6]

4. Iteración 3: 5 se inserta antes de 11:
[5, 11, 12, 13] | [6]

5. Iteración 4: 6 se inserta entre 5 y 11:
[5, 6, 11, 12, 13]

La lista final ordenada es [5, 6, 11, 12, 13].

                    Aplicaciones

El ordenamiento por inserción se utiliza en aplicaciones donde la lista de datos es pequeña o casi ordenada, como en sistemas embebidos o para ordenar datos a medida que se reciben.