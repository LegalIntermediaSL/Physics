# El Principio de Mínima Acción (Principio de Hamilton)

La mecánica analítica trasciende la formulación vectorial de fuerzas de Newton para basarse enteramente en escalares energéticos y métodos variacionales. El cimiento absoluto de esta formulación es el Principio de Hamilton, o Principio de Acción Estacionaria.

## 1. El Funcional de Acción
Consideremos un sistema mecánico cuyas posiciones se describen mediante un conjunto de coordenadas generalizadas $q(t) = (q_1, \dots, q_n)$. Definimos la función **Lagrangiana** $L(q, \dot{q}, t)$ como la diferencia entre la energía cinética $T$ y la energía potencial $V$:

$$
L(q, \dot{q}, t) = T(\dot{q}, q) - V(q, t)
$$

Para cualquier trayectoria posible que conecte un punto inicial $(q(t_1), t_1)$ con un punto final $(q(t_2), t_2)$, se define un escalar funcional denominado **Acción ($S$)**:

$$
S[q(t)] = \int_{t_1}^{t_2} L(q(t), \dot{q}(t), t) \, dt
$$

## 2. Cálculo de Variaciones y Acción Estacionaria
El Principio de Hamilton postula que la trayectoria física real que sigue el sistema es aquella que hace que el funcional de Acción sea estacionario (típicamente un mínimo) ante pequeñas variaciones virtuales de la trayectoria.
Introducimos una variación arbitraria infinitesimal $\delta q(t)$ tal que las posiciones en los extremos estén fijas: $\delta q(t_1) = \delta q(t_2) = 0$.
La variación de la Acción es:

$$
\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt
$$

Utilizando que $\delta \dot{q} = \frac{d}{dt}(\delta q)$ e integrando por partes el segundo término:

$$
\delta S = \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2} + \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt = 0
$$

Como los extremos están fijos, el término de frontera se anula. Para que la integral se anule ante cualquier variación arbitraria $\delta q(t)$, el integrando debe ser cero de forma idéntica, produciendo las Ecuaciones de Euler-Lagrange.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
