# Expresiones Esenciales por Área (Cheat Sheet Nivel Doctorado)

Este documento centraliza las ecuaciones fundamentales y más trascendentales de todas las áreas de la física teórica y experimental. Está diseñado como el "Cheat Sheet" definitivo de nivel investigación, enfocado puramente en la arquitectura matemática absoluta del universo.

---

## 1. Mecánica Clásica y Dinámica No Lineal

**El Principio de Mínima Acción (Hamilton):**

$$
\delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt = 0
$$

**Ecuaciones de Euler-Lagrange con Multiplicadores (Vínculos Holonómicos):**

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = \sum_k \lambda_k \frac{\partial f_k}{\partial q_i}
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

**Ecuación Diferencial de Hamilton-Jacobi:**

$$
H\left( q_i, \frac{\partial S}{\partial q_i}, t \right) + \frac{\partial S}{\partial t} = 0
$$

**Teorema de Liouville (Conservación del Volumen en el Espacio de Fases):**

$$
\frac{d\rho}{dt} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0
$$

**Tensor de Inercia (Cuerpo Rígido):**

$$
I_{jk} = \int \rho(\vec{r}) (r^2 \delta_{jk} - x_j x_k) dV
$$

**Ecuaciones de Euler para Dinámica Rígida:**

$$
I_1 \dot{\omega}_1 + (I_3 - I_2)\omega_2 \omega_3 = \tau_1
$$

**Variables de Acción-Ángulo (Sistemas Integrables):**

$$
J_i = \frac{1}{2\pi} \oint p_i \, dq_i, \quad \omega_i = \frac{\partial H}{\partial J_i}
$$

**Corchetes de Dirac (Sistemas Singulares / Vínculos de Segunda Clase):**

$$
\{f, g\}_D = \{f, g\} - \sum_{a,b} \{f, \phi_a\} C^{-1}_{ab} \{\phi_b, g\}
$$

---

## 2. Mecánica de Fluidos y Medios Continuos

**Ecuación de Continuidad (Conservación de Masa):**

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0
$$

**Ecuaciones de Navier-Stokes (Flujo Viscoso):**

$$
\rho \left( \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot \nabla \vec{v} \right) = -\nabla P + \mu \nabla^2 \vec{v} + \left( \zeta + \frac{\mu}{3} \right) \nabla (\nabla \cdot \vec{v}) + \vec{f}
$$

**Ecuación de Euler (Fluidos Ideales Inviscidos):**

$$
\frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} = -\frac{1}{\rho}\nabla P + \vec{g}
$$

**Tensor de Esfuerzos de Cauchy:**

$$
\sigma_{ij} = -P \delta_{ij} + \mu \left( \frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i} \right) + \left( \zeta - \frac{2}{3}\mu \right) (\nabla \cdot \vec{v}) \delta_{ij}
$$

**Ecuación de Vorticidad de Helmholtz:**

$$
\frac{\partial \vec{\omega}}{\partial t} + (\vec{v} \cdot \nabla)\vec{\omega} = (\vec{\omega} \cdot \nabla)\vec{v} + \nu \nabla^2 \vec{\omega} \quad (\text{donde } \vec{\omega} = \nabla \times \vec{v})
$$

---

## 3. Electromagnetismo Clásico y Óptica

**Ecuaciones de Maxwell (Forma Diferencial Vectorial):**

$$
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}, \quad \nabla \cdot \vec{B} = 0
$$

$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
$$

**Tensor de Faraday (Campo Electromagnético) y Forma Covariante:**

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu, \quad \partial_\mu F^{\mu\nu} = \mu_0 J^\nu
$$

**Fuerza de Lorentz:**

$$
\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})
$$

**Teorema de Poynting (Conservación de Energía EM):**

$$
-\frac{\partial u}{\partial t} = \nabla \cdot \vec{S} + \vec{J} \cdot \vec{E}, \quad \vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}
$$

**Potenciales Retardados de Liénard-Wiechert:**

$$
\phi(\vec{r}, t) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{q}{(1 - \vec{\beta}\cdot\hat{n})R} \right]_{t_{ret}}
$$

**Fórmula de Radiación de Larmor y Fuerza de Abraham-Lorentz:**

