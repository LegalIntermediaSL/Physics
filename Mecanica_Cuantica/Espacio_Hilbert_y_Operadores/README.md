# Espacio de Hilbert y Operadores

La formulación matemática rigurosa de la mecánica cuántica fue desarrollada por Paul Dirac y John von Neumann.

## Espacios de Hilbert
Los estados cuánticos se representan como "vectores" de estado ($|\psi\rangle$) en un espacio vectorial complejo infinito-dimensional llamado Espacio de Hilbert.
- **Notación Bra-Ket (Dirac)**:
El estado se denota como un "ket" $|\psi\rangle$. Su dual transpuesto conjugado es un "bra" $\langle\psi|$. 
El producto interno $\langle\phi|\psi\rangle$ es un número complejo relacionado con las probabilidades de transición.

## Observables como Operadores Hermíticos
Las magnitudes medibles de la física clásica (posición, momento, energía) son reemplazadas por operadores lineales hermíticos ($\hat{A}$).
- **Valores posibles**: Los únicos resultados que podemos obtener de una medición son los autovalores ($a_n$) de dicho operador: $\hat{A}|a_n\rangle = a_n|a_n\rangle$.
- **Colapso de la función de onda**: Al medir, el sistema "salta" a uno de esos autoestados con una probabilidad $|\langle a_n | \psi \rangle|^2$.

## Principio de Incertidumbre Generalizado
Para dos observables correspondientes a operadores $\hat{A}$ y $\hat{B}$ que no conmutan (es decir, el conmutador $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A} \neq 0$), no se pueden medir simultáneamente con precisión arbitraria:
$ \Delta A \Delta B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle| $
Para posición ($\hat{x}$) y momento ($\hat{p}$), su conmutador es $i\hbar$, recuperando la famosa relación de Heisenberg:
$ \Delta x \Delta p \ge \frac{\hbar}{2} $
