# [MTH-07] Teoría de Grafos Cuánticos y Quantum Walks

## 1. Operadores de Schrödinger en Grafos
Un Grafo Cuántico es un grafo matemático donde a cada "arista" (enlace) se le asigna una longitud y una Ecuación de Schrödinger diferencial $1D$, acopladas entre sí mediante condiciones de contorno estrictas en los vértices (nodos) para conservar la corriente probabilística (ej. condiciones de Neumann o de acoplamiento de Kirchhoff). 
Son la base para modelar redes neuronales artificiales, nano-circuitos y moléculas complejas (como el grafeno y nanotubos de carbono).

## 2. Caminatas Cuánticas (Quantum Walks)
Es el equivalente cuántico del "Paseo Aleatorio" (Random Walk o Borracho caminando). En lugar de lanzar una moneda clásica para moverse a derecha o izquierda, se aplica una "Moneda Cuántica" (un operador unitario como la Puerta de Hadamard) sobre el estado interno de espín.
A diferencia de la partícula clásica cuya varianza crece linealmente con el tiempo (Difusión estocástica, $\sigma^2 \propto t$), la partícula cuántica está en superposición de todos los caminos simultáneamente e interfiere consigo misma. El resultado es que la varianza estalla cuadráticamente (Propagación Balística, $\sigma^2 \propto t^2$). 
Esto otorga una ventaja de velocidad abrumadora, siendo la columna vertebral matemática de los algoritmos de búsqueda rápida en computadores cuánticos (como el Algoritmo de Grover).
