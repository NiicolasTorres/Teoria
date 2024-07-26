# Crear una tupla
mi_tupla = (18,20,30,"cuarenta",50)

# Acceder al primer y último elemento
print(mi_tupla[0])
print(mi_tupla[-1])

# Slicing para obtener una sub-tupla
sub_tupla = mi_tupla[1:4]
print(sub_tupla)

#Concatenación de tuplas
nueva_tupla = mi_tupla + (60, 70)
print(nueva_tupla)

# Repetición de tuplas
repetida = mi_tupla * 2
print(repetida)

longitud = len(mi_tupla)
print(longitud)

cuenta = mi_tupla.count(20)
print(cuenta)

indice = mi_tupla.index("cuarenta")
print(indice)