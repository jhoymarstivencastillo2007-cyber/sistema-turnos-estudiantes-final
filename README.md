# Sistema de Turnos para Atención de Estudiantes

## 1. Descripción del sistema

Este proyecto consiste en un sistema de turnos para atender estudiantes en una institución educativa.

El sistema permite registrar los datos de los estudiantes, buscar y eliminar registros, organizar estudiantes en una cola de atención y consultar diferentes estructuras de datos.

La idea es representar una situación real en la que varios estudiantes necesitan realizar diferentes trámites y deben ser atendidos de manera organizada.

## 2. Datos de los estudiantes

Cada estudiante tiene los siguientes datos:

- Código
- Nombre
- Motivo de la atención
- Dependencia

Ejemplos:

- 1001 - María - Matrícula - Registro Académico
- 1002 - José - Certificado - Secretaría
- 1003 - Santiago - Notas - Registro Académico

## 3. Estructuras de datos utilizadas

En el proyecto se utilizan las siguientes estructuras:

- Lista enlazada simple
- Cola
- Árbol binario de búsqueda (BST)
- Grafo con listas de adyacencia

También se implementaron dos versiones de la cola:

- Cola utilizando un arreglo.
- Cola utilizando una lista enlazada.

## 4. Justificación de las estructuras

### Lista enlazada

Se utiliza una lista enlazada simple para almacenar los registros principales de los estudiantes.

Se escogió porque permite recorrer los estudiantes y realizar operaciones como insertar, buscar y eliminar sin utilizar estructuras como ArrayList o LinkedList.

Cada nodo contiene un estudiante y una referencia al siguiente nodo.

### Cola

La cola se utiliza para organizar la atención de los estudiantes.

Se escogió porque sigue el principio de primero en entrar, primero en salir. De esta manera, el estudiante que llega primero es atendido primero.

La cola fue implementada de dos formas:

1. Utilizando un arreglo.
2. Utilizando una lista enlazada.

Las dos versiones utilizan las mismas operaciones principales: encolar, desencolar y mostrar.

### Árbol BST

El árbol binario de búsqueda utiliza el código del estudiante como clave.

Los códigos menores se colocan hacia la izquierda y los códigos mayores hacia la derecha.

Esto permite realizar búsquedas siguiendo el orden de los códigos.

También se implementaron los recorridos:

- Preorden
- Inorden
- Postorden

El recorrido inorden permite obtener los códigos en orden ascendente.

### Grafo

El grafo representa las conexiones entre diferentes dependencias de la institución.

Se utilizaron listas de adyacencia para representar las conexiones.

Las dependencias utilizadas son:

- Registro Académico
- Secretaría
- Tesorería

Se pueden consultar las conexiones de una dependencia y comprobar si existe una conexión entre dos dependencias.

## 5. Organización de las clases

La organización principal del sistema es:

Estudiante
|
|-- ListaEnlazada
|      |
|      |-- Nodo
|
|-- Cola
|
|-- ColaLista
|      |
|      |-- NodoCola
|
|-- ArbolBST
|      |
|      |-- NodoArbol
|
|-- Grafo

La clase Estudiante contiene los datos principales de cada estudiante.

Las demás clases utilizan estos datos para realizar las diferentes operaciones del sistema.

## 6. Comparación de costos

| Operación | Cola con arreglo | Cola con lista enlazada |
|-----------|------------------|-------------------------|
| Encolar   | O(1)             | O(1)                    |
| Desencolar| O(n)             | O(1)                    |
| Mostrar   | O(n)             | O(n)                    |

En la cola con arreglo, agregar un estudiante al final es una operación rápida. Sin embargo, al atender al primer estudiante se utiliza pop(0), lo que puede hacer que los demás elementos tengan que desplazarse.

En la cola con lista enlazada se mantienen referencias al frente y al final de la cola. Por eso, agregar y retirar un estudiante se pueden realizar sin desplazar los demás elementos.

Para mostrar todos los estudiantes, las dos implementaciones deben recorrer los elementos, por lo que esta operación tiene un costo O(n).

## 7. Costos de la lista enlazada principal

| Operación | Costo |
|-----------|-------|
| Insertar al final | O(n) |
| Buscar | O(n) |
| Eliminar | O(n) |
| Recorrer | O(n) |

La lista enlazada utilizada en el proyecto recorre los nodos desde el primero hasta encontrar la posición necesaria. Por esta razón, estas operaciones pueden necesitar recorrer una parte importante de la lista.

## 8. Experimento de altura del BST

Se realizó un experimento utilizando diferentes cantidades de claves para observar cómo cambia la altura del árbol.

| Cantidad de claves | Altura |
|---------------------|--------|
| 5                   | 3      |
| 10                  | 4      |
| 15                  | 5      |

En este proyecto la altura se cuenta por cantidad de niveles. Por eso, un árbol con un solo nodo tiene altura 1.

Al aumentar la cantidad de claves, la altura del árbol también aumentó.

