# Entropía y el Teorema de Fluctuación-Disipación

El concepto macroscópico de entropía adquiere un significado físico preciso cuando se analiza desde la mecánica estadística y la teoría de la información.

## 1. Definición Estadística de la Entropía
Ludwig Boltzmann conectó por primera vez la entropía termodinámica $S$ con el número de microestados accesibles $\Omega$ de un sistema aislado:

$$
S = k_B \ln \Omega
$$

Donde $k_B$ es la constante de Boltzmann.

Para un sistema que no está aislado y puede encontrarse en varios microestados $i$ con probabilidad $p_i$, la entropía generalizada de Gibbs (equivalente a la entropía de la información de Shannon) es:

$$
S = -k_B \sum_i p_i \ln p_i
$$

Si formulamos el sistema mediante una matriz densidad $\rho$ en mecánica cuántica, la entropía se generaliza como la entropía de von Neumann:

$$
S = -k_B \text{Tr}(\rho \ln \rho)
$$

## 2. Fluctuaciones Térmicas
Los sistemas termodinámicos en equilibrio no son estáticos; exhiben fluctuaciones microscópicas alrededor de sus valores medios.
Consideremos una magnitud macroscópica observable $X$. Si el sistema está descrito por la distribución canónica, la probabilidad de observar una fluctuación está regida por la relación de Einstein:

$$
p(X) \propto \exp\left( \frac{S(X)}{k_B} \right)
$$

Expandiendo la entropía en serie de Taylor alrededor del estado de equilibrio ($X = 0$, donde la entropía es máxima):

$$
S(X) \approx S(0) - \frac{1}{2} \beta X^2
$$

Esto produce una distribución de probabilidad Gaussiana para las fluctuaciones de variables extensivas en sistemas grandes.

## 3. Teorema de Fluctuación-Disipación
Este poderoso teorema vincula la respuesta de un sistema en equilibrio térmico frente a una pequeña perturbación externa (disipación) con sus fluctuaciones espontáneas internas (ruido) en ausencia de perturbación.
Si aplicamos un campo externo oscilante de frecuencia $\omega$, la energía disipada es proporcional a la parte imaginaria de la función de respuesta generalizada $\chi''(\omega)$.
El teorema de fluctuación-disipación establece que la función de correlación temporal del ruido observable en equilibrio, $S_X(\omega)$, satisface:

$$
S_X(\omega) = \frac{2 k_B T}{\omega} \chi''(\omega)
$$

El ejemplo más clásico es el ruido de Johnson-Nyquist en resistencias eléctricas, donde las fluctuaciones térmicas espontáneas de voltaje predicen exactamente la resistencia eléctrica del conductor.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Statistical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtj_3l8x1k-D1H_cMB-x162) - Colectivos microcanónicos y fluctuaciones cuánticas.
- [MIT 8.044: Statistical Physics I (Thomas J. Greytak)](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Enfoque riguroso termodinámico (disponible en OCW/YouTube).
