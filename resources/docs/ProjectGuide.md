# Guia de proyectos de la asignatura "Machine learning techniques"
Autor/es:
* Roberto Plaza Romero

Miembros del equipo de proyecto:
* Alfonso Barragán Carmona
* Javier Monescillo Buitrón
* Roberto Plaza Romero

Miembros pendientes de aprobación:
* Alfonso Barragán Carmona
* Javier Monescillo Buitrón
* Roberto Plaza Romero

Esta es una guía para contribuir y participar al proyecto de machine learning techniques. Todos los participantes debrán aprobar, vía firma o acuerdo verbal, que están de acuerdo con esta guía y, por ende, la acatarán en todos los aspectos que cubran.

Las directivas podrán cambiarse hasta que todos los miembros del equipo de proyecto den su aprobación, una vez aprobada la guía de proyecto, para cambiar esta se deberá mediante una comitiva de por lo menos 3 de los miembros del equipo de proyecto.

## Guía de github
### Guia de branches
El repositorio github consta de 2 branches:
* Master: branch principal, es aquí donde se subirá el contenido final.
* Experimental: branch secundaria, se usará para transferir archivos entre el equipo de proyecto. Análogamente el grupo de telegram del mismo equipo de proyecto podrá también ser usado para compartir archivos.
### Guía de commits
Los "push" a la branch master realizarán **una vez al día**, en un periodo de tiempo comprendido entre las **20:00 y las 24:00** con motivo de no saturar la main branch de commits mínimos.

Caso de que se haga un push extraordinario a la branch "master" hay que notificarlo por escrito y en ningún caso se podrán realizar más de 1 de estos al día.

## Guía de Directorios
El projecto está dividido en subdirectorios.

Habrá un subdirectorio por entregable en el proyecto final, la estructura de este subdirectorio dependerá del entregable, pero siempre tendrá un directorio "data/" en el cual estarán guardadas las bases de datos a usar durante los milestones.

Análogamente habrá una carpeta "resources", en la cual se incorporarán el resto de archivos dentro de subdirectorios nombrados según la naturaleza de los archivos que guardan.
E.g: los archivos .png, .jpg, .bmp, ... al ser todos imágenes irán dentro de la carpeta img/

## Guía de estilos: Python
Diccionario de nomenclatura:
* Pascal case = CadenasComoEsta
* Camel case = cadenasComoEsta
* Snake case = cadenas_como_esta o Cadenas_Como_Esta o cadenas_Como_Esta
* Kebab case = cadenas-como-esta o Cadenas-Como-Esta o cadenas-Como-Esta

### Nombramiento en este proyecto
**Escribiremos el código en inglés**
* Variables --> Snake Case todo minúsculas. e.g: variable_entera = 0, variable_cadena = ""
* Nombres de clases --> Pascal case. e.g: ObjetoUno, AsistendeDeConcurrencia, GraficoKMeans
* Nombres de funciones --> Camel case. e.g: nombreDeFuncion(), otroNombreDeFuncion()
* Atributos --> Snake Case todo minúsculas, igual que las variables.

Todas las variables han de tener nombres representativos.
* Las clases han de ser sustantivos.
* Las funciones han de ser verbos. **Caso especial**, las funciones que devuelvan valores booleanos deberan empezar por "is" segido del nombre representativo a elección. e.g: isEven(), isOdd()
* Los atributos han de ser adjetivos.

### Formato de declaraciones
#### Variables
Siempre que sea posible se declararán las variables de antemano como si de C o java se tratase, las variables enteras se inicializarán a 0, las reales a 0.0, las cadenas a "" y las TAD's a None. Después de estas declaraciones iniciales se dejará una (1) línea en blanco.

Se procurará dentro de un mismo bloque que todos los símbolos de asignación sean estén alineados (a.k.a: en la misma columna), para ello se tabulará lo que sea necesario hasta conseguirlo.

Código Ejemplo:
```python
unused_integer_variable = 0
used_integer_variable   = 1
unused_string           = ""
used_string             = "Hello, World"
unused_object           = None
used_object             = ObjectFactory()

# Some Code

unused_object           = used_object.create()
```

#### Clases y Métodos
##### Métodos
Se definirán los métodos de la siguiente manera:
* Nombre del método, los atributos en una lista separada por coma y espacio.
* Se empezará a definir en método sin dejar una línea en blanco.
* El siguiente método seguido de una (1) línea en blanco
* En el caso de que empiece un entrypoint se dejarán dos (2) líneas en blanco.
* En el caso de que no quede muy claro donde acaba una función se deberá hacer un "return None" para dejarlo claro.

##### Clases
Para definir una clase se hará de la siguiente manera:
* Nombre de la clase y constructor en la línea siguiente sin dejar línea una línea en blanco.
* Dentro del constructor se inicializarán los atributos como si de variables se trataran, usando la convención anterior.
* Los métodos de la clase se definirán dejando una (1) línea en blanco entre método y método, como en la convención anterior.
* Se acabará con dos (2) líneas en blanco hasta la siguiente definición.

Código Ejemplo:
```python
class MyClase():
    def __init__(self, value):
        self.not_init_variable  = ""
        self.init_variable      = value

    def funcion(self):
        pass


def otraFuncion(objeto):
    objeto.not_init_variable    = "Hola, mundo"

def terceraFunción():
    pass


# Resto del código
```

### Entrypoint
El punto de entrada de un módulo será definido de la siguiente forma:
```python
if __name__ == '__main__':
    # El programa empieza aquí
```

### Imports
Vía libre, pero entre imports y definiciones será obligatorio dejar dos (2) líneas en blanco.

### Casos adicionales
Se adjuntará por cada entregable un archivo "paths.py" en el cual estará guardado el nombre de todos los archivos relevantes. **Importante:** Ninguna de las variables deberá tener más de un '/', véase, si los directorios han de guardarse también. e.g:
```python
databases           = 'data/'
untreated_database  = databases + 'T2.csv'
```

## Disclaimer
Este documento está escrito en español puesto que no compete al contenido de la asignatura, por ende el autor original consideró que español era la mejor lengua para redactar y este documento y hacerlo comprensible.
