# Algoritmos Cuánticos
Los algoritmos cuánticos son conjuntos de instrucciones diseñadas para ser ejecutadas en un ordenador cuántico, aprovechando la superposición, interferencia y entrelazamiento para resolver problemas exponencialmente más rápido que los ordenadores clásicos en algunos casos específicos.

## 📜 Contexto Histórico
El campo de los algoritmos cuánticos despegó en 1992 con el algoritmo de Deutsch-Jozsa, el primero en demostrar una ventaja cuántica determinista. Sin embargo, el punto de inflexión llegó en 1994, cuando Peter Shor introdujo el algoritmo de Shor para factorizar números grandes y calcular logaritmos discretos en tiempo polinómico. En 1996, Lov Grover presentó el algoritmo de Grover para búsqueda no estructurada, ofreciendo una aceleración cuadrática.

## 🧮 Desarrollo Teórico Profundo
Un algoritmo cuántico se modela a menudo mediante un circuito cuántico, compuesto por un conjunto finito de puertas unitarias $ U_i $ que actúan sobre $ n $ qubits. El estado final es $ U_k \dots U_2 U_1 |0\rangle^{\otimes n} $.

El **Algoritmo de Grover** busca un elemento marcado en una base de datos de tamaño $ N = 2^n $. 
El operador de Grover es $ G = (2|\psi\rangle\langle\psi| - I)O $, donde $ |\psi\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle $ es la superposición uniforme y $ O $ es el oráculo que invierte la fase del estado objetivo $|w\rangle$: $ O|x\rangle = (-1)^{f(x)}|x\rangle $ (donde $ f(w)=1 $ y $ 0 $ de lo contrario).
La aplicación repetida de $ G $, aproximadamente $ \frac{\pi}{4}\sqrt{N} $ veces, amplifica la amplitud de probabilidad de $|w\rangle$ a un valor cercano a 1.

La transformación de Hadamard (fundamental en algoritmos cuánticos) en $ n $ qubits es:
$$ H^{\otimes n} |x\rangle = \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} (-1)^{x \cdot y} |y\rangle $$

## 🛠 Ejemplo Práctico
**Problema:** Aplica el algoritmo de Deutsch (un qubit) para determinar si la función $ f(x) : \{0, 1\} \to \{0, 1\} $ es constante o balanceada.

**Solución paso a paso:**
1. **Estado inicial:** Partimos de dos qubits en el estado $ |0\rangle |1\rangle $.
2. **Aplicación de puertas de Hadamard:**
   $$ (H \otimes H) |0\rangle |1\rangle = \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) \left( \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) $$
3. **Aplicación del Oráculo $ U_f $:** El oráculo mapea $ |x, y\rangle \to |x, y \oplus f(x)\rangle $. 
   Para el qubit de abajo (que está en $ |-\rangle $), esto resulta en un "phase kickback":
   $$ U_f |x\rangle |-\rangle = (-1)^{f(x)} |x\rangle |-\rangle $$
   El estado del sistema se convierte en:
   $$ \frac{1}{\sqrt{2}} \left( (-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle \right) |-\rangle $$
4. **Segunda puerta Hadamard al primer qubit:**
   Ignorando el segundo qubit y sacando factor común $ (-1)^{f(0)} $:
   $$ |\psi_1\rangle = \pm \frac{1}{\sqrt{2}} ( |0\rangle + (-1)^{f(0) \oplus f(1)} |1\rangle ) $$
   Aplicando $ H $:
   $$ H |\psi_1\rangle = \pm |f(0) \oplus f(1)\rangle $$
5. **Medición:** 
   Si la función es constante ($ f(0) = f(1) $), medimos $ |0\rangle $. 
   Si es balanceada ($ f(0) \neq f(1) $), medimos $ |1\rangle $. ¡En un solo intento!

## 📚 Recursos Específicos

### Cursos
1. [Quantum Machine Learning (edX - University of Toronto)](https://www.edx.org/course/quantum-machine-learning)
2. [Introduction to Quantum Computing (Coursera - St. Petersburg State University)](https://www.coursera.org/learn/quantum-computing)
3. [Qiskit Global Summer School (IBM Quantum)](https://qiskit.org/events/summer-school/)
4. [Quantum Algorithms (Coursera - University of Colorado Boulder)](https://www.coursera.org/specializations/quantum-algorithms)
5. [Applied Quantum Computing (edX - Purdue University)](https://www.edx.org/course/applied-quantum-computing)
6. [Quantum Computing: Algorithms and Software (FutureLearn)](https://www.futurelearn.com/courses/quantum-computing-algorithms)

### Artículos y Simulaciones
1. [Qiskit Textbook (Learn Quantum Computation using Qiskit)](https://qiskit.org/textbook/preface.html)
2. [Pennylane (Simulador de algoritmos cuánticos e IA)](https://pennylane.ai/)
3. [Polynomial-Time Algorithms for Prime Factorization (P. W. Shor, 1997)](https://arxiv.org/abs/quant-ph/9508027)
4. [Quantum Computation and Shor's Factoring Algorithm (A. Ekert, R. Jozsa, 1996)](https://arxiv.org/abs/quant-ph/9603011)
5. [A fast quantum mechanical algorithm for database search (L. K. Grover, 1996)](https://arxiv.org/abs/quant-ph/9605043)
6. [Quantum algorithm for linear systems of equations (Harrow, Hassidim, Lloyd, 2009)](https://arxiv.org/abs/0811.3171)
7. [Variational Quantum Eigensolver (Peruzzo et al., 2014)](https://arxiv.org/abs/1304.3061)
8. [Quantum Approximate Optimization Algorithm (Farhi, Goldstone, Gutmann, 2014)](https://arxiv.org/abs/1411.4028)

### 📖 Referencias Útiles y Bibliografía
1. [Quantum Computation and Quantum Information (Nielsen & Chuang)](https://doi.org/10.1017/CBO9780511976667)
2. [Quantum Computer Science: An Introduction (N. David Mermin)](https://doi.org/10.1017/CBO9780511813870)
3. [An Introduction to Quantum Computing (Kaye, Laflamme, Mosca)](https://global.oup.com/academic/product/an-introduction-to-quantum-computing-9780198570493)
