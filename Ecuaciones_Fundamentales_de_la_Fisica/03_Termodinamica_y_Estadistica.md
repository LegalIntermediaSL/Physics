# Ecuaciones Fundamentales: Termodinámica y Estadística

## 1. Leyes de la Termodinámica
**Primera Ley (Conservación de Energía Diferencial):**
$$ dU = \delta Q - \delta W = T dS - p dV + \sum \mu_i dN_i $$
**Segunda Ley (Desigualdad de Clausius y Entropía):**
$$ dS \ge \frac{\delta Q}{T}, \quad \Delta S_{\text{universo}} \ge 0 $$

## 2. Potenciales Termodinámicos (Transformadas de Legendre)
**Entalpía ($H$):**
$$ H = U + pV, \quad dH = T dS + V dp $$
**Energía Libre de Helmholtz ($F$):**
$$ F = U - TS, \quad dF = -S dT - p dV $$
**Energía Libre de Gibbs ($G$):**
$$ G = H - TS, \quad dG = -S dT + V dp $$

## 3. Mecánica Estadística
**Fórmula de la Entropía de Boltzmann:**
$$ S = k_B \ln \Omega $$
**Función de Partición Canónica ($Z$):**
$$ Z = \sum_i e^{-\beta E_i}, \quad \beta = \frac{1}{k_B T} $$
**Conexión Estadística-Termodinámica:**
$$ F = - k_B T \ln Z, \quad \langle E \rangle = - \frac{\partial \ln Z}{\partial \beta} $$
**Distribuciones de Partículas Indistinguibles:**
$$ \langle n_i \rangle_{\text{Bose-Einstein}} = \frac{1}{e^{\beta(E_i - \mu)} - 1} $$
$$ \langle n_i \rangle_{\text{Fermi-Dirac}} = \frac{1}{e^{\beta(E_i - \mu)} + 1} $$

## 4. Dinámica Estocástica
**Ecuación Íntegro-Diferencial de Boltzmann:**
$$ \frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_{\vec{r}} f + \frac{\vec{F}}{m} \cdot \nabla_{\vec{v}} f = \left( \frac{\partial f}{\partial t} \right)_{\text{colisiones}} $$
**Teorema H de Boltzmann:**
$$ H_B = \int f \ln f \, d^3v, \quad \frac{dH_B}{dt} \le 0 $$
