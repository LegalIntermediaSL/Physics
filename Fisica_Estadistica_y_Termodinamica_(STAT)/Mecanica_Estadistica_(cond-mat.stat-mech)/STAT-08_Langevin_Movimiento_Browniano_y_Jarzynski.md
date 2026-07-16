# [STAT-08] Termodinámica del No-Equilibrio y Ecuación de Langevin

## 1. La Ecuación Estocástica de Langevin
El Movimiento Browniano (observado primero en granos de polen) es la prueba microscópica de la teoría atómica. Una partícula pesada en un fluido sufre trillones de colisiones de moléculas de agua. Paul Langevin propuso modelar esto con una fuerza estocástica aleatoria (ruido blanco térmico) $\eta(t)$ empujando a la partícula:
$$
m \frac{dv}{dt} = -\gamma v + \eta(t)
$$
Donde $-\gamma v$ es la fricción de arrastre. A partir del caos microscópico más absoluto de $\eta(t)$, la Mecánica Estadística demuestra que emerge el orden macroscópico de la Difusión (Relación de Einstein: $D = k_B T / \gamma$).

## 2. Teoremas de Fluctuación (Igualdad de Jarzynski)
La Segunda Ley de la Termodinámica afirma que el trabajo $W$ realizado sobre un sistema siempre es mayor o igual que el cambio de Energía Libre ($\Delta F$). Pero a nanoescala (como al estirar ADN), el ruido térmico domina. La Igualdad de Jarzynski dictamina que:
$$
\langle e^{-W / k_B T} \rangle = e^{-\Delta F / k_B T}
$$
Esto demuestra matemáticamente que a nivel molecular, **el sistema viola ocasionalmente la Segunda Ley**, extrayendo energía del calor ambiente para realizar trabajo extra, pero el promedio estadístico general siempre respeta la macroscópica flecha del tiempo.
