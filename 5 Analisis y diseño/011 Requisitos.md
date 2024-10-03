
### Requisitos en Ingeniería de Software

Los requisitos son condiciones o capacidades que un sistema informático debe poseer para resolver un problema específico o alcanzar un objetivo determinado. En el contexto del desarrollo de software, los requisitos definen lo que el sistema debe hacer y cómo debe comportarse para satisfacer las necesidades del usuario y los objetivos del negocio.

#### Clasificación de los Requisitos

1. **Requisitos Funcionales:**

   - **Descripción:** Los requisitos funcionales especifican las acciones que el sistema debe ser capaz de realizar. Estos requisitos describen la funcionalidad básica y esencial del software.
   - **Formato:** Se suelen formular como acciones utilizando verbos, por ejemplo: "El usuario podrá dar de alta un elemento".
   - **Ejemplos:**
     - "El sistema permitirá a los usuarios registrar nuevos clientes."
     - "El sistema debe enviar una confirmación por correo electrónico tras completar una compra."

2. **Requisitos No Funcionales:**

   - **Descripción:** Los requisitos no funcionales describen las características y atributos generales del sistema, como la eficiencia, seguridad, usabilidad, y mantenibilidad. No especifican acciones, sino cualidades que el sistema debe cumplir.
   - **Clasificación según la IEEE Std 830-1993:** Este estándar identifica 13 tipos de requisitos no funcionales que deben considerarse en cualquier especificación de software:
     - **Disponibilidad:** Tiempo durante el cual el sistema debe estar operativo.
     - **Eficiencia:** Medidas de rendimiento, como tiempo de respuesta y utilización de recursos.
     - **Interfaz externa:** Requisitos para la interacción con otros sistemas.
     - **Flexibilidad:** Capacidad del sistema para adaptarse a cambios.
     - **Interfaz con el usuario:** Requisitos de usabilidad y accesibilidad.
     - **Mantenibilidad:** Facilidad para realizar modificaciones, correcciones o mejoras.
     - **Portabilidad:** Capacidad del sistema para ser utilizado en diferentes entornos.
     - **Fiabilidad:** Probabilidad de funcionamiento libre de fallos durante un periodo de tiempo.
     - **Reusabilidad:** Capacidad de utilizar componentes del sistema en otros proyectos.
     - **Escalabilidad:** Capacidad del sistema para crecer en términos de usuarios, datos, etc.
     - **Seguridad:** Medidas para proteger el sistema contra accesos no autorizados y daños.
     - **Trazabilidad:** Capacidad de rastrear cada requerimiento a lo largo del ciclo de vida del proyecto.
     - **Restricciones legales y normativas:** Cumplimiento de leyes y regulaciones aplicables.
   - **Ejemplos:**
     - "El sistema debe ser capaz de manejar hasta 10,000 usuarios concurrentes."
     - "El sistema debe garantizar que los datos personales estén cifrados."

#### Diferenciación entre Requisitos de Usuario y Requisitos Software

1. **Requisitos de Usuario:**

   - **Descripción:** Son declaraciones en lenguaje natural que describen las funciones y restricciones desde la perspectiva del usuario. Estos requisitos detallan lo que los usuarios pueden hacer con el sistema.
   - **Documento de Requisitos de Usuario (DRU):** Recoge todas estas declaraciones y es utilizado para capturar las expectativas y necesidades del usuario.
   - **Ejemplo:**
     - "Un estudiante podrá matricularse de todas las asignaturas pendientes de un curso."

2. **Requisitos Software:**

   - **Descripción:** Derivados de los requisitos de usuario, especifican de manera detallada y técnica qué debe hacer el software y cómo debe comportarse para cumplir con los objetivos planteados.
   - **Especificación de Requisitos Software (ERS):** Este documento recoge todos los requisitos técnicos y sirve como base para el diseño y desarrollo del sistema.
   - **Proceso de Traducción:**
     - **Requisito de Usuario:** "Un estudiante podrá matricularse de todas las asignaturas pendientes de un curso."
     - **Requisitos Software:** 
       - "El sistema debe consultar los datos del expediente del estudiante."
       - "El sistema debe validar que las asignaturas seleccionadas están disponibles para matriculación."
       - "El sistema debe calcular el importe de la matrícula según el número de asignaturas y el número de matrículas anteriores."
       - "El sistema debe generar una confirmación de matrícula y enviarla por correo electrónico."

#### Importancia del Análisis de Requisitos

El análisis de requisitos es fundamental para el éxito del proyecto de software. Es en esta fase donde se define claramente lo que el sistema debe hacer y bajo qué condiciones y restricciones. Cualquier error o ambigüedad en los requisitos puede propagarse a lo largo del ciclo de vida del desarrollo, resultando en un producto final que no satisface las necesidades del usuario.

#### Validación de Requisitos

Para asegurar que los requisitos son correctos y completos, se deben validar mediante revisiones con el cliente y verificaciones internas. Los requisitos deben cumplir con los siguientes atributos:

- **Completitud:** Todos los aspectos necesarios del sistema están cubiertos.
- **No Ambigüedad:** Cada requisito tiene una única interpretación.
- **Trazabilidad:** Cada requisito debe poder ser rastreado a lo largo del desarrollo y vinculado a un componente del diseño o una funcionalidad.
- **Corrección:** Los requisitos reflejan fielmente las necesidades del usuario y del negocio.
- **Consistencia:** No existen requisitos contradictorios.

Finalmente, en metodologías ágiles, los requisitos se gestionan a través de historias de usuario, que capturan funcionalidades de manera incremental y adaptable a lo largo del desarrollo del proyecto.

