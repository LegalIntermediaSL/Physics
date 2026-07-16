# Dinámica No Lineal y Teoría del Caos

## 1. Definición y Conceptos Fundamentales
La dinámica no lineal estudia sistemas cuya evolución temporal obedece a ecuaciones diferenciales donde la superposición de soluciones no es válida. A diferencia de los sistemas lineales, donde las perturbaciones crecen proporcionalmente, un sistema no lineal puede presentar bifurcaciones, comportamiento caótico determinista y formación de estructuras disipativas.

Un sistema dinámico continuo autónomo se representa como:

$$
\frac{d\vec{x}}{dt} = \vec{f}(\vec{x})
$$

Donde $\vec{x} \in \mathbb{R}^n$ es el vector de estado en el espacio de fases y $\vec{f}$ es un campo vectorial no lineal. El comportamiento caótico estricto requiere que la dimensión del espacio de fases sea $n \ge 3$ para sistemas de tiempo continuo (por el Teorema de Poincaré-Bendixson).

## 2. Sensibilidad a las Condiciones Iniciales
La huella digital del caos es la divergencia exponencial de trayectorias infinitesimalmente cercanas. Si dos trayectorias inician con una separación inicial $\delta \vec{x}(0)$, la divergencia a un tiempo $t$ obedece:

$$
|\delta \vec{x}(t)| \approx |\delta \vec{x}(0)| e^{\lambda t}
$$

Donde $\lambda$ es el Exponente de Lyapunov máximo. Si $\lambda > 0$, el sistema es caótico; el horizonte de predictibilidad del sistema está dictado por $t \sim \frac{1}{\lambda} \ln\left(\frac{L}{|\delta \vec{x}(0)|}\right)$.

## 3. Mapas Discretos y Ecuaciones en Diferencias
En tiempo discreto, el caos puede manifestarse en dimensión 1 (ej. Mapeo Logístico). La iteración toma la forma:

$$
x_{n+1} = f(x_n)
$$

## 4. Teorema de KAM (Kolmogorov-Arnold-Moser)
En mecánica Hamiltoniana no lineal, sistemas integrables levemente perturbados no se vuelven inmediatamente ergódicos. Los toros invariantes del espacio de fases persisten para frecuencias inconmensurables "suficientemente irracionales", impidiendo la termalización inmediata.
