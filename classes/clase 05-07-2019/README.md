# Clique
https://en.wikipedia.org/wiki/Clique_problem#Algorithms

Bron–Kerbosch algorithm: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

## optimal cliques
Los cliques para sacarlos a fuerza bruta lo que se hace es obtener todos los posibles subs sets que tiene el grafo, los subs sets son todos los subsgrafos DIFERENTES en donde su resultado siempre contenga nodos diferentes a los subsets ya obtenidos y de ahi cada uno chequea si es clique.


```python
Bron-Kerbosch Algorithm Version 1
R={}
P={V}
X={}

proc: BronKerbosch(P, R, X)
1: if P union X = {} then 
2:      R is a maximal clique
3: end if
4: for each vertex in v P do
5:      BronKerbosch(P intersection nbrs(v), R U (v), X intersection nbrs(v))
6:      P=P\v
7:      X=X union v
8: end for
```
R -> son los posibles cliques
P -> Mantiene los nodos adjacentes cada nodo que hay actualmente en R, ya sea ninguno/pocos/todos cuando agrega a R haciendo el maximal (los arcos que no tienen nodo en comun)
X -> Contiene nodes que ya estan en alguno de los cliques procesados (removiendo cliques duplicados)





```python
if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = [None]

    subg = set(G)
    cand = set(G)
    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    stack = []

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:]
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass
```

# Algoritmo de ford fulkarsor
* hacer matching al grafo bipartito
* Despues agregar un nodo y conectarllo a los que NO tienen MATCH

# Matching en bipartitos
Thorem 7.2.5, libro amarillo

# 7.3.1 Marriage theorem
Es la unión de los conjuntos por medios de un matching donde se garantice que el lado derecho tenga todos unicamente uno y diferente cada uno relacionado

# Gale-Shapley


|.|BCDA  a|CBDA  b|CBAD  c|CBDA  d
|-|-|-|-|-|
|badac A|
|dabc B|
|bcda C|
|bcda D