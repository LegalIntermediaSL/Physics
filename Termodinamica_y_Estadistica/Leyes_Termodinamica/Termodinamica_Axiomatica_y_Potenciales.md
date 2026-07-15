# Termodinámica Axiomática y Potenciales Termodinámicos

La termodinámica clásica puede formularse rigurosamente a partir de axiomas matemáticos sobre el equilibrio y las transiciones de estado, independientemente de la naturaleza microscópica de la materia.

## 1. Primer y Segundo Principio
El **Primer Principio** postula la existencia de una función de estado llamada Energía Interna ($U$), cuya variación en un sistema cerrado es igual a la suma del calor absorbido ($Q$) y el trabajo realizado sobre el sistema ($W$):

$$
dU = \delta Q + \delta W
$$

El diferencial $dU$ es exacto, mientras que $\delta Q$ y $\delta W$ dependen de la trayectoria del proceso.

El **Segundo Principio**, en su formulación de Clausius, estipula que el calor no fluye espontáneamente de un cuerpo frío a uno caliente. Matemáticamente, esto implica la existencia de un factor integrante $1/T$ para el calor reversible, definiendo la **Entropía ($S$)**:

$$
dS = \frac{\delta Q_{\text{rev}}}{T}
$$

Para cualquier proceso real (irreversible), se cumple la desigualdad de Clausius: $dS \geq \delta Q / T$.

## 2. Ecuación Fundamental
Combinando ambos principios para un sistema hidrostático reversible donde $\delta W = -P dV$, obtenemos la Ecuación Fundamental de la Termodinámica:

$$
dU = T dS - P dV
$$

Aquí, $U$ es una función de sus variables naturales: la entropía $S$ y el volumen $V$. Las derivadas parciales definen las variables conjugadas intensivas:

$$
T = \left( \frac{\partial U}{\partial S} \right)_V, \quad P = -\left( \frac{\partial U}{\partial V} \right)_S
$$

## 3. Transformadas de Legendre y Potenciales Termodinámicos
A menudo es difícil controlar experimentalmente la entropía $S$ o el volumen $V$. Para describir el sistema en términos de variables controlables (como $T$ o $P$), aplicamos transformadas de Legendre sobre la energía interna $U$.

- **Entalpía ($H$)**: Útil para procesos a presión constante.
  

$$
H = U + PV \implies dH = T dS + V dP
$$

- **Energía Libre de Helmholtz ($F$)**: Útil para procesos a temperatura y volumen constantes.
  

$$
F = U - TS \implies dF = -S dT - P dV
$$

- **Energía Libre de Gibbs ($G$)**: Fundamental en química, ideal para procesos a temperatura y presión constantes.
  

$$
G = H - TS = U + PV - TS \implies dG = -S dT + V dP
$$

En el equilibrio, un sistema mantenido a temperatura y presión constantes minimizará espontáneamente su Energía Libre de Gibbs ($dG \leq 0$).

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Statistical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtj_3l8x1k-D1H_cMB-x162) - Colectivos microcanónicos y fluctuaciones cuánticas.
- [MIT 8.044: Statistical Physics I (Thomas J. Greytak)](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Enfoque riguroso termodinámico (disponible en OCW/YouTube).
