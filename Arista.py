class Arista:



    def __init__(self, origen, destino, dirigida=False):
        """
        Inicializa una arista entre dos nodos.
        
        -origen: Nodo de origen
        -destino: Nodo de destino
        -dirigida: Booleano que indica si la arista es dirigida
                    (por defecto False)
        """
        self.origen = origen
        self.destino = destino
        self.dirigida = dirigida
    


    def obtener_nodos(self):
        """
        Devuelve los nodos conectados por la arista.
        
        -tipo_de_dato:  tupla.
        -retorna:       (origen, destino).
        """
        return (self.origen, self.destino)
    

    
    def es_dirigida(self):
        """
        Indica si la arista es dirigida.
        
        -tipo_de_dato:  booleano.
        -retorna:       'True' si es dirigida, 'False' si no lo es.
        """
        return self.dirigida
    


    def __str__(self):
        """
        Representación en string de la arista.
        
        -tipo_de_dato:  string.
        -retorna:       '->' si es dirigida, '--' en otro caso.
        """
        direccion = "->" if self.dirigida else "--"
        return f"{self.origen.obtener_valor()} {direccion} {self.destino.obtener_valor()}"
    

    