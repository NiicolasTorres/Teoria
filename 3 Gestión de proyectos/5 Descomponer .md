
**Estimación de Proyectos de Software: Técnicas de Descomposición**

### ¿Cómo Estimamos?

Para la estimación del esfuerzo en un proyecto de software, es muy útil descomponer el problema en subproblemas o subsistemas siguiendo el enfoque conocido como “divide y vencerás”. Este enfoque consiste en dividir el sistema completo en distintos módulos y, a su vez, descomponer estos en tareas o funciones lo más elementales posibles.

#### Descomposición del Proyecto

1. **División en Módulos:**
   - Primero, se divide el sistema completo en módulos o subsistemas. Por ejemplo, en un proyecto de software, podríamos tener módulos como:
     - Comunicaciones
     - Razonamiento
     - Interfaz de Usuario
     - Base de Datos

2. **Descomposición en Tareas:**
   - Luego, cada uno de estos módulos se descompone en tareas específicas, como análisis, diseño, codificación y pruebas. Estas tareas son más pequeñas y manejables, lo que facilita su estimación.

#### Modelo Matricial

Una manera útil de hacer esta descomposición es siguiendo un modelo matricial. En este modelo, se utiliza una tabla donde:

- **Filas:** Representan los distintos módulos.
- **Columnas:** Representan las distintas fases de cada módulo (análisis, diseño, codificación, pruebas).

Cada celda de la tabla contendrá la estimación de recursos necesarios para completar esa tarea específica en el módulo correspondiente. Por ejemplo:

| **Módulo/Fase**         | **Análisis** | **Diseño** | **Codificación** | **Pruebas** | **Total (p-s)** |
|-------------------------|--------------|------------|------------------|-------------|-----------------|
| **Comunicaciones**      |       3      |     2      |        1,5       |      2      |       8,5       |
| **Razonamiento**        |       7      |     6      |         5        |      5      |       23        |
| **Interfaz de Usuario** |       5      |     4      |         4        |      4      |       17        |
| **Base de Datos**       |       2      |     2      |        1,5       |      3      |       8,5       |
| **Total**               |      17      |    14      |        11        |     14      |      57 p-s     |

#### Estimación Total

Sumando las filas, obtenemos la estimación para cada módulo. Sumando las columnas, obtenemos la estimación para cada tarea. En nuestro ejemplo, el esfuerzo total estimado es de 57 persona-semanas (p-s).

### Coste Total

Para calcular el coste total del proyecto, también se debe considerar la tarifa o ratio de cada perfil. Esta tarifa no es el salario directo, sino el ingreso que debe generar cada perfil para cubrir todos los gastos de la empresa y asegurar un balance positivo. Por ejemplo, las tarifas pueden ser:

| **Fase**          | **Tarifa (euros)** |
|-------------------|--------------------|
| **Análisis**      |      1.800         |
| **Diseño**        |      1.600         |
| **Codificación**  |      1.400         |
| **Pruebas**       |      1.400         |

Multiplicando la estimación de recursos por la tarifa, obtenemos el coste de cada tarea y, finalmente, sumando estos costos, obtenemos el coste total del proyecto:

| **Fase**                | **Análisis** | **Diseño** | **Codificación** | **Pruebas** | **Total** |
|-------------------------|--------------|------------|------------------|-------------|-----------|
| **Coste Total (euros)** |   30.600     |  22.400    |      15.400      |    19.600   |   88.000  |

En este ejemplo, el coste total estimado del proyecto es de 88.000 euros.

### Resumen

El enfoque de descomposición permite dividir el proyecto en partes más pequeñas y manejables, facilitando la estimación del esfuerzo y coste. Utilizando un modelo matricial, podemos organizar y visualizar claramente las estimaciones por módulo y fase, lo que simplifica el proceso y proporciona una estimación completa y detallada del proyecto.
La técnica de descomposición no solo hace que las estimaciones sean más precisas, sino que también facilita la planificación y el seguimiento del progreso del proyecto, asegurando que cada parte del proyecto se maneje de manera eficiente y efectiva.