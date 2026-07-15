# Postulados y el Espacio de Hilbert

La Mecánica Cuántica no es una teoría sobre ondas físicas clásicas; es una teoría geométrica sobre vectores abstractos que rotan en un espacio vectorial complejo de infinitas dimensiones. Este marco fue codificado matemáticamente por Paul Dirac y John von Neumann.

## 1. El Estado Cuántico (El Ket)
Todo sistema físico está completamente descrito por un vector de estado, denominado **Ket** $|\psi\rangle$, que pertenece a un Espacio de Hilbert complejo separable $\mathcal{H}$. 
El producto interno (overlap) entre dos estados define el **Bra-Ket** $\langle \phi | \psi \rangle$, el cual es una amplitud de probabilidad compleja. La norma debe ser unitaria: $\langle \psi | \psi \rangle = 1$.

## 2. Los Observables como Operadores Hermitianos
En la física clásica, propiedades como la Posición ($x$) o el Momento ($p$) son simples números reales. En cuántica, son matrices u **Operadores Hermitianos** $\hat{A}$ ($\hat{A} = \hat{A}^\dagger$).
El resultado de una medición ideal *solo* puede ser uno de los autovalores reales $a_n$ del operador, resolviendo la ecuación de autovalores:

$$
\hat{A} |a_n\rangle = a_n |a_n\rangle
$$

Donde los autovectores $|a_n\rangle$ forman una base ortonormal completa de $\mathcal{H}$.

## 3. La Regla de Born y el Colapso (Proyección)
La mecánica cuántica es inherentemente probabilística. La probabilidad de medir el valor $a_n$ estando en el estado $|\psi\rangle$ es el cuadrado del valor absoluto de la amplitud de proyección:

$$
P(a_n) = |\langle a_n | \psi \rangle|^2
$$

Inmediatamente después de la medición, si el resultado fue $a_n$, el estado del universo colapsa abrupta y discontinuamente hacia el autovector correspondiente: $|\psi\rangle \to |a_n\rangle$.

## 4. El Principio de Incertidumbre de Heisenberg Generalizado
Si dos operadores no conmutan ($[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A} \neq 0$), son variables incompatibles; no pueden tener valores definidos simultáneamente. La varianza estadística de sus mediciones en cualquier estado está obligada por el teorema de Robertson:

$$
\sigma_A^2 \sigma_B^2 \geq \left( \frac{1}{2i} \langle [\hat{A}, \hat{B}] \rangle \right)^2
$$

Para posición y momento ($[\hat{x}, \hat{p}] = i\hbar$), esto arroja la famosa $\sigma_x \sigma_p \geq \hbar/2$.
