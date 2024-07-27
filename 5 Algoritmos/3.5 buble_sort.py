# Lista de números desordenados
arr = [5, 3, 4, 8, 7, 5, 1, 2, 3]

# Imprime la lista original
print(arr)

# Bucle externo: Recorre toda la lista
# 'i' representa el número de pasadas que hemos hecho
for i in range(len(arr)):
    # Bucle interno: Recorre la lista desde el inicio hasta el final menos las pasadas hechas
    # 'len(arr) - i - 1' porque con cada pasada, el mayor de los elementos sin ordenar llega a su posición correcta
    for j in range(len(arr) - i - 1):
        # Compara el elemento actual con el siguiente
        if arr[j] > arr[j + 1]:
            # Si el elemento actual es mayor que el siguiente, intercámbialos
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Imprime la lista ordenada
print(arr)



