# [FUN-06] Ecuaciones Fundamentales: TCC y Modelo Estándar

## 1. Ecuaciones Relativistas de Campos Libres
**Ecuación de Klein-Gordon (Campos Escalares Espín 0):**

$$
(\partial_\mu \partial^\mu + m^2) \phi = 0 \quad \implies \quad (\Box + m^2) \phi = 0
$$

**Ecuación de Dirac (Campos Espinoriales Espín 1/2):**

$$
(i\gamma^\mu \partial_\mu - m) \psi = 0 \quad \implies \quad (i\not{\partial} - m) \psi = 0
$$

**Álgebra de Clifford (Matrices Gamma de Dirac):**

$$
\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2\eta^{\mu\nu} I_4
$$

## 2. Formulaciones Integrales y Propagadores
**Propagador de Feynman (Campo Escalar Libre):**

$$
\Delta_F(x - y) = \int \frac{d^4p}{(2\pi)^4} \frac{i}{p^2 - m^2 + i\epsilon} e^{-ip \cdot (x - y)}
$$

**Integral de Camino de Feynman (Funcional Generador $Z[J]$):**

$$
Z[J] = \int \mathcal{D}\phi \, \exp\left[ i \int d^4x (\mathcal{L} + J\phi) \right]
$$

## 3. El Modelo Estándar de la Física de Partículas
El Modelo Estándar es una Teoría de Campos Gauge basada en el grupo de simetría local: $SU(3)_C \times SU(2)_L \times U(1)_Y$.
**Densidad Lagrangiana Total del Modelo Estándar:**

$$
\mathcal{L}_{SM} = -\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu} + i \bar{\psi} \not{D} \psi + |D_\mu \phi|^2 - V(\phi) + \bar{\psi}_i y_{ij} \psi_j \phi + h.c.
$$

*Desglose:*
- **Término Gauge (Cromodinámica + Electrodébil):** $-\frac{1}{4} G_{\mu\nu}^A G^{A\mu\nu} -\frac{1}{4} W_{\mu\nu}^a W^{a\mu\nu} -\frac{1}{4} B_{\mu\nu} B^{\mu\nu}$
- **Término Fermiónico (Acoplamiento a Bosones Gauge):** $i \bar{\psi} \gamma^\mu D_\mu \psi \quad \text{donde} \quad D_\mu = \partial_\mu - i g_s T^A G_\mu^A - i g \frac{\tau^a}{2} W_\mu^a - i g' \frac{Y}{2} B_\mu$
- **Término del Higgs (Ruptura Espontánea de Simetría):** $|D_\mu \phi|^2 - \mu^2 |\phi|^2 - \lambda |\phi|^4$
- **Término de Yukawa (Masas Fermiónicas):** $- y_f \bar{\psi}_L \phi \psi_R + h.c.$

## 4. Renormalización
**Ecuación del Grupo de Renormalización de Callan-Symanzik:**

$$
\left[ \mu \frac{\partial}{\partial \mu} + \beta(g) \frac{\partial}{\partial g} + n \gamma(g) \right] G^{(n)}(x_1, \dots, x_n; \mu, g) = 0
$$


---
## 📚 Referencias, Enlaces y Cursos Recomendados
- **Cursos Universitarios:**
  - [MIT 8.01 / 8.02 / 8.03 / 8.04](https://ocw.mit.edu/courses/physics/) - El ciclo completo de Walter Lewin y Allan Adams.
  - [The Theoretical Minimum](https://theoreticalminimum.com/) - Leonard Susskind. Todo el marco teórico de la física moderna.
- **Libros de Texto Canónicos:**
  - *The Feynman Lectures on Physics* (Vol. I, II, III) - Richard Feynman. [Disponible online gratuitamente por Caltech](https://www.feynmanlectures.caltech.edu/).
  - *University Physics* - Young & Freedman (Para bases rigurosas).
