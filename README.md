# Árbol Binario de Búsqueda en Python

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un programa en Python que permite implementar y administrar un **Árbol Binario de Búsqueda (ABB)** mediante una interfaz gráfica creada con Tkinter.

El programa permite insertar, buscar, eliminar y recorrer elementos, además de calcular información sobre la estructura del árbol y comprobar si cumple las propiedades de un árbol binario completo o lleno.

Su desarrollo está basado en los conceptos vistos en clase sobre árboles binarios.

## Estructura interna del código

El programa está organizado en tres partes principales:

### 1. Clase `Nodo`

Representa cada elemento del árbol. Almacena un dato y dos referencias que permiten conectar el nodo con sus hijos: uno izquierdo y otro derecho.

### 2. Clase `Arbol`

Es la encargada de administrar la estructura del árbol binario de búsqueda. Contiene la raíz y los métodos necesarios para realizar las operaciones.

Entre sus principales funciones se encuentran:

- **Inserción y búsqueda:** agrega elementos respetando las reglas del árbol y permite localizar valores.
- **Recorridos:** realiza los recorridos PreOrden, InOrden, PostOrden y por niveles.
- **Cálculos:** obtiene la altura, cantidad de hojas y cantidad total de nodos.
- **Comprobaciones:** verifica si el árbol es completo o lleno.
- **Eliminación:** permite eliminar elementos utilizando el predecesor o sucesor.
- **Visualización:** muestra el árbol acostado o mediante una representación gráfica.
- **Eliminación total:** permite vaciar completamente el árbol.

### 3. Clase `ArbolApp`

Se encarga de crear y controlar la interfaz gráfica utilizando Tkinter. Administra el menú de operaciones, recibe los datos introducidos por el usuario, ejecuta los métodos correspondientes y muestra los resultados.

El método ejecutar() identifica la opción seleccionada y determina qué operación debe realizarse.

## Funcionamiento del programa

Al ejecutar el programa aparece una ventana que contiene un menú desplegable con las operaciones disponibles, un campo para introducir números, botones para ejecutar y limpiar resultados, un área de texto y una representación gráfica del árbol.

### Opciones del menú

| Opción | Funcionamiento |
|---|---|
| 1. Insertar elemento | Agrega un nuevo número al árbol respetando el orden del ABB. No permite valores repetidos. |
| 2. Mostrar árbol acostado | Representa el árbol mediante texto, colocando la raíz hacia la izquierda. |
| 3. Graficar árbol | Abre una ventana que muestra gráficamente los nodos y sus conexiones. |
| 4. Buscar elemento | Busca un número y lo resalta en verde en la representación gráfica cuando existe. |
| 5. PreOrden | Visita primero la raíz, después el subárbol izquierdo y finalmente el derecho. |
| 6. InOrden | Recorre primero el subárbol izquierdo, después la raíz y finalmente el derecho. |
| 7. PostOrden | Recorre primero el subárbol izquierdo, después el derecho y finalmente la raíz. |
| 8. Eliminar mediante predecesor | Elimina un elemento utilizando el predecesor cuando tiene dos hijos. |
| 9. Eliminar mediante sucesor | Elimina un elemento utilizando el sucesor cuando tiene dos hijos. |
| 10. Recorrido por niveles | Visita los nodos comenzando por la raíz y continuando de izquierda a derecha por niveles. |
| 11. Altura del árbol | Calcula la cantidad de niveles que tiene el árbol. |
| 12. Cantidad de hojas | Cuenta los nodos que no tienen hijos. |
| 13. Cantidad de nodos | Cuenta todos los elementos que forman parte del árbol. |
| 14. Información general | Muestra la raíz, altura, cantidad de nodos, hojas, estado del árbol y recorrido por niveles. |
| 15. Árbol completo | Comprueba si todos los niveles, excepto posiblemente el último, están llenos y si sus nodos están colocados de izquierda a derecha. |
| 16. Árbol lleno | Comprueba que cada nodo tenga cero o dos hijos. |
| 17. Eliminar árbol | Elimina todos los elementos después de solicitar una confirmación. |

**Nota:** La opción 14 es una función adicional incorporada al programa; no aparece en la lista original de operaciones de la presentación de clase.

## Conceptos aplicados

### Árbol Binario de Búsqueda

Es una estructura de datos en la que cada nodo puede tener como máximo dos hijos. Los valores menores se colocan en el subárbol izquierdo y los mayores en el derecho.

### Árbol binario completo

Es aquel en el que todos los niveles, excepto posiblemente el último, están completamente ocupados. Los nodos del último nivel deben colocarse de izquierda a derecha.

### Árbol binario lleno

Es aquel en el que cada nodo tiene exactamente cero o dos hijos. No puede existir un nodo con un solo hijo.

### Recursividad

Se utiliza en diferentes métodos del programa para recorrer, buscar, insertar, calcular y comprobar las características del árbol.

### Cola

Se utiliza en el recorrido por niveles y en la comprobación de si el árbol es completo, permitiendo procesar los nodos en el orden correspondiente.

## Tecnologías utilizadas

- **Python:** lenguaje utilizado para desarrollar la lógica del programa.
- **Tkinter:** biblioteca utilizada para construir la interfaz gráfica.
- **ttk:** componentes adicionales para los elementos visuales.
- **messagebox:** ventanas de información, advertencia y confirmación.
- **deque:** estructura utilizada para implementar las colas.

## Requisitos para ejecutar el programa

- Tener Python instalado.
- Contar con Tkinter disponible en la instalación de Python.
- Utilizar un editor de código como Visual Studio Code.

## Ejecución del programa

1. Descargar o clonar este repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir el archivo Python que contiene el programa.
4. Ejecutar el archivo desde la terminal:

bash
python nombre_del_archivo.py

## Ejemplo de prueba

Para comprobar el funcionamiento del programa se pueden insertar los siguientes valores:

text
8, 3, 1, 20, 5, 10, 7, 4


Después de insertar los elementos, se pueden probar los recorridos, la búsqueda, las eliminaciones y las comprobaciones de árbol completo y lleno.

## Objetivo del proyecto

Aplicar los conocimientos adquiridos en clase sobre árboles binarios de búsqueda mediante la implementación de sus clases, métodos y operaciones en Python, utilizando una interfaz gráfica que facilite su manipulación y visualización.

---

**Proyecto académico: Estructuras de Datos**

**Lenguaje:** Python
