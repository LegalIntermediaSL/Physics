# Flujo Potencial y Aerodinámica Ideal

## 1. Irrotacionalidad
Bajo ciertas condiciones aerodinámicas (fuera de las finas "capas límite" viscosas), el flujo puede aproximarse como no viscoso e incompresible. Por el Teorema de Kelvin, si el fluido parte del reposo, permanecerá **Irrotacional** ($\nabla \times \vec{v} = 0$).

Debido a que el rotacional de un gradiente es siempre cero matemáticamente, podemos definir el campo de velocidades a partir de una función escalar potencial $\Phi$:

$$
\vec{v} = \nabla \Phi
$$

## 2. La Ecuación de Laplace
Combinando esta irrotacionalidad con la ecuación de continuidad incompresible ($\nabla \cdot \vec{v} = 0$), obtenemos la joya de la física matemática armónica: la **Ecuación de Laplace**.

$$
\nabla^2 \Phi = 0
$$

La linealidad de esta ecuación permite resolver problemas de vuelo complejos usando el **Principio de Superposición**. Los flujos se construyen sumando singularidades matemáticas elementales.

## 3. Fuentes, Sumideros, Dobletes y Vórtices
- **Fuente:** Flujo radial emitido desde un punto. $\Phi = \frac{m}{2\pi} \ln r$.
- **Vórtice Libre:** Flujo giratorio sin cizalladura radial local. $\Phi = \frac{\Gamma}{2\pi} \theta$, donde $\Gamma$ es la circulación.
- **Doblete:** Un par fuente-sumidero infinitamente cercano.

El flujo real sobre un cilindro de radio $R$ (flujo no perturbado más perturbación del cilindro) se modela sumando un flujo uniforme y un doblete:

$$
\Phi(r, \theta) = U r \cos\theta + \frac{\mu}{2\pi r} \cos\theta
$$

Si añadimos un vórtice al cilindro, rompemos la simetría arriba/abajo. Por el **Teorema de Kutta-Joukowski**, esta circulación de fluido genera una fuerza ortogonal a la velocidad. Es la derivación exacta y fundamental de por qué los aviones pueden generar Sustentación (Lift).

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
