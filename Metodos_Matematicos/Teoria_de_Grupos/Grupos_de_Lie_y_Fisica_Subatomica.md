# Grupos de Lie y Simetrías Gauge

El Teorema de Noether (1915) estableció que cada simetría continua de la naturaleza implica una ley de conservación (Simetría traslacional $\to$ Conservación del Momento). En física de partículas moderna, la naturaleza fundamental de las fuerzas está dictada enteramente por la Teoría de Grupos de Lie.

## 1. Grupos de Lie
Un Grupo de Lie es un grupo matemático que también es una variedad diferenciable suave. Esto permite que el grupo actúe de manera continua.

Los elementos del grupo cercano a la identidad se pueden escribir exponencializando los generadores del álgebra de Lie (los operadores infinitesimales):

$$
U(\theta) = e^{i \theta_a T^a}
$$

Donde $T^a$ son los generadores del álgebra, que obedecen unas reglas de conmutación dadas por las constantes de estructura $f^{abc}$:

$$
[T^a, T^b] = i f^{abc} T^c
$$

## 2. El Modelo Estándar (SU(3) $\times$ SU(2) $\times$ U(1))
Las partículas de materia (fermiones) y sus interacciones se rigen por exigir que el Lagrangiano sea invariante (Simetría Gauge) bajo transformaciones locales de grupos de Lie específicos.

- **U(1) - Electromagnetismo:** Un grupo abeliano continuo (simetría circular de fase). Exigir invarianza local U(1) "fuerza" matemáticamente la existencia del Campo Electromagnético ($A_\mu$) y de la partícula bosónica conocida como fotón.
- **SU(2) - Fuerza Débil:** Un grupo no abeliano de matrices unitarias $2\times 2$ con determinante 1. Sus 3 generadores (Matrices de Pauli) exigen la existencia de 3 bosones mediadores ($W^+, W^-, Z^0$).
- **SU(3) - Cromodinámica Cuántica (QCD):** Matrices $3\times 3$. Gobierna la fuerza nuclear fuerte que une a los quarks dentro del protón. Sus 8 generadores (Matrices de Gell-Mann) requieren la existencia de 8 bosones mediadores (los gluones), que a su vez llevan carga de color y por tanto interactúan entre sí.

La unificación de la física moderna es, en esencia, la búsqueda de un Grupo de Lie más grande (como SU(5) o SO(10)) que contenga al Modelo Estándar como subgrupos en su interior (Grandes Teorías Unificadas, GUT).
