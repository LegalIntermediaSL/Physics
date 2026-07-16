# Ecuaciones Fundamentales: Mecánica Cuántica

## 1. Postulados y Dinámica
**Ecuación de Schrödinger (Dependiente del Tiempo):**

$$
i\hbar \frac{\partial |\Psi\rangle}{\partial t} = \hat{H} |\Psi\rangle
$$

**Ecuación de Schrödinger (Independiente del Tiempo, Estados Estacionarios):**

$$
\hat{H} |\psi_n\rangle = E_n |\psi_n\rangle
$$

**Probabilidad de Born:**

$$
P(\vec{r}, t) = |\Psi(\vec{r}, t)|^2 = \Psi^* \Psi
$$

## 2. Conmutadores y Observables
**Principio de Incertidumbre Generalizado (Heisenberg-Robertson):**

$$
\sigma_A \sigma_B \ge \frac{1}{2} \left| \langle [\hat{A}, \hat{B}] \rangle \right|
$$

**Relación de Conmutación Canónica Fundamental:**

$$
[\hat{x}, \hat{p}_x] = i\hbar
$$

**Ecuación de Movimiento de Heisenberg (Imagen de Heisenberg):**

$$
\frac{d\hat{A}}{dt} = \frac{i}{\hbar} [\hat{H}, \hat{A}] + \frac{\partial \hat{A}}{\partial t}
$$

## 3. Momento Angular y Espín
**Álgebra del Momento Angular:**

$$
[\hat{L}_i, \hat{L}_j] = i\hbar \epsilon_{ijk} \hat{L}_k
$$

**Estados Propios del Momento Angular:**

$$
\hat{L}^2 |l, m\rangle = \hbar^2 l(l+1) |l, m\rangle, \quad \hat{L}_z |l, m\rangle = \hbar m |l, m\rangle
$$

**Matrices de Pauli (Generadores del Espín 1/2 en SU(2)):**

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

## 4. Teoría de Perturbaciones
**Corrección de Energía (Primer Orden, Independiente del tiempo):**

$$
E_n^{(1)} = \langle \psi_n^{(0)} | \hat{H}' | \psi_n^{(0)} \rangle
$$

**Regla de Oro de Fermi (Tasa de Transición a un Continuo):**

$$
\Gamma_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f)
$$


---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.01 / 8.02 / 8.03 / 8.04](https://ocw.mit.edu/courses/physics/) - El ciclo completo de Walter Lewin y Allan Adams.
  - [The Theoretical Minimum](https://theoreticalminimum.com/) - Leonard Susskind. Todo el marco teórico de la física moderna.
- **Libros de Texto Canónicos:**
  - *The Feynman Lectures on Physics* (Vol. I, II, III) - Richard Feynman. [Disponible online gratuitamente por Caltech](https://www.feynmanlectures.caltech.edu/).
  - *University Physics* - Young & Freedman (Para bases rigurosas).
