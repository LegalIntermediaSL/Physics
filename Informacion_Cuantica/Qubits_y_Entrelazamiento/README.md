# Qubits y Entrelazamiento
El estudio de los qubits (bits cuánticos) y el entrelazamiento cuántico forma la base de toda la teoría de la información cuántica. Mientras un bit clásico solo puede ser 0 o 1, un qubit puede existir en una superposición de ambos estados.

## 📜 Contexto Histórico
El concepto de qubit se formalizó en las décadas de 1980 y 1990 con pioneros como Paul Benioff, Richard Feynman y David Deutsch, quienes propusieron que los sistemas cuánticos podrían usarse para el procesamiento de información. El entrelazamiento, sin embargo, se remonta a 1935, cuando Albert Einstein, Boris Podolsky y Nathan Rosen (paradoja EPR) cuestionaron su existencia, llamándolo "acción fantasmal a distancia". Erwin Schrödinger acuñó el término "entrelazamiento" poco después.

## 🧮 Desarrollo Teórico Profundo
Un qubit es matemáticamente descrito por un vector de estado unitario en un espacio de Hilbert de dos dimensiones, $ \mathcal{H} \cong \mathbb{C}^2 $. 
El estado general de un qubit se escribe como:
$$ |\psi\rangle = \alpha|0\rangle + \beta|1\rangle $$
donde $ \alpha, \beta \in \mathbb{C} $ son amplitudes de probabilidad complejas y $ |\alpha|^2 + |\beta|^2 = 1 $.

El entrelazamiento ocurre en sistemas multipartitos, como dos qubits. El espacio de estado compuesto es el producto tensorial de los espacios individuales: $ \mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B $.
Un estado entrelazado famoso es el estado de Bell:
$$ |\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle) $$
En este estado, el estado de un qubit no puede describirse independientemente del otro. La matriz densidad $ \rho = |\psi\rangle\langle\psi| $ para un estado entrelazado puro tiene una entropía de von Neumann para el subsistema (traza parcial $ \rho_A = \text{Tr}_B(\rho) $) mayor que cero:
$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) = 1 $ bit (para estados máximamente entrelazados).

## 🛠 Ejemplo Práctico
**Problema:** Calcula la traza parcial y demuestra que el estado de Bell $ |\Phi^+\rangle $ está máximamente entrelazado.

**Solución paso a paso:**
1. **Definir la matriz densidad total:**
   $$ \rho = |\Phi^+\rangle\langle\Phi^+| = \frac{1}{2} (|00\rangle\langle00| + |00\rangle\langle11| + |11\rangle\langle00| + |11\rangle\langle11|) $$

2. **Calcular la traza parcial respecto al sistema B ($ \rho_A $):**
   $$ \rho_A = \text{Tr}_B(\rho) = \sum_{i \in \{0,1\}} \langle i_B | \rho | i_B \rangle $$
   $$ \langle 0_B | \rho | 0_B \rangle = \frac{1}{2} |0_A\rangle\langle0_A| $$
   $$ \langle 1_B | \rho | 1_B \rangle = \frac{1}{2} |1_A\rangle\langle1_A| $$
   $$ \rho_A = \frac{1}{2} (|0\rangle\langle0| + |1\rangle\langle1|) = \frac{1}{2} I $$

3. **Calcular la entropía de von Neumann:**
   La matriz densidad reducida es proporcional a la identidad (estado mixto máximo). Los valores propios son $ \lambda_1 = 1/2, \lambda_2 = 1/2 $.
   $ S(\rho_A) = - \left( \frac{1}{2} \log_2\frac{1}{2} + \frac{1}{2} \log_2\frac{1}{2} \right) = - \left( -\frac{1}{2} - \frac{1}{2} \right) = 1 $ bit.
   Como $ S(\rho_A) = 1 $, el estado está máximamente entrelazado.

## 📚 Recursos Específicos

### Cursos
1. [Quantum Information Science I, Part 1 (MITx on edX)](https://www.edx.org/course/quantum-information-science-i-part-1)
2. [Understanding Quantum Mechanics (Coursera)](https://www.coursera.org/learn/quantum-mechanics)
3. [Qubits and Quantum States (FutureLearn)](https://www.futurelearn.com/courses/qubits-quantum-states)
4. [Quantum Entanglement and Its Applications (Stanford Online)](https://online.stanford.edu/courses/quantum-entanglement)
5. [The Physics of Quantum Information (edX)](https://www.edx.org/course/physics-of-quantum-information)
6. [Quantum Mechanics and Quantum Computation (UC Berkeley)](https://www.coursera.org/learn/quantum-mechanics-computation)

### Artículos y Simulaciones
1. [IBM Quantum Composer (Simulador online de circuitos)](https://quantum-computing.ibm.com/composer/)
2. [Quirk (Simulador cuántico de código abierto)](https://algassert.com/quirk)
3. [Quantum entanglement for babies (Chris Ferrie)](https://csferrie.com/books/quantum-entanglement-for-babies/)
4. [Quantum mechanics of multi-particle systems (E. Schrödinger, 1935)](https://doi.org/10.1017/S030500410001355X)
5. [On the Einstein Podolsky Rosen paradox (J. S. Bell, 1964)](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)
6. [Can Quantum-Mechanical Description of Physical Reality Be Considered Complete? (Einstein, Podolsky, Rosen, 1935)](https://doi.org/10.1103/PhysRev.47.777)
7. [Decoherence and the transition from quantum to classical (W. Zurek, 2003)](https://arxiv.org/abs/quant-ph/0306072)
8. [Experimental realization of EPR paradox (Aspect et al., 1982)](https://doi.org/10.1103/PhysRevLett.49.1804)

### 📖 Referencias Útiles y Bibliografía
1. [Quantum Computation and Quantum Information (Nielsen & Chuang)](https://doi.org/10.1017/CBO9780511976667)
2. [Speakable and Unspeakable in Quantum Mechanics (J. S. Bell)](https://doi.org/10.1017/CBO9780511815676)
3. [Principles of Quantum Mechanics (R. Shankar)](https://doi.org/10.1007/978-1-4757-0576-8)
