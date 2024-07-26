
                    Simplificacion logica

La simplificación lógica es un proceso en el ámbito de la lógica proposicional que consiste en reducir una expresión lógica compleja a una forma más simple y equivalente, utilizando reglas y técnicas específicas. El objetivo principal de la simplificación lógica es mejorar la legibilidad, facilitar el análisis y reducir la complejidad de las expresiones lógicas sin alterar su significado lógico.

Algunas técnicas comunes de simplificación lógica incluyen la aplicación de leyes lógicas como la ley de idempotencia, la ley de absorción, la ley distributiva, entre otras. Estas leyes permiten combinar términos redundantes, eliminar redundancias y reorganizar la expresión para hacerla más concisa y comprensible sin cambiar su valor de verdad.

En el contexto de la informática y la ingeniería de software, la simplificación lógica es fundamental para diseñar y optimizar circuitos digitales, algoritmos y sistemas que dependen de decisiones lógicas basadas en condiciones booleanas.


Repaso rapido:  

1. Ley de Idempotencia: En lógica booleana, la ley de idempotencia establece que una variable booleana operada consigo misma (a OR a) o (a AND a) siempre es igual a la propia variable (a).

2. Leyes de De Morgan: Las leyes de De Morgan permiten transformar una negación de una conjunción (NOT (a AND b)) en una disyunción de negaciones (NOT a OR NOT b), y viceversa para una negación de una disyunción.

3. Ley Asociativa: En lógica y álgebra booleana, la ley asociativa establece que el agrupamiento de operaciones (a OR b) OR c es igual a a OR (b OR c), y lo mismo para la conjunción.

4. Ley Conmutativa: La ley conmutativa establece que el orden de los operandos en una operación booleana (a OR b) es igual a (b OR a), y lo mismo aplica para la conjunción.

5. Ley Distributiva: La ley distributiva en lógica booleana indica que una operación distribuida sobre otra se puede expresar como una combinación de operaciones (a AND (b OR c)) es igual a (a AND b) OR (a AND c), y lo mismo para la disyunción distribuida sobre la conjunción.

6. Ley de Doble Negación: La doble negación de una proposición es equivalente a la proposición original, es decir, NOT (NOT a) es lo mismo que a

7. Ley de Implicación Material: En lógica proposicional, a -> b es verdadero si y solo si a es falso o b es verdadero.

8. Ley de Complemento: La disyunción de una proposición con su negación es siempre verdadera (a OR NOT a), y la conjunción de una proposición con su negación es siempre falsa (a AND NOT a).

9. Lógica de Identidad: La conjunción de una proposición con True es la propia proposición (a AND True es a), y la disyunción de una proposición con False es la propia proposición (a OR False es a).

10. Ley de Absorción: En la conjunción, si a es verdadero, entonces a AND (a OR b) es simplemente a; y en la disyunción, a OR (a AND b) es equivalente a a si a es verdadero.

11. Ley de Negación: En lógica proposicional, la negación de una conjunción es equivalente a la disyunción de las negaciones de las proposiciones individuales, y viceversa. Es decir, NOT (a AND b) es equivalente a (NOT a) OR (NOT b), y NOT (a OR b) es equivalente a (NOT a) AND (NOT b).

Expresión lógica a resolver:  q V ¬[¬( P ∧ Q ) → ¬Q ]


1. q ∧ ¬[¬( P ∧ Q ) → ¬Q ] ≡ Q V ¬[( P ∧ Q ) ∨ ¬Q ]
2.                         ≡ Q V [ ¬( P ∧ Q ) ∨ Q ]
3.                         ≡ Q 
 
Leyes usadas: 
1.Disyuncon
2.Ley de De Morgan
3.ley de absorcion