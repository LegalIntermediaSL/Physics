# Ecuación de Hamilton-Jacobi y el Límite Ondulatorio

La idea suprema de las transformaciones canónicas: *¿Y si inventamos una transformación matemática mágica $(q, p) \to (Q, P)$ tal que, en los nuevos ejes, el nuevo Hamiltoniano $\mathcal{K}$ sea exactamente **CERO** en todas partes?*

Si logramos eso, las nuevas ecuaciones de Hamilton dictarán que $\dot{Q}=0$ y $\dot{P}=0$. ¡Todas las variables del universo serán estáticas y el problema estará instantáneamente resuelto!

## 1. La Función Principal de Hamilton
Para lograr esto, necesitamos encontrar una Función Generatriz tipo 2 que mapee $q$ viejo con $P$ nuevo. A esta función mágica la llamamos la **Función Principal de Hamilton**, representada por $S(q, P, t)$ (¡que resulta ser exactamente la Acción Clásica!).

El requisito de que el nuevo Hamiltoniano sea nulo ($\mathcal{H} + \frac{\partial S}{\partial t} = \mathcal{K} = 0$) fuerza una Ecuación en Derivadas Parciales no lineal monstruosa para $S$:

$$
\mathcal{H}\left(q_1...q_n, \frac{\partial S}{\partial q_1}...\frac{\partial S}{\partial q_n}, t\right) + \frac{\partial S}{\partial t} = 0
$$

Esta es la sagrada **Ecuación de Hamilton-Jacobi**.

## 2. Analogía Óptica (La conexión Newton - Schrödinger)
La ecuación de Hamilton-Jacobi deforma la mecánica de partículas aisladas y las reinterpreta como frentes de onda.

En óptica geométrica, los rayos de luz siguen la trayectoria de menor tiempo (Principio de Fermat), lo que se describe con la **Ecuación de la Eikonal**, que dictamina cómo los frentes de onda ($S$) se propagan.

La ecuación de Hamilton-Jacobi es *idéntica* a la Ecuación de la Eikonal de la óptica. Esto permitió a Schrödinger (1926) adivinar su famosa ecuación de ondas para el electrón. De hecho, la ecuación de Schrödinger de la Cuántica **colapsa matemáticamente e irrefutablemente en la Ecuación de Hamilton-Jacobi clásica** cuando tomamos el límite macroscópico donde la constante de Planck tiende a cero ($\hbar \to 0$).

La mecánica analítica es la membrana que separa la relatividad, la cuántica y la óptica bajo un mismo paraguas variacional.
