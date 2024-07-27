                    Empezando una Conversación con Python

Ahora que ya sabemos una palabra (print) y cómo crear una frase sencilla en Python, vamos a aprender cómo conversar con Python para practicar.

                    Instalación de Python

Antes de conversar con Python, necesitas instalar el software en tu computadora. Puedes encontrar instrucciones detalladas en https://es.py4e.com/ para configurar e iniciar Python en sistemas Macintosh y Windows. El sitio oficial de python es: https://www.python.org/.


                    Iniciar Python

Una vez instalado, abre una ventana de comandos (terminal) y escribe python. Verás algo como esto:

                    C:\Users\Feder>python
                    Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>>

El símbolo >>> es Python preguntando "¿Qué quieres que haga ahora?". Python está listo para conversar contigo.


                    Analogía del Astronauta

Imagina que eres un astronauta en un planeta lejano y tratas de hablar con los habitantes. Primero intentas esto:


>>> Vengo en son de paz, por favor llévame ante tu líder
File "<stdin>", line 1
Vengo en son de paz, por favor llévame ante tu líder
    ^^
SyntaxError: invalid syntax


Pero Python no entiende y da un error. Es como si los habitantes del planeta no entendieran tu idioma y se prepararan para atacarte. Entonces intentas de nuevo con algo más simple que sí entienden:

>>> print("Hola mundo ")
Hola mundo


Esto funciona. Ahora puedes seguir conversando:

>>> print("Usted debe ser el dios legendario que viene del cielo")
Usted debe ser el dios legendario que viene del cielo
>>> print("Hemos estado esperandole durante mucho tiempo")
Hemos estado esperandole durante mucho tiempo
>>>


                    Sintaxis Correcta

Pero si cometes un error, Python no entiende y te da otro error:

>>> Tendremos un festin esta noche a menos que diga
  File "<stdin>", line 1
    Tendremos un festin esta noche a menos que diga
              ^^
SyntaxError: invalid syntax
>>> print "Tendremos un festin esta noche a menos que diga"
  File "<stdin>", line 1
    print "Tendremos un festin esta noche a menos que diga"
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>


Python necesita que uses la sintaxis correcta. Es como un robot que sigue reglas estrictas y no puede adivinar lo que quieres decir.


                    Conversación con Programadores

Cuando usas un programa hecho por otra persona, en realidad estás "conversando" con el programador a través de Python. Python es solo una herramienta que permite a los programadores expresar cómo debe fluir la conversación.


                    Decir Adiós a Python

Para terminar la conversación con Python, debes usar quit():

>>> Adios
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Adios' is not defined
>>> quit()

El primer intento falla porque "adiós" no es una palabra que Python entiende y requiere una sintaxis correcta. Pero quit() funciona.