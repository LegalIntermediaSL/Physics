# Algoritmos Cuánticos
Los algoritmos cuánticos son conjuntos de instrucciones diseñadas para ser ejecutadas en un ordenador cuántico, aprovechando la superposición, interferencia y entrelazamiento para resolver problemas exponencialmente más rápido que los ordenadores clásicos en algunos casos específicos.

## 📜 Contexto Histórico
El campo de los algoritmos cuánticos despegó en 1992 con el algoritmo de Deutsch-Jozsa, el primero en demostrar una ventaja cuántica determinista. Sin embargo, el punto de inflexión llegó en 1994, cuando Peter Shor introdujo el algoritmo de Shor para factorizar números grandes y calcular logaritmos discretos en tiempo polinómico. En 1996, Lov Grover presentó el algoritmo de Grover para búsqueda no estructurada, ofreciendo una aceleración cuadrática.

## 🧮 Desarrollo Teórico Profundo

El estudio formal de los algoritmos cuánticos requiere un entendimiento profundo del álgebra lineal aplicada a los espacios de Hilbert de dimensión finita. A diferencia de la computación clásica, donde las transformaciones sobre bits son funciones booleanas disipativas, la evolución de los estados cuánticos cerrados es estrictamente unitaria y reversible.

### 1. El Paradigma del Circuito Cuántico y la Interferencia
Un algoritmo cuántico se modela formalmente mediante una sucesión de transformaciones unitarias aplicadas a un estado inicial, el cual suele inicializarse en el estado base computacional $|0\rangle^{\otimes n}$.
La evolución matemática del sistema de $n$ qubits hasta el estado final se describe como:

$$
|\psi_f\rangle = U_k U_{k-1} \dots U_1 |0\rangle^{\otimes n}
$$

Donde cada $U_i$ es una matriz compleja unitaria ($U_i^\dagger U_i = I$) de dimensiones $2^n \times 2^n$. El diseño de estos algoritmos explora el fenómeno de la **interferencia**. El algoritmo está configurado de forma que la suma de amplitudes de probabilidad de las trayectorias computacionales que conducen a la respuesta correcta interfieran **constructivamente**, mientras que aquellas que conducen a respuestas incorrectas interfieran **destructivamente**.

### 2. Transformada de Hadamard Generalizada
La base del paralelismo cuántico reside en la capacidad de evaluar una función sobre todos los valores posibles de su dominio simultáneamente. La puerta de Hadamard $H$ sobre un qubit transforma los autoestados de la base computacional $Z$ en los de la base $X$:

$$
H |x\rangle = \frac{1}{\sqrt{2}} \left( |0\rangle + (-1)^x |1\rangle \right) \quad \text{para} \quad x \in \{0, 1\}
$$

Extendiendo este operador a un registro de $n$ qubits mediante el producto tensorial, obtenemos la superposición uniforme de todos los estados de la base de Hilbert $\mathcal{H}_2^{\otimes n}$. Para un estado base $|x\rangle$ donde $x \in \{0,1\}^n$:

$$
H^{\otimes n} |x\rangle = \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} (-1)^{x \cdot y} |y\rangle
$$

donde $x \cdot y = \sum_{i=1}^n x_i y_i \pmod 2$ es el producto escalar bit a bit módulo 2.

### 3. Algoritmo de Deutsch-Jozsa (Demostración Formal)
Este algoritmo ilustra de manera rigurosa la separación exponencial determinista respecto a cualquier equivalente clásico determinista. 

**Definición del Problema:** Dada una función booleana $f: \{0,1\}^n \rightarrow \{0,1\}$ implementada como un oráculo cuántico ("Black-box") que garantiza ser **constante** o **balanceada** (exactamente la mitad de las entradas evalúan a 0, y la otra mitad a 1), determinar a qué categoría pertenece en el mínimo número de consultas. Clásicamente, en el peor caso se necesitan $2^{n-1} + 1$ evaluaciones.

