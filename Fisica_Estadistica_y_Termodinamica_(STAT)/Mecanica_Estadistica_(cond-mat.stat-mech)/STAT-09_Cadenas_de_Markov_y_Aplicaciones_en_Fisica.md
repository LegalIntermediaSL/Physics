# [STAT-09] Cadenas de Markov y Aplicaciones en Física

## 1. Qué es una Cadena de Markov
Una **cadena de Markov** es un proceso estocástico en el que la probabilidad del siguiente estado depende solo del estado presente y no de toda la historia previa. Esta propiedad se conoce como **falta de memoria** o propiedad de Markov:

$$
P(X_{n+1}=j \mid X_n=i, X_{n-1}, \dots, X_0)
=
P(X_{n+1}=j \mid X_n=i)
$$

En física, esta hipótesis aparece de manera natural cuando las variables microscópicas relevantes se mezclan tan rápido que el sistema puede describirse efectivamente por transiciones entre estados macroscópicos o mesoscópicos.

## 2. Matriz de Transición
Si el espacio de estados es discreto, la dinámica queda determinada por una **matriz de transición** $P$ cuyas entradas

$$
P_{ij} = P(X_{n+1}=j \mid X_n=i)
$$

deben satisfacer

$$
P_{ij} \ge 0,
\qquad
\sum_j P_{ij} = 1
$$

para cada estado $i$. Si el vector de probabilidades en el tiempo $n$ es $\boldsymbol{\pi}^{(n)}$, entonces

$$
\boldsymbol{\pi}^{(n+1)} = \boldsymbol{\pi}^{(n)} P
$$

y, tras $n$ pasos,

$$
\boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}^{(0)} P^n
$$

La potencia de la matriz codifica toda la evolución estadística del sistema.

## 3. Distribución Estacionaria y Equilibrio
Un objeto central es la **distribución estacionaria** $\boldsymbol{\pi}^{*}$, definida por

$$
\boldsymbol{\pi}^{*} P = \boldsymbol{\pi}^{*}
$$

Si la cadena es irreducible y aperiódica, esta distribución suele ser única y el sistema converge hacia ella desde un conjunto amplio de condiciones iniciales.

En física estadística, la distribución estacionaria suele coincidir con el equilibrio térmico o con un estado estacionario fuera del equilibrio. Cuando además se cumple **equilibrio detallado**,

$$
\pi_i^{*} P_{ij} = \pi_j^{*} P_{ji}
$$

no hay corriente neta entre pares de estados en el régimen estacionario. Esta condición es fundamental en muchos algoritmos de Monte Carlo y en modelos reversibles de equilibrio.

## 4. Del Tiempo Discreto a la Ecuación Maestra
Muchas aplicaciones físicas se formulan en tiempo continuo. En ese caso se usan tasas de transición $W_{ij}$ y la evolución de las probabilidades viene dada por la **ecuación maestra**:

$$
\frac{dP_i}{dt}
=
\sum_j \left[ W_{ji} P_j - W_{ij} P_i \right]
$$

La interpretación es simple: el cambio de probabilidad de estar en el estado $i$ es la diferencia entre el flujo entrante y el flujo saliente. Esta ecuación unifica una enorme variedad de problemas físicos: difusión, cinética química, relajación de espines, procesos de nacimiento-muerte y transporte estocástico.

## 5. Aplicación 1: Caminatas Aleatorias y Difusión
La caminata aleatoria es el ejemplo más clásico de proceso markoviano. Una partícula que en cada paso se mueve a derecha o izquierda con cierta probabilidad define una cadena de Markov sobre la red espacial.

Aunque la dinámica microscópica es discreta y probabilística, en el límite de muchas colisiones y pasos pequeños emerge la ecuación de difusión:

$$
\frac{\partial \rho}{\partial t} = D \nabla^2 \rho
$$

Este puente entre caminatas aleatorias y difusión es una de las ideas más profundas de la física estadística: un proceso local, ciego y sin memoria produce leyes macroscópicas suaves e irreversibles.

## 6. Aplicación 2: Monte Carlo en Mecánica Estadística
Las cadenas de Markov son la base de los algoritmos **Markov Chain Monte Carlo** (MCMC), esenciales para estudiar sistemas con muchos grados de libertad. En el modelo de Ising, por ejemplo, no se enumeran todas las configuraciones posibles, porque su número crece exponencialmente. En su lugar, se genera una cadena de configuraciones

$$
\sigma^{(0)} \to \sigma^{(1)} \to \sigma^{(2)} \to \cdots
$$

de forma que la distribución estacionaria sea la de Boltzmann:

$$
\pi(\sigma) \propto e^{-\beta E(\sigma)}
$$

El algoritmo de Metropolis-Hastings acepta o rechaza cambios elementales con probabilidad

$$
A(i \to j) = \min\left(1, e^{-\beta (E_j - E_i)}\right)
$$

cuando la propuesta es simétrica. Así, la cadena explora el espacio de configuraciones respetando equilibrio detallado y permite estimar promedios térmicos como magnetización, energía o calor específico.

## 7. Aplicación 3: Cinética de Estados y Relajación
Muchos sistemas físicos complejos pueden aproximarse como saltos entre estados metastables: conformaciones moleculares, niveles excitados, pozos de potencial o dominios magnéticos. En estos casos, una cadena de Markov proporciona una descripción efectiva muy poderosa.

Ejemplos típicos incluyen:

- relajación de poblaciones entre niveles cuánticos,
- dinámica conformacional de proteínas,
- transporte entre trampas energéticas,
- procesos de activación térmica entre mínimos de un paisaje libre.

La ventaja del enfoque markoviano es que separa dos escalas: el movimiento microscópico rápido dentro de cada estado y los saltos lentos entre estados.

## 8. Aplicación 4: Procesos Fuera del Equilibrio
Cuando no se cumple equilibrio detallado, pueden existir corrientes estacionarias no nulas. Esto es común en materia activa, motores moleculares, transporte en redes, sistemas biológicos y modelos de conducción.

En estos casos, la cadena de Markov sigue siendo válida, pero la distribución estacionaria ya no representa un equilibrio termodinámico. En cambio, describe un **estado estacionario fuera del equilibrio**, donde hay producción continua de entropía y flujos mantenidos por fuentes externas.

## 9. Por Qué Importan en Física
Las cadenas de Markov son tan importantes porque conectan cuatro niveles de descripción:

- azar microscópico,
- evolución probabilística mesoscópica,
- leyes macroscópicas emergentes,
- y algoritmos numéricos prácticos.

No son solo una herramienta matemática; son un lenguaje para describir cómo la incertidumbre local se organiza en comportamiento físico observable.

## 10. Idea Final
Desde una partícula browniana hasta una simulación de Monte Carlo, desde una reacción química hasta la relajación de un sistema cuántico abierto, las cadenas de Markov aparecen una y otra vez como el marco mínimo que permite introducir dinámica, probabilidad y flecha temporal de forma controlada. Por eso ocupan un lugar central en la física moderna, tanto teórica como computacional.
