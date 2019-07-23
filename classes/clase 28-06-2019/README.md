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