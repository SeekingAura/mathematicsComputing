1. Algoritmo 3.9.1 (Floyd and nlhrshal) ejemplo 3.9.4
2. Algoritmo 4.4.12 (Borurka) ejemplo 4.4.14

Texto jungnickel

# Algoritmo 3.9.1 - Floyd and Warshall
https://www.youtube.com/watch?v=h-nmexY9gtA
w(ij) -> infinite
```
Procedure FLOYD(G, w; d)
(1) for i = 1 to n do
(2)     for j = 1 to n do
(3)         if i = j then d(i, j) ← w(ij) else d(i, j) ← 0 fi
(4)     od
(5) od
(6) for k = 1 to n do
(7)     for i = 1 to n do
(8)         for j = 1 to n do
(9)             d(i, j) ← min(d(i, j), d(i, k) + d(k, j))
(10)        od
(11)    od
(12) od
```
# Algorithm - BORUVKA
https://www.youtube.com/watch?v=t92xyTDvl_c
Procedure BORUVKA(G, w;T )
(1) for i = 1 to n do Vi ← {i} od
(2)     T ← ∅; M ← {V1,...,Vn};
(3)     while |T| < n − 1 do
(4)         for U ∈ M do
(5)             find an edge e = uv with u ∈ U, v /∈ U and w(e) < w(e)
                for all edges e = uv with u ∈ U, v ∈/ U;
(6)             find the component U containing v;
(7)             T ← T ∪ {e};
(8)         od
(9)     for U ∈ M do MERGE(U, U) od
(10) od

1. de cada nodo sus arcos salientes identifican el de peso menor y lo colorean
2. Luego de cada conjunto de arboles (viendo los arcos pintados) toma todos los arcos no conectados (que están conexos en un mismo arbol) y elije el menor (utilice un grafo como principal para efectuar bien el mst)
3. este paso se repite en los arboles no conexos al grafo principal


# Problema de la partición independiente
Se quiere dividir un grupo de personas en subconjuntos tales que:
* En cada subconjunto no haya dos personas amigas
* la cantidad de subconjuntos sea minima

```python
para i=1 hasta |v| haga
    para j=1 hasta |s| haga
        si S_j U {v_i} es independiente
            S_i <- S_j U salir
        si no j <- j+1
    si j> |S| entonces
        S_j = {V_j}
        S= S U S_j
```

# El problema del cubrimiento por vértices
G:(v,A)
S C__ V es un cubrimiento por vértices de G, si para todo uv pertenece A, u pertenece S ó v pertenece a S


## Problema: 
dado un grafo G, encontrar un cubrimiento de tamaño minimo. Un clique en un grafo G es un sugbrafo completo

## Problemas:
* Dado un grafo G, ¿Existe un cliqué de tamaño k?
* Cuál es el tamaño del máximo cliqué en un grafo G?



### Teorema:
* un grafo G tiene un cliqué de tamaño k, si y solo si G complemento (los arcos que no tiene) tiene un cubrimiento por vértices de tamaño |v|-k
* El cubrimienot de G complemento está formado por los vértices que no están en el cliqué de G_1

#### Cliqué
Es un subgrafo completmaente conexo en el grafo


# TSP Problem
* ¿Hay una solución al problema TSP con un costo menor a k?
* ¿Cuál es la solución a un problema TS de costo mínimo?

# Grafos bipartitos
Un grafo G=(V,A) es bipartito si existe una partición (X,Y), del conjunto de vertices tal que
* V = X U Y
* Para todo arco u v pertenece A, u pertenece X, v pertenece Y ó u pertenece a Y, v pertenece a X

## Teorema:
Un grafo es bipartito si y solo si no tiene ciclos de longitud impar

* Sea G un grafo conexo
* Sea T un árbol span para G

1. De cualquier nodo v se tomará como raiz

X = {v | vTr tiene longitud par}
Y = {v | vTr tiene longitud impar}

Sean u_1, u_2 vértices en X no puede existir arco entre u_1 y u_2, pues  
* Si u_1 u_2 pertenence a T, u_1 y u_2 no pueden estar ambos en X en X.
    * Si rTu_1 es par, rTu_2 es impar y si r T u_1 es impar, rTy_2 es par

* Al agregar un arco u_1_u2 se forma un ciclo


```python
graphEdgesList=[
		[1, 2], 
		[1, 5],
		[2, 6],
		[5, 6],
		[5, 10],
		[6, 11],
		[10, 11],
		[11, 12],
		[11, 15],
		[12, 16],
		[12, 7],
		[12, 13],
		[15, 16],
		[16, 18],
		[7, 3],
		[3, 4],
		[4, 8],
		[8, 9],
		[8, 13],
		[9, 14],
		[13, 14],
		[13, 17],
		[17, 19],
		[18, 19],
	]
X=[1,3,6,8,10,12,14,15,17,18]
Y=[2,4,5,7,9,11,13,16,19]
```

# Matching
Es un conjunto de arcos que no tienen nodos en comun; es decir que ningún arco se encuentre con otro (arcos disconexos)

# tarea
Investigar sobre algoritmos para encontrar cliques en grafos