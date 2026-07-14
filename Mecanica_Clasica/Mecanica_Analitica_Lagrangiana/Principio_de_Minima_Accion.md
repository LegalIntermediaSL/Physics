# El Principio de Mínima Acción (Principio de Hamilton)

La mecánica newtoniana es vectorial e imperativa: dictamina cómo cambian las cosas instante a instante a través de fuerzas ($\mathbf{F} = m\mathbf{a}$). A finales del siglo XVIII, Joseph-Louis Lagrange y William Rowan Hamilton reformularon toda la mecánica en términos puramente escalares y teleológicos (basados en un propósito global): **El Principio de Mínima Acción**.

## 1. La Acción ($\mathcal{S}$)
Definimos una nueva cantidad escalar llamada el Lagrangiano $L$, que para sistemas conservativos ordinarios es simplemente la diferencia entre la Energía Cinética ($T$) y la Energía Potencial ($V$):

$$
L(q, \dot{q}, t) = T - V
$$

*(Nota: Las variables $q_i$ son coordenadas generalizadas, que no tienen por qué ser cartesianas. Pueden ser ángulos, distancias, o combinaciones de ambas).*

La **Acción** $\mathcal{S}$ de una trayectoria particular entre un instante inicial $t_1$ y un instante final $t_2$ es la integral temporal del Lagrangiano a lo largo de esa trayectoria:

$$
\mathcal{S}[q(t)] = \int_{t_1}^{t_2} L(q(t), \dot{q}(t), t) dt
$$

La Acción es un **Funcional**: toma como entrada una trayectoria completa (una función) y escupe un único número real (con unidades de Energía $\times$ Tiempo, los mismísimos Joules-segundo de la constante de Planck $\hbar$).

## 2. El Principio de Hamilton
De todas las infinitas trayectorias imaginables mediante las cuales una partícula podría viajar de un punto $A$ a un punto $B$, la naturaleza escoge única y exclusivamente **aquella trayectoria que hace que la Acción sea un extremo** (generalmente un mínimo local). 

En el lenguaje del Cálculo de Variaciones, esto significa que la variación de primer orden de la acción es nula:

$$
\delta \mathcal{S} = 0
$$

Este principio no es solo para masas y muelles. El Principio de Mínima Acción dicta las trayectorias de la luz en Relatividad General (geodésicas) y genera literalmente todas las interacciones de partículas en la Teoría Cuántica de Campos cuando insertamos un Lagrangiano electromagnético o nuclear.
