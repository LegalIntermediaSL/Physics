# Algoritmos Cuánticos
Los algoritmos cuánticos son conjuntos de instrucciones diseñadas para ser ejecutadas en un ordenador cuántico, aprovechando la superposición, interferencia y entrelazamiento para resolver problemas exponencialmente más rápido que los ordenadores clásicos en algunos casos específicos.

## 📜 Contexto Histórico
El campo de los algoritmos cuánticos despegó en 1992 con el algoritmo de Deutsch-Jozsa, el primero en demostrar una ventaja cuántica determinista. Sin embargo, el punto de inflexión llegó en 1994, cuando Peter Shor introdujo el algoritmo de Shor para factorizar números grandes y calcular logaritmos discretos en tiempo polinómico. En 1996, Lov Grover presentó el algoritmo de Grover para búsqueda no estructurada, ofreciendo una aceleración cuadrática.

## 🧮 Desarrollo Teórico Profundo

El estudio formal de los algoritmos cuánticos requiere un entendimiento profundo del álgebra lineal aplicada a los espacios de Hilbert de dimensión finita. A diferencia de la computación clásica, donde las transformaciones sobre bits son funciones booleanas disipativas, la evolución de los estados cuánticos cerrados es estrictamente unitaria y reversible.

### 1. El Paradigma del Circuito Cuántico y la Interferencia
Un algoritmo cuántico se modela formalmente mediante una sucesión de transformaciones unitarias aplicadas a un estado inicial, el cual suele inicializarse en el estado base computacional $|0\rangle^{\otimes n}$.
La evolución matemática del sistema de $n$ qubits hasta el estado final se describe como:
$$ |\psi_f\rangle = U_k U_{k-1} \dots U_1 |0\rangle^{\otimes n} $$
Donde cada $U_i$ es una matriz compleja unitaria ($U_i^\dagger U_i = I$) de dimensiones $2^n \times 2^n$. El diseño de estos algoritmos explora el fenómeno de la **interferencia**. El algoritmo está configurado de forma que la suma de amplitudes de probabilidad de las trayectorias computacionales que conducen a la respuesta correcta interfieran **constructivamente**, mientras que aquellas que conducen a respuestas incorrectas interfieran **destructivamente**.

### 2. Transformada de Hadamard Generalizada
La base del paralelismo cuántico reside en la capacidad de evaluar una función sobre todos los valores posibles de su dominio simultáneamente. La puerta de Hadamard $H$ sobre un qubit transforma los autoestados de la base computacional $Z$ en los de la base $X$:
$$ H |x\rangle = \frac{1}{\sqrt{2}} \left( |0\rangle + (-1)^x |1\rangle \right) \quad \text{para} \quad x \in \{0, 1\} $$

Extendiendo este operador a un registro de $n$ qubits mediante el producto tensorial, obtenemos la superposición uniforme de todos los estados de la base de Hilbert $\mathcal{H}_2^{\otimes n}$. Para un estado base $|x\rangle$ donde $x \in \{0,1\}^n$:
$$ H^{\otimes n} |x\rangle = \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} (-1)^{x \cdot y} |y\rangle $$
donde $x \cdot y = \sum_{i=1}^n x_i y_i \pmod 2$ es el producto escalar bit a bit módulo 2.

### 3. Algoritmo de Deutsch-Jozsa (Demostración Formal)
Este algoritmo ilustra de manera rigurosa la separación exponencial determinista respecto a cualquier equivalente clásico determinista. 

**Definición del Problema:** Dada una función booleana $f: \{0,1\}^n \rightarrow \{0,1\}$ implementada como un oráculo cuántico ("Black-box") que garantiza ser **constante** o **balanceada** (exactamente la mitad de las entradas evalúan a 0, y la otra mitad a 1), determinar a qué categoría pertenece en el mínimo número de consultas. Clásicamente, en el peor caso se necesitan $2^{n-1} + 1$ evaluaciones.

