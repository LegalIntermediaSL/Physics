# Corrección de Errores

Los sistemas cuánticos son frágiles frente a ruido, pérdidas y decoherencia. La corrección de errores cuántica muestra que, pese a ello, la computación cuántica escalable es compatible con las leyes de la física si se codifica la información de manera redundante y estructurada.

## 🧮 Desarrollo Teórico Profundo

La corrección de errores cuánticos (Quantum Error Correction, QEC) aborda el problema de preservar información cuántica en presencia de decoherencia y ruido. A diferencia de la computación clásica, en la cuántica enfrentamos el **Teorema de No-Clonación**, que prohíbe la copia exacta de estados cuánticos desconocidos, y la observación de que la medida destruye la superposición. A continuación, desarrollamos el formalismo riguroso que permite superar estas limitaciones.

### 1. Condiciones de Knill-Laflamme para la Corrección de Errores

Para que un código cuántico pueda corregir un conjunto de errores $\mathcal{E} = \{E_i\}$, debe existir una operación de recuperación $\mathcal{R}$ tal que, para cualquier estado codificado $|\psi\rangle$ en el subespacio lógico $\mathcal{C}$, se cumpla $\mathcal{R}(E_i |\psi\rangle \langle\psi| E_i^\dagger) \propto |\psi\rangle \langle\psi|$.

**Teorema (Condiciones de Knill-Laflamme):**
Un código cuántico $\mathcal{C}$ con proyector asociado $P = \sum_k |k_L\rangle \langle k_L|$ (donde $\{|k_L\rangle\}$ forma una base ortonormal para $\mathcal{C}$) puede corregir exactamente un conjunto de errores $\{E_i\}$ si y solo si:
$$ P E_i^\dagger E_j P = C_{ij} P $$
donde $C_{ij}$ es una matriz hermitiana y definida positiva independiente del estado.

**Demostración Paso a Paso:**
1. **Diagonalización de la matriz de error:** Al ser $C_{ij}$ hermitiana, puede diagonalizarse mediante una transformación unitaria $U$: $C = U D U^\dagger$, donde $D$ es diagonal con elementos $d_{kk}$.
2. **Base de errores ortogonales:** Definimos un nuevo conjunto de errores $F_k = \sum_i U_{ki} E_i$. Evaluando la condición de Knill-Laflamme con esta nueva base, obtenemos:
   $$ P F_k^\dagger F_l P = \sum_{i,j} U_{ki}^* U_{lj} P E_i^\dagger E_j P = \sum_{i,j} U_{ki}^* C_{ij} U_{lj} P = d_{kl} \delta_{kl} P $$
3. **Medida del Síndrome:** Esta ortogonalidad implica que los subespacios de error $\mathcal{E}_k = F_k \mathcal{C}$ son mutuamente ortogonales para distintos $k$. Esto permite realizar una medida proyectiva (síndrome) descrita por los proyectores $P_k = F_k P F_k^\dagger / d_{kk}$ sin colapsar la superposición de estados lógicos.
4. **Operación de Recuperación:** Si el resultado de la medida es $k$, el estado proyectado es proporcional a $F_k |\psi\rangle$. La recuperación se efectúa aplicando $R_k = U_k F_k^\dagger$, donde $U_k$ es un operador unitario que invierte $F_k$ sobre su soporte. Entonces:
   $$ R_k F_k |\psi\rangle = U_k F_k^\dagger F_k P |\psi\rangle = U_k (d_{kk} P) |\psi\rangle \propto |\psi\rangle $$
Esto concluye la demostración formal: el estado inicial se restaura perfectamente.

### 2. El Código de Repetición de 3 Qubits (Bit-Flip Code)

El error más simple es el de salto de bit (bit-flip), representado por la matriz de Pauli $X$. Supongamos un canal cuántico donde cada qubit sufre un error $X$ con probabilidad $p$.

