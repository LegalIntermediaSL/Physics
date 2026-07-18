# [BIO-05] Sincronización Neural y Redes de Osciladores

## 1. Ritmos Colectivos del Cerebro
El cerebro no opera como una suma de neuronas aisladas. Grandes poblaciones pueden sincronizarse y producir ritmos coherentes, desde bandas theta y gamma hasta oscilaciones patológicas asociadas a epilepsia o temblores.

## 2. De Neuronas a Fases
Cuando el detalle microscópico no es esencial, una población oscilante puede aproximarse por variables de fase $\theta_i$ con acoplamiento:

$$
\frac{d\theta_i}{dt}
=
\omega_i
+
\frac{K}{N}
\sum_{j=1}^{N}
\sin(\theta_j - \theta_i)
$$

como en el modelo de Kuramoto. Aquí $\omega_i$ son frecuencias naturales y $K$ mide el acoplamiento efectivo.

## 3. Transición a la Coherencia
Cuando el acoplamiento supera un umbral, emerge un orden colectivo medido por el parámetro

$$
re^{i\psi}
=
\frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j}
$$

Si $r \approx 0$, la población está descoordinada; si $r \approx 1$, la actividad es casi perfectamente sincronizada.

## 4. Retrasos, Ruido y Arquitectura
En redes biológicas reales, la sincronización depende de:

- tiempos finitos de transmisión,
- heterogeneidad neuronal,
- ruido sináptico,
- topología de conectividad,
- acoplamientos excitadores e inhibidores.

Esto produce fenómenos como clusters, quimeras, locking parcial y ondas viajeras.

## 5. Relevancia Biofísica
La sincronización es funcional en atención, memoria de trabajo y coordinación sensoriomotora, pero también puede volverse patológica. La física de osciladores permite estudiar ambos escenarios dentro de un mismo marco matemático.
