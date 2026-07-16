# Atractores Extraños y Ecuaciones de Lorenz

## 1. El Sistema de Lorenz
En 1963, Edward Lorenz simplificó las ecuaciones de convección térmica atmosférica de Navier-Stokes en un conjunto de tres ecuaciones diferenciales ordinarias acopladas y no lineales:

$$
\dot{x} = \sigma (y - x)
$$

$$
\dot{y} = x (\rho - z) - y
$$

$$
\dot{z} = xy - \beta z
$$

Donde:
- $x$: Tasa de convección.
- $y$: Variación horizontal de la temperatura.
- $z$: Variación vertical del perfil de temperatura.
- Parámetros: $\sigma$ (Número de Prandtl), $\rho$ (Número de Rayleigh), $\beta$ (Factor geométrico).

## 2. Puntos Fijos y Análisis de Estabilidad Lineal
Para encontrar el equilibrio, se igualan las derivadas a cero.
El origen $(0,0,0)$ es un punto fijo. La matriz Jacobiana evaluada en el origen es:

$$
J = \begin{pmatrix} -\sigma & \sigma & 0 \\ \rho & -1 & 0 \\ 0 & 0 & -\beta \end{pmatrix}
$$

Los valores propios de $J$ dictan que el origen se desestabiliza cuando $\rho > 1$ mediante una bifurcación de tridente (pitchfork), creando dos nuevos puntos fijos simétricos $C_1, C_2$.

## 3. El Atractor Extraño
Cuando $\rho > 24.74$ (con $\sigma=10, \beta=8/3$), los puntos fijos se vuelven inestables (vía bifurcación de Hopf subcrítica). Las trayectorias son confinadas a un volumen acotado en el espacio de fases pero no cruzan ni convergen a un límite periódico; caen en un **Atractor Extraño** de geometría fractal con dimensión de Hausdorff fraccionaria $d \approx 2.06$.
