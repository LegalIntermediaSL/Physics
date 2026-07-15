# Teoría de Cuerdas Bosónica y Supercuerdas

El pilar fundacional de la teoría de cuerdas es el reemplazo de partículas puntuales 0-dimensionales por hilos vibrantes 1-dimensionales.

## 1. La Acción de Nambu-Goto y Polyakov
Mientras que una partícula puntual traza una **Línea de Universo** $1D$ y minimiza su longitud inercial $S = -m \int ds$, una cuerda cerrada o abierta traza una **Hoja de Universo (Worldsheet)** bidimensional parametrizada por $(\sigma, \tau)$.
El principio de mínima acción estipula que la dinámica clásica de la cuerda minimiza el área del Worldsheet. Esta es la **Acción de Nambu-Goto**:

$$
S_{NG} = -T \int d^2\sigma \sqrt{-\det(h_{ab})}
$$

Donde $T = \frac{1}{2\pi\alpha'}$ es la tensión de la cuerda y $h_{ab} = \partial_a X^\mu \partial_b X^\nu \eta_{\mu\nu}$ es la métrica inducida.

Para facilitar la cuantización (Path Integral), pasamos a la **Acción de Polyakov**, clásicamente equivalente pero que evita la raíz cuadrada introduciendo una métrica intrínseca auxiliar $h_{ab}(\sigma,\tau)$:

$$
S_P = -\frac{T}{2} \int d^2\sigma \sqrt{-h} h^{ab} \partial_a X^\mu \partial_b X_\mu
$$

## 2. Álgebra de Virasoro y Anomalía Conforme
La simetría residual en el Worldsheet permite fijar el gauge conforme ($h_{ab} = \eta_{ab}$). Los vínculos dinámicos $T_{ab} = 0$ (Tensor de Energía-Momento del Worldsheet) dictan la cinemática.
Al cuantizar, estos vínculos se convierten en los generadores del álgebra de **Virasoro** ($L_n$):

$$
[L_m, L_n] = (m - n) L_{m+n} + \frac{c}{12} m(m^2 - 1) \delta_{m+n, 0}
$$

El término $c$ es la anomalía central. Para que la teoría sea cuánticamente consistente y evite probabilidades negativas (estados fantasma), la anomalía total (Materia + Fantasmas) debe cancelarse a cero. Esto fuerza al espaciotiempo exterior a tener **$D = 26$** dimensiones para la cuerda puramente bosónica.

## 3. Supercuerdas y Condición GSO
Dado que la cuerda bosónica carece de fermiones y su estado fundamental es inestable (un taquión con $M^2 < 0$), se introduce supersimetría en el Worldsheet acoplando un campo espinorial $\psi^\mu$.
Esto altera la anomalía central, fijando la dimensión crítica a **$D = 10$**.
Implementando la proyección matemática **GSO** (Gliozzi-Scherk-Olive), truncamos el espectro eliminando el taquión. El primer estado excitado de la cuerda cerrada contiene obligatoriamente un tensor simétrico sin traza: **El Gravitón ($g_{\mu\nu}$)**. La gravedad queda naturalmente incluida.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: String Theory and M-Theory (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAul6f91XgBv0W2c8B2O9Eic) - Introducción accesible a dimensiones extra y bosones vibrantes.
- [Perimeter Institute: Quantum Gravity](https://www.youtube.com/user/PIOutreach) - Clases magistrales sobre gravedad cuántica de lazos (LQG) y holografía (AdS/CFT).