$$
P = \frac{q^2 a^2}{6\pi \varepsilon_0 c^3}, \quad \vec{F}_{rad} = \frac{\mu_0 q^2}{6\pi c} \dot{\vec{a}}
$$

**Ecuaciones de Fresnel (Coeficiente de Reflexión, Polarización S):**

$$
R_s = \left| \frac{n_1 \cos \theta_i - n_2 \cos \theta_t}{n_1 \cos \theta_i + n_2 \cos \theta_t} \right|^2
$$

---

## 4. Termodinámica y Mecánica Estadística

**Identidad Termodinámica Fundamental:**

$$
dU = T dS - P dV + \sum_i \mu_i dN_i
$$

**Entropía de Boltzmann y Gibbs-Shannon:**

$$
S = k_B \ln \Omega, \quad S = -k_B \sum_i p_i \ln p_i
$$

**Funciones de Partición ($\mathcal{Z}$ y $\mathcal{Q}$):**

$$
\mathcal{Z} = \sum_i e^{-\beta E_i}, \quad \mathcal{Q} = \sum_N \sum_i e^{-\beta(E_{i,N} - \mu N)}
$$

**Ecuación de Transporte de Boltzmann (Con Colisiones):**

$$
\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_{\vec{r}} f + \frac{\vec{F}}{m} \cdot \nabla_{\vec{v}} f = \left( \frac{\partial f}{\partial t} \right)_{col}
$$

**Ecuación de Fokker-Planck (Movimiento Browniano / Difusión):**

$$
\frac{\partial P(x,t)}{\partial t} = -\frac{\partial}{\partial x} [D^{(1)}(x) P(x,t)] + \frac{\partial^2}{\partial x^2} [D^{(2)}(x) P(x,t)]
$$

**Relaciones de Onsager (Termodinámica del No Equilibrio):**

$$
L_{ij} = L_{ji} \quad \text{(Matriz de coeficientes cinéticos simétrica)}
$$

**Teorema de Fluctuación-Disipación y Relaciones de Green-Kubo:**

$$
D = \int_0^\infty \langle v(t) v(0) \rangle dt
$$

**Distribuciones Cuánticas (Fermi-Dirac y Bose-Einstein):**

$$
\langle n_i \rangle = \frac{1}{e^{\beta(E_i - \mu)} \pm 1}
$$

---

## 5. Física de Estado Sólido y Materia Condensada

**Teorema de Bloch (Electrones en un Cristal Periódico):**

$$
\psi_{\vec{k}}(\vec{r}) = e^{i\vec{k} \cdot \vec{r}} u_{\vec{k}}(\vec{r})
$$

**Ecuaciones de London (Superconductividad - Expulsión del campo EM):**

$$
\vec{J} = -\frac{n_s e^2}{m} \vec{A}, \quad \nabla \times \vec{J} = -\frac{n_s e^2}{m} \vec{B}
$$

**Energía Libre de Ginzburg-Landau (Transiciones de Fase Continuas):**

$$
F = F_n + \alpha |\psi|^2 + \frac{\beta}{2} |\psi|^4 + \frac{1}{2m^*} \left| \left( -i\hbar\nabla - 2e\vec{A} \right) \psi \right|^2 + \frac{|\vec{B}|^2}{2\mu_0}
$$

**Frecuencia de Plasma (Modelo de Drude):**

$$
\omega_p = \sqrt{\frac{n e^2}{m \varepsilon_0}}
$$

**Densidad de Estados Cuántica en 3D (Electrones Libres):**

$$
g(E) = \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \sqrt{E}
$$

---

## 6. Relatividad Especial y General

**Tensor de Curvatura de Riemann (Conmutador de Derivadas Covariantes):**

$$
R^\rho_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}
$$

**Ecuaciones de Campo de Einstein:**

$$
R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

**Ecuación de Desvío Geodésico (Fuerzas de Marea Reales):**

$$
\frac{D^2 \xi^\mu}{d\tau^2} = -R^\mu_{\nu\rho\sigma} U^\nu \xi^\rho U^\sigma
$$

**Tensor de Weyl (Curvatura Libre de Traza):**

