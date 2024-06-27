"""
#algoritmo de insertion sort

arr = [3, 5, 1,7,10,4,6,8,9]
print(arr)

for j in range(1, len(arr)):
    actual = arr[j]
    
    i = j -1
    
    while i >= 0 and arr[i] > actual:
        arr[i+1] = arr[i]
        i-=1
    arr[i+1] = actual
    
print(arr)


#escritura nuevamente del algoritmo
# creamos la lista
arr = [3, 5, 1,7,10,4,6,8,9]
# la imprimimos
print(arr)

# creamos el inicio del bucle que recorre la lista desde el segundo elemento hasta el final
for j in range(1, len(arr)):
    # guardamos el elemento actual en la variable actual
    actual = arr[j]
    
    #iniciamos la variable 'i' con el indice del anterior al actual
    i = j - 1
    
    #iniciamos el bucle que se ejecutara mientras 'i' sea igual o mayor a 0
    # y el elemento en 'arr[i]' sea mayor que el actual
    while i >=0 and arr[i] > actual:
        #desplazamos 'i' a un lugar a la derecha 
        arr[ i + 1] = arr[i]
        #decrementamos 'i' para comparar el numero anterior
        i-=1 
        #insertamos actual en la posicion correcta 
        arr[i+1] = actual
        
# Imprimimos la lista ordenada
print(arr)
  """      
        
arr = [3, 5, 1, 7, 10, 4, 6, 8, 9]
print(arr)



                 