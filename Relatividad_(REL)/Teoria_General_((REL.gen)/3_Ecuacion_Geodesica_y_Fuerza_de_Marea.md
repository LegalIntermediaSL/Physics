# Ecuación Geodésica y Fuerzas de Marea

## 1. Movimiento en el Espacio Curvo
En ausencia de fuerzas electromagnéticas o nucleares, un cuerpo en caída libre sigue el camino "más recto" posible a través del espacio-tiempo tetradimensional curvo. Esta trayectoria se denomina **Geodésica**.

Maximizando (o minimizando) el tiempo propio $\tau$ ($\delta \int d\tau = 0$), se obtiene la **Ecuación Geodésica**:

$$
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0
$$

Donde $x^\mu(\tau)$ son las coordenadas de la partícula paramétrizadas por su tiempo propio, y $\Gamma^\mu_{\alpha\beta}$ son los símbolos de Christoffel derivados de la métrica. Notablemente, **la "gravedad" desaparece como fuerza** ($\vec{F}$); todo es aceleración cinemática debido a la conexión geométrica $\Gamma$.

## 2. Desvío Geodésico (Las Fuerzas de Marea)
El Principio de Equivalencia prohíbe detectar la gravedad localmente si estás en caída libre. Sin embargo, dos cuerpos que caen libremente cerca uno del otro en un campo gravitatorio no uniforme se acercarán o alejarán con el tiempo. 

Este acercamiento (Fuerza de Marea Física) es la única manifestación "real" y no-coordinada de la curvatura. La separación $\xi^\mu$ entre dos geodésicas vecinas obedece a la **Ecuación de Desvío Geodésico de Jacobi**:

$$
\frac{D^2 \xi^\mu}{d\tau^2} = -R^\mu_{\nu\rho\sigma} U^\nu \xi^\rho U^\sigma
$$

Donde $U^\nu$ es el cuadrivector velocidad y $R^\mu_{\nu\rho\sigma}$ es el formidable Tensor de Riemann. Esto prueba que la "gravedad" tidal es matemáticamente idéntica a la curvatura topológica Riemanniana.
