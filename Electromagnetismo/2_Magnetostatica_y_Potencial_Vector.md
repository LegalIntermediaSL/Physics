# Magnetostática y Potencial Vector

La magnetostática rige cuando las corrientes eléctricas son estacionarias ($\partial \vec{J} / \partial t = 0$), implicando que las densidades de carga también deben ser inmutables (Ecuación de Continuidad $\nabla \cdot \vec{J} = 0$).

## 1. Ley de Biot-Savart y Ampère
La fuerza repulsiva/atractiva magnética asintótica empírica entre hilos se resume en la Ley integral de Biot-Savart.
Aplicando rotacionales sobre esta ley de campos generados, recuperamos la Ecuación diferencial de Ampère:

$$
\nabla \times \vec{B} = \mu_0 \vec{J}
$$

Y la Monopolaridad nula impone que el campo magnético carezca de divergencia asintótica:

$$
\nabla \cdot \vec{B} = 0
$$

## 2. El Potencial Vector Magnético ($\vec{A}$)
Ya que el campo magnético no tiene monopolos ($\nabla \cdot \vec{B} = 0$), el Teorema de Helmholtz dictamina que siempre puede ser expresado íntegramente como el rotacional puro de otro campo abstracto superior: El Potencial Vector $\vec{A}$.

$$
\vec{B} = \nabla \times \vec{A}
$$

Sustituyendo en la Ley de Ampère y usando identidades vectoriales:

$$
\nabla(\nabla \cdot \vec{A}) - \nabla^2 \vec{A} = \mu_0 \vec{J}
$$

## 3. Invariancia Gauge (Coulomb)
El potencial vector $\vec{A}$ no es único. Podemos sumar arbitrariamente el Gradiente de cualquier función escalar sin alterar el Campo Real $\vec{B}$, dado que $\nabla \times (\nabla \lambda) = 0$.
Aprovechamos este grado de libertad (Transformación Gauge) y elegimos el **Gauge de Coulomb** estipulando brutalmente que $\nabla \cdot \vec{A} = 0$.
Bajo este Gauge milagroso, la ecuación de Ampère colapsa simétricamente en 3 Ecuaciones de Poisson independientes (una para cada eje cartesiano):

$$
\nabla^2 \vec{A} = -\mu_0 \vec{J}
$$

Cuyas soluciones por superposición asintótica son idénticas a las del potencial electrostático:

$$
\vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|} d\tau'
$$

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.02: Electricity and Magnetism (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro2314mKyUiALIcyEP7uHTy1I) - Experimentos magistrales y derivaciones desde cero.
- [Yale PHYS 201: Fundamentals of Physics II (Ramamurti Shankar)](https://www.youtube.com/playlist?list=PLD07B2225BBFA0681) - Énfasis matemático riguroso en electrostática y radiación.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.02: Physics II: Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/) - Walter Lewin.
  - [Stanford: Special Relativity and Electrodynamics](https://theoreticalminimum.com/courses/special-relativity-and-electrodynamics/2012/spring) - Leonard Susskind.
- **Libros de Texto Canónicos:**
  - *Classical Electrodynamics* - John David Jackson. (El texto definitivo a nivel posgrado).
  - *Introduction to Electrodynamics* - David J. Griffiths. (El texto estándar a nivel pregrado).
  - *The Feynman Lectures on Physics (Vol. II)*.