**Derivación Paso a Paso:**
1. **Estado Inicial:** Preparamos un registro de entrada de $n$ qubits y un qubit auxiliar (ancilla).
   $$ |\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle $$
2. **Superposición (Hadamard en todos los qubits):** Aplicamos $H^{\otimes n}$ al primer registro y $H$ al ancilla para crear el estado superpuesto global.
   $$ |\psi_1\rangle = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} |x\rangle \right) \otimes \left( \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} |x\rangle \right) \otimes |-\rangle $$
3. **Aplicación del Oráculo $U_f$ (Retroceso de Fase / Phase Kickback):**
   El oráculo unitario evalúa la función sobre el qubit ancilla: $U_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$. 
   Al aplicarlo sobre el estado $|-\rangle$, la fase intrínseca se transfiere al registro de entrada:
   $$ U_f \left( |x\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) = (-1)^{f(x)} |x\rangle \otimes |-\rangle $$
   Por lo tanto, el estado completo evoluciona a:
   $$ |\psi_2\rangle = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} (-1)^{f(x)} |x\rangle \right) \otimes |-\rangle $$
4. **Interferencia Final:** Para recolectar la información extraída de la fase de nuevo en la amplitud observable, aplicamos $H^{\otimes n}$ otra vez al registro de entrada. Sustituyendo la expresión teórica deducida previamente para $H^{\otimes n}$:
   $$ |\psi_3\rangle = \left( \frac{1}{2^n} \sum_{x \in \{0,1\}^n} \sum_{y \in \{0,1\}^n} (-1)^{f(x) + x \cdot y} |y\rangle \right) \otimes |-\rangle $$
5. **Medición Analítica:**
   Procedemos a medir la amplitud de probabilidad del estado $|0\rangle^{\otimes n}$ (donde el vector $y = \vec{0}$). Como $x \cdot \vec{0} = 0$, la amplitud de este estado específico resulta en:
   $$ \langle 0^{\otimes n} | \psi_{3,\text{reg}} \rangle = a_{0} = \frac{1}{2^n} \sum_{x \in \{0,1\}^n} (-1)^{f(x)} $$
   - **Caso 1: $f$ es constante.** $f(x) = c$ para todo $x$, siendo $c \in \{0,1\}$. 
     Entonces, $a_{0} = \frac{1}{2^n} 2^n (-1)^c = \pm 1$. La probabilidad de medir $|0\rangle^{\otimes n}$ es $|a_{0}|^2 = 1$.
   - **Caso 2: $f$ es balanceada.** Hay el mismo número de resultados donde $f(x)=0$ como donde $f(x)=1$. Los términos se cancelan mutuamente en la sumatoria. 
     Entonces, $a_{0} = 0$. La probabilidad de medir $|0\rangle^{\otimes n}$ es $0$.

Concluyentemente, con **una única consulta** (1 oráculo), determinamos determinísticamente la naturaleza global de $f$.

### 4. Algoritmo de Búsqueda de Grover
El algoritmo de Grover provee una aceleración cuadrática para la búsqueda no estructurada, resolviendo problemas de búsqueda en $O(\sqrt{N})$ tiempo frente a la cuota clásica de $O(N)$.

**Formulación Matemática:**
Para una base de datos de tamaño $N = 2^n$, queremos encontrar un elemento especial $w$ tal que $f(w) = 1$ y $f(x) = 0$ para $x \neq w$.
El algoritmo ejecuta la repetida aplicación del operador de Grover $\mathcal{G} = D \cdot O$:
1. **Oráculo de Inversión de Fase ($O$):**
   Cambia el signo del elemento objetivo, dejando los demás intactos.
   $$ O = I - 2|w\rangle\langle w| $$
2. **Difusión de Grover ($D$):**
   Conocido como "Inversión respecto a la Media". Si $|s\rangle = \frac{1}{\sqrt{N}}\sum_x |x\rangle$ es el estado de superposición uniforme, este operador se define como:
   $$ D = 2|s\rangle\langle s| - I $$

