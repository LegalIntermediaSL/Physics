# Derivación Rigurosa de las Ecuaciones de Navier-Stokes

## 1. Conservación de la Masa y Ecuación de Continuidad
Para describir un fluido, utilizamos el enfoque Euleriano (estudiamos puntos fijos en el espacio mientras el fluido fluye). Sea $\rho(\vec{x}, t)$ el campo escalar de densidad y $\vec{v}(\vec{x}, t)$ el campo vectorial de velocidad. La masa en cualquier volumen de control $V$ con superficie $\partial V$ debe conservarse:

$$
\frac{d}{dt} \int_V \rho dV = -\oint_{\partial V} (\rho \vec{v}) \cdot \hat{n} dA
$$

Aplicando el Teorema de la Divergencia de Gauss y considerando un volumen diferencial arbitrario, obtenemos la **Ecuación de Continuidad**:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0
$$

Para un fluido incompresible (líquidos como el agua), la densidad material es constante, por lo que la ecuación colapsa a la condición de incompresibilidad: $\nabla \cdot \vec{v} = 0$.

## 2. Conservación del Momento (Segunda Ley de Newton en Fluidos)
El momento de una parcela de fluido cambia debido a las fuerzas externas e internas. La derivada material (o convectiva) describe la tasa de cambio siguiendo al fluido:

$$
\frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla) \vec{v}
$$

Las fuerzas internas provienen del **Tensor de Esfuerzos de Cauchy** $\sigma_{ij}$, que se descompone en presión isotrópica $p$ y el tensor de esfuerzos viscosos $\tau_{ij}$:

$$
\sigma_{ij} = -p \delta_{ij} + \tau_{ij}
$$

Bajo la hipótesis Newtoniana de fluidos isótropos, los esfuerzos viscosos son proporcionales a las tasas de deformación:

$$
\tau_{ij} = \mu \left( \frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i} \right) + \lambda (\nabla \cdot \vec{v})\delta_{ij}
$$

Donde $\mu$ es la viscosidad dinámica. Si asumimos la hipótesis de Stokes (viscosidad de volumen nula), $\lambda = -2/3 \mu$.

## 3. Las Ecuaciones Completas
Igualando el balance de cantidad de movimiento $\rho \frac{D\vec{v}}{Dt} = \nabla \cdot \sigma + \vec{f}$, obtenemos las **Ecuaciones de Navier-Stokes para fluido compresible**:

$$
\rho \left( \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot \nabla \vec{v} \right) = -\nabla p + \mu \nabla^2 \vec{v} + \left( \zeta + \frac{1}{3}\mu \right) \nabla (\nabla \cdot \vec{v}) + \rho \vec{g}
$$

Para un fluido incompresible estándar ($\nabla \cdot \vec{v} = 0$), se reducen a su forma más legendaria (uno de los Problemas del Milenio del Instituto Clay):

$$
\frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla) \vec{v} = -\frac{1}{\rho} \nabla p + \nu \nabla^2 \vec{v} + \vec{g}
$$

Donde $\nu = \mu/\rho$ es la viscosidad cinemática.