**Derivación Paso a Paso:**
1. **Estado Inicial:** Preparamos un registro de entrada de $n$ qubits y un qubit auxiliar (ancilla).

   

$$
|\psi_0\rangle = |0\rangle^{\otimes n} \otimes |1\rangle
$$

2. **Superposición (Hadamard en todos los qubits):** Aplicamos $H^{\otimes n}$ al primer registro y $H$ al ancilla para crear el estado superpuesto global.

   

$$
|\psi_1\rangle = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} |x\rangle \right) \otimes \left( \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} |x\rangle \right) \otimes |-\rangle
$$

3. **Aplicación del Oráculo $U_f$ (Retroceso de Fase / Phase Kickback):**
   El oráculo unitario evalúa la función sobre el qubit ancilla: $U_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$. 
   Al aplicarlo sobre el estado $|-\rangle$, la fase intrínseca se transfiere al registro de entrada:

   

$$
U_f \left( |x\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}} \right) = (-1)^{f(x)} |x\rangle \otimes |-\rangle
$$

   Por lo tanto, el estado completo evoluciona a:

   

$$
|\psi_2\rangle = \left( \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} (-1)^{f(x)} |x\rangle \right) \otimes |-\rangle
$$

4. **Interferencia Final:** Para recolectar la información extraída de la fase de nuevo en la amplitud observable, aplicamos $H^{\otimes n}$ otra vez al registro de entrada. Sustituyendo la expresión teórica deducida previamente para $H^{\otimes n}$:

   

$$
|\psi_3\rangle = \left( \frac{1}{2^n} \sum_{x \in \{0,1\}^n} \sum_{y \in \{0,1\}^n} (-1)^{f(x) + x \cdot y} |y\rangle \right) \otimes |-\rangle
$$

5. **Medición Analítica:**
   Procedemos a medir la amplitud de probabilidad del estado $|0\rangle^{\otimes n}$ (donde el vector $y = \vec{0}$). Como $x \cdot \vec{0} = 0$, la amplitud de este estado específico resulta en:

   

$$
\langle 0^{\otimes n} | \psi_{3,\text{reg}} \rangle = a_{0} = \frac{1}{2^n} \sum_{x \in \{0,1\}^n} (-1)^{f(x)}
$$

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

   

$$
O = I - 2|w\rangle\langle w|
$$

2. **Difusión de Grover ($D$):**
   Conocido como "Inversión respecto a la Media". Si $|s\rangle = \frac{1}{\sqrt{N}}\sum_x |x\rangle$ es el estado de superposición uniforme, este operador se define como:

   

$$
D = 2|s\rangle\langle s| - I
$$

**Geometría de la Rotación del Espacio:**
Podemos definir un subespacio de Hilbert de dimensión dos abarcado por la solución y el resto de elementos. Sean:
- $|w\rangle$: el estado que deseamos encontrar.
- $|s'\rangle = \frac{1}{\sqrt{N-1}}\sum_{x \neq w} |x\rangle$: la superposición uniforme de todos los elementos incorrectos.

El estado inicial $|s\rangle$ puede escribirse en esta base ortonormal como un vector real:

$$
|s\rangle = \sin(\theta)|w\rangle + \cos(\theta)|s'\rangle
$$

donde $\sin(\theta) = \frac{1}{\sqrt{N}}$.

La aplicación de $O$ es una reflexión sobre el eje $|s'\rangle$, y la de $D$ es una reflexión sobre $|s\rangle$. El producto de estas dos reflexiones resulta en una rotación estricta $\mathcal{G}$ en el plano $(|s'\rangle, |w\rangle)$ por un ángulo exacto de $2\theta$.
Aplicar $\mathcal{G}$ un número $k$ de veces conduce al estado:

$$
\mathcal{G}^k |s\rangle = \sin((2k+1)\theta)|w\rangle + \cos((2k+1)\theta)|s'\rangle
$$

Para maximizar la probabilidad de éxito (colapso sobre $|w\rangle$), deseamos que $\sin((2k+1)\theta) \approx 1$, lo que implica $(2k+1)\theta \approx \pi/2$. Usando la aproximación para $N$ grande, $\theta \approx 1/\sqrt{N}$:

