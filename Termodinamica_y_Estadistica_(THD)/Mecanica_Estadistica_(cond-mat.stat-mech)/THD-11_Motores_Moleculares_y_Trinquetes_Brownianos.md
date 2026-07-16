# [THD-11] Motores Moleculares y Trinquetes Brownianos (Brownian Ratchets)

## 1. El Paradoja del Demonio de Maxwell Estocástico
Un trinquete browniano es un dispositivo teórico (y biológico real) que extrae trabajo útil de fluctuaciones aleatorias en un baño térmico sin violar la Segunda Ley, gracias a un aporte de energía externa que rompe el equilibrio detallado (ej. hidrólisis de ATP).

## 2. Ecuación de Fokker-Planck para el Flashing Ratchet
El modelo más famoso es el *flashing ratchet*, donde una partícula browniana difunde en un potencial asimétrico periódico $V(x)$ que se enciende y apaga estocásticamente.
La densidad de probabilidad $P(x,t)$ sigue la ecuación:

$$
\frac{\partial P(x,t)}{\partial t} = D \frac{\partial^2 P(x,t)}{\partial x^2} + \frac{\partial}{\partial x} \left[ \frac{V'(x,t)}{\gamma} P(x,t) \right]
$$

donde $D$ es la constante de difusión y $\gamma$ la fricción. La asimetría espacial y la modulación temporal generan una corriente neta $\langle J \rangle > 0$.