Codificamos los estados base en tres qubits físicos:
$$ |0_L\rangle = |000\rangle, \quad |1_L\rangle = |111\rangle $$
Un estado lógico general es $|\psi\rangle = \alpha|0_L\rangle + \beta|1_L\rangle = \alpha|000\rangle + \beta|111\rangle$.

Si un bit-flip ocurre en el primer qubit, el estado se convierte en:
$$ X_1 |\psi\rangle = \alpha|100\rangle + \beta|011\rangle $$
Para detectar este error sin medir $\alpha$ y $\beta$, medimos la paridad de los pares de qubits (los generadores del estabilizador):
- Paridad $Z_1 Z_2$: compara el qubit 1 y 2.
- Paridad $Z_2 Z_3$: compara el qubit 2 y 3.

```mermaid
graph TD;
    A[Estado Codificado |000> o |111>] --> B{Ocurrencia de Error};
    B -- Sin Error --> C(Z1Z2 = +1, Z2Z3 = +1);
    B -- X1 en Qubit 1 --> D(Z1Z2 = -1, Z2Z3 = +1);
    B -- X2 en Qubit 2 --> E(Z1Z2 = -1, Z2Z3 = -1);
    B -- X3 en Qubit 3 --> F(Z1Z2 = +1, Z2Z3 = -1);
    
    C --> G[No hacer nada];
    D --> H[Aplicar X1];
    E --> I[Aplicar X2];
    F --> J[Aplicar X3];
    
    G --> K((Estado Lógico Restaurado));
    H --> K;
    I --> K;
    J --> K;
```

**Análisis de Medidas:**
$$ \langle \psi| X_1^\dagger (Z_1 Z_2) X_1 |\psi\rangle = \langle \psi| (-Z_1 X_1 X_1 Z_2) |\psi\rangle = -\langle \psi| Z_1 Z_2 |\psi\rangle $$
Como $Z_1 Z_2 |000\rangle = |000\rangle$ y $Z_1 Z_2 |111\rangle = |111\rangle$, el valor propio antes del error es $+1$. Después de $X_1$, el valor medido es $-1$. El síndrome $(Z_1 Z_2, Z_2 Z_3) = (-1, +1)$ nos indica unívocamente (para un solo error) que el error $X_1$ ha ocurrido, permitiéndonos aplicar $X_1$ de nuevo para restaurar $|\psi\rangle$.

### 3. Formalismo Estabilizador

El código de 3 qubits es un ejemplo de un **código estabilizador**. Sea el grupo de Pauli en $n$ qubits $\mathcal{P}_n = \{ \pm 1, \pm i \} \times \{I, X, Y, Z\}^{\otimes n}$.

Un código estabilizador se define por un subgrupo abeliano $S \subset \mathcal{P}_n$ que no contiene a $-I$. El subespacio codificado (espacio del código) es el subespacio simultáneo de +1 autovalores de todos los elementos $s \in S$:
$$ \mathcal{C} = \{ |\psi\rangle \in (\mathbb{C}^2)^{\otimes n} \mid s |\psi\rangle = |\psi\rangle, \forall s \in S \} $$

**Propiedades Algebraicas:**
Dado un grupo estabilizador $S$ generado por $n-k$ operadores independientes $\langle g_1, \dots, g_{n-k} \rangle$, el subespacio $\mathcal{C}$ codifica exactamente $k$ qubits lógicos (dimensión $2^k$).
Los errores pueden describirse como operadores $E \in \mathcal{P}_n$. El síndrome del error $E$ está dado por las relaciones de conmutación con los generadores de $S$:
$$ E g_i = (-1)^{c_i} g_i E $$
donde $c_i = 0$ si $E$ y $g_i$ conmutan, y $c_i = 1$ si anticonmutan. El vector $(c_1, \dots, c_{n-k})$ es el **síndrome clásico**. 