$$
k \approx \frac{\pi}{4}\sqrt{N}
$$

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

$$
\text{QFT}|x\rangle = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{2\pi i x y / N} |y\rangle
$$

En el algoritmo de estimación de fase o búsqueda de periodos (esencia de Shor):
1. El sistema evalúa exponencialmente la función periódica modular $f(x) = a^x \pmod M$.
2. Cuando el registro se mide, el espacio de Hilbert colapsa a una superposición de desplazamientos periódicos $\sum_{m} |x_0 + m \cdot r\rangle$.
3. La aplicación de la inversa $\text{QFT}^\dagger$ aísla las frecuencias de esta señal discreta inter-estados. Extrae la periodicidad del patrón de interferencia en fases complejas para obtener el periodo $r$.
4. Dado $r$ y con la certidumbre matemática de que si es par y $a^{r/2} \not\equiv -1 \pmod M$, los factores del módulo se pueden obtener clásicamente en tiempo polinómico mediante el algoritmo de Euclides calculando $\text{mcd}(a^{r/2} \pm 1, M)$.

## 📝 Guía de Ejercicios Resueltos

### Ejercicio 1: Desigualdad CHSH y Entrelazamiento
Demuestre que el estado singlete de dos qubits $|\psi^{-}\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ viola la desigualdad CHSH y encuentre el valor máximo de la correlación cuántica.

**Solución paso a paso:**
1. El operador CHSH es $S = A \otimes B + A \otimes B' + A' \otimes B - A' \otimes B'$. Para variables clásicas locales, $|\langle S \rangle| \le 2$.
2. Elegimos las mediciones para Alice como $A = \sigma_z$ y $A' = \sigma_x$.
3. Elegimos las mediciones para Bob como $B = \frac{-\sigma_z - \sigma_x}{\sqrt{2}}$ y $B' = \frac{\sigma_z - \sigma_x}{\sqrt{2}}$.
4. Evaluamos las correlaciones para el estado singlete $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle = -\delta_{ij}$.
5. Calculamos cada término:

   

$$
\langle A \otimes B \rangle = \frac{1}{\sqrt{2}}, \quad \langle A \otimes B' \rangle = \frac{1}{\sqrt{2}}, \quad \langle A' \otimes B \rangle = \frac{1}{\sqrt{2}}, \quad \langle A' \otimes B' \rangle = -\frac{1}{\sqrt{2}}
$$

6. Sumando los términos, el valor de expectación es:

   

$$
\langle S \rangle = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} - \left(-\frac{1}{\sqrt{2}}\right) = 2\sqrt{2}
$$

7. Como $2\sqrt{2} > 2$, la mecánica cuántica viola el límite clásico (Desigualdad de Bell).

### Ejercicio 2: Código de Corrección de Errores de Shor (9 qubits)
Muestre cómo el código de Shor protege contra un error de fase $Z$ arbitrario en el primer qubit.

**Solución paso a paso:**
1. El estado lógico $|0\rangle_L$ está codificado como $\frac{1}{2\sqrt{2}}(|000\rangle + |111\rangle)^{\otimes 3}$.
2. Supongamos un error de fase en el primer qubit: $Z_1 |\psi_L\rangle$. El término interior pasa a ser $\frac{1}{\sqrt{2}}(Z|000\rangle + Z|111\rangle) = \frac{1}{\sqrt{2}}(|000\rangle - |111\rangle)$.
3. Para detectar el error, realizamos mediciones de síndrome con los operadores estabilizadores del código de fase: $X_1 X_2 X_3 X_4 X_5 X_6$ y $X_4 X_5 X_6 X_7 X_8 X_9$.
4. El error de fase es detectado por la medición cruzada entre los bloques. Equivalentemente, al aplicar compuertas Hadamard en cada bloque y realizar paridad $Z$ como en el código bit-flip, identificamos en qué bloque ocurrió el cambio de signo.
5. Tras identificar que el error ocurrió en el primer bloque de 3 qubits, aplicamos el operador de corrección $Z$ correspondiente al bloque, el cual restaura la fase global relativa.
6. El estado vuelve exactamente a $|\psi_L\rangle$ sin pérdida de información, probando la efectividad contra un error $Z_1$.

