# Proyecto 1

> Proyecto de generación de grafos utilizando Python.

Crea y exporta grafos a archivos <code>.dot</code> para su posterior visualización. El código implementa una estructura de datos de grafo desde cero, con clases para Nodos, Aristas y el Grafo mismo. A partir de esta base, se desarrollan funciones para generar grafos siguiendo los siguientes algoritmos:

- Malla: Genera un grafo con una estructura de rejilla (filas y columnas).
- Erdös-Rényi: Crea un grafo aleatorio con un número específico de nodos y aristas.
- Gilbert: Genera un grafo aleatorio donde cada par de nodos tiene una probabilidad definida de estar conectado.
- Geográfico Simple: Crea un grafo donde los nodos se distribuyen en un espacio y se conectan si su distancia es menor o igual a un radio r.
- Dorogovtsev-Mendes: Genera un grafo a partir de un triángulo inicial, añadiendo nodos que se conectan a los extremos de una arista seleccionada al azar.
- Barabási-Albert: Construye un grafo "libre de escala" donde los nuevos nodos tienden a conectarse a los nodos que ya tienen un alto grado (conexión preferencial).

