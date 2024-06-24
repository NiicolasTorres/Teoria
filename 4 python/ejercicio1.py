# Escribe una función que encuentre el máximo común divisor (MCD) de dos números.



# Algoritmo de Euclides

def encontrar_mcd(a, b):
    # Escribe tu código aquí
    while b !=0:
        a, b = b, a % b
    return a

# Ejemplo de uso
print(encontrar_mcd(54, 24))  # Debería imprimir 6