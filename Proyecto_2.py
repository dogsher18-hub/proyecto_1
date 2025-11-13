import time
import Grafo as gr

#creacion de grafos Gilbert y sus recorridos BFS y DFS
# ===== Grafo Gilbert con 30 nodos =====
grafo_gilbert_30 = gr.Grafo()
grafo_gilbert_30.grafoGilbert(nodos=30, pro=0.1)
grafo_gilbert_30.archivo_grafo('GrafoGilbert30')
#BFS
arbol_bfs_gilbert_30 = grafo_gilbert_30.BFS(inicio="1")
arbol_bfs_gilbert_30.archivo_grafo('ArbolBfsGilbert30')
#DFS Iterativo
arbol_dfs_iter_gilbert_30 = grafo_gilbert_30.DfsIte(inicio="1")
arbol_dfs_iter_gilbert_30.archivo_grafo('ArbolDfsIterGilbert30')
#DFS Recursivo
arbol_dfs_rec_gilbert_30 = grafo_gilbert_30.DfsR(inicio="1")
arbol_dfs_rec_gilbert_30.archivo_grafo('ArbolDfsRecGilbert30')
# ===== Grafo Gilbert con 100 nodos =====
grafo_gilbert_100 = gr.Grafo()
grafo_gilbert_100.grafoGilbert(nodos=100, pro=0.1)
grafo_gilbert_100.archivo_grafo('GrafoGilbert100')
#BFS
arbol_bfs_gilbert_100 = grafo_gilbert_100.BFS(inicio="1")
arbol_bfs_gilbert_100.archivo_grafo('ArbolBfsGilbert100')
#DFS Iterativo
arbol_dfs_iter_gilbert_100 = grafo_gilbert_100.DfsIte(inicio="1")
arbol_dfs_iter_gilbert_100.archivo_grafo('ArbolDfsIterGilbert100')
#DFS Recursivo
arbol_dfs_rec_gilbert_100 = grafo_gilbert_100.DfsR(inicio="1")
arbol_dfs_rec_gilbert_100.archivo_grafo('ArbolDfsRecGilbert100')
# ===== Grafo Gilbert con 500 nodos =====
grafo_gilbert_500 = gr.Grafo()
grafo_gilbert_500.grafoGilbert(nodos=500, pro=0.1)
grafo_gilbert_500.archivo_grafo('GrafoGilbert500')
#BFS
arbol_bfs_gilbert_500 = grafo_gilbert_500.BFS(inicio="1")
arbol_bfs_gilbert_500.archivo_grafo('ArbolBfsGilbert500')
#DFS Iterativo
arbol_dfs_iter_gilbert_500 = grafo_gilbert_500.DfsIte(inicio="1")
arbol_dfs_iter_gilbert_500.archivo_grafo('ArbolDfsIterGilbert500')
#DFS Recursivo
arbol_dfs_rec_gilbert_500 = grafo_gilbert_500.DfsR(inicio="1")
arbol_dfs_rec_gilbert_500.archivo_grafo('ArbolDfsRecGilbert500')
print('Terminó de crear grafos Gilbert', time.strftime("%H:%M:%S"))