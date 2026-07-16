# [NLD-12] Dinámica Neuronal y el Modelo de Hodgkin-Huxley

## 1. Potencial de Membrana
La membrana de la neurona actúa como un condensador $C_m$, y los canales iónicos como resistencias variables o conductancias $g_i$.
La ecuación fundamental del circuito biofísico de la membrana establece que la suma de corrientes capacitivas, de iones ($Na^+, K^+$) y de fuga ($L$) iguala a la corriente inyectada $I_{ext}$:

$$
C_m \frac{dV}{dt} = I_{ext} - \bar{g}_{Na} m^3 h (V - E_{Na}) - \bar{g}_K n^4 (V - E_K) - \bar{g}_L (V - E_L)
$$

## 2. Variables de Activación y Compuertas
A diferencia de los circuitos pasivos, los canales tienen compuertas de voltaje que abren y cierran con dinámicas no lineales. Las probabilidades de apertura $m, h, n$ siguen ecuaciones diferenciales de primer orden:

$$
\frac{dx}{dt} = \alpha_x(V)(1-x) - \beta_x(V)x \quad \text{para } x \in \{m,h,n\}
$$
Este sistema rígido es el motor del "Potencial de Acción" o disparo eléctrico del cerebro.
