                    Diccionario

Es una estrictira de datos que permite almacenar en pares de clave-valor.
cada clave es unica y se utiliza para acceder a su valor asociado de manera eficiente.

                    Caracteristicas

Desordenado: Los diccionarios no mantienen un orden especifico de los elementos.Aunque no a partir de python 3.7, los diccionarios mantienen el orden de insercion de los elementos, esto no debe ser una caracteristica sobre la que se dependa necesariamente en todas las versiones de python

Mutable: Los diccionarios son mutables, lo que significa que puedes añadir, eliminar y modificar pares de clave-valor despues de haberlos creado

Claves Unicas: Cada clave en un diccionario debe ser unica. Si intentas añadir una clave que ya existe, el valor existente se sobrescribira

Claves inmutables: Las claves deben ser de un tipo de dato inmutable, como cadenas, numeros o tuplas (que contienen solo tipos inmutables)

                    Implementacion tecnica

Internamente los diccionarios en python estan implementados usando tablas (hash). Esto permite que las operaciones de busqueda, insercion y eliminacion tengan un promedio de tiempo constante, O(1), bajo condiciones ideales

Tabla Hash: Los diccionarios utilizan una estructura de datos llamada tabla hash para mapear las claves a sus valores correspondientes. Cada clave se pasa a travez de una funcion hash que la convierte en un indice en la tabla hash


Colisiones: Cuando dos claves tienen el mismo valor hash ( una colision ), Python maneja esto mediante tecnicas como encadenamiento (listas enlazadas) o direccionamiento abierto (probing)

                    Operaciones comunes:


                    Creacion

diccionario = {"clave1":"valor1", "clave2":"valor2"}


                    Acceso

valor = diccionario["clave1]


                    Modificacion

diccionario["clave1"] = "nuevo_valor"


                    Adicion


diccionario["clave3"] = "valor3" 


                    Eliminacion

del diccionario["clave2"]  #Elimina el par clave-valor con 'clave2'
valor  = diccionario.pop("clave1")  # Elimina y devuelve el valor asociado con 'clave1'


                    Iteracion

for clave in diccionario:
    print(clave, diccionario[clave]) # Itera sobre las claves y sus valores

for clave, valor in diccionario.items():
    print(clave, valor)  # Itera sobre los pares clave-valor


                    Metodos comunes

keys(): devuelve una lista de las claves del diccionario

claves = diccionario.keys()


values(): Devuelve una vista de los valores del diccionario

valores = diccionario.values()


items(): Devuelve una vista de los pares clave-valor del diccionario

elementos = diccionario.items()


get(): Devuelve el valor para una clave o un valor por defecto si la clave no existe

valor = diccionario.get("clave1", "valor_por_defecto")


update(): actualiza el diccionario con pares de clave-valor de otro diccionario o de un iterable de pares clave-valor

diccionario.update({"clave4":"valor4", "clave5":"valor5"})



                    Resumen tecnico

Mutabilidad: Permite modificar, añadir y eliminar pares clave-valor

Acceso rapido: Implementado mediante una tabla hash que permite acceso y modificacion en tiempo constante promedio

Claves unicas: Cada clave debe ser unica y debe ser de un tipo inmutable y hashable.

Flexibilidad: puede almacenar cualquier tipo de datos como claves y valores, lo que lo hace muy versatil para diversas aplicaciones.