### Ejercicio 3: Transformada de Fourier Cuántica (QFT)
Construya el circuito y derive la acción de la QFT sobre un estado de base computacional de 3 qubits $|x\rangle = |x_2 x_1 x_0\rangle$.

**Solución paso a paso:**
1. La definición de la QFT en $n$ qubits es $|x\rangle \to \frac{1}{\sqrt{2^n}} \sum_{y=0}^{2^n-1} e^{2\pi i x y / 2^n} |y\rangle$.
2. Para 3 qubits, se puede reescribir como un producto tensorial:

   

$$
\frac{1}{\sqrt{8}} (|0\rangle + e^{2\pi i 0.x_0}|1\rangle) \otimes (|0\rangle + e^{2\pi i 0.x_1 x_0}|1\rangle) \otimes (|0\rangle + e^{2\pi i 0.x_2 x_1 x_0}|1\rangle)
$$

3. Se aplica primero una compuerta Hadamard al qubit $x_2$, obteniendo $\frac{1}{\sqrt{2}}(|0\rangle + e^{2\pi i 0.x_2}|1\rangle)$.
4. Se aplican rotaciones controladas $R_2$ dependiente de $x_1$ y $R_3$ dependiente de $x_0$, transformando el estado a $\frac{1}{\sqrt{2}}(|0\rangle + e^{2\pi i 0.x_2 x_1 x_0}|1\rangle)$.
5. Se repite el proceso para los qubits restantes, aplicando Hadamard y $R_2$ en $x_1$, y finalmente Hadamard en $x_0$.
6. El circuito final requiere operaciones SWAP para invertir el orden de los qubits y coincidir con la convención estándar.

## 💻 Simulaciones Computacionales

A continuación se presenta una simulación completa del Algoritmo de Búsqueda de Grover utilizando un simulador de vectores de estado en Python.

```python
import numpy as np
import matplotlib.pyplot as plt

def hadamard_transform(n):
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    H_n = H
    for _ in range(n - 1):
        H_n = np.kron(H_n, H)
    return H_n

def grover_oracle(n, target_state):
    N = 2**n
    oracle = np.eye(N)
    oracle[target_state, target_state] = -1
    return oracle

def grover_diffusion(n):
    N = 2**n
    H_n = hadamard_transform(n)
    U_0 = np.eye(N)
    U_0[0, 0] = -1
    return H_n @ U_0 @ H_n

def simulate_grover(n_qubits, target):
    N = 2**n_qubits
    state = np.zeros(N)
    state[0] = 1.0
    
    # Superposición inicial
    H_n = hadamard_transform(n_qubits)
    state = H_n @ state
    
    # Número óptimo de iteraciones
    iterations = int(np.pi / 4 * np.sqrt(N))
    
    oracle = grover_oracle(n_qubits, target)
    diffusion = grover_diffusion(n_qubits)
    
    probs = []
    probs.append(np.abs(state)**2)
    
    for _ in range(iterations):
        state = oracle @ state
        state = diffusion @ state
        probs.append(np.abs(state)**2)
        
    return probs

n = 4  # 4 qubits, 16 estados
target_idx = 11
probabilities = simulate_grover(n, target_idx)

plt.figure(figsize=(10, 5))
plt.bar(range(2**n), probabilities[-1], color='indigo')
plt.title(f"Probabilidades finales - Algoritmo de Grover (Target: |{target_idx}⟩)")
plt.xlabel("Estado Base")
plt.ylabel("Probabilidad")
plt.xticks(range(2**n))
plt.grid(axis='y', alpha=0.5)
plt.show()
```

## 🚀 Fronteras de Investigación y Problemas Abiertos

