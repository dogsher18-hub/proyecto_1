# Proyecto 1

> Proyecto de generación de grafos utilizando Python.

Crea y exporta grafos a archivos <code>.dot</code> para su posterior visualización. El código implementa una estructura de datos de grafo desde cero, con clases para Nodos, Aristas y el Grafo mismo. A partir de esta base, se desarrollan funciones para generar grafos siguiendo los siguientes algoritmos:

- Malla: Genera un grafo con una estructura de rejilla (filas y columnas).
- Erdös-Rényi: Crea un grafo aleatorio con un número específico de nodos y aristas.
- Gilbert: Genera un grafo aleatorio donde cada par de nodos tiene una probabilidad definida de estar conectado.
- Geográfico Simple: Crea un grafo donde los nodos se distribuyen en un espacio y se conectan si su distancia es menor o igual a un radio r.
- Dorogovtsev-Mendes: Genera un grafo a partir de un triángulo inicial, añadiendo nodos que se conectan a los extremos de una arista seleccionada al azar.
- Barabási-Albert: Construye un grafo "libre de escala" donde los nuevos nodos tienden a conectarse a los nodos que ya tienen un alto grado (conexión preferencial).

---

# Proyecto 2

> Implementación de algoritmos de búsqueda sobre la estructura de grafos.

A partir de la estructura desarrollada en el Proyecto 1, se incorporan algoritmos clásicos de **recorrido de grafos**. Estos métodos permiten explorar los nodos del grafo y construir árboles de expansión que representan la secuencia en la que se descubren los nodos durante la búsqueda.

Los algoritmos implementados son los siguientes:

- **Búsqueda a lo ancho (BFS)**:  
  Recorre el grafo nivel por nivel, comenzando desde un nodo inicial. Utiliza una cola para explorar primero todos los vecinos inmediatos antes de pasar a los nodos más lejanos. El método `BFS(inicio)` construye y devuelve el árbol BFS correspondiente.

- **Búsqueda en profundidad recursiva (DfsR)**:  
  Explora el grafo profundizando en cada rama antes de retroceder. Este método se implementa de manera recursiva, registrando los nodos visitados y construyendo el árbol DFS resultante.

- **Búsqueda en profundidad iterativa (DfsIte)**:  
  Variante iterativa de la búsqueda en profundidad. Utiliza una pila en lugar de recursión para recorrer los nodos del grafo. Al igual que en la versión recursiva, genera el árbol de expansión asociado.

Estos métodos permiten analizar la conectividad y estructura del grafo.
