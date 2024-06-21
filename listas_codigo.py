mi_lista = [10,20,30,40,50]

# Acceder al primer y último elemento
print(mi_lista[0]) # muestra el primer elemento
print(mi_lista[-1]) # muestra el ultimo

# Modificar un elemento
mi_lista[2] = 35
print(mi_lista)

# Añadir elementos
mi_lista.append(60)
mi_lista.extend([70,80])
mi_lista.insert(1,15)
print(mi_lista)

# Eliminar elementos
mi_lista.remove(40)
elemento = mi_lista.pop(3)
print(mi_lista)
print(elemento)

# Slicing
sub_lista = mi_lista[1:4]
print(sub_lista)
