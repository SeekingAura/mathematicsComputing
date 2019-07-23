Pagina 50, 51, 52
65 en el pdf

Ejercicio 2.6.9
orden topoligo cambia el label de los nodos de tal manera que sus siguientes terngan valor mayor.

de los nodos que no le llegan nada es donde inician sus valores.

# Taller 1 
## punto 1
Para n nodos se los grados posibles que tendria es 0, 1, 2, 3, ..., n-1, para colocar grados diferentes requieren cubrirse todos los grados posibles al hecho de cubrir el grado maximo implica que no haya de grado 0.

## Punto 2
Dado n vértices, ¿Cuantos grafos se pueden construir?

Pares de vertices es -> (n combinado 2) = (n!/(2!(n-2)))

Subconjuntos -> 2^((n(n-1))/2)
Cada sub-conjunto son otros grafos posibles que se pueden formar formas de conectar (incluyendo isomorfos)

No hay modo para calcular todos los grafos que hay diferentes, sin embargo a fuerza fue calculado algunos y aqui una tabla con algunos

|n|sub-conjuntos|
|-|-|
|1|1|
|2|2|
|3|4|
|4|11|
|5|34|
|6|156|
|7|1044|
|8|12346|
|9|274668|

## Punto 3
Teorema  
Si grado_minimo >= ((n-1)/2) tiene que ser un grafo conexo

### Demostración por contradicción
Supongamos que existe un grafo con n nodos, con grado_minimo >= ((n-1)/2) y que sea no conexo.

Para que un conjunto sea conexo requiere que hayan al menos un total de (n+1)/2 Por conjunto, PERO si se aplica resultará que el total de nodos será "n+1" ((n+1)/2)+((n+1)/2) por lo tanto se demuestra que el grafo tiene que ser conexo.


# Ejercicio 2.2.5 del GraphsNetworksAlgorithms (amarillo)
A -> es matriz de adyacencia del grafo G.  
A^2= B -> (b_ij)

los elementos indicará cuantos "paseos" del vértice i al vértice j de longitud 2

A^k=C -> (c_ij)
los elementos indicará cuantos "paseos" del vértice i al vértice j de longitud k

## Demostraciones por inducción (Recursión)
Una técnica de prueba es por **inducción**

Para probar alguna propiedad P(n)

### paso 1 - Caso base
P(1)

### Paso inductivo - Hipotesis de inducción
Plantear una hipotesis una suponer que si cumple para valor k, estrictamente debe cumplir para k+1

es decir p(k) ==> P(k+1)



### ejemplo con ejercicio 2.2.5
#### Paso base 
A=(a_ij)  
a_ij : número de paseos del vértice i al vértice j de longitud 1

#### Paso inductivo
Hipotesis: A^k=(c_ij)=C  
c_ij -> es el número de paseos del vértice i al vértice j de longitud k

Verifiquemos para A^(k+1)

al efectuar A^(k+1)=A^k*A
d_ij=c_i1*a_1j+c_i2*a2_j+c_i3*a_3j+ ... + c_in*a_nj

Tarea 1.  
Lema 1.2.6  -> A connected graph on n vertices has at least n − 1 edges.

Lema 1.2.7 -> An acyclic graph on n vertices has at most n − 1 edges