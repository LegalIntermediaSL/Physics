# Mecánica Estadística

La mecánica estadística proporciona el marco matemático subyacente de la termodinámica. Usa teoría de la probabilidad para deducir el comportamiento promedio del sistema a partir de sus microestados.

## Microestados y Macroestados
- **Microestado**: Una configuración exacta y detallada de un sistema (posición y momento de *todas* las partículas).
- **Macroestado**: Una descripción a nivel macroscópico (definido por $P$, $V$, $T$, $E$). Un macroestado puede ser realizado por una inmensa cantidad de microestados, denotada por $\Omega$.

## Entropía de Boltzmann
La ecuación fundamental grabada en la tumba de Boltzmann:
$ S = k_B \ln \Omega $
A mayor número de microestados (mayor "desorden"), mayor entropía.

## La Colectividad Canónica y la Función de Partición
Para un sistema en contacto térmico con un baño a temperatura $T$, la probabilidad $P_i$ de que el sistema esté en un microestado de energía $E_i$ es proporcional al factor de Boltzmann $e^{-\beta E_i}$ (donde $\beta = 1/k_B T$).

$ P_i = \frac{1}{Z} e^{-\beta E_i} $

**Función de Partición ($Z$)**:
$ Z = \sum_{i} e^{-\beta E_i} $
Conocida la función de partición, se pueden derivar todas las magnitudes termodinámicas del sistema (Energía interna, Entropía, Presión). Por ejemplo:
$ U = -\frac{\partial \ln Z}{\partial \beta} $
