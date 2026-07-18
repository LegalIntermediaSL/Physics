# [BIO-04] Potenciales de Acción y Modelo Hodgkin-Huxley

## 1. La Neurona como Sistema Excitable
Una neurona transforma pequeñas corrientes iónicas en pulsos eléctricos abruptos llamados **potenciales de acción**. Desde la física, esto convierte a la membrana en un sistema no lineal excitado por corrientes externas y por el estado de sus canales iónicos.

## 2. Circuito Biofísico de la Membrana
La membrana se modela como un condensador $C_m$ en paralelo con conductancias dependientes del voltaje. La ecuación principal es

$$
C_m \frac{dV}{dt}
=
I_{ext}
- \bar g_{Na} m^3 h (V - E_{Na})
- \bar g_K n^4 (V - E_K)
- \bar g_L (V - E_L)
$$

donde $V$ es el potencial de membrana y $m,h,n$ describen compuertas de apertura y cierre.

## 3. Variables de Compuerta
Cada variable obedece una cinética de relajación:

$$
\frac{dx}{dt} = \alpha_x(V)(1-x) - \beta_x(V)x
\qquad x \in \{m,h,n\}
$$

La no linealidad de estas ecuaciones produce umbral, disparo regenerativo y periodo refractario.

## 4. Excitabilidad y Bifurcaciones
El disparo neuronal puede interpretarse mediante teoría de bifurcaciones: al variar una corriente o un parámetro de compuerta, el sistema pasa de un punto fijo estable a oscilaciones límite. Esta lectura conecta neurociencia con sistemas dinámicos, osciladores no lineales y teoría de estabilidad.

## 5. Reducciones Efectivas
Modelos como FitzHugh-Nagumo, Morris-Lecar o integrate-and-fire capturan rasgos esenciales con menos variables. Son muy útiles para estudiar poblaciones grandes, sincronización y codificación temporal sin la carga completa de Hodgkin-Huxley.

## 6. Alcance del Modelo
El valor del modelo no es solo fisiológico: muestra cómo un circuito microscópico con ruido térmico y canales discretos produce una dinámica macroscópica robusta, reproducible y altamente no lineal.
