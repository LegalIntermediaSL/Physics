# [BIO-09] Dinámica Replicadora y Juegos Evolutivos

## 1. Estrategias que Compiten
En evolución no solo importan individuos, sino estrategias cuyo éxito depende de la composición de la población. Esta dependencia de frecuencia se modela con teoría de juegos evolutivos.

## 2. Ecuación Replicadora
Si $x_i$ es la fracción de la estrategia $i$ y $f_i(\mathbf{x})$ su fitness, la dinámica básica es

$$
\frac{dx_i}{dt}
=
x_i \left(f_i(\mathbf{x}) - \bar f(\mathbf{x})\right)
$$

donde $\bar f = \sum_j x_j f_j$ es el fitness medio. Las estrategias por encima de la media crecen; las inferiores decrecen.

## 3. Equilibrios y Estabilidad
Los puntos fijos pueden interpretarse como estrategias evolutivamente estables bajo ciertas condiciones. La estabilidad depende de la geometría del simplex, de la matriz de pagos y de la presencia de ruido o mutación.

## 4. Fenómenos Típicos
La dinámica replicadora explica:

- coexistencia,
- dominancia,
- ciclos tipo piedra-papel-tijera,
- cooperación condicionada,
- y transiciones abruptas de composición.

## 5. Conexiones Físicas
Matemáticamente, estos sistemas enlazan con dinámica no lineal, procesos de nacimiento-muerte, ecuaciones maestras y aproximaciones de campo medio. Son un ejemplo muy claro de cómo ideas de estabilidad y flujo en el espacio de estados se aplican a sistemas biológicos.
