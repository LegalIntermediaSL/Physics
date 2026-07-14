# Variedades Diferenciables y Campos Tensoriales

La física moderna (especialmente la Relatividad General y las Teorías de Campo Gauge) está formulada en el lenguaje de la geometría diferencial. El espacio-tiempo no es un fondo plano euclidiano, sino una **variedad diferenciable** curva.

## 1. Variedades Diferenciables ($\mathcal{M}$)
Una variedad diferenciable de dimensión $n$ es un espacio topológico que localmente se parece a $\mathbb{R}^n$. Esto significa que podemos cubrir la variedad con "parches" (cartas locales) donde podemos usar coordenadas reales $(x^1, ..., x^n)$. Las funciones de transición entre parches superpuestos deben ser suaves (infinitamente diferenciables o $C^\infty$).

## 2. El Espacio Tangente ($T_p\mathcal{M}$)
En cada punto $p$ de la variedad, existe un espacio vectorial de la misma dimensión llamado Espacio Tangente. Los vectores tangentes no son "flechas" en el espacio, sino **operadores de derivada direccional** sobre funciones suaves.

Una base del espacio tangente viene dada por las derivadas parciales respecto a las coordenadas locales:

$$
\mathbf{e}_\mu = \frac{\partial}{\partial x^\mu}
$$

Un vector $V$ se escribe como $V = V^\mu \partial_\mu$.

## 3. Formas Diferenciales y el Espacio Cotangente ($T^*_p\mathcal{M}$)
El espacio dual al espacio tangente es el espacio cotangente. Sus elementos se llaman $1$-formas. Mapean vectores a números reales.

La base del espacio cotangente está formada por los diferenciales de las coordenadas:

$$
dx^\mu (\partial_\nu) = \delta^\mu_\nu
$$

Una $1$-forma $\omega$ se escribe como $\omega = \omega_\mu dx^\mu$.

## 4. Tensores
Un tensor de tipo $(p,q)$ en un punto $p$ es una función multilineal que toma $p$ covectores ($1$-formas) y $q$ vectores y devuelve un número real.

$$
T = T^{\mu_1 ... \mu_p}_{\nu_1 ... \nu_q} \frac{\partial}{\partial x^{\mu_1}} \otimes ... \otimes \frac{\partial}{\partial x^{\mu_p}} \otimes dx^{\nu_1} \otimes ... \otimes dx^{\nu_q}
$$

Las leyes de transformación tensorial garantizan que las ecuaciones físicas escritas con tensores sean verdaderas para cualquier observador, independientemente de su sistema de coordenadas (Covariancia General).
