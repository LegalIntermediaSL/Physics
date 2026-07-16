# [CMA-10] Aislantes Topológicos y Estados de Borde (Edge States)

## 1. Introducción a la Topología en Materia Condensada
Un aislante topológico es un material con un *gap* de energía en su interior (bulk) que se comporta como un aislante ordinario, pero cuyos bordes (en 2D) o superficies (en 3D) albergan estados conductores protegidos por simetría de inversión temporal.

## 2. Invariante Topológico (Z2)
El carácter topológico se describe mediante el invariante $\nu \in \mathbb{Z}_2$:

$$
(-1)^\nu = \prod_i \delta_i
$$

donde $\delta_i$ son las paridades de las bandas ocupadas en los puntos de alta simetría (TRIM) de la zona de Brillouin. Si $\nu = 1$, el material es topológicamente no trivial.

## 3. Modelo de Kane-Mele
Describe el efecto Hall de espín cuántico en grafeno con acoplamiento espín-órbita.

$$
H = -t \sum_{\langle i,j \rangle, s} c_{i,s}^\dagger c_{j,s} + i \lambda_{SO} \sum_{\langle \langle i,j \rangle \rangle, s, s'} \nu_{ij} c_{i,s}^\dagger \sigma_{s s'}^z c_{j,s'}
$$

Este Hamiltoniano genera canales de conducción helicoidales en los bordes, inmunes a la retrodispersión (*backscattering*) no magnética.
