# Árbolres Binarios
* Un único nodo de grado 2 (raíz)
* Todos los demás nodos deben tener grado 3 o 1

n: # nodos
p: # hojas  
q: # nodos internos

p = (n+1)/2

la cantidad de grados de arboles es

2+3q+p=2a=2(n-1)

# Altura de arboles
El maximo de nodos por nivel de arbol es n^i -> donde i es el nivel del arbol. por lo cual se cumple que n <= 2^i
l: maximo nivel o profundidad del arbol  
n_0+n_1+n_2+ ... + n_l <= 1+2+2^2+2^3 + ... +2^l = 2^(l+1)-1  
n<=2^(l+1)-1
log_2(n+1)-1<=l

# Arboles de cubirimiento/expansion(Spanning Trees)

Sea G= (V,A) un grafo conexo. Un árbol span para G es todo subgrafo G'=(V, A') que sea árbol.

## Teorema:
Todo grafo conexo tiene un árbol de expasión

### Demostración 1
1. G no tiene ciclos. G es su propio árbol de expansión
2. Si G tiene ciclos
    * sea C un ciclo de G
    * Borre cualquier arco del ciclo. El grafo no se desconecta

*  sean u,v dos vértices cualquiera del grafo
    * si el camino de u, v no incluye al arco xy. No hay problema de desconexión
* Si el camino de u a v incluye a xy. No hay problema de desconexión

Es decir que de un grafo conexo cualquiera puede formarse como subgrafo un arbol de expansión (ST)

# creación de Spanning Trees con Depth Search
Es practica 


# Tarea
1. Algoritmo 3.9.1 (Floyd and nlhrshal) ejemplo 3.9.4
2. Algoritmo 4.4.12 (Boruvka) ejemplo 4.4.14

Texto jungnickel