                    #Operaciones comunes

# Crear un diccionario
mi_diccionario = {"Nombre": "Alice", "Edad": 30, "Ocupacion": "Ingeniera"}

# Acceder a un valor
print(mi_diccionario["nombre"]) # Output: Alice

# Modificar un valor
mi_diccionario["edad"] = 31  # Output: {'nombre': 'Alice', 'edad': 31, 'ocupación': 'Ingeniera'}

# Añadir un nuevo par clave-valor
mi_diccionario["ciudad"] = "Madrid" # Output: {'nombre': 'Alice', 'edad': 31, 'ocupación': 'Ingeniera', 'ciudad': 'Madrid'}

# Eliminar un par clave-valor

del mi_diccionario["Ocupacion"]
print(mi_diccionario)  # Output: {'nombre': 'Alice', 'edad': 31, 'ciudad': 'Madrid'}


# Iterar sobre claves y valores

for clave, valor in mi_diccionario.items():
    print(clave,valor)

# Output:
# nombre Alice
# edad 31
# ciudad Madrid