A partir de 2026, la frontera de los algoritmos cuánticos ha evolucionado más allá de los prototipos teóricos, enfocándose en la obtención de Ventaja Cuántica Práctica en la era de los dispositivos ruidosos de escala intermedia (NISQ) y la incipiente transición hacia la Tolerancia a Fallos Temprana (Early Fault-Tolerance). 

- **Algoritmos de Aprendizaje Automático Cuántico (QML) y Barren Plateaus:** Un problema abierto fundamental es cómo mitigar sistemáticamente el fenómeno de los "Barren Plateaus" (mesetas estériles), donde el gradiente de la función de coste decae exponencialmente con el número de qubits en circuitos cuánticos parametrizados (PQCs) profundos.
- **Ventaja en Optimización Combinatoria:** Si bien QAOA (Quantum Approximate Optimization Algorithm) prometía ventajas computacionales, recientes resultados teóricos de 2026 sugieren que para grafos aleatorios estructurados (como los Max-Cut d-regulares), el límite asintótico cuántico a profundidad constante no supera heurísticas clásicas avanzadas (ej. algoritmo de Goemans-Williamson). El problema abierto radica en identificar familias de instancias (ej. grafos con simetrías no triviales u oculta estructura topológica) que aseguren separación superpolinómica.
- **Resolución Cuántica de Ecuaciones Diferenciales no Lineales (EDNLs):** Los algoritmos de simulación cuántica para dinámica de fluidos y ecuaciones de Navier-Stokes sufren de inestabilidades al mapear no-linealidades (que son intrínsecamente no unitarias) en el espacio de Hilbert lineal cuántico. El uso de linealizaciones de Carleman truncadas genera sobrecarga computacional.

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

El estudio avanzado de los algoritmos cuánticos se abstrae a la **Teoría de Representaciones de Grupos de Lie** y la **Geometría Algebraica** de los circuitos cuánticos.

Cualquier evolución temporal parametrizada de $n$ qubits puede interpretarse como una trayectoria en la variedad del grupo unitario $SU(d)$ con $d=2^n$. El álgebra de Lie $\mathfrak{su}(d)$ está generada por elementos $i P_j$, donde $P_j$ son cadenas de Pauli.

La complejidad óptima del circuito, es decir, el número mínimo de compuertas necesarias para sintetizar una unitaria $U \in SU(d)$, se modela equivalentemente al problema geométrico de encontrar la **geodésica más corta** en la variedad riemanniana de $SU(d)$ equipada con una métrica de Finsler penalizada (que asigna un coste enorme a operaciones altamente no locales). 

La distancia geodésica $D(I, U)$ viene dada por el ínfimo de la longitud funcional de la curva $c(t)$:

$$
D(I, U) = \inf_{c: c(0)=I, c(1)=U} \int_0^1 \mathcal{F}\left( c(t), \frac{dc}{dt} \right) dt
$$

donde la función de Finsler define la norma en el espacio tangente. La métrica se escinde penalizando severamente direcciones generadas por hamiltonianos multiqubit:

$$
ds^2 = \sum_{P \in \mathcal{P} \text{ (local)}} (dx^P)^2 + \Lambda \sum_{Q \in \mathcal{Q} \text{ (no-local)}} (dx^Q)^2
$$

donde $\Lambda \gg 1$ es la penalización de complejidad. Esta formulación permite usar la teoría de campos de Killing y variedades sub-riemannianas para demostrar cotas inferiores en la profundidad de los algoritmos, estableciendo que la síntesis de un $U$ genérico exige una distancia que escala exponencialmente con $n$, lo cual fundamenta geométricamente el porqué de la intratabilidad de los algoritmos de simulación general estocástica.

## 📚 Recursos Específicos

