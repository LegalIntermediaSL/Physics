# Emisión de Radiación (Larmor y Abraham-Lorentz)

## 1. La Fórmula de Larmor
Cuando una partícula con carga $q$ es acelerada de forma no-relativista ($v \ll c$), radia energía hacia el infinito. La potencia electromagnética total radiada en todas las direcciones se obtiene integrando el vector de Poynting del campo de radiación de Liénard-Wiechert, resultando en la histórica **Fórmula de Larmor**:

$$
P = \frac{\mu_0 q^2 a^2}{6\pi c}
$$

Donde $a$ es la magnitud de la aceleración.

## 2. Generalización de Liénard
Si la partícula es relativista (su $\gamma$ es grande), la radiación no es isotrópica; se colima bruscamente hacia adelante formando un cono estrecho tipo láser (Radiación Sincrotrón). La potencia generalizada relativista (invariante de Lorentz) es:

$$
P = -\frac{\mu_0 q^2 c}{6\pi} \left( \frac{dp^\mu}{d\tau} \frac{dp_\mu}{d\tau} \right) = \frac{\mu_0 q^2 \gamma^6}{6\pi c} \left( a^2 - \frac{(\vec{v} \times \vec{a})^2}{c^2} \right)
$$

## 3. Fuerza de Fricción de Radiación (Abraham-Lorentz)
Si una carga emite energía en forma de luz debido a la aceleración, por conservación de energía, la carga debe sentir un retroceso físico, una fuerza de freno.
Max Abraham y Hendrik Lorentz derivaron la fuerza de auto-interacción (fricción de radiación) requerida para compensar la energía perdida por Larmor:

$$
\vec{F}_{rad} = \frac{\mu_0 q^2}{6\pi c} \dot{\vec{a}}
$$

Donde $\dot{\vec{a}}$ (el tirón, jerk o *jolt*) es la derivada temporal de la aceleración.

## 4. Problemas Filosóficos y Preaceleración
La Ecuación de Newton generalizada queda como $m\vec{a} = \vec{F}_{ext} + \vec{F}_{rad}$. Como $\vec{F}_{rad}$ depende de $\dot{a}$ (derivada tercera de la posición), genera **Soluciones Exponenciales Runaway** (la partícula acelera espontáneamente al infinito sin fuerzas).

Además, implica una ruptura de la causalidad: la carga comienza a acelerar *antes* de que una fuerza externa se aplique (Pre-aceleración). Esto delata que la electrodinámica clásica falla al nivel cuántico del tamaño del electrón.
