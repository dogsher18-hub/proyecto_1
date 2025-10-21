import Grafo as gr

##########malla
#8x8=64 nodos, 112 aristas.
grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=8,columnas=8)
grafoMalla.archivo_grafo('GrafoMalla50')
#15x15=225 nodos, 420 aristas.
grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=15,columnas=15)
grafoMalla.archivo_grafo('GrafoMalla200')
#25x25=625 nodos, 1200 aristas.
grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=25,columnas=25)
grafoMalla.archivo_grafo('GrafoMalla500')

##########erdosreny
#50 nodos, 150 aristas.
grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=50,aristas=150)
grafoErdosReny.archivo_grafo('ErdosReny50')
#200 nodos, 600 aristas.
grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=300,aristas=900)
grafoErdosReny.archivo_grafo('ErdosReny300')
#500 nodos, 1500 aristas.
grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=500,aristas=1500)
grafoErdosReny.archivo_grafo('ErdosReny500')
    
##########gilbert
#50 nodos, probabilidad 0.25
grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(50,0.25)
grafoGilbert.archivo_grafo('grafoGilbert50')
#200 nodos, probabilidad 0.05
grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(200,0.05)
grafoGilbert.archivo_grafo('grafoGilbert200')
#500 nodos, probabilidad 0.01
grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(500,0.01)
grafoGilbert.archivo_grafo('grafoGilbert500')

###########grafo simple
#50 nodos, r=10
grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=50,r=10)
grafoSimple.archivo_grafo('grafoSimple50')
#200 nodos, r=20
grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=200,r=20)
grafoSimple.archivo_grafo('grafoSimple200')
#500 nodos, r=30
grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=500,r=30)
grafoSimple.archivo_grafo('grafoSimple500')

###########dorogovtsevmendes
#50 nodos
grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(50)
grafoDoroMendes.archivo_grafo('grafoDoroMendes50')
#200 nodos
grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(200)
grafoDoroMendes.archivo_grafo('grafoDoroMendes200')
#500 nodos
grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(500)
grafoDoroMendes.archivo_grafo('grafoDoroMendes500')

###########barabasi-albert
#50 nodos, m=3
grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(50,3)
grafoGusano.archivo_grafo('Gusano50')
#200 nodos, m=5
grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(200,5)
grafoGusano.archivo_grafo('Gusano200')
#500 nodos, m=7
grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(500,7)
grafoGusano.archivo_grafo('Gusano500')














