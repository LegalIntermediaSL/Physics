# Corrección de Errores y Hardware
La computación cuántica es extremadamente susceptible a la decoherencia y al ruido ambiental. La corrección de errores cuánticos (QEC) y el desarrollo de hardware cuántico robusto son los mayores desafíos en la construcción de ordenadores cuánticos escalables (tolerantes a fallos).

## 📜 Contexto Histórico
El teorema de no-clonación cuántica (descubierto en 1982 por Wootters, Zurek y Dieks) parecía imposibilitar la corrección de errores clásica, que se basa en hacer copias de la información. Sin embargo, en 1995, Peter Shor y Andrew Steane propusieron de manera independiente los primeros códigos de corrección de errores cuánticos, demostrando que la información podía distribuirse entre varios qubits entrelazados para protegerla sin clonarla. Simultáneamente, investigadores comenzaron a proponer arquitecturas físicas como iones atrapados (Cirac y Zoller, 1995) y superconductores.

## 🧮 Desarrollo Teórico Profundo
Un código estabilizador (el formalismo dominante en QEC) utiliza un subgrupo abeliano $ \mathcal{S} \subset \mathcal{P}_n $ (donde $ \mathcal{P}_n $ es el grupo de Pauli en $ n $ qubits) que no contiene $ -I $. El subespacio de los códigos es el espacio simultáneo de vectores propios con autovalor +1 para todos los operadores en $ \mathcal{S} $:
$$ \mathcal{C} = \{ |\psi\rangle \mid S_i |\psi\rangle = |\psi\rangle, \forall S_i \in \mathcal{S} \} $$

El modelo de error más común es la aplicación de un operador de Pauli $ E \in \mathcal{P}_n $. Para detectar un error sin destruir la información superpuesta, medimos los generadores $ S_i $ (los "síndromes"). Si $ E $ anticonmuta con $ S_i $ ($ \{E, S_i\} = 0 $), el autovalor medido cambia a -1.

El famoso código de Shor de 9 qubits protege contra cualquier error arbitrario en un solo qubit, combinando el código de repetición de 3 qubits para bit flip (errores $ X $) y el de phase flip (errores $ Z $).

## 🛠 Ejemplo Práctico
**Problema:** Muestra cómo el código de repetición cuántica de 3 qubits para errores de inversión de fase (Phase-flip, error $ Z $) codifica y protege la información.

**Solución paso a paso:**
1. **Codificación:** 
   El error de fase $ Z $ en la base computacional actúa como un bit flip en la base de Hadamard ($ |+\rangle, |-\rangle $).
   Codificamos los estados lógicos como:
   $$ |0_L\rangle = |+++\rangle = H^{\otimes 3} |000\rangle $$
   $$ |1_L\rangle = |---\rangle = H^{\otimes 3} |111\rangle $$
   El estado lógico es $ |\psi_L\rangle = \alpha|+++\rangle + \beta|---\rangle $.

2. **Ocurrencia de Error:**
   Supongamos que el entorno aplica una puerta $ Z $ al primer qubit:
   $$ |\psi'\rangle = Z_1 |\psi_L\rangle = \alpha|--+\rangle + \beta|++-\rangle $$

3. **Medición de Síndromes:**
   Aplicamos compuertas de Hadamard a todos los qubits para volver a la base computacional:
   $$ H^{\otimes 3} |\psi'\rangle = \alpha|100\rangle + \beta|011\rangle $$
   Realizamos la medición de paridad de los qubits (equivalente a medir los observables $ X_1X_2 $ y $ X_2X_3 $).
   La paridad de (Q1, Q2) es impar, y (Q2, Q3) es par. Este síndrome nos indica que el qubit 1 sufrió el error.

4. **Corrección:**
   Aplicamos una puerta de corrección (en la base computacional sería $ X_1 $, en la base original $ Z_1 $). El estado vuelve a ser $ \alpha|000\rangle + \beta|111\rangle $, y tras las compuertas Hadamard recuperamos $ |\psi_L\rangle $ perfecto.

## 📚 Recursos Específicos

### Cursos
1. [Quantum Hardware y Control (Qutech/TU Delft en edX)](https://www.edx.org/course/quantum-hardware-and-control)
2. [Quantum Computing Systems (Coursera)](https://www.coursera.org/learn/quantum-computing-systems)
3. [Building a Quantum Computer (FutureLearn)](https://www.futurelearn.com/courses/building-a-quantum-computer)
4. [Quantum Error Correction (edX - Delft University)](https://www.edx.org/course/quantum-error-correction)
5. [Architecture of Quantum Computers (Coursera)](https://www.coursera.org/learn/architecture-quantum-computers)
6. [Fault-Tolerant Quantum Computing (Coursera)](https://www.coursera.org/learn/fault-tolerant-quantum-computing)

### Artículos y Simulaciones
1. [Scheme for reducing decoherence in quantum computer memory (P. Shor, 1995)](https://doi.org/10.1103/PhysRevA.52.R2493)
2. [Surface codes: Towards practical large-scale quantum computation (A. Fowler et al., 2012)](https://arxiv.org/abs/1208.0928)
3. [Stim (Fast Quantum Error Correction Simulator)](https://github.com/quantumlib/Stim)
4. [Qiskit Metal (Diseño de hardware cuántico)](https://qiskit.org/metal/)
5. [Superconducting Qubits: Current State of Play (Kjaergaard et al., 2020)](https://arxiv.org/abs/1905.13641)
6. [Trapped-Ion Quantum Computing: Progress and Challenges (Bruzewicz et al., 2019)](https://arxiv.org/abs/1904.04178)
7. [Fault-tolerant quantum computation with constant error rate (Aharonov & Ben-Or, 1997)](https://arxiv.org/abs/quant-ph/9611025)
8. [Quantum Error Correction for Beginners (Devitt et al., 2013)](https://arxiv.org/abs/0905.2794)

### 📖 Referencias Útiles y Bibliografía
1. [Quantum Computation and Quantum Information (Nielsen & Chuang)](https://doi.org/10.1017/CBO9780511976667)
2. [Quantum Error Correction (D. A. Lidar, T. A. Brun)](https://doi.org/10.1017/CBO9781139034807)
3. [Topological Quantum Computation (Z. Wang)](https://bookstore.ams.org/cbms-112/)
