# [FUN-01] Ecuaciones Fundamentales: Mecánica Clásica y Analítica

## 1. Mecánica Vectorial (Newtoniana)
**Segunda Ley de Newton (Dinámica de Traslación):**

$$
\vec{F}_{net} = \frac{d\vec{p}}{dt} = m \vec{a}
$$

**Dinámica de Rotación:**

$$
\vec{\tau}_{net} = \frac{d\vec{L}}{dt} = I \vec{\alpha}
$$

**Conservación de la Energía Mecánica:**

$$
E = K + U = \frac{1}{2}mv^2 + V(r) = \text{constante} \quad (\text{Fuerzas conservativas})
$$

## 2. Formalismo Lagrangiano
**El Funcional de Acción (Principio de Hamilton):**

$$
S = \int_{t_1}^{t_2} L(q_i, \dot{q}_i, t) \, dt, \quad \delta S = 0
$$

**Ecuaciones de Euler-Lagrange:**

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

**Ecuaciones de Lagrange con Multiplicadores (Vínculos holonómicos):**

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = \sum_k \lambda_k \frac{\partial f_k}{\partial q_i}
$$

**Momento Conjugado y Corriente de Noether:**

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}, \quad Q = \sum_i p_i \delta q_i - F = \text{constante}
$$

## 3. Formalismo Hamiltoniano
**Transformada de Legendre y Hamiltoniano:**

$$
H(q, p, t) = \sum_i p_i \dot{q}_i - L(q, \dot{q}, t)
$$

**Ecuaciones Canónicas de Hamilton:**

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

**Corchetes de Poisson (Evolución Temporal de un Observable $f$):**

$$
\{f, g\} = \sum_i \left( \frac{\partial f}{\partial q_i} \frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i} \right)
$$

$$
\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}
$$

**Ecuación de Hamilton-Jacobi:**

$$
H\left( q_i, \frac{\partial S}{\partial q_i}, t \right) + \frac{\partial S}{\partial t} = 0
$$


---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.01 / 8.02 / 8.03 / 8.04](https://ocw.mit.edu/courses/physics/) - El ciclo completo de Walter Lewin y Allan Adams.
  - [The Theoretical Minimum](https://theoreticalminimum.com/) - Leonard Susskind. Todo el marco teórico de la física moderna.
- **Libros de Texto Canónicos:**
  - *The Feynman Lectures on Physics* (Vol. I, II, III) - Richard Feynman. [Disponible online gratuitamente por Caltech](https://www.feynmanlectures.caltech.edu/).
  - *University Physics* - Young & Freedman (Para bases rigurosas).
