# Conectividad en grafos
## Arco conectividad de un grafo

Cual es el minimo cantidad de arcos que hay que quitar para que el arco se desconecte  
lambda(G)

## Nodo conectividad de un grafo
Cual es la minima cantidad de nodos que debe qutiar para que se desconecte ese grafo  
K(G)

## Teorema 7.6 (whitney Inequality)
Condición de grafos conectividad para todo grafo debe de un grafo g su conectividad (por nodos<=conectividad por arcos<=su grado minimo) -> k(G) <= lambda(G) <= GradoMinimo(G)

## Teorema de withney - sea G un grafo tal que cantidad de nodos >= 3
Si K(G)=2, entonces para cada par de vértices distintos u, v, existen dos trayectorias de u a v internamente disyuntas, es decir que sus rutas intermedias no se pueden cruzar.

Es decir que el valor de la nodo conectividad esa cantidad hay de trayectorias que no se cruzan

### Demostración por inducción en la distancia entre vectices d(u, v)
Sean u, v dos nodos cualquiera de G.

#### Caso base
d(u,v) = 1

si es asi es por que son vecinos; si G\uv (quitar el arco uv) ¿el grafo se desconecta? 

si tenemos en cuenta que K(G)=2 por el teorema es  

K(G) <= lambda(G) <= grado minimo(G)

por lo tanto hay otra trayectoria (que no incluye al arco u v)

#### Paso inductivo
**Hipotesis:** Suponemos u, v nodos tales que la distancia d(u, v)=n
* Hay 2 trayectorias internamente disyuntas de u a v
* Sean u, w vértices tal que d(u, w)=n+1

si seguimos la premisa, si ejecutamos G\uw (quitar el arco de u a w) es conexo. Por lo tanto debe haber una trayectoria T*  
A. T* es internamente disyunta con T1 y T2  
B. T* se cruze con T1 o T2 o ambas (resultan caminos por medios combinatorios donde no se cruzan entre si), sea z el último punto en que T* cruza
    * Seguir T1 hasta llegar al punto z y continuar por T*
    * ir por T2 de u a v y finalizar con el arco vw

En genera, si K(G)=n entre cualquier par de nodos hay **n** trayectorias internamente disyuntas


# Problema del corte minimo 
Un **corte** en un grafo G=(v,A) es una partición de V en dos subconjuntos no vacios X,Y un arco u v cruza el corte si un extremo está en X y otro en y

Problema: en un grafo dado, encontrar un corte con el número mínimo de arcos que lo crucen


# Contracción de grafos - MinCutRep
Para que el algoritmo suelte una buena respuesta se dice que con repetirlo n(n-1) donde n es la cantidad de arcos que tien eel grafo, guardando la mejor solución, de esta manera la probabildiad de que la repsuesta sea la correcta es el 86%, entre menor sea mejor es la solución