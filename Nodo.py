class Nodo:



    def __init__(self, valor):
        """
        Inicializa un nodo con un valor especifico.
        
        -valor: El valor que almacenará el nodo
                (puede ser cualquier tipo de dato).
        """
        self.valor = valor
        #Diccionario para almacenar nodos adyacentes (para grafos ponderados)
        self.vecinos = {}  
    


    def agregar_vecino(self, nodo):
        """
        Agrega un nodo vecino.
        
        -nodo: El nodo vecino a agregar.
        """
        # Se asigna un peso de 1 por defecto
        self.vecinos[nodo] = 1
    


    def obtener_vecinos(self):
        """
        Devuelve los nodos vecinos.
        
        -tipo_de_dato:  diccionario.
        -retorna:       Diccionario de nodos vecinos con sus pesos.
        """
        return self.vecinos
    


    def obtener_valor(self):
        """
        Devuelve el valor almacenado en el nodo.
        """
        return self.valor
    
    def __str__(self):
        """
        Representación en string del nodo.

        -tipo_de_dato:  string.
        -retorna:       String que muestra el valor del nodo y sus vecinos.
        """
        vecinos_str = ", ".join([f"{n.obtener_valor()}" for n in self.vecinos.items()])
        return f"Nodo({self.valor}) -> [{vecinos_str}]"