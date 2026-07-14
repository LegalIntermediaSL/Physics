# Teoría de Representaciones de Grupos y el Lema de Schur

En física, un grupo abstracto $G$ (por ejemplo, "rotar un cristal 90 grados") no tiene utilidad práctica hasta que no hace "algo" a los vectores (ej. coordenadas de los átomos). Mapear los elementos abstractos del grupo a **matrices lineales** que actúan sobre un espacio vectorial físico se llama **Representación**.

## 1. Representaciones Irreducibles (Irreps)
Una representación $D(g)$ asocia a cada elemento $g \in G$ una matriz. 
Si estas matrices operan sobre un espacio grande, es posible que el espacio se pueda partir en subespacios más pequeños que no se mezclan entre sí bajo las transformaciones del grupo (matrices en forma de bloque diagonal).

Cuando un espacio no puede ser subdividido más, la representación geométrica sobre ese espacio mínimo se llama **Representación Irreducible (Irrep)**. Las Irreps son los "átomos" puros de la teoría de grupos; dictan la degeneración energética y las propiedades de selección en moléculas y cristales.

## 2. El Lema de Schur
El Lema de Schur es una verdad profunda y restrictiva que gobierna las Irreps.
> **Parte 1:** Si una matriz $M$ conmuta con todas las matrices de una representación irreducible ($M D(g) = D(g) M$ para todo $g$), entonces $M$ debe ser un múltiplo escalar de la matriz identidad ($M = c \mathbb{I}$).

> **Parte 2:** Si $D_1$ y $D_2$ son dos irreps de dimensiones diferentes, y una matriz $M$ las conecta ($M D_1(g) = D_2(g) M$), entonces obligatoriamente $M = 0$.

## 3. Teoría de Caracteres
Analizar matrices de $10\times 10$ a mano es infernal. El **Carácter** ($\chi(g)$) de una transformación es la **traza** de su matriz representativa (la suma de su diagonal):

$$
\chi(g) = \text{Tr}(D(g))
$$

El carácter condensa la geometría compleja del grupo en un simple número complejo. Las Tablas de Caracteres permiten a los físicos predecir (sin resolver ni una sola ecuación diferencial de Schrödinger) qué transiciones atómicas están prohibidas (Reglas de Selección) simplemente analizando las simetrías (Pares/Impares) del entorno molecular.
