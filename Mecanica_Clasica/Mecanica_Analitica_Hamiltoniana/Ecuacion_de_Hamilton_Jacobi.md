# La Ecuación de Hamilton-Jacobi

La meta de este formalismo es encontrar una Transformación Canónica maestra $(q, p) \to (Q, P)$ tal que el nuevo Hamiltoniano transformado ($K$) sea idénticamente cero, logrando que el problema quede trivialmente resuelto.

## 1. La Función Generatriz de Hamilton
Para que el nuevo Hamiltoniano se anule ($K = 0$), las nuevas ecuaciones canónicas exigen que $\dot{Q}_i = 0$ y $\dot{P}_i = 0$. Por lo tanto, todas las nuevas variables ($Q_i, P_i$) son constantes de movimiento puras dictadas por las condiciones iniciales.
Buscamos una Función Generatriz dependiente de las coordenadas espaciales antiguas y los nuevos momentos constantes formales. A esta función se le llama **Función Principal de Hamilton ($S(q, P, t)$)**.

La relación de transformación canónica exige que $K = H + \frac{\partial S}{\partial t}$. Imponiendo $K = 0$, obtenemos la relación central:

$$
H(q, p, t) + \frac{\partial S}{\partial t} = 0
$$

## 2. Derivación de la EDP de Hamilton-Jacobi
Dado que la función generatriz relaciona los momentos antiguos como $p_i = \frac{\partial S}{\partial q_i}$, al sustituir esto en la ecuación anterior obtenemos la **Ecuación Diferencial en Derivadas Parciales de Hamilton-Jacobi**:

$$
H\left( q_1, \dots, q_n, \frac{\partial S}{\partial q_1}, \dots, \frac{\partial S}{\partial q_n}, t \right) + \frac{\partial S}{\partial t} = 0
$$

Para un sistema conservativo ($H$ no depende del tiempo), la función se separa como: $S(q, P, t) = W(q, P) - E t$, donde $E$ es la energía total constante y $W$ es la **Función Característica de Hamilton**. La EDP se reduce a:

$$
H\left( q, \frac{\partial W}{\partial q} \right) = E
$$

La relevancia de la ecuación de Hamilton-Jacobi radica en ser el puente matemático directo con la mecánica cuántica. Al sustituir la función $S$ en la fase de una onda eikonal ($\Psi \sim e^{iS/\hbar}$), se recupera de manera asintótica la ecuación de onda de Schrödinger.

## 📺 Clases Magistrales en YouTube

Si deseas profundizar en estos conceptos con los mejores profesores del mundo, aquí tienes algunas clases magistrales gratuitas recomendadas:

- [Stanford: Theoretical Minimum - Classical Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PL47F408D36D615022) - El Lagrangiano, Hamiltoniano y el Principio de Mínima Acción desmitificados.
- [MIT 8.01: Classical Mechanics (Walter Lewin)](https://www.youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e) - Física newtoniana icónica.
