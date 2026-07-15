# Ecuaciones Fundamentales: Relatividad General y Especial

## 1. Relatividad Especial (Minkowski)
**Intervalo Espacio-Temporal Invariante:**

$$
ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu = -c^2 dt^2 + dx^2 + dy^2 + dz^2
$$

**Factor de Lorentz ($\gamma$):**

$$
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}
$$

**Energía Relativista (Cuadrimomento $p^\mu$):**

$$
E^2 = (pc)^2 + (m_0 c^2)^2, \quad p^\mu = m_0 U^\mu = (\gamma m_0 c, \gamma m_0 \vec{v})
$$

## 2. Geometría Diferencial (Variedad Riemanniana)
**Símbolos de Christoffel (Conexión Afín de Levi-Civita):**

$$
\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} ( \partial_\mu g_{\sigma\nu} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu} )
$$

**Tensor de Curvatura de Riemann ($R^\rho_{\sigma\mu\nu}$):**

$$
R^\rho_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}
$$

## 3. Relatividad General
**Ecuaciones de Campo de Einstein:**

$$
R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

**Ecuación Geodésica (Movimiento en Caída Libre):**

$$
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0
$$

**Acción de Einstein-Hilbert:**

$$
S_{EH} = \int \left[ \frac{c^4}{16\pi G} (R - 2\Lambda) + \mathcal{L}_{\text{materia}} \right] \sqrt{-g} \, d^4x
$$

## 4. Soluciones Clásicas Exactas
**Métrica de Schwarzschild (Vacío, Estático, Esférico):**

$$
ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta \, d\phi^2), \quad r_s = \frac{2GM}{c^2}
$$

**Métrica FLRW (Universo Homogéneo e Isotrópico):**

$$
ds^2 = -c^2 dt^2 + a(t)^2 \left[ \frac{dr^2}{1 - kr^2} + r^2 (d\theta^2 + \sin^2\theta \, d\phi^2) \right]
$$

