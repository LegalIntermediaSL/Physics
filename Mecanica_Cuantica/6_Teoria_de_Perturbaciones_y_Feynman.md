# Teoría de Perturbaciones e Integrales de Camino

Salvo para el oscilador armónico y el átomo de hidrógeno, la Ecuación de Schrödinger es un monstruo diferencial imposible de resolver analíticamente. Para resolver problemas físicos reales, los físicos usamos dos enfoques colosales: las Perturbaciones y el formalismo de Feynman.

## 1. Teoría de Perturbaciones (Independiente del Tiempo)
Supón un sistema exacto $H_0$ (ej: átomo de hidrógeno) al que le aplicas un pequeño campo magnético externo $V$ (Efecto Zeeman). El Hamiltoniano real es $H = H_0 + \lambda V$.
Asumiendo que $\lambda$ es un parámetro pequeño, expandimos la energía desconocida y el estado en series de Taylor:
- La corrección de primer orden a la energía es maravillosamente simple: es solo el valor esperado de la perturbación en el estado original no perturbado: $E_n^{(1)} = \langle n^{(0)} | V | n^{(0)} \rangle$.

## 2. Perturbaciones Dependientes del Tiempo y la Regla de Oro
Si enciendes un láser (un campo electromagnético oscilante $V(t)$), el sistema empieza a saltar de un estado a otro. El parámetro físico crucial es la Tasa de Transición $W_{i\to f}$ (probabilidad por segundo de saltar del estado inicial $i$ al final $f$).
La física estadística de este salto está dictada por la **Regla de Oro de Fermi**:

$$
W_{i\to f} = \frac{2\pi}{\hbar} |\langle f | V | i \rangle|^2 \rho(E_f)
$$

La tasa depende críticamente de la "Densidad de Estados Finales" $\rho(E_f)$.

## 3. Integrales de Camino de Feynman
En 1948, Richard Feynman tiró a la basura el espacio de Hilbert y la ecuación diferencial de Schrödinger, reimaginando la cuántica desde cero a través de la Acción clásica $S = \int L dt$.
En la cuántica de Feynman, para calcular la amplitud de que una partícula viaje de A hasta B, asumes que la partícula viaja por **TODAS** las trayectorias posibles del universo simultáneamente.
La amplitud total de transición es una suma (una integral funcional infinita) sobre todos los caminos $x(t)$, ponderados por una fase matemática dependiente de su Acción:

$$
K(A, B) = \int \mathcal{D}x(t) e^{i S[x(t)] / \hbar}
$$

Esta fórmula (El Path Integral) contiene toda la cuántica entera. Caminos destructivos (fases oscilantes) se cancelan. Cuando $\hbar \to 0$, el único camino que sobrevive sin cancelarse por su vecino es el camino de "Mínima Acción", recuperando milagrosamente la mecánica clásica de Newton y Lagrange.
