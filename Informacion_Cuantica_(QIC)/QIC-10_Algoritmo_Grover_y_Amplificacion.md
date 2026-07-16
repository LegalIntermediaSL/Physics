# [QIC-10] Amplificación de Amplitud y Algoritmo de Grover

## 1. El Problema de Búsqueda No Estructurada
Supongamos que tenemos una base de datos no estructurada (o un espacio de soluciones) de tamaño $N=2^n$, y queremos encontrar un elemento específico $x^*$. Clásicamente, tendríamos que buscar uno por uno, necesitando en promedio $O(N)$ consultas al oráculo.

El algoritmo de Grover, propuesto por Lov Grover en 1996, encuentra el elemento en $O(\sqrt{N})$ consultas, proporcionando una aceleración cuadrática.

## 2. El Oráculo de Fase
El problema se formaliza mediante un oráculo cuántico $O_f$ que "marca" el estado correcto invirtiendo su fase. Si la función $f(x) = 1$ para la solución $x^*$ y $0$ en caso contrario:

$$
O_f |x\rangle = (-1)^{f(x)} |x\rangle
$$

El estado de la solución invierte su signo, mientras que los demás quedan intactos.

## 3. El Operador de Difusión (Inversión sobre la Media)
El oráculo por sí solo no aumenta la probabilidad de medir la solución (las probabilidades dependen del módulo al cuadrado, por lo que los signos negativos no importan al medir). 
Para amplificar la probabilidad, Grover introdujo el operador de difusión $D$, que realiza una "inversión sobre la media".

$$
D = 2|s\rangle\langle s| - I
$$
Donde $|s\rangle = \frac{1}{\sqrt{N}} \sum_{x} |x\rangle$ es la superposición uniforme de todos los estados.

## 4. La Iteración de Grover
El algoritmo comienza en el estado $|s\rangle$. Cada iteración de Grover $G$ consiste en aplicar el oráculo y luego el operador de difusión:
$$
G = D O_f
$$

Geométricamente, el estado inicial $|s\rangle$ es casi perpendicular al estado solución $|x^*\rangle$. Cada aplicación de $G$ rota el vector de estado hacia la solución un ángulo constante $\theta \approx 2/\sqrt{N}$.
Después de aplicar $G$ aproximadamente $\frac{\pi}{4}\sqrt{N}$ veces, el vector de estado está alineado casi perfectamente con $|x^*\rangle$. Al medir, obtendremos la solución con una probabilidad cercana al 100%.
