# Espacio de Minkowski y Cuadrivectores

## 1. El Espacio-Tiempo como un Continuo 4D
Antes de 1905, el espacio y el tiempo eran entidades absolutas e independientes (Mecánica Newtoniana). Hermann Minkowski reformuló la Relatividad Especial de Einstein demostrando que habitamos una variedad pseudoeuclidiana de cuatro dimensiones (una dimensión temporal y tres espaciales), conocida como el **Espacio de Minkowski**.

## 2. El Invariante de Espacio-Tiempo (El Intervalo)
A diferencia del espacio euclidiano (donde la distancia $ds^2 = dx^2 + dy^2 + dz^2$ es invariante), en relatividad la velocidad de la luz $c$ es constante para todo observador. Esto requiere un nuevo invariante: el **Intervalo Espacio-Temporal** $ds^2$:

$$
ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2
$$

Dependiendo del signo de $ds^2$, los eventos pueden ser:
- **Separación Temporal ($ds^2 < 0$)**: Causalmente conectados (una partícula masiva puede viajar entre ellos).
- **Separación Lumínica ($ds^2 = 0$)**: Conectados exactamente por un rayo de luz (Cubo de Luz).
- **Separación Espacial ($ds^2 > 0$)**: Causalmente desconectados.

## 3. El Tensor Métrico de Minkowski ($\eta_{\mu\nu}$)
El intervalo se escribe de manera tensorial compacta usando la métrica plana $\eta_{\mu\nu}$:

$$
ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu
$$

Donde la matriz diagonal es (convención de la física de partículas: $-+++$):

$$
\eta_{\mu\nu} = \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

## 4. Cuadrivectores
Cualquier objeto matemático que se transforme bajo las reglas del Grupo de Lorentz es un Cuadrivector $A^\mu = (A^0, A^1, A^2, A^3)$.
- **Cuadrivector Posición:** $X^\mu = (ct, x, y, z)$
- **Cuadrivelocidad:** $U^\mu = \gamma (c, \vec{v})$. Su magnitud es siempre constante e igual a $-c^2$.
- **Cuadrimomento:** $P^\mu = m_0 U^\mu = (\frac{E}{c}, \vec{p})$. 

La magnitud invariante del Cuadrimomento nos da la ecuación más famosa de la física relativista:

$$
P^\mu P_\mu = -\frac{E^2}{c^2} + |\vec{p}|^2 = -m_0^2 c^2 \implies E^2 = (pc)^2 + (m_0 c^2)^2
$$

