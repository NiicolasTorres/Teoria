# Inicializamos una lista de números desordenados
arr = [5, 3, 4, 8, 7, 5, 1, 2, 3]
# Imprimimos la lista original
print(arr)

# Comenzamos un bucle que recorrerá la lista desde el segundo elemento hasta el final
for j in range(1, len(arr)):
    # Guardamos el elemento actual en una variable 'actual'
    actual = arr[j]
    
    # Inicializamos otra variable 'i' con el índice del elemento anterior al actual
    i = j - 1
    # Iniciamos un bucle que se ejecuta mientras 'i' sea mayor o igual a 0
    # y el elemento en 'arr[i]' sea mayor que 'actual'
    while i >= 0 and arr[i] > actual:
        # Desplazamos el elemento 'arr[i]' una posición a la derecha
        arr[i + 1] = arr[i]
        # Decrementamos 'i' para comparar el siguiente elemento hacia la izquierda
        i -= 1
    # Insertamos el 'actual' en la posición correcta, después de haber desplazado los mayores
    arr[i + 1] = actual

# Imprimimos la lista ordenada
print(arr)