$$
C_{\mu\nu\rho\sigma} = R_{\mu\nu\rho\sigma} - \frac{1}{2}(g_{\mu\rho}R_{\nu\sigma} - \dots) + \frac{1}{6}R(g_{\mu\rho}g_{\nu\sigma} - \dots)
$$

**Agujero Negro de Schwarzschild y Kerr (Estático vs Rotatorio):**

$$
ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right) c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2 d\Omega^2
$$

$$
ds^2_{Kerr} = - \left( 1 - \frac{r_s r}{\rho^2} \right) c^2 dt^2 - \frac{2r_s r a \sin^2\theta}{\rho^2} c dt d\phi + \frac{\rho^2}{\Delta} dr^2 + \rho^2 d\theta^2 + \dots
$$

**Ecuación de Ondas Gravitacionales (Aproximación de Campo Débil TT):**

$$
\Box \bar{h}_{\mu\nu}^{TT} = 0, \quad \bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}h \eta_{\mu\nu}
$$

**Formulación ADM (Arnowitt-Deser-Misner / Geometrodinámica):**

$$
ds^2 = -N^2 dt^2 + \gamma_{ij} (dx^i + N^i dt)(dx^j + N^j dt)
$$

---

## 7. Mecánica Cuántica (No Relativista)

**Ecuación de Schrödinger y Principio de Incertidumbre Generalizado:**

$$
i\hbar \frac{\partial |\Psi\rangle}{\partial t} = \hat{H} |\Psi\rangle, \quad \sigma_A \sigma_B \ge \frac{1}{2} \left| \langle [\hat{A}, \hat{B}] \rangle \right|
$$

**Teorema de Ehrenfest (Límite Clásico):**

$$
\frac{d}{dt}\langle \hat{A} \rangle = \frac{1}{i\hbar} \langle [\hat{A}, \hat{H}] \rangle + \left\langle \frac{\partial \hat{A}}{\partial t} \right\rangle
$$

**Ecuación de Von Neumann (Evolución de la Matriz Densidad $\rho$):**

$$
i\hbar \frac{\partial \hat{\rho}}{\partial t} = [\hat{H}, \hat{\rho}]
$$

**Fase de Berry (Transporte Paralelo Adiabático):**

$$
\gamma_n(C) = i \oint_C \langle n(\vec{R}) | \nabla_{\vec{R}} | n(\vec{R}) \rangle \cdot d\vec{R}
$$

**Aproximación WKB (Coeficiente de Transmisión por Efecto Túnel):**

$$
T \approx \exp\left( -\frac{2}{\hbar} \int_{x_1}^{x_2} \sqrt{2m(V(x) - E)} \, dx \right)
$$

**Ecuación de Lippmann-Schwinger (Dispersión):**

$$
|\psi^{(\pm)}\rangle = |\phi\rangle + \frac{1}{E - \hat{H}_0 \pm i\epsilon} \hat{V} |\psi^{(\pm)}\rangle
$$

---

## 8. Teoría Cuántica de Campos (QFT) y Modelo Estándar

**Corriente de Noether Conservada:**

$$
j^\mu = \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \delta \phi - \mathcal{L} \delta x^\mu
$$

**Ecuaciones de Dirac y Klein-Gordon:**

$$
(i\gamma^\mu \partial_\mu - m) \psi = 0, \quad (\Box + m^2) \phi = 0
$$

**Integral de Camino de Feynman (Funcional Generador $Z[J]$):**

$$
Z[J] = \int \mathcal{D}\phi \, \exp\left( i \int d^4x (\mathcal{L} + J\phi) \right)
$$

**Lagrangiano de Yang-Mills (Gauge No Abeliano - QCD):**

$$
\mathcal{L}_{YM} = -\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu}, \quad F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c
$$

**Fórmula de Reducción LSZ (Matriz S a partir de correladores):**

$$
\langle f | S | i \rangle \propto \int d^4x_1 \dots d^4x_n e^{ip_i x_i} (\Box + m^2) \langle 0 | T\{ \phi(x_1) \dots \phi(x_n) \} | 0 \rangle
$$

**Identidades de Ward-Takahashi (Análogos Cuánticos de Conservación):**

$$
q_\mu \mathcal{M}^\mu = 0
$$

