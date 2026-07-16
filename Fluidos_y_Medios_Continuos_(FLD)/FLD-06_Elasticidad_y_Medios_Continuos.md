# [FLD-06] Elasticidad Lineal y Teoría de Sólidos Continuos

Los sólidos son simplemente fluidos donde los esfuerzos resisten deformaciones estáticas y no solo tasas de deformación. La Teoría de la Elasticidad es la mecánica de la materia sólida continua.

## 1. El Tensor de Tensión de Cauchy ($\boldsymbol{\sigma}$) y Deformación ($\boldsymbol{\varepsilon}$)
- La fuerza interna en cualquier corte del sólido es el **Tensor de Tensiones** de Cauchy $\sigma_{ij}$ (Fuerza por unidad de área).
- El desplazamiento macroscópico de los puntos se describe mediante el campo $\mathbf{u}(\mathbf{x})$. El **Tensor de Deformación** infinitesimal asume gradientes pequeños:

$$
\varepsilon_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right)
$$

## 2. La Ley de Hooke Generalizada
Para sólidos elásticos y elásticos lineales (como el acero bajo cargas normales), el esfuerzo es directamente proporcional a la deformación. Esto es una contracción tensorial de cuarto orden $C_{ijkl}$:

$$
\sigma_{ij} = C_{ijkl} \varepsilon_{kl}
$$

Para un material isótropo e ideal, los 81 parámetros se colapsan espectacularmente en solo 2 coeficientes independientes (Las Constantes de Lamé $\lambda$ y $\mu$):

$$
\sigma_{ij} = 2\mu \varepsilon_{ij} + \lambda (\nabla \cdot \mathbf{u}) \delta_{ij}
$$

La ingeniería suele usar el Módulo de Young ($E$) y el Coeficiente de Poisson ($\nu$).

## 3. Ondas Elásticas Sólidas (Sismología)
Inyectando la Ley de Hooke en la ecuación de movimiento clásico de Cauchy ($\rho \ddot{\mathbf{u}} = \nabla \cdot \boldsymbol{\sigma}$), obtenemos la Ecuación de Ondas de Navier-Cauchy para la propagación del sonido dentro de los sólidos.
Aplicando identidades vectoriales genéricas, la perturbación se divide mágicamente en dos ecuaciones de ondas fundamentales con velocidades de propagación independientes:
- **Ondas P (Primarias / Compresionales)**: Asociadas a la divergencia $\nabla \cdot \mathbf{u}$. Deformación del volumen, como el sonido acústico normal. Viajan a altísima velocidad ($c_p = \sqrt{(\lambda + 2\mu)/\rho}$).
- **Ondas S (Secundarias / Cizalla)**: Asociadas al rotacional $\nabla \times \mathbf{u}$. Deformación de pura cizalla (cambio de forma). No pueden existir en líquidos ni gases porque $\mu=0$. Viajan más lento ($c_s = \sqrt{\mu/\rho}$).

Este es el santo grial de la geofísica: las ondas S no cruzan el Núcleo Externo de la Tierra, demostrando indiscutiblemente que el núcleo externo es líquido puro fundido.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 2.006: Thermal-Fluids Engineering](https://ocw.mit.edu/courses/2-006-thermal-fluids-engineering-ii-spring-2004/).
  - [National Committee for Fluid Mechanics Films (NCFMF)](https://web.mit.edu/hml/ncfmf.html) - Serie histórica de vídeos del MIT (obligatorio para visualizar fluidos).
- **Libros de Texto Canónicos:**
  - *Fluid Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 6 del Curso de Física Teórica).
  - *An Introduction to Fluid Dynamics* - G.K. Batchelor.
  - *Turbulence: The Legacy of A.N. Kolmogorov* - Uriel Frisch.
