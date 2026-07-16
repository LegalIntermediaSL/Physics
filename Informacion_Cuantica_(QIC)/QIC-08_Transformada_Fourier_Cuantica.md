# [QIC-08] Transformada de Fourier Cuántica (QFT) y Estimación de Fase

## 1. La Transformada de Fourier Cuántica (QFT)
La Transformada de Fourier Cuántica (QFT) es la versión cuántica de la Transformada de Fourier Discreta (DFT). Mientras que la DFT clásica sobre $N=2^n$ puntos requiere $O(N \log N) = O(n 2^n)$ operaciones (usando FFT), la QFT requiere solo $O(n^2)$ puertas cuánticas, logrando una aceleración exponencial.

Matemáticamente, la QFT actúa sobre una base computacional $|x\rangle$ de $n$ qubits como:

$$
QFT |x\rangle = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{2\pi i x y / N} |y\rangle
$$

Donde $N = 2^n$. El circuito de la QFT se construye usando puertas Hadamard (H) y puertas de fase controlada ($R_k$), donde $R_k$ aplica una fase $e^{2\pi i / 2^k}$.

## 2. El Circuito de la QFT
Para un estado de $n$ qubits $|x_1 x_2 \dots x_n\rangle$, el estado transformado se puede factorizar en un producto tensorial de superposiciones de un solo qubit:

$$
QFT |x\rangle = \frac{1}{\sqrt{N}} \left( |0\rangle + e^{2\pi i 0.x_n} |1\rangle \right) \otimes \left( |0\rangle + e^{2\pi i 0.x_{n-1}x_n} |1\rangle \right) \otimes \dots
$$

Esta factorización permite que la QFT se implemente eficientemente.

## 3. Algoritmo de Estimación de Fase Cuántica (QPE)
La Estimación de Fase es el corazón de muchos algoritmos cuánticos (incluyendo Shor). Dado un operador unitario $U$ y un autovector $|\psi\rangle$ tal que $U|\psi\rangle = e^{2\pi i \theta} |\psi\rangle$, el objetivo es estimar la fase $\theta$.

El algoritmo usa dos registros:
1.  Un registro de estimación de $t$ qubits inicializado en $|0\rangle^{\otimes t}$.
2.  Un registro objetivo inicializado en el estado $|\psi\rangle$.

Se aplican puertas Hadamard al primer registro, y luego se aplican operaciones $U^{2^j}$ controladas por los qubits del primer registro. El estado resultante en el primer registro es exactamente la Transformada de Fourier Cuántica Inversa (IQFT) del valor $\theta$. Aplicando la IQFT y midiendo, leemos una excelente aproximación binaria de $\theta$.
