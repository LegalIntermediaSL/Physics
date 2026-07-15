# Métricas, Conexiones y Curvatura

Para hacer física sobre una variedad, necesitamos medir distancias y comparar vectores en puntos distintos. Para ello introducimos dos estructuras geométricas vitales: el Tensor Métrico y la Conexión Afín.

## 1. El Tensor Métrico ($g_{\mu\nu}$)
El tensor métrico es un tensor simétrico de rango $(0,2)$ que define el producto escalar entre dos vectores tangentes. Dicta la noción de longitud y ángulo, y por ende, la distancia (intervalo) en el espacio-tiempo.

El elemento de línea invariante se define como:

$$
ds^2 = g_{\mu\nu} dx^\mu dx^\nu
$$

El tensor métrico también permite "subir y bajar índices" (isomorfismo musical entre el espacio tangente y cotangente):

$$
V_\mu = g_{\mu\nu} V^\nu
$$

## 2. Derivada Covariante y Conexión ($\Gamma^\rho_{\mu\nu}$)
En un espacio curvo, la derivada parcial ordinaria de un tensor no resulta en un tensor, debido a que la base vectorial cambia de un punto a otro. Para corregir esto, introducimos la Derivada Covariante $\nabla$.

Para un vector contravariante $V^\mu$:

$$
\nabla_\nu V^\mu = \partial_\nu V^\mu + \Gamma^\mu_{\nu\lambda} V^\lambda
$$

El término $\Gamma^\mu_{\nu\lambda}$ son los **Símbolos de Christoffel** (o conexión de Levi-Civita). Representan cómo giran y se contraen los vectores de la base al moverse por la variedad. Si exigimos que la derivada covariante de la métrica sea nula ($\nabla_\lambda g_{\mu\nu} = 0$), la conexión queda fijada unívocamente por la métrica.

## 3. Tensor de Curvatura de Riemann ($R^\rho_{\sigma\mu\nu}$)
La curvatura intrínseca de la variedad se mide transportando paralelamente un vector alrededor de un lazo cerrado infinitesimal. Si la variedad es plana (espacio de Minkowski), el vector vuelve idéntico. Si es curva, el vector rota.

Esta rotación está cuantificada por el conmutador de derivadas covariantes:

$$
[\nabla_\mu, \nabla_\nu] V^\rho = R^\rho_{\sigma\mu\nu} V^\sigma
$$

El tensor de Riemann codifica todo sobre las fuerzas de marea gravitacionales en la Relatividad General de Einstein.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Carl Bender: Mathematical Physics (Washington University)](https://www.youtube.com/playlist?list=PL1B1123DDB9DD4668) - Brillantes clases de perturbaciones, asintóticos y WKB impartidas por un genio del análisis.
- [ICTP: Mathematics for Physicists](https://www.youtube.com/user/ictp) - Herramientas analíticas puras desde Trieste.