Con 5 claves la altura fue 3, con 10 claves fue 4 y con 15 claves fue 5.

También se probó insertar las 15 claves en orden ascendente. En este caso el árbol quedó prácticamente como una lista y su altura llegó a 15.

Esto muestra que el orden en el que se insertan las claves puede afectar bastante la forma del árbol. Cuando el árbol queda muy inclinado, una búsqueda puede necesitar recorrer muchos nodos.

Por esta razón, mantener el árbol más equilibrado ayuda a que las operaciones sean más eficientes.

## 9. Árbol AVL

Como parte del análisis del árbol BST, se realizó manualmente un ejemplo de inserción de claves en orden ascendente:

10, 20, 30, 40, 50, 60, 70.

Al insertar las claves, el árbol puede quedar desbalanceado. Para solucionar esto se realizan rotaciones que cambian la posición de algunos nodos sin eliminar los datos.

En el ejercicio se realizaron rotaciones hacia la izquierda para mantener el árbol equilibrado.

El resultado final del ejemplo fue:

        40
       /  \
     20    60
    / \    / \
   10 30  50 70

Este ejemplo permite observar cómo un árbol equilibrado puede tener una altura menor que un árbol que queda completamente inclinado hacia un lado.

Evidencia del ejercicio:

Se incluye una fotografía del dibujo manual realizado durante la actividad.

avl_dibujo.jpg

## 10. Cómo ejecutar el programa

### Requisitos

- Python 3 instalado.
- Visual Studio Code u otro editor de código.

### Ejecución

1. Abrir la carpeta del proyecto.
2. Abrir una terminal.
3. Ejecutar:

python sistema.py

También se puede ejecutar el archivo de pruebas:

python main.py

## 11. Pruebas realizadas

Durante el desarrollo se realizaron diferentes pruebas para comprobar que el sistema funcionara correctamente.

### Registro de estudiantes

Se comprobó que los estudiantes se puedan registrar con su código, nombre, motivo y dependencia.

### Búsqueda

Se probó la búsqueda de estudiantes registrados y también la búsqueda de un código que no existe.

### Eliminación

Se comprobó que un estudiante pueda ser eliminado correctamente y también se probó el caso de eliminar un estudiante que no existe.

### Cola

Se comprobó que:

- Los estudiantes se agreguen en orden de llegada.
- El primero en entrar sea el primero en ser atendido.
- La cola pueda quedar vacía.
- La cola muestre un mensaje cuando esté llena.
- Se pueda utilizar la cola con arreglo.
- Se pueda utilizar la cola con lista enlazada.

### Árbol BST

Se probaron:

- La inserción de estudiantes.
- La búsqueda por código.
- La eliminación de estudiantes.
- Los códigos repetidos.
- El recorrido preorden.
- El recorrido inorden.
- El recorrido postorden.
- La altura del árbol.

### Grafo

Se probaron dos consultas:

- Mostrar las conexiones de una dependencia.
- Comprobar si existe conexión entre dos dependencias.

### Casos extremos

También se probaron algunos casos especiales:

- Intentar registrar dos estudiantes con el mismo código.
- Buscar un estudiante que no existe.
- Eliminar un estudiante que no existe.
- Intentar atender cuando la cola está vacía.
- Intentar agregar estudiantes cuando la cola está llena.
- Eliminar un estudiante y comprobar que también desaparezca del árbol BST.

## 12. Limitaciones y mejoras

### Limitaciones

El sistema funciona correctamente para una cantidad pequeña de estudiantes, pero actualmente los datos no se guardan de manera permanente cuando se cierra el programa.

Además, la cola tiene una capacidad limitada de 5 estudiantes.

El sistema funciona desde la terminal y no cuenta con una interfaz gráfica.

### Posibles mejoras

En el futuro se podría agregar una base de datos para guardar la información de los estudiantes.

También se podría crear una interfaz gráfica para que el sistema sea más fácil de utilizar.

Otra mejora sería permitir configurar la capacidad de la cola y agregar más opciones para administrar los estudiantes.

## 13. Video de presentación

En el video se explica el funcionamiento del sistema y las estructuras de datos utilizadas.

También se muestran las pruebas realizadas, el funcionamiento de la cola, el árbol BST, el grafo, el experimento de altura y el ejercicio manual del árbol AVL.

### Enlace del video

PEGAR AQUÍ EL ENLACE DEL VIDEO

## 14. Conclusión

El proyecto permitió aplicar diferentes estructuras de datos en un caso práctico relacionado con la atención de estudiantes.

Se implementaron una lista enlazada, dos tipos de cola, un árbol binario de búsqueda y un grafo.

También se realizaron pruebas con diferentes casos y un experimento para observar cómo cambia la altura del árbol dependiendo del orden de inserción.

Finalmente, el ejercicio del árbol AVL permitió comprender la importancia de mantener un árbol equilibrado para mejorar las búsquedas.