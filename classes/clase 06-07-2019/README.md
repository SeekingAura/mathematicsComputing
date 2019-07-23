# Ciclos eulerianos y hamiltonianos

## Ciclos hamiltonianos
 El juego icosian

## Euler Theorem 1.7.5
Un grafo eureliano es aquel donde es posible ir a todos los arcos una unica vez.

1. G es Euleriano

* Si un grafo tiene todos los vertices de grafo par, existe por lo menos un ciclo en G

# Problema del cartero chino
Si el grafo no es eureliano indica que tiene que pasar al menos dos veces por un mismo arco para poder pasar por todos los arcos


# Trayectoria hamiltoniana (tournament)
En todo torneo hay una trayectoria hamiltoniania

Los torneos son un grafo el cual indica siendo nodos jugadores las conexiones de forma dirigida indica que ganó al otro nodo, por ejemplo ela rco de A a B indica que A le ganó a B.

## Demostración por inducción fuerte
Teorema: En todo torneo hay una trayectoria hamiltoniana  
Demostracion: (inducción fuerte)  

### Caso base
Un grafo de nodo 'a' y 'b' con un unico arco a -> b

### Paso inductivo
Sea T un torneo con n vértoices  

Sea v pertence a V  
sea T_1 el conjunto de jugadores que ganna a v  
T_2 el conjunto de jugadores que perdieron con v

m-jugadores que ganaron



Por hipótesis de inducción en T_1 y en T_2 hay trayectoria hamiltonianas. Como se ve en la grafica, esas trayectorias se conectan por v para obtener una trayectoria en todo el grafo