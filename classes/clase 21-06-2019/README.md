# Arboles
T= (V,A)  
* Un árbol es un grafo conexo sin ciclos
* Un grafo no conexo sin ciclos, se llama un bosque (arbol)

En los arboles debe de cumplirse que la cantidad de de nodos (|V|) es la cantidad total de arcos más 1 (|A|+1)

|V|=|A|+1

## Demostración por inducción (Inducción fuerte en el número de arcos)
La inducción "comun" supone que n ya es cierto y va demostrarse que n+1 puede ser cierto.

En la inducción fuerte supone desde 1 hasta n-1 que es cierto y lo que pretende demostrar es que cumple para n

### Caso base:
A=1  Entonces;  
n=a+1
n=2  
2=1+1

### Paso inductivo
#### Hipotesis
Suponga que todo árbol con menos de **m** arcos tiene la propiedad dada por el teorema.

Sea T un árbol con **m** arcos.

Sea **e** un arco cualquiera de T T/e es no conexo

Los componentes conexos C_1 y c_2 son árboles con menos arcos que T

Por hipotesis

|V_1|=|A_1|+1  
|V_2|=|A_2|+1  
\---------------  
|V_1|+|V_2|=|A_1|+|A_2|+1+1


##Teorema
Si G no tiene ciclos y si |V|=|A|+1 -> G es un arbol

### Demostración
Falta probar que G es conexo, para ello será **por contradicción** supongase que G **no** es conexo.

supongamos que hay k componentes conexos, cada componente conexa de C_i es un árbol

|V|=|V_1|+|V_2|+ ... + |V_k| = |A1|+1 + |A2|+1 + ... + |A_k|+1  
|V|=|A|+k
|A|+1=|A|+k -> k=1

Por lo tanto es un arbol.


# Corollary 1.1.11 (libro amarillo)
El número de arboles posibles con n vertices es n^(n-2)


## Código prüfer
para n>=3 usará la hoja menor del arbol.

1. De todas las hojas (los nodos con grado entrante 1) identifique el nodo que tenga su nombre/label de menor valor
2. Del nodo identificado con el menor valor tome el nodo al que está conectado y agrege a una lista w
3. elimine el nodo del menor valor y el arco a los que conecta
4. repetir el proceso (recordar que se forman nuevas hojas)
5. cuando llegue al a 2 nodos 1 arco no ese agrega a w

## Recronstrucción de prufer
se toma el código o bien la "lista" y se agrega un 0 al final, recordemos que el código indica los "hijos" ahora empieza desde el primer hijo y mira de los padres anteriores cual es el minimo y de los hijos siguientes cual es el valor minimo que **NO** está.





