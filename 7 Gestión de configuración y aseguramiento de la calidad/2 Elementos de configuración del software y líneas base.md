### Gestión de Configuraciones de Software

En la gestión de configuraciones de software, hay dos conceptos clave: **elemento de configuración del software** y **línea base**. Estos conceptos son esenciales para mantener el control y la coherencia del desarrollo del software a lo largo de su ciclo de vida.

#### 1. Elemento de Configuración del Software (EC)

Un **elemento de configuración del software** es cualquier componente del producto software que cumple dos condiciones:
1. **Evoluciona a lo largo del ciclo de vida**: Esto significa que el componente cambia y se actualiza durante el desarrollo del software.
2. **Nos interesa controlar esa evolución**: Queremos supervisar y gestionar los cambios que se hacen en este componente.

Cada elemento de configuración recibe un identificador y un nombre único. Esto facilita su seguimiento y gestión.

##### Ejemplos:
- **Documento de análisis**: Este documento describe las necesidades y requisitos del software. Evoluciona a medida que se clarifican y refinan los requisitos.
- **Documento de diseño**: Describe cómo se implementarán los requisitos en el software. Evoluciona a medida que se detallan y ajustan los planes de diseño.

##### Ejemplos de lo que NO sería un EC:
- **Contrato**: No evoluciona durante el ciclo de vida del software.
- **Maqueta**: Puede evolucionar hasta un punto, pero una vez finalizada, no se sigue utilizando ni actualizando.

#### 2. Línea Base

Una **línea base** es una configuración de referencia en el ciclo de vida del software. Marca un punto específico donde todos los productos del software están en una versión estable y controlada. A partir de este punto, cualquier cambio realizado debe ser justificado y controlado formalmente.

##### Ejemplo:
Al finalizar la etapa de análisis, se establece una línea base. Los documentos que cumplen las condiciones de ser elementos de configuración (como el plan de proyecto y el documento de especificación de requisitos) pasan a formar parte de esta línea base. Cualquier cambio posterior en estos documentos debe ser autorizado y gestionado cuidadosamente.

### Proceso de Gestión de Cambios

Para hacer un cambio controlado en un elemento de configuración que forma parte de una línea base, se sigue este procedimiento:

1. **Justificación y Autorización**: Asegurarse de que el cambio es necesario y está autorizado.
2. **Modificación**: Sacar el elemento de configuración de la base de datos, hacer los cambios necesarios, y volver a introducirlo.
3. **Notificación**: Informar a todas las partes interesadas sobre el cambio.

### Fases del Proyecto y Líneas Base

Las líneas base se definen al inicio del proyecto, generalmente durante la fase de planificación. Estas líneas coinciden con los hitos importantes del proyecto:

1. **Línea Base Funcional**: Después de la etapa de análisis.
2. **Línea Base de Diseño**: Después de la etapa de diseño.
3. **Línea Base de Producto**: Después de las pruebas del sistema.
4. **Línea Base Operativa**: Cuando el producto final se entrega al cliente y empieza a ser utilizado.

### Importancia

Definir y usar elementos de configuración y líneas base permite desarrollar el software de manera controlada y coherente. Esto asegura que:

- Se pueden realizar cambios necesarios sin perder el control.
- Se mantiene la consistencia del producto.
- Se asegura que el proyecto no se desvíe de su curso planificado.

### Resumen

- **Elemento de Configuración del Software**: Componente que evoluciona y necesita ser controlado.
- **Línea Base**: Configuración de referencia donde los cambios futuros son controlados y justificados.
- **Gestión de Cambios**: Proceso formal para asegurar que todos los cambios son necesarios y bien gestionados.

Estos conceptos son herramientas poderosas para asegurar que el desarrollo del software se lleva a cabo de manera organizada y controlada.