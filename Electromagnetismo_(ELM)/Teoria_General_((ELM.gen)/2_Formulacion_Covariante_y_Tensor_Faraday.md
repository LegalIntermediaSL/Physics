# Formulación Covariante del Electromagnetismo (Tensor de Faraday)

## 1. Unificando E y B
Bajo la luz de la Relatividad de Minkowski, los campos Eléctrico y Magnético no son entidades independientes. Dependiendo del sistema de referencia inercial del observador, un campo eléctrico puramente estático puede manifestar componentes magnéticas dinámicas y viceversa. 

Las Ecuaciones de Maxwell, inherentemente relativistas antes de la formulación de Einstein, se compactan hermosamente al definir el **Tensor Electromagnético Antisimétrico o Tensor de Faraday** ($F^{\mu\nu}$).

## 2. Definición Geométrica del Tensor $F^{\mu\nu}$
Se construye a partir de la derivada exterior (conmutador) del cuadripotencial $A^\mu = (\phi/c, \vec{A})$:

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu
$$

En componentes matriciales $4 \times 4$:

$$
F^{\mu\nu} = \begin{pmatrix} 0 & E_x/c & E_y/c & E_z/c \\ -E_x/c & 0 & B_z & -B_y \\ -E_y/c & -B_z & 0 & B_x \\ -E_z/c & B_y & -B_x & 0 \end{pmatrix}
$$

## 3. Las Ecuaciones de Maxwell en Forma Tensorial
Con este tensor, las 4 engorrosas ecuaciones de Maxwell vectoriales colapsan en solo dos ecuaciones cuadridimensionales de una elegancia matemática abrumadora:

**1. Ecuación Inhomogénea (Ley de Gauss y Ley de Ampère-Maxwell):**

$$
\partial_\mu F^{\mu\nu} = \mu_0 J^\nu
$$

Donde $J^\nu = (\rho c, \vec{J})$ es la cuadricorriente.

**2. Ecuación Homogénea (Ley de Faraday y Ausencia de Monopolos):**
Usando el tensor dual de Hodge $\tilde{F}^{\mu\nu} = \frac{1}{2} \epsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$ o las identidades cíclicas de Bianchi:

$$
\partial_{[\lambda} F_{\mu\nu]} = 0 \quad \text{o} \quad \partial_\mu \tilde{F}^{\mu\nu} = 0
$$

## 4. Invariantes de Lorentz
La formulación tensorial revela la existencia de cantidades conservadas absolutas para todo observador:
1. $F_{\mu\nu} F^{\mu\nu} = 2(|\vec{B}|^2 - \frac{|\vec{E}|^2}{c^2}) = \text{Invariante}$
2. $F_{\mu\nu} \tilde{F}^{\mu\nu} = -\frac{4}{c} (\vec{E} \cdot \vec{B}) = \text{Invariante}$
