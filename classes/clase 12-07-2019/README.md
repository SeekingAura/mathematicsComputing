# Coloring nodes

   * ``'largest_first'``
    * ``'random_sequential'``
    * ``'smallest_last'``
    * ``'independent_set'``
    * ``'connected_sequential_bfs'``
    * ``'connected_sequential_dfs'``
    * ``'connected_sequential'`` (alias for the previous strategy)
    * ``'strategy_saturation_largest_first'``
    * ``'DSATUR'`` (alias for the previous strategy)

https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.coloring.greedy_color.html

```python
for u in nodes:
        # Set to keep track of colors of neighbours
        neighbour_colors = {colors[v] for v in G[u] if v in colors}
        # Find the first unused color.
        for color in itertools.count():
            if color not in neighbour_colors:
                break
        # Assign the new color to the current node.
        colors[u] = color
    return colors
```

# Algoritmo coloreado secuencial

1. Cada nodo tendrá una lista de los indices donde el primer nodo tendrá el primer nodo y el siguiente tendrá los primeros 2 y asi hasta que el último tnedrá una lista con todos
2. Una vez se tenga las listas se itera en cada uno y se toma su primer elemento
3. Ese elemento se verifica en los vecinos sus listas y si la tienen se les remueve
4. se toma el siguiente elemento y se repite el punto 3.


# Ejercicio 9.1.2

# Graph triangular

Los grafos triangulares se pueden colorear con 3 colores

Al llevar a cabo la triaungulación y efectuar el isocromatico 

# Guardias a vigilar

piso(n/3) donde se redondea por debajo el resultado y n es la cantidad de paredes

# Grafo planar
arcos que no se crucen con otros

formula

nodos - arcos + caras = 2

arcos - nodos + 2 = caras

donde la cara son las regiones del grafo