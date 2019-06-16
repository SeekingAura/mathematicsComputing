# Componentes fuertemente conexas

En digrafos...  

La notación uTv significa que "hay una trayectoria del vértice u al vértice v"

u, v están en la misma componente fuertemente conexa C si uTv y vTu o el vértice u solo si no existe ningún v.

## Problema
un algoritmo que dado un digrafo encuentre su scomponentes fuertmenete conexas

u 'pertenece V

C^+(u)={v|uTv}
C^-(u)={w|wTu}

C=C^+NC^-

## Caso de demostración
Sea A la matriz de abyacencia del digrafo

A^k : B  
(b_ij) != 0 -> Hay un paseo del vértice i al vértice j

Donde
D= A+A^2+A^3+ ... + A^n
n -> número de vertices
Si d_ij son diferentes de cero, los vértices 'i' y 'j' están en la misma cfc

D=(I-A)^(-1)

### Ejercicio
Construir un ejemplo para el anterior algoritmo

### Tarea
Dado un grafo G

¿Se pueden orientar los arcos de modo que el diagrafo resultante sea fuertemente conexo?

# Grado en grafos dirigidos
d_in(n) -> El grado entrante es los arcos que entran al nodo n
d_out(n) -> El grado saliente es los arcos que salen del nodo n


# Recorriendo grafos
## Algoritmos BFS (Primero en anchura)

BFS(G, s)

1. Marcar s como visitado
2. Sea Q una cola inicializada con s
3. Mientras Q!=vacio
    * Sacar el primer elemento v de Q para cada arco de dicho elelemento vw (v es nodeFrom y w es nodeTo):  
       * si w no marcado:
            * 1 marcarlo como visitado  
            * colocar la distancia del nodo proveniente +1 en el nodo a que se llega
        else:
            * poner w en la cola

para el grafo
```python
edgesList=[
    ["s", "f"],
    ["s", "a"],
    ["s", "d"],
    ["s", "f"],
    ["d", "e"],
]
```

## DFS (primero en profundidad)

```
Explorar(nodo)
    Marcar nodo como visitado  
    Para cada arco **nodeFrom** **nodeTo** en A haga si **nodeTo** no visitado   
    Explorar(w)
```
```
DFS(G)  
para nodeFrom=1 hasta n haga:
    si node no visitado
    Explorar(nodeFrom)
```