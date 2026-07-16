# [QM-02] Evolución Temporal y la Ecuación de Schrödinger

A diferencia del violento colapso estocástico que ocurre durante una medición, la evolución de un estado cuántico en ausencia de observaciones es completamente determinista, suave, continua y matemáticamente reversible (Unitaria).

## 1. La Ecuación de Schrödinger
La dinámica está dictada por el Operador Hamiltoniano $\hat{H}$ (que representa la energía total del sistema: Cinética + Potencial).

$$
i\hbar \frac{\partial}{\partial t} |\Psi(t)\rangle = \hat{H} |\Psi(t)\rangle
$$

Si $\hat{H}$ no depende explícitamente del tiempo, la solución formal es una simple rotación unitaria:

$$
|\Psi(t)\rangle = \hat{U}(t) |\Psi(0)\rangle = e^{-i\hat{H}t/\hbar} |\Psi(0)\rangle
$$

## 2. Tres Representaciones de la Dinámica
En cuántica, las predicciones físicas (Valores Esperados $\langle \hat{A} \rangle$) son lo único que medimos en el laboratorio. La matemática nos da tres formas equivalentes (Pictures) de calcular lo mismo:

- **La Imagen de Schrödinger**: Los estados $|\Psi(t)\rangle$ se mueven como manecillas de un reloj. Los operadores (como $\hat{x}$) son fijos e inmóviles.
- **La Imagen de Heisenberg**: Los estados $|\Psi\rangle$ están congelados eternamente en el tiempo. Son los operadores (las reglas de medir) los que cambian dinámicamente según la Ecuación de Movimiento de Heisenberg: $\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \frac{\partial \hat{A}_H}{\partial t}$. (Esto es idéntico a los corchetes de Poisson de la mecánica clásica de Hamilton).
- **La Imagen de Interacción (Dirac)**: Un híbrido usado en Teoría Cuántica de Campos (QFT). Si $\hat{H} = \hat{H}_0 + \hat{V}$, los estados evolucionan debido al potencial perturbativo $\hat{V}$, mientras que los operadores evolucionan debido al Hamiltoniano libre $\hat{H}_0$.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [MIT 8.04: Quantum Physics I (Barton Zwiebach)](https://www.youtube.com/playlist?list=PLUl4u3cNGP61-9PEhRognw5vryrSEVLPr) - Excelente tratamiento riguroso de la mecánica ondulatoria y espinores.
- [Stanford: Theoretical Minimum - Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL701CD168D02FF56F) - El estándar de oro para entender el entrelazamiento y los espacios de Hilbert de forma intuitiva.
- [Perimeter Institute: Quantum Mechanics](https://www.youtube.com/user/PIOutreach) - Clases de nivel máster para investigadores.

---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [Stanford: Quantum Mechanics](https://theoreticalminimum.com/courses/quantum-mechanics/2012/winter) - Leonard Susskind.
  - [MIT 8.04: Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/) - Allan Adams (Una de las mejores introducciones visuales y matemáticas del mundo).
- **Libros de Texto Canónicos:**
  - *Principles of Quantum Mechanics* - R. Shankar.
  - *Modern Quantum Mechanics* - J.J. Sakurai. (Estándar de posgrado).
  - *Quantum Mechanics* - L.D. Landau & E.M. Lifshitz (Vol. 3).
