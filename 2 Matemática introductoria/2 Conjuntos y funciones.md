                    Conjuntos y funciones


### 1. ¿Qué es un conjunto?
Un **conjunto** es simplemente una colección de objetos, llamados **elementos**. Por ejemplo, si tienes un grupo de números como \(X = \{1, 2, 3\}\), estás formando un conjunto con tres elementos. Hay dos posibilidades para cualquier objeto cuando hablamos de conjuntos:
- El objeto **pertenece** al conjunto, como \(1 ∈ X\) (1 está en \(X\)).
- El objeto **no pertenece** al conjunto, como \(4 ∉ X\) (4 no está en \(X\)).

Una característica importante de los conjuntos es que no importa el **orden** de los elementos ni si están repetidos. Por ejemplo, el conjunto \(X = \{1, 2\}\) es igual a \(X = \{2, 1\}\) y también igual a \(X = \{1, 2, 2\}\).

### 2. Cómo describir un conjunto
Hay dos maneras comunes de describir conjuntos:

- **Por extensión**, enumerando sus elementos. Por ejemplo, el conjunto de provincias de Argentina se puede escribir como:
  \(Y = \{Chaco, Córdoba, Misiones, Salta, Buenos Aires, Chubut, Jujuy, Mendoza\}\).
  
- **Por comprensión**, describiendo una propiedad común a todos sus elementos. Por ejemplo, podrías definir el mismo conjunto de provincias así:
  \(Y = \{y : yesunaprovinciadeArgentina\}\),
  lo que se lee como "Y es el conjunto de todos los \(y\) tales que \(y\) es una provincia de Argentina".

### 3. Conjuntos especiales y vacíos
El **conjunto vacío**, denotado por \(∅\), es un conjunto que no tiene ningún elemento. Aunque esto suene raro, es útil en matemáticas, ya que el conjunto vacío puede representarse de muchas maneras. Por ejemplo:
- \(∅ = \{x : x^2 = -1\}\), ya que no hay ningún número real cuyo cuadrado sea -1.
- También podemos decir que \(∅\) es el conjunto de provincias que están tanto en Andalucía como en Galicia, ya que no hay ninguna provincia que pertenezca a ambos lugares.

### 4. Operaciones con conjuntos
Las **operaciones** básicas que podemos hacer con conjuntos son:

- **Unión** (\(∪\)): Todos los elementos que están en \(X\), en \(Y\), o en ambos. Por ejemplo, si \(X = \{1, 2, a, c\}\) y \(Y = \{a, b\}\), entonces \(X ∪ Y = \{1, 2, a, b, c\}\).
  
- **Intersección** (\(∩\)): Los elementos que están tanto en \(X\) como en \(Y\). En el ejemplo anterior, \(X ∩ Y = \{a\}\).

- **Diferencia** (\(\backslash\)): Los elementos que están en \(X\) pero no en \(Y\). En este caso, \(X \ Y = \{1, 2, c\}\).

- **Producto cartesiano** (\(×\)): Forma pares ordenados con todos los elementos de \(X\) y \(Y\). Por ejemplo, \(X × Y = \{(1, a), (1, b), (2, a), (2, b), (a, a), (a, b), (c, a), (c, b)\}\).

### 5. ¿Qué es una función?
Una **función** es una regla que asigna a cada elemento de un conjunto \(X\) un único elemento de otro conjunto \(Y\). Por ejemplo, si tenemos una función \(f\) que toma números en \(X = \{1, 2, 3\}\) y les asigna \(f(x) = x^2\), entonces \(f(1) = 1^2 = 1\), \(f(2) = 4\), y \(f(3) = 9\).

Las funciones tienen diferentes tipos:

- **Inyectiva**: Cada valor de salida es único para cada valor de entrada. Si dos entradas diferentes te dan la misma salida, la función no es inyectiva.
- **Sobreyectiva**: Cada valor de \(Y\) tiene al menos un valor de \(X\) que lo produce.
- **Biyectiva**: Es inyectiva y sobreyectiva a la vez, es decir, cada elemento de \(X\) tiene un único correspondiente en \(Y\), y viceversa.

### 6. Ejemplos y ejercicios
Por último, aquí hay algunos ejemplos para ayudarte a practicar:

1. **Ejercicio**: Si \(f : N \to Z\) es una función que asigna a cada número natural \(n\), \(f(n)\) basado en si \(n\) es par o impar. Define \(f(n)\) así:
   - Si \(n\) es par: \(f(n) = n/2\).
   - Si \(n\) es impar: \(f(n) = (1 - n)/2\).
   
   ¿Es esta función inyectiva? ¿Es sobreyectiva? ¿Podrías calcular su inversa si es biyectiva?
