                    Tuplas 

Es una estructura de datos que permite almacenar una coleccion ordeanda de elmentos, similar a una lista, pero con la diferencia crucial de que es inmutable.


            Caracteristicas de una tupla

Ordenada: Al igual que las listas, las tuplas mantienen un orden fico de los elementos. Cada elemento tiene un indice, comenzado desde 0 para el primer elemento.

Inmutable: Una vez que una tupla es creada, no se puede modificar. Esto significa que no puedes cambiar, añadir ni eliminar elementos despues de su creacion.

Heterogenea: Las tuplas pueden contener elementos de diferentes tipos de datos, como enteros, cadenas, otras tuplas, objetos, etc.

Indexacion y slicing: Puedes acceder a los elementos de una tupla mediante indices y tambien puedes obtener sub-tuplas utilizando el slicing.

                Implementacion tecnica

Internamente las tuplas en python son gestionadas de manera similar a las listas en terminos de almacenamiento de elementos, pero con la diferencia de que su inmutabilidad permite ciertas optimizaciones

1 Almacenamiento en memoria: las tuplas son almacenadas en un bloque continuo de memoria, lo que facilita el acceso rapido a los elementos. La inmutabilidad significa que el tamaño de la tupla no puede cambiar, lo que permite una gestion de memoria mas eficiente.

2 Optimizacion: Debidp a su inmutabilidad, python puede realizar varias optimizaciones. Por ejemplo, las tuplas pueden ser usadas como claves en diccionarios, ya que sus valores no cambian durante el tiempo de vida de la tupla.

                Operaciones comunes

Aunque las tuplas son inmutables se pueden realizar varias operaciones que no implican modificar su contenido

                    Creacion

tupla = (1, 2, 3, "cuatro")


                    Acceso

primer_elemento = tupla[0]
ultimo_elemento = tupla[-1]


                    slicing

sub_tupla = tupla[1:3]


                    concatenacion

nueva_tupla = tupla + (5, 0)


                    repeticion

repetida = tupla * 2


                    metodos disponibles:

longitud = len(tupla)
cuenta = tupla.count(2)
indice = tupla.index("cuatro")




                    Resumen tecnico

Inmutabilidad: Una vez creada, no se puede modificar, añadir ni eliminar elementos.

Optimizacion de memoria: La inmutabilidad permite optimizaciones en la gestion de memoria.

Rendimiento: Acceso mas rapido y uso en estructuras de datos como claves de diccionarios debido a la inmutabilidad.

Uso: Ideal para colecciones de datos constantes y seguros que no deberian cambiar a lo largo del tiempo.