**Ecuación del Grupo de Renormalización de Callan-Symanzik:**

$$
\left[ \mu \frac{\partial}{\partial \mu} + \beta(g) \frac{\partial}{\partial g} + n \gamma(g) \right] G^{(n)} = 0
$$

**Lagrangiano de Faddeev-Popov (Término de Fantasmas para Calibre Gauge):**

$$
\mathcal{L}_{ghost} = \bar{c}^a (-\partial^\mu D_\mu^{ab}) c^b
$$

---

## 9. Astrofísica, Cosmología e Inflación Cósmica

**Métrica FLRW (Cosmología Homogénea e Isotrópica):**

$$
ds^2 = -c^2 dt^2 + a^2(t) \left[ \frac{dr^2}{1 - kr^2} + r^2 d\Omega^2 \right]
$$

**Ecuaciones de Friedmann Completas:**

$$
H^2 = \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}, \quad \frac{\ddot{a}}{a} = -\frac{4\pi G}{3} \left( \rho + \frac{3P}{c^2} \right) + \frac{\Lambda c^2}{3}
$$

**Ecuación Tolman-Oppenheimer-Volkoff (TOV) para Estrellas de Neutrones:**

$$
\frac{dP}{dr} = -\frac{G}{r^2} \left( \rho + \frac{P}{c^2} \right) \left( M(r) + \frac{4\pi r^3 P}{c^2} \right) \left( 1 - \frac{2GM(r)}{c^2 r} \right)^{-1}
$$

**Ecuación de Campo de Inflación Cósmica (Slow-Roll):**

$$
\ddot{\phi} + 3H\dot{\phi} + V'(\phi) = 0, \quad H^2 \approx \frac{8\pi G}{3} V(\phi)
$$

**Espectro de Potencias de Perturbaciones (Harrison-Zel'dovich CMB):**

$$
\mathcal{P}_{\mathcal{R}}(k) = A_s \left( \frac{k}{k_*} \right)^{n_s - 1} \approx \text{constante}
$$

**Masa de Jeans (Colapso Gravitatorio Nube de Gas):**

$$
M_J = \left( \frac{5 k_B T}{G m_p \mu} \right)^{3/2} \left( \frac{3}{4\pi \rho_0} \right)^{1/2}
$$

**Ecuación de Saha (Fracción de Ionización del Plasma Cosmico):**

$$
\frac{n_i n_e}{n_n} = \frac{2}{\lambda_e^3} \frac{g_i}{g_n} e^{-I / k_B T}
$$

---

## 10. Teoría de Cuerdas y Gravedad Cuántica

**Acción de Nambu-Goto (Cuerda Relativista Clásica):**

$$
S_{NG} = -T_0 \int d\tau d\sigma \sqrt{(\dot{X} \cdot X')^2 - (\dot{X})^2 (X')^2}
$$

**Acción de Polyakov (Superficie de Mundo bidimensional):**

$$
S_P = -\frac{T}{2} \int d^2\sigma \sqrt{-h} h^{\alpha\beta} \partial_\alpha X^\mu \partial_\beta X^\nu \eta_{\mu\nu}
$$

**Entropía de Bekenstein-Hawking (Holografía / Gravedad Cuántica):**

$$
S_{BH} = \frac{k_B c^3 A}{4 G \hbar} = \frac{A}{4 l_P^2}
$$

**Temperatura de Radiación de Hawking:**

$$
T_H = \frac{\hbar c^3}{8\pi G M k_B}
$$

**Ecuación de Wheeler-DeWitt (Gravedad Cuántica Canónica):**

$$
\hat{\mathcal{H}} |\Psi\rangle = 0 \quad \text{(Donde el espacio-tiempo carece de evolución temporal global)}
$$

**Condiciones de Anulación del Álgebra de Virasoro:**

$$
[L_m, L_n] = (m - n) L_{m+n} + \frac{c}{12} m(m^2 - 1) \delta_{m+n, 0}
$$

**Fórmula ADS/CFT de Maldacena (Límite 't Hooft):**

$$
Z_{AdS}[\phi_0] = \langle \exp \left( \int d^d x \phi_0 \mathcal{O} \right) \rangle_{CFT}
$$
