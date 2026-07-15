# El Teorema de Noether y las Leyes de Conservación

En 1915, la matemática Emmy Noether demostró lo que quizás sea el teorema más bello y profundo de la historia de la física teórica, uniendo indisolublemente la geometría abstracta (Simetrías) con las leyes físicas del universo (Leyes de Conservación).

## 1. Coordenadas Cíclicas
Observando la ecuación de Euler-Lagrange: $\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) = \frac{\partial L}{\partial q_i}$.
Si el Lagrangiano *no depende explícitamente* de una cierta coordenada $q_k$ (es decir, $\frac{\partial L}{\partial q_k} = 0$), decimos que $q_k$ es una **Coordenada Cíclica o Ignorable**.

Consecuencia inmediata: $\frac{d}{dt}(p_k) = 0 \implies p_k = \text{constante}$.
**Si la naturaleza es ciega (invariante) a una coordenada, el momento conjugado a esa coordenada se conserva eternamente.**

## 2. El Teorema de Noether
Noether generalizó esto a cualquier transformación continua diferenciable (Grupos de Lie) bajo la cual la Acción $\mathcal{S}$ permanece invariante.
**"Por cada simetría diferenciable y continua en la Acción de un sistema, existe una cantidad física estricta que se conserva en el tiempo."**

### A. Homogeneidad del Espacio $\implies$ Conservación del Momento Lineal
Si las leyes de la física son iguales aquí que a 5 metros de distancia (invariancia bajo traslaciones espaciales $x \to x + \delta x$), el momento lineal total del universo $\mathbf{p}$ jamás cambiará.

### B. Isotropía del Espacio $\implies$ Conservación del Momento Angular
Si las leyes de la física no discriminan ninguna dirección (invariancia bajo rotaciones $\theta \to \theta + \delta\theta$, arriba, abajo, izquierda y derecha no existen fundamentalmente), el momento angular total del universo $\mathbf{L}$ se conservará.

### C. Homogeneidad del Tiempo $\implies$ Conservación de la Energía
Si las leyes de la física hoy son idénticas a las leyes de la física ayer (invariancia bajo traslaciones temporales $t \to t + \delta t$), entonces el Lagrangiano no depende explícitamente del tiempo ($\frac{\partial L}{\partial t} = 0$). Y esto matemáticamente obliga a que exista una cantidad que denominamos **Energía Total ($H$)** que ni se crea ni se destruye.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
