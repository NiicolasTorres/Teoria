Ejercicios de logica:

Condicional:

P → Q ≡ ¬ P v Q

P → Q ≡ ¬Q → ¬P

Bicondicional

P ↔ Q ≡ ( P → Q ) ∧ ( Q → P )


Expresión lógica a resolver: P → Q ≡ ¬ P v Q

| P | Q | P → Q | ¬ P | ¬ P v Q | P → Q ↔ ¬ P v Q   |
|---|---|-------|-----|---------|-------------------|
| V | V |   V   |  F  |    V    |        V          |
| V | F |   F   |  F  |    F    |        V          |
| F | V |   V   |  V  |    V    |        V          |
| F | F |   V   |  V  |    V    |        V          |


Expresión lógica a resolver: P → Q ≡ ¬Q → ¬P


| P | Q | P → Q | ¬ P |  ¬Q  | ¬Q → ¬P |  P → Q ↔ ¬Q → ¬P  |
|---|---|-------|-----|------|---------|-------------------|
| V | V |   V   |  F  |  F   |    V    |        V          |
| V | F |   F   |  F  |  V   |    V    |        F          |
| F | V |   V   |  V  |  F   |    F    |        F          |
| F | F |   V   |  V  |  V   |    V    |        V          |



Expresión lógica a resolver:  P ↔ Q ≡ ( P → Q ) ∧ ( Q → P )

| P | Q | ( P → Q ) | ( Q → P )  | ( P → Q ) ∧ ( Q → P )  | P ↔ Q | P ↔ Q ≡ ( P → Q ) ∧ ( Q → P ) |
|---|---|-----------|------------|------------------------|-------|-------------------------------|
| V | V |     V     |     V      |          V             |   V   |             V                 |
| V | F |     F     |     F      |          F             |   F   |             F                 |
| F | V |     V     |     V      |          V             |   F   |             F                 |
| F | F |     V     |     V      |          V             |   v   |             V                 |