**Geometría de la Rotación del Espacio:**
Podemos definir un subespacio de Hilbert de dimensión dos abarcado por la solución y el resto de elementos. Sean:
- $|w\rangle$: el estado que deseamos encontrar.
- $|s'\rangle = \frac{1}{\sqrt{N-1}}\sum_{x \neq w} |x\rangle$: la superposición uniforme de todos los elementos incorrectos.

El estado inicial $|s\rangle$ puede escribirse en esta base ortonormal como un vector real:
$$ |s\rangle = \sin(\theta)|w\rangle + \cos(\theta)|s'\rangle $$
donde $\sin(\theta) = \frac{1}{\sqrt{N}}$.

La aplicación de $O$ es una reflexión sobre el eje $|s'\rangle$, y la de $D$ es una reflexión sobre $|s\rangle$. El producto de estas dos reflexiones resulta en una rotación estricta $\mathcal{G}$ en el plano $(|s'\rangle, |w\rangle)$ por un ángulo exacto de $2\theta$.
Aplicar $\mathcal{G}$ un número $k$ de veces conduce al estado:
$$ \mathcal{G}^k |s\rangle = \sin((2k+1)\theta)|w\rangle + \cos((2k+1)\theta)|s'\rangle $$

Para maximizar la probabilidad de éxito (colapso sobre $|w\rangle$), deseamos que $\sin((2k+1)\theta) \approx 1$, lo que implica $(2k+1)\theta \approx \pi/2$. Usando la aproximación para $N$ grande, $\theta \approx 1/\sqrt{N}$:
$$ k \approx \frac{\pi}{4}\sqrt{N} $$
Este resultado prueba la optimización matemática del esfuerzo computacional necesario para búsquedas invertidas exhaustivas.

```mermaid
graph TD
    A[Inicialización: Estado base |0>^n] -->|Aplicar H^n| B(Superposición Uniforme |s>)
    B --> C{Bucle de Grover k ≈ π/4 √N}
    C -->|Paso 1| D[Oráculo O: Reflejar amplitudes \n e Invertir fase de |w>]
    D -->|Paso 2| E[Operador de Difusión D: \n Inversión sobre la Media |s>]
    E --> C
    C -->|Fin del bucle \n Amplitud Maximizada| F[Medición Final: \n Colapso en estado solución |w>]
```

### 5. Algoritmo de Shor y la Transformada de Fourier Cuántica (QFT)
El algoritmo de Shor provee una resolución de tiempo polinómico ($O(n^3)$) para la factorización de enteros, que quiebra criptografía asimétrica como RSA, reduciendo el problema a encontrar el periodo de una función modular.

El pilar estructural de la técnica de Shor es la **Transformada de Fourier Cuántica (QFT)**, el análogo cuántico de la Transformada Discreta de Fourier clásica (DFT):
$$ \text{QFT}|x\rangle = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{2\pi i x y / N} |y\rangle $$

En el algoritmo de estimación de fase o búsqueda de periodos (esencia de Shor):
1. El sistema evalúa exponencialmente la función periódica modular $f(x) = a^x \pmod M$.
2. Cuando el registro se mide, el espacio de Hilbert colapsa a una superposición de desplazamientos periódicos $\sum_{m} |x_0 + m \cdot r\rangle$.
3. La aplicación de la inversa $\text{QFT}^\dagger$ aísla las frecuencias de esta señal discreta inter-estados. Extrae la periodicidad del patrón de interferencia en fases complejas para obtener el periodo $r$.
4. Dado $r$ y con la certidumbre matemática de que si es par y $a^{r/2} \not\equiv -1 \pmod M$, los factores del módulo se pueden obtener clásicamente en tiempo polinómico mediante el algoritmo de Euclides calculando $\text{mcd}(a^{r/2} \pm 1, M)$.

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
