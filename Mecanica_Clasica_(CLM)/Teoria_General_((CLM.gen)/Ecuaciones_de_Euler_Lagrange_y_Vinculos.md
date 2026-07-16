# Ecuaciones de Euler-Lagrange y Sistemas Ligados

El requisito de que el funcional de acción sea estacionario genera directamente las ecuaciones diferenciales del movimiento.

## 1. Las Ecuaciones de Euler-Lagrange
Como corolario del Cálculo de Variaciones, para cada coordenada generalizada $q_i$, se satisface la ecuación diferencial de segundo orden:

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

Definimos formalmente el **Momento Generalizado** o Momento Canónico Conjugado $p_i$ y la Fuerza Generalizada $F_i$:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}, \quad F_i = \frac{\partial L}{\partial q_i}
$$

La ecuación de movimiento se reduce elegantemente a $\dot{p}_i = F_i$. Si el Lagrangiano no depende explícitamente de una coordenada concreta $q_k$ (coordenada cíclica), entonces $\frac{\partial L}{\partial q_k} = 0$, lo que implica que su momento conjugado correspondiente $p_k$ es una constante exacta del movimiento.

## 2. Vínculos Holonómicos y Multiplicadores de Lagrange
En sistemas reales, las partículas a menudo están restringidas a moverse sobre superficies o curvas. Un vínculo es **Holonómico** si puede escribirse algebraicamente en función de las coordenadas como $f(q_1, \dots, q_n, t) = 0$.
Para derivar las ecuaciones de movimiento con vínculos sin tener que despejar las coordenadas, utilizamos el método de los **Multiplicadores de Lagrange ($\lambda$)**.

Se modifica el Principio de Acción añadiendo el vínculo al Lagrangiano:

$$
L' = L + \lambda f(q, t)
$$

El requerimiento variacional $\delta \int L' dt = 0$ rinde el nuevo conjunto de ecuaciones acopladas:

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = \lambda \frac{\partial f}{\partial q_i}
$$

El término $\lambda \frac{\partial f}{\partial q_i}$ es la componente $i$-ésima de la **Fuerza de Ligadura**.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
