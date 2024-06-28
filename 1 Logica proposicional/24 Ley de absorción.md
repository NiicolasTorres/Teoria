                    ley de absorción

La ley de absorción en lógica proposicional es una de las leyes fundamentales que simplifica expresiones lógicas. Esta ley describe cómo una proposición se puede simplificar en presencia de una disyunción (OR) o una conjunción (AND) con una de sus subproposiciones.

                    Formulación de la Ley de Absorción

Existen dos formas principales de la ley de absorción en lógica proposicional:

1. Primera Forma:

- Formalmente: P∨(P∧Q)≡P
- Descripción: La disyunción de P con la conjunción de P y Q se simplifica a P.
- Ejemplo: Si P es "Es de día" y Q es "Está soleado":
    - P∨(P∧Q)≡P
    - "Es de día o (es de día y está soleado)" se simplifica a "Es de día".

2. Segunda Forma:

- Formalmente: P∧(P∨Q)≡P
- Descripción: La conjunción de P con la disyunción de P y Q se simplifica a P.
- Ejemplo: Si P es "Es de día" y Q es "Está soleado":
    - P∧(P∨Q)≡P
    - "Es de día y (es de día o está soleado)" se simplifica a "Es de día".

Explicación con Ejemplos

Primera Forma de la Ley de Absorción

- Explicación:
    - Si P es verdadero, entonces P∧Q también es verdadero (sin importar Q).
    - Por lo tanto, P∨(P∧Q) es simplemente P porque P ya cubre todas las situaciones en que P∧Q podría ser verdadero.

Ejemplo Específico:
- P: "Tengo una manzana"
- Q: "La manzana es roja".
- P∨(P∧Q): "Tengo una manzana o (tengo una manzana y la manzana es roja)".
- Simplificación: "Tengo una manzana".

Segunda Forma de la Ley de Absorción

- Explicación:
    - Si P es verdadero, entonces P∨Q también es verdadero (sin importar Q).
    - Por lo tanto, P∧(P∨Q) es simplemente P porque P ya cubre todas las situaciones en que P∨Q podría ser verdadero.

- Ejemplo Específico:
    - P: "Tengo una manzana".
    - Q: "La manzana es roja".
    - P∧(P∨Q): "Tengo una manzana y (tengo una manzana o la manzana es roja)".
    Simplificación: "Tengo una manzana".


                    Resumen Visual

1. Primera Forma:
    - P∨(P∧Q)≡P
    - Ejemplo: "Es de día o (es de día y está soleado)" se simplifica a "Es de día".

2. Segunda Forma:
    - P∧(P∨Q)≡P
    - Ejemplo: "Es de día y (es de día o está soleado)" se simplifica a "Es de día".

Estas leyes de absorción ayudan a simplificar y reducir expresiones lógicas, haciendo que los cálculos y razonamientos sean más fáciles de manejar.


La ley de absorción en lógica proposicional también se puede aplicar en presencia de negaciones. Vamos a explorar cómo funciona esto con ejemplos y explicaciones claras.

Primera Forma con Negación:

- Formalmente: P∨(P∧¬Q)≡P
    - Descripción: La disyunción de P con la conjunción de P y la negación de Q se simplifica a P.

- Ejemplo:
    - P: "Está soleado".
    - Q: "Es de noche".
    - P∨(P∧¬Q)≡P: "Está soleado o (está soleado y no es de noche)" se simplifica a "Está soleado".

Segunda Forma con Negación:

- Formalmente: P∧(P∨¬Q)≡P
    - Descripción: La conjunción de P con la disyunción de P y la negación de Q se simplifica a P.

- Ejemplo:
    - P: "Está soleado".
    - Q: "Es de noche".
    - P∧(P∨¬Q)≡P: "Está soleado y (está soleado o no es de noche)" se simplifica a "Está soleado".

Explicación con Ejemplos

Primera Forma con Negación

- Explicación:
    - Si P es verdadero, P∧¬Q también puede ser verdadero (dependiendo de ¬Q).
    - Pero P∨(P∧¬Q) es simplemente P porque P ya cubre todas las situaciones donde P∧¬Q podría ser verdadero.

Ejemplo Específico:

- P: "Tengo una manzana".
- Q: "La manzana está podrida".
- ¬Q: "La manzana no está podrida".
- P∨(P∧¬Q): "Tengo una manzana o (tengo una manzana y la manzana no está podrida)".
- Simplificación: "Tengo una manzana".

Segunda Forma con Negación

- Explicación:
    - Si P es verdadero, P∨¬Q también puede ser verdadero (dependiendo de ¬Q).
    - Pero P∧(P∨¬Q) es simplemente P porque P ya cubre todas las situaciones donde P∨¬Q podría ser verdadero.

Ejemplo Específico:

- P: "Tengo una manzana".
- Q: "La manzana está podrida".
- ¬Q: "La manzana no está podrida".
- P∧(P∨¬Q): "Tengo una manzana y (tengo una manzana o la manzana no está podrida)".
- Simplificación: "Tengo una manzana".

Resumen Visual con Negación
1. Primera Forma con Negación:
    - P∨(P∧¬Q)≡P
    - Ejemplo: "Está soleado o (está soleado y no es de noche)" se simplifica a "Está soleado".

2. Segunda Forma con Negación:
    - P∧(P∨¬Q)≡P
    - Ejemplo: "Está soleado y (está soleado o no es de noche)" se simplifica a "Está soleado".


Ultimo ejemplo: 

Expresión ¬P∧(P∨Q)

Para simplificar esta expresión, vamos a usar algunas leyes de la lógica proposicional:

1. Distribución: A∧(B∨C)≡(A∧B)∨(A∧C)

2. Ley de Contradicción: P∧¬P≡F

3. Ley de Identidad: F∨A≡A

Paso a Paso

1. Distribución:

                    ¬P∧(P∨Q)≡(¬P∧P)∨(¬P∧Q)

2. Ley de Contradicción:

                    (¬P∧P)≡F

3. Ley de Identidad:

                    F∨(¬P∧Q)≡(¬P∧Q)

Resultado Final

La expresión ¬P∧(P∨Q) se simplifica a ¬P∧Q.

Explicación Intuitiva

- Distribución: Distribuimos ¬P sobre (P∨Q) para obtener dos términos: (¬P∧P) y (¬P∧Q).

- Contradicción: Sabemos que ¬P∧P es siempre falso porque una proposición y su negación no pueden ser verdaderas al mismo tiempo.

- Identidad: Finalmente, la disyunción de falso con cualquier otra proposición es simplemente esa otra proposición.

Ejemplo Específico

- Original: ¬P∧(P∨Q)
    - P: "Está lloviendo".
    - Q: "Es de noche".
    - ¬P: "No está lloviendo".

- Simplificación: ¬P∧Q
    - "No está lloviendo y es de noche".

Por lo tanto, la expresión ¬P∧(P∨Q) se simplifica a ¬P∧Q, lo que significa "No está lloviendo y es de noche".