### Cursos Recomendados
1. [Quantum Information Science I (MITx on edX)](https://www.edx.org/course/quantum-information-science-i-part-1)
2. [Introduction to Quantum Computing (Coursera - St. Petersburg State University)](https://www.coursera.org/learn/quantum-computing)
3. [Qiskit Global Summer School (IBM Quantum)](https://qiskit.org/events/summer-school/)

### Artículos y Simulaciones
1. **Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer (P. W. Shor, 1997)**
   - **Enlace:** [https://arxiv.org/abs/quant-ph/9508027](https://arxiv.org/abs/quant-ph/9508027)
   - **Importancia Teórica:** Artículo fundacional que demostró la factorización en tiempo polinómico, desafiando la seguridad criptográfica moderna (RSA).
   - **Fondo Matemático:** Aplica la Transformada de Fourier Cuántica (QFT) para estimar el periodo $r$ de $f(x) = a^x \pmod N$. La QFT mapea la periodicidad:

     

$$
\text{QFT} |x\rangle = \frac{1}{\sqrt{q}} \sum_{y=0}^{q-1} e^{2\pi i x y / q} |y\rangle
$$

   - **Implicaciones Físicas:** Probó que el entrelazamiento y la interferencia permiten el cálculo determinista global en el espacio de Hilbert superando exponencialmente el paradigma de la máquina de Turing clásica.

2. **A fast quantum mechanical algorithm for database search (L. K. Grover, 1996)**
   - **Enlace:** [https://arxiv.org/abs/quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043)
   - **Importancia Teórica:** Logra aceleración cuadrática en la búsqueda no estructurada.
   - **Fondo Matemático:** Iteración del operador de Grover $\mathcal{G} = D O$. El oráculo invierte la fase $O = I - 2|w\rangle\langle w|$, y el operador de difusión efectúa una reflexión sobre la media:

     

$$
D = 2|s\rangle\langle s| - I
$$

   - **Implicaciones Físicas:** Demuestra el límite asintótico cuántico $\Omega(\sqrt{N})$ para búsquedas en caja negra, evidenciando cómo la amplitud probabilística se condensa dinámicamente mediante interferencia constructiva.

3. **Quantum algorithm for linear systems of equations (Harrow, Hassidim, Lloyd, 2009)**
   - **Enlace:** [https://arxiv.org/abs/0811.3171](https://arxiv.org/abs/0811.3171)
   - **Importancia Teórica:** El algoritmo HHL resuelve sistemas $A\vec{x} = \vec{b}$ en tiempo logarítmico, abriendo paso al aprendizaje automático cuántico.
   - **Fondo Matemático:** Usa estimación de fase para rotar el estado de un ancilla basado en los autovalores $\lambda_j$ de $A$:

     

$$
\sum_j \beta_j |u_j\rangle \left( \sqrt{1 - \frac{C^2}{\lambda_j^2}}|0\rangle + \frac{C}{\lambda_j}|1\rangle \right)
$$

   - **Implicaciones Físicas:** Convierte la inversión matricial en un proceso de evolución unitaria hamiltoniana natural.

### 📖 Referencias Útiles y Bibliografía
1. [Quantum Computation and Quantum Information (Nielsen & Chuang)](https://doi.org/10.1017/CBO9780511976667)
2. [Quantum Computer Science: An Introduction (N. David Mermin)](https://doi.org/10.1017/CBO9780511813870)

## 🌐 Seminarios Avanzados y Literatura de Frontera

### Seminarios y Cursos
- [Perimeter Institute - Quantum Information Seminars](https://pirsa.org/)
- [Institute for Quantum Computing (IQC) Seminars](https://uwaterloo.ca/institute-for-quantum-computing/events)
- [Harvard Quantum Initiative](https://quantum.harvard.edu/events)

### Literatura de Frontera
- [npj Quantum Information](https://www.nature.com/npjqi/): Publica avances líderes en computación cuántica, criptografía y algoritmos.
- [PRX Quantum](https://journals.aps.org/prxquantum/): Revista open-access de la APS centrada en tecnologías cuánticas y su aplicación interdisciplinar.
- [Quantum (Journal)](https://quantum-journal.org/): Ofrece publicaciones revisadas por pares de alto impacto impulsadas por la propia comunidad cuántica.
