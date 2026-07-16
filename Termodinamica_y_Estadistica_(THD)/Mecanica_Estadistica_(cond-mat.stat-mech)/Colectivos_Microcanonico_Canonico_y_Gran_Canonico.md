# Ensambles Estadísticos: Microcanónico, Canónico y Gran Canónico

El objetivo de la mecánica estadística es derivar el comportamiento macroscópico (termodinámica) a partir del análisis probabilístico de un gran número de constituyentes microscópicos. Para ello, Willard Gibbs introdujo el concepto de **Ensamble**: una colección idealizada de un número infinito de copias del sistema, distribuidas sobre todos los microestados posibles.

## 1. El Ensamble Microcanónico (Energía Aislada)
Describe un sistema rigurosamente aislado del entorno. Por tanto, su energía $E$, volumen $V$ y número de partículas $N$ son fijos.
El **Postulado Fundamental de la Mecánica Estadística** afirma que un sistema aislado en equilibrio térmico tiene la misma probabilidad de encontrarse en cualquiera de sus microestados accesibles $\Omega(E, V, N)$.

$$
p_i = \begin{cases} \frac{1}{\Omega} & \text{si } E_i = E \\ 0 & \text{en otro caso} \end{cases}
$$

La termodinámica se recupera usando la relación de Boltzmann: $S = k_B \ln \Omega$. La temperatura se define estadísticamente como $\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N}$.

## 2. El Ensamble Canónico (Intercambio Térmico)
Describe un sistema con volumen $V$ y número de partículas $N$ fijos, pero sumergido en un baño térmico mucho mayor a temperatura $T$. El sistema puede intercambiar energía con el baño, por lo que su energía $E_i$ fluctúa.
La probabilidad de encontrar al sistema en un microestado específico $i$ con energía $E_i$ decae exponencialmente según el **Factor de Boltzmann**:

$$
p_i = \frac{1}{Z} e^{-\beta E_i}
$$

Donde $\beta = \frac{1}{k_B T}$. 
La constante de normalización $Z$ es la **Función de Partición Canónica**:

$$
Z(T, V, N) = \sum_i e^{-\beta E_i}
$$

La función de partición contiene toda la información mecánica y estadística del sistema. Nos permite conectar directamente el mundo microscópico con la variable macroscópica del Energía Libre de Helmholtz:

$$
F = -k_B T \ln Z
$$

## 3. El Gran Ensamble Canónico (Sistemas Abiertos)
Describe un sistema que puede intercambiar tanto energía como partículas con un reservorio externo. Ahora el volumen $V$, la temperatura $T$ y el potencial químico $\mu$ están fijos. El número de partículas $N_i$ fluctúa.
La probabilidad de ocupar un microestado específico es:

$$
p_i = \frac{1}{\mathcal{Z}} e^{-\beta (E_i - \mu N_i)}
$$

La normalización $\mathcal{Z}$ es la **Gran Función de Partición**:

$$
\mathcal{Z}(T, V, \mu) = \sum_{N=0}^{\infty} \sum_i e^{-\beta (E_{i,N} - \mu N)}
$$

La termodinámica se extrae a través del Gran Potencial Termodinámico $\Phi = -PV$:

$$
\Phi = -k_B T \ln \mathcal{Z}
$$

Este ensamble es indispensable para derivar las estadísticas cuánticas (Bose y Fermi), donde el número de partículas en cada estado cuántico particular fluctúa abiertamente.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Statistical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtj_3l8x1k-D1H_cMB-x162) - Colectivos microcanónicos y fluctuaciones cuánticas.
- [MIT 8.044: Statistical Physics I (Thomas J. Greytak)](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Enfoque riguroso termodinámico (disponible en OCW/YouTube).
