# Expresiones Esenciales por Área (Cheat Sheet Nivel Doctorado)

Este documento centraliza las ecuaciones fundamentales y más trascendentales de todas las áreas de la física moderna. Está diseñado como una hoja de referencia rápida (Cheat Sheet) de alto nivel, libre de descripciones extensas y enfocada puramente en la arquitectura matemática subyacente del universo.

---

## 1. Mecánica Clásica y Analítica

**El Principio de Mínima Acción (Hamilton):**

$$
\delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt = 0
$$

**Ecuaciones de Euler-Lagrange:**

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

**Transformada de Legendre y Hamiltoniano:**

$$
H(q, p, t) = \sum_i p_i \dot{q}_i - L(q, \dot{q}, t)
$$

**Ecuaciones Canónicas de Hamilton:**

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

**Corchetes de Poisson (Evolución Temporal):**

$$
\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}
$$

**Ecuación Diferencial No Lineal de Hamilton-Jacobi:**

$$
H\left( q_i, \frac{\partial S}{\partial q_i}, t \right) + \frac{\partial S}{\partial t} = 0
$$

---

## 2. Electromagnetismo Clásico

**Ecuaciones de Maxwell (Forma Diferencial Vectorial):**

$$
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}, \quad \nabla \cdot \vec{B} = 0
$$

$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
$$

**Potenciales Electromagnéticos:**

$$
\vec{B} = \nabla \times \vec{A}, \quad \vec{E} = - \nabla \phi - \frac{\partial \vec{A}}{\partial t}
$$

**Fuerza de Lorentz:**

$$
\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})
$$

**Tensor de Faraday (Campo Electromagnético):**

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu
$$

**Maxwell Covariante:**

$$
\partial_\mu F^{\mu\nu} = \mu_0 J^\nu
$$

---

## 3. Termodinámica y Mecánica Estadística

**Identidad Termodinámica Fundamental:**

$$
dU = T dS - P dV + \sum_i \mu_i dN_i
$$

**Entropía de Boltzmann (Microestados):**

$$
S = k_B \ln \Omega
$$

**Función de Partición Canónica ($\mathcal{Z}$):**

$$
\mathcal{Z} = \sum_i e^{-\beta E_i}, \quad \beta = \frac{1}{k_B T}
$$

**Energía Libre de Helmholtz a partir de $\mathcal{Z}$:**

$$
F = -k_B T \ln \mathcal{Z}
$$

**Ecuación de Transporte de Boltzmann:**

$$
\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_{\vec{r}} f + \frac{\vec{F}}{m} \cdot \nabla_{\vec{v}} f = \left( \frac{\partial f}{\partial t} \right)_{col}
$$

**Distribuciones Cuánticas (Fermi-Dirac y Bose-Einstein):**

$$
\langle n_i \rangle = \frac{1}{e^{\beta(E_i - \mu)} \pm 1}
$$

---

## 4. Relatividad Especial y General

**Intervalo Invariante de Minkowski:**

$$
ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu = -c^2 dt^2 + dx^2 + dy^2 + dz^2
$$

**Tensor de Energía-Momento (Fluido Perfecto):**

$$
T^{\mu\nu} = (\rho + P) U^\mu U^\nu + P g^{\mu\nu}
$$

**Ecuaciones de Campo de Einstein:**

$$
R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

**Ecuación Geodésica (Caída Libre):**

$$
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0
$$

**Agujero Negro de Schwarzschild (Métrica Exterior):**

$$
ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 d\Omega^2
$$

---

## 5. Mecánica Cuántica (No Relativista)

**Ecuación de Schrödinger Dinámica:**

$$
i\hbar \frac{\partial |\Psi\rangle}{\partial t} = \hat{H} |\Psi\rangle
$$

**Relación de Conmutación Canónica:**

$$
[\hat{x}, \hat{p}] = i\hbar
$$

**Principio de Incertidumbre Generalizado:**

$$
\sigma_A \sigma_B \ge \frac{1}{2} \left| \langle [\hat{A}, \hat{B}] \rangle \right|
$$

**Teoría de Perturbaciones (Primer Orden en Energía):**

$$
E_n^{(1)} = \langle \psi_n^{(0)} | \hat{H}' | \psi_n^{(0)} \rangle
$$

**Regla de Oro de Fermi (Tasa de Decaimiento a un Continuo):**

$$
\Gamma_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2 \rho(E_f)
$$

---

## 6. Teoría Cuántica de Campos (QFT) y Modelo Estándar

**Ecuación de Klein-Gordon (Campos Escalares Espín 0):**

$$
(\partial_\mu \partial^\mu + m^2) \phi = 0
$$

**Ecuación de Dirac (Campos Espinoriales Espín 1/2):**

$$
(i\gamma^\mu \partial_\mu - m) \psi = 0
$$

**Integral de Camino de Feynman (Funcional Generador $Z[J]$):**

$$
Z[J] = \int \mathcal{D}\phi \, \exp\left( i \int d^4x (\mathcal{L} + J\phi) \right)
$$

**Ecuación del Grupo de Renormalización de Callan-Symanzik:**

$$
\left[ \mu \frac{\partial}{\partial \mu} + \beta(g) \frac{\partial}{\partial g} + n \gamma(g) \right] G^{(n)}(x_1, \dots, x_n; \mu, g) = 0
$$

**Lagrangiano del Modelo Estándar (Compacto):**

$$
\mathcal{L}_{SM} = -\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu} + i \bar{\psi} \not{D} \psi + |D_\mu \phi|^2 - V(\phi) + \bar{\psi}_i y_{ij} \psi_j \phi + h.c.
$$

---

## 7. Astrofísica y Cosmología

**Métrica FLRW (Cosmología Homogénea e Isotrópica):**

$$
ds^2 = -c^2 dt^2 + a^2(t) \left[ \frac{dr^2}{1 - kr^2} + r^2 d\Omega^2 \right]
$$

**Ecuación de Friedmann (Expansión del Universo):**

$$
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}
$$

**Temperatura de Radiación de Hawking (Agujero Negro):**

$$
T_H = \frac{\hbar c^3}{8\pi G M k_B}
$$

**Límite de Chandrasekhar (Masa máxima Enana Blanca):**

$$
M_{Ch} \approx 1.44 M_\odot
$$

**Corrimiento al Rojo Cosmológico ($z$):**

$$
1 + z = \frac{a(t_{obs})}{a(t_{em})}
$$