**Condición de Corrección:** Dos errores $E_1$ y $E_2$ tienen el mismo síndrome si y solo si $E_1^\dagger E_2$ conmuta con todos los elementos de $S$ (pertenece al centralizador $C(S)$). Para evitar errores lógicos irrecuperables, requerimos que $E_1^\dagger E_2 \notin C(S) \setminus S$, es decir, la distancia del código $d$ es el peso mínimo de un operador en $C(S) \setminus S$. Un código corrige cualquier error de peso $\lfloor (d-1)/2 \rfloor$.

### 4. El Código de Shor (9 Qubits)

El código de Shor concatena un código de bit-flip y uno de phase-flip ($Z$) para corregir errores arbitrarios de un qubit. La codificación lógica es:
$$ |0_L\rangle = \frac{(|000\rangle + |111\rangle)(|000\rangle + |111\rangle)(|000\rangle + |111\rangle)}{2\sqrt{2}} $$
$$ |1_L\rangle = \frac{(|000\rangle - |111\rangle)(|000\rangle - |111\rangle)(|000\rangle - |111\rangle)}{2\sqrt{2}} $$

Este código tiene 8 generadores estabilizadores:
- Para detectar bit-flips internos: $Z_1 Z_2$, $Z_2 Z_3$, $Z_4 Z_5$, $Z_5 Z_6$, $Z_7 Z_8$, $Z_8 Z_9$.
- Para detectar phase-flips entre bloques: $X_1 X_2 X_3 X_4 X_5 X_6$ y $X_4 X_5 X_6 X_7 X_8 X_9$.

Gracias a la linealidad de la mecánica cuántica y la discretización de errores, si un código puede corregir los errores de la base de Pauli $X$, $Y$, y $Z$, también corrige superposiciones de ellos $c_1 X + c_2 Y + c_3 Z$, demostrando que **la continuidad de los estados cuánticos no impide la corrección**.

## 📚 Recursos Específicos

### Cursos
1. [Quantum Error Correction (edX - Delft University)](https://www.edx.org/course/quantum-error-correction)
2. [Fault-Tolerant Quantum Computing (Coursera)](https://www.coursera.org/learn/fault-tolerant-quantum-computing)
3. [Quantum Codes and Topology (MIT OpenCourseWare)](https://ocw.mit.edu/courses/quantum-codes)
4. [Introduction to Stabilizer Codes (Stanford)](https://quantum.stanford.edu/courses/stabilizer-codes)
5. [Error Correction in Quantum Systems (FutureLearn)](https://www.futurelearn.com/courses/error-correction-quantum)

### Artículos y Simulaciones
1. [Scheme for reducing decoherence in quantum computer memory (P. Shor, 1995)](https://doi.org/10.1103/PhysRevA.52.R2493)
2. [Surface codes: Towards practical large-scale quantum computation (A. Fowler et al., 2012)](https://arxiv.org/abs/1208.0928)
3. [Stim: Fast Quantum Error Correction Simulator (C. Gidney, 2021)](https://arxiv.org/abs/2103.02202)
4. [PyMatching: A Python package for decoding quantum error-correcting codes (Higgott, 2021)](https://arxiv.org/abs/2105.13082)
5. [Topological quantum memory (E. Dennis et al., 2002)](https://arxiv.org/abs/quant-ph/0110143)
6. [Fault-tolerant quantum computation with constant error rate (Aharonov & Ben-Or, 1997)](https://arxiv.org/abs/quant-ph/9611025)
7. [Quantum Error Correction for Beginners (Devitt et al., 2013)](https://arxiv.org/abs/0905.2794)
8. [Stabilizer Codes and Quantum Error Correction (Gottesman, 1997)](https://arxiv.org/abs/quant-ph/9705052)

### 📖 Referencias Útiles y Bibliografía
1. [Quantum Computation and Quantum Information (Nielsen & Chuang)](https://doi.org/10.1017/CBO9780511976667)
2. [Quantum Error Correction (D. A. Lidar, T. A. Brun)](https://doi.org/10.1017/CBO9781139034807)
3. [Topological Quantum Computation (Z. Wang)](https://bookstore.ams.org/cbms-112/)
