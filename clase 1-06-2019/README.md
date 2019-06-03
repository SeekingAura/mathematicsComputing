## El grado de un vértice
Grado de un vertice d(v)es la cantidad de arcos que llegan al nodo (arcos incidentes al nodo)

por el momento los arcos son bidireccionales.

## Teorema
* La cantidad grados de un vertice que sean impares tiene que ser par
* La suma de grados de un vertice es el doble de arcos que tiene el grafo
    * sumd(v)=2|A|
    * Se debe a que la suma de cada grado implica sumar 2 veces por cada arco dado.
    * d(v_1)+ ... + d(v_k) de grados par debe su suma dar par
    * d(v_(k+1))+ ... + d(v_n) de grados impar debe ser una cantidad par para que su suma de par
* El número de nodos de grado impar en cualquier grafo es par.


# Isomorfismo de grafos
Los grafos dibujados de diferente forma pero conectados de la misma forma (aunq ue los nodos tengan nombres diferentes) son isoformosfos

por ejemplo para determinar la cantidad de conexiones posibles entre nodos es cantidadNodos! que en si logra determinar las biyecciones posibles

## Aplicacion
criptografia, pruebas de conocimiento cero (zero knowledge Proofs)

## Conocimiento cero
Demostrar que uno sabe de un proceso, procedimiento o algun conocimiento como tal, por ejemplo un grafo 

## Ciclo hamiltoniano
Recorrer todas las ciudades sin repetir ninguna

# Representación de grafos
## Matriz de abyacencia
[
    [0,1,1,0,1],
    [1,0,1,1,1],
    [1,1,0,1,0],
    [0,1,1,0,0],
    [1,1,0,0,0]
]
*
[
    [0,1,1,0,1],
    [1,0,1,1,1],
    [1,1,0,1,0],
    [0,1,1,0,0],
    [1,1,0,0,0]
]
=
[
    [3,2,1,2,1],
    [1,4,2,1,1],
    [1,1,3,1,2],
    [0,1,1,2,1],
    [1,1,0,0,2]
]

esto es A^2  
La diagonal que en este caso la diagonal de A^2 es [3,4,3,2,2] indica los grados que tiene el grafo

Teorema:
Sea M=A^K
(M_ij) es igual al número de paseos diferentes desde el vértice v_i hasta el ´vertice v_j de longitud k_i


## Listas de abyacencia


# Definiciones
* una trayectoria (path) es un paseo en el que no se repite ningun arco
* la distancia entre el vértice u y el vertice v, d(u,v), es la longitud de la trayectoria más corta de u hasta v
* un grafo es conexo si para cualquier par de vértices u,v hay por lo menos una trayectoria que los une

# Grafos dirigidos (diagrafo)
es el conjunto de vértices, A es un conjunto de pares ordenados {(v_i, v_j)}