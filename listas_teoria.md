                    Listas 

Es una estructura de datos que permite almacenar una coleccion ordenada y mutable de elementos.

                Caracteristicas

Ordenada: Los elementos en una lista tienen un orden especifico. Cada elemento tiene una posicion o un indice que empieza desde 0 para el primer eleemnto, 1 para el segundo y asi sucesivamente.

Mutable: A diferencia de las tuplas, la listas son mutables, lo que sifnifica que puedes modificar sus elementos despues de haberlas creado. Puedes añadir, eliminar o cambiar sus elementos.

Heterogenea: Las listas pueden contener elementos de diferentes tipos de datos, como enteros, cadenas, otras listas, objeos, etc.

Indezacion y Slicing: Puedes acceder a los elementos de una lista mediante indices y tambien puedes obtener sublistas utilizando el slicing.


                Implementacion tecnica

1 Arreglo dinamico: Aunque se comporta como una lista enlazada en cuanto a su mutabilidad, esta omplementada como un arreglo dinamico, lo que significa que tiene una capacidad preasignada y puede crecer segun sea necesario. Cuando la lista excede su capacidad actual, se crea un nuevo arreglo con mas espacio y elementos de la lista original se copian al nuevo arreglo

2 Gestion de Memoria: la capacidad de la lista (el numero de elementos puede contener sin requerur un redimensionamiento) y su tamaño actual (el numero de elementos que contiene) son dos aspectos distintos. La lista gestiona la memora de manera eficiente para minimizar el numero de redimensionamientos, lo que implica copiar elementos y suele incrementar su capacidad en un factor constante (usualmente 1.125 o 9/8)



                    Creacion

lista = [1,2,3,"Cuatro",[5,6]]


                    Acceso

primer_elemento = lista[0]
segundo_elemento = lista[1]


                    Modificacion

lista[1] = "Dos"


                    Adicion

lista.append(7)  Agrega un elemento al final
lista.extend([8,9]) Agrega multiples elemenos al final
lista.insert(1, "nuevo") Inserta un elemento en una posicion especifica


                    Eliminacion

lista.remove("Cuatro") elimina el primer elemento que coincide con el valor dado
elemento_eliminado = lista.pop(2) Elimina y devuelve el elemento en la posición dada

                    slicing

sublista = lista[1:4]


                    Resumen tecnico

Mutables, sintaxis con [], metodos variados para modificacion, adecuadas para colecciones dinamicas