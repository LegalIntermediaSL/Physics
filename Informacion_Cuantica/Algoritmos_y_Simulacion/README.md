# Algoritmos y Simulación

Los algoritmos cuánticos intentan aprovechar interferencia y entrelazamiento para resolver ciertos problemas de manera más eficiente que los métodos clásicos conocidos. La simulación cuántica, además, es una de las motivaciones más profundas del campo.

## 🧮 Desarrollo Teórico Profundo

Los algoritmos cuánticos y la simulación se basan en una estructura matemática subyacente que aprovecha la mecánica cuántica de manera directa. A continuación, desarrollaremos detalladamente dos de los pilares de esta disciplina: la Transformada de Fourier Cuántica (QFT) y los fundamentos de la Simulación Cuántica de sistemas hamiltonianos.

### 1. Transformada de Fourier Cuántica (QFT)

La Transformada de Fourier Cuántica es el análogo cuántico de la transformada de Fourier discreta (DFT). Dada una base computacional ortonormal $|0\rangle, |1\rangle, \dots, |N-1\rangle$, donde $N = 2^n$ (con $n$ el número de qubits), la QFT se define mediante la siguiente transformación lineal:

$$

\text{QFT} |j\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i j k / N} |k\rangle

$$

Para entender la estructura en términos de qubits, podemos escribir $j$ y $k$ en representación binaria:
$j = j_1 j_2 \dots j_n = j_1 2^{n-1} + j_2 2^{n-2} + \dots + j_n 2^0$
$k = k_1 k_2 \dots k_n = k_1 2^{n-1} + k_2 2^{n-2} + \dots + k_n 2^0$

La acción sobre el estado base se puede reescribir como un producto tensorial. Observando que la fase $e^{2\pi i j k / 2^n}$ se puede separar:

$$

\frac{k}{2^n} = \sum_{l=1}^n k_l 2^{-l}

$$

Por lo tanto:

$$

\text{QFT} |j\rangle = \frac{1}{\sqrt{2^n}} \bigotimes_{l=1}^n \left( |0\rangle + e^{2\pi i j 2^{-l}} |1\rangle \right)

$$

Desarrollando los términos exponenciales $j 2^{-l}$, notamos que la parte entera no contribuye a la fase (puesto que $e^{2\pi i m} = 1$ para $m \in \mathbb{Z}$). Al introducir la notación de fracción binaria $0.j_l j_{l+1} \dots j_n = \sum_{m=l}^n j_m 2^{-(m-l+1)}$, obtenemos la forma factorizada de la QFT:

$$

\text{QFT} |j_1 j_2 \dots j_n\rangle = \frac{1}{\sqrt{2^n}} \left( |0\rangle + e^{2\pi i 0.j_n} |1\rangle \right) \otimes \left( |0\rangle + e^{2\pi i 0.j_{n-1} j_n} |1\rangle \right) \otimes \dots \otimes \left( |0\rangle + e^{2\pi i 0.j_1 j_2 \dots j_n} |1\rangle \right)

$$

Este desarrollo muestra que el circuito cuántico correspondiente requiere únicamente compuertas de Hadamard ($H$) y rotaciones de fase condicionales ($R_k$):

$$

R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{2\pi i / 2^k} \end{pmatrix}

$$

El número de compuertas requeridas escala como $\mathcal{O}(n^2)$, proporcionando una ventaja exponencial frente al análogo clásico (la Fast Fourier Transform), que requiere $\mathcal{O}(n 2^n)$ operaciones.

### 2. Simulación Cuántica Universal y Trotterización

La simulación cuántica busca reproducir la dinámica de un sistema cuántico gobernado por un hamiltoniano $H$. La evolución temporal se describe por el operador unitario $U(t) = e^{-iHt}$ (tomando $\hbar = 1$). Si el hamiltoniano se puede descomponer como la suma de hamiltonianos locales o interacciones de pocos cuerpos, $H = \sum_{j=1}^m H_j$, el desafío radica en que, en general, los $H_j$ no conmutan: $[H_j, H_k] \neq 0$.

Para implementar $U(t)$ en un ordenador cuántico universal, utilizamos la fórmula de Lie-Trotter-Suzuki:

$$

e^{-i(A+B)t} = \lim_{n \to \infty} \left( e^{-i A t/n} e^{-i B t/n} \right)^n

$$

Para un paso de tiempo finito $\Delta t = t/r$, podemos aproximar la evolución completa dividiendo el tiempo total $t$ en $r$ intervalos o "pasos de Trotter". La aproximación de primer orden es:

$$

U(t) = e^{-i \sum_j H_j t} \approx \left( \prod_{j=1}^m e^{-i H_j \Delta t} \right)^r + \mathcal{O}(m^2 \Delta t^2)

$$

Donde el término de error $\mathcal{O}(m^2 \Delta t^2)$ surge de los conmutadores no nulos entre los sub-hamiltonianos. El límite de error riguroso (según la expansión de Baker-Campbell-Hausdorff) para la descomposición de primer orden es:

$$

\| e^{-i(A+B)t} - (e^{-i A t/r} e^{-i B t/r})^r \| \leq \frac{t^2}{2r} \| [A,B] \|

$$

Para mejorar la precisión, se recurre a aproximaciones de orden superior, como la fórmula de Trotter-Suzuki de segundo orden:

$$

S_2(t) = \prod_{j=1}^m e^{-i H_j \Delta t / 2} \prod_{j=m}^1 e^{-i H_j \Delta t / 2}

$$

cuyo error se reduce a $\mathcal{O}(\Delta t^3)$. De esta manera, al segmentar la simulación temporal en circuitos cuánticos elementales, logramos resolver dinámicas extremadamente complejas, que clásicamente sufrirían del crecimiento exponencial del espacio de Hilbert.

### Diagrama de Arquitectura de Simulación

El siguiente diagrama ilustra el flujo de un algoritmo clásico-cuántico híbrido, como el **Variational Quantum Eigensolver (VQE)**, comúnmente empleado en simulaciones moleculares bajo la era NISQ.

```mermaid
graph TD
    A[Inicio: Hamiltoniano Molecular H] --> B[Mapeo a Qubits: Transformación de Jordan-Wigner]
    B --> C[Inicialización del Ansatz Cuántico Parametrizado Uθ]
    C --> D[Ejecución en QPU: Medición de Expectativas ⟨H⟩]
    D --> E{Cálculo de Energía Eθ}
    E -->|Gradiente/Optimización| F[Actualización Clásica de Parámetros θ]
    F --> C
    E -->|Convergencia| G[Resultado Final: Energía del Estado Base]
    
    style A fill:#1e3a8a,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#047857,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#8b5cf6,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#b91c1c,stroke:#333,stroke-width:2px,color:#fff
```

En VQE, el ordenador cuántico evalúa eficientemente el valor esperado de la energía $\langle \psi(\theta) | H | \psi(\theta) \rangle$, mientras que un optimizador clásico ajusta $\theta$ para minimizarla, en virtud del principio variacional de Rayleigh-Ritz:

$$

E_0 \leq \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}

$$

Este método evita los largos circuitos de fase necesarios en el Algoritmo de Estimación de Fase Cuántica (QPE), convirtiéndose en la principal herramienta de simulación cuántica hoy en día.

## 📝 Guía de Ejercicios Resueltos

### Ejercicio 1: Desigualdad CHSH y Entrelazamiento
Demuestre que el estado singlete de dos qubits $|\psi^{-}\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ viola la desigualdad CHSH y encuentre el valor máximo de la correlación cuántica.

**Solución paso a paso:**
1. El operador CHSH es $S = A \otimes B + A \otimes B' + A' \otimes B - A' \otimes B'$. Para variables clásicas locales, $|\langle S \rangle| \le 2$.
2. Elegimos las mediciones para Alice como $A = \sigma_z$ y $A' = \sigma_x$.
3. Elegimos las mediciones para Bob como $B = \frac{-\sigma_z - \sigma_x}{\sqrt{2}}$ y $B' = \frac{\sigma_z - \sigma_x}{\sqrt{2}}$.
4. Evaluamos las correlaciones para el estado singlete $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle = -\delta_{ij}$.
5. Calculamos cada término:

   $$ \langle A \otimes B \rangle = \frac{1}{\sqrt{2}}, \quad \langle A \otimes B' \rangle = \frac{1}{\sqrt{2}}, \quad \langle A' \otimes B \rangle = \frac{1}{\sqrt{2}}, \quad \langle A' \otimes B' \rangle = -\frac{1}{\sqrt{2}} $$

6. Sumando los términos, el valor de expectación es:

   $$ \langle S \rangle = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} - \left(-\frac{1}{\sqrt{2}}\right) = 2\sqrt{2} $$

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

   $$ \frac{1}{\sqrt{8}} (|0\rangle + e^{2\pi i 0.x_0}|1\rangle) \otimes (|0\rangle + e^{2\pi i 0.x_1 x_0}|1\rangle) \otimes (|0\rangle + e^{2\pi i 0.x_2 x_1 x_0}|1\rangle) $$

3. Se aplica primero una compuerta Hadamard al qubit $x_2$, obteniendo $\frac{1}{\sqrt{2}}(|0\rangle + e^{2\pi i 0.x_2}|1\rangle)$.
4. Se aplican rotaciones controladas $R_2$ dependiente de $x_1$ y $R_3$ dependiente de $x_0$, transformando el estado a $\frac{1}{\sqrt{2}}(|0\rangle + e^{2\pi i 0.x_2 x_1 x_0}|1\rangle)$.
5. Se repite el proceso para los qubits restantes, aplicando Hadamard y $R_2$ en $x_1$, y finalmente Hadamard en $x_0$.
6. El circuito final requiere operaciones SWAP para invertir el orden de los qubits y coincidir con la convención estándar.

## 💻 Simulaciones Computacionales

A continuación, una simulación de la Transformada de Fourier Cuántica (QFT) sobre estados computacionales utilizando tensores.

```python
import numpy as np
import matplotlib.pyplot as plt

def qft_matrix(n):
    N = 2**n
    omega = np.exp(2j * np.pi / N)
    matrix = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            matrix[i, j] = omega ** (i * j)
    return matrix / np.sqrt(N)

def simulate_qft(n_qubits, input_state_idx):
    N = 2**n_qubits
    state = np.zeros(N, dtype=complex)
    state[input_state_idx] = 1.0
    
    qft_op = qft_matrix(n_qubits)
    out_state = qft_op @ state
    
    return out_state

n = 3
input_idx = 3 # Estado |011>
out_state = simulate_qft(n, input_idx)

phases = np.angle(out_state)
magnitudes = np.abs(out_state)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(range(2**n), magnitudes**2, color='teal')
ax1.set_title("Magnitud (Probabilidades) post-QFT")
ax1.set_xticks(range(2**n))

ax2.stem(range(2**n), phases, linefmt='orange', markerfmt='D')
ax2.set_title("Fases Complejas post-QFT (Radianes)")
ax2.set_xticks(range(2**n))
plt.show()
```

## 🚀 Fronteras de Investigación y Problemas Abiertos

La simulación cuántica a 2026 se encuentra inmersa en el paradigma de la simulación cuántica analógica-híbrida (VQE avanzado y Trotterización dinámica).
- **El Problema del Signo Fermiónico en el Espacio de Hilbert:** Aunque los simuladores cuánticos teóricamente soslayan el problema del signo (Fermionic Sign Problem) de Monte Carlo Cuántico Clásico, la implementación física de hamiltonianos fuertemente correlacionados (como el modelo de Hubbard en 2D cerca del dopaje crítico) exige un mapeo de Fermión-a-Qubit (Bravyi-Kitaev o Jordan-Wigner). Este mapeo propaga errores lógicos de manera no local.
- **Hamiltonianos No Hermíticos y Sistemas Abiertos:** Simular dinámica disipativa acoplada a baños markovianos es un problema activo. El uso del algoritmo de simulación cuántica universal para la ecuación maestra de Lindblad sufre cuellos de botella en la inicialización estocástica (Quantum State Preparation) y el purgado de entropía.
- **Errores de Trotter y Complejidad QMA:** Reducir drásticamente los errores empíricos del producto Trotter-Suzuki, implementando aleatorización de Trotter o simulación guiada por qDrift. Entender qué subconjuntos de simulaciones moleculares recaen en QMA-Completo, lo cual implicaría que ni siquiera un ordenador cuántico puede calcular su estado fundamental eficientemente.

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

La simulación de sistemas cuánticos exige la utilización del marco del **Álgebra de Operadores y la Topología Simpléctica**. 

Considerando la simulación cuántica de campos bosónicos, el espacio de fases cuántico es infinito-dimensional. Introducimos el álgebra del conmutador de variables conjugadas generadoras de transformaciones simplécticas. Para el formalismo Gaussiano y las simulaciones GBS (Gaussian Boson Sampling), los estados se representan a través de matrices de covarianza en el grupo simpléctico $\text{Sp}(2M, \mathbb{R})$.

Para simulaciones moleculares de muchos cuerpos, la geometría del Ansatz (el espacio paramétrico $\mathcal{M}$ explorado por un circuito de la forma $|\psi(\vec{\theta})\rangle$) se equipa con la **Métrica de Fubini-Study**, que provee una estructura de variedad de Kähler al espacio de rayos proyectivos $\mathbb{CP}^{2^n-1}$. La métrica empírica es el Tensor de Información Cuántica (QGT) y su parte real es el Tensor Métrico Cuántico (QMT):

$$ g_{\mu \nu}(\vec{\theta}) = \text{Re}\left( \langle \partial_\mu \psi(\vec{\theta}) | \partial_\nu \psi(\vec{\theta}) \rangle - \langle \partial_\mu \psi(\vec{\theta}) | \psi(\vec{\theta}) \rangle \langle \psi(\vec{\theta}) | \partial_\nu \psi(\vec{\theta}) \rangle \right) $$

Para que el VQE escape de la trampa topológica de los mínimos locales, la optimización geométrica requiere la ecuación de flujo del Descenso Gradiente Cuántico Natural:

$$ \dot{\theta}^\mu = - \eta \sum_\nu g^{\mu \nu}(\vec{\theta}) \frac{\partial E(\vec{\theta})}{\partial \theta^\nu} $$

En 2026, la teoría del transporte óptimo en variedades singulares se emplea para demostrar rigurosamente que ciertas parametrizaciones dinámicas del álgebra de Lie limitan las holonomías adiabáticas no deseadas, posibilitando la simulación hamiltoniana tolerante al ruido topológico.

## 📚 Recursos Específicos

### Cursos Recomendados
1. [Quantum Computing and Simulation (Coursera)](https://www.coursera.org/learn/quantum-computing-simulation)
2. [Simulating Nature with Quantum Computers (edX)](https://www.edx.org/course/simulating-nature)
3. [Quantum Information Science I (MITx on edX)](https://www.edx.org/course/quantum-information-science-i-part-1)

### Artículos y Simulaciones
1. **Simulating Physics with Computers (R. Feynman, 1982)**
   - **Enlace:** [https://doi.org/10.1007/BF02650179](https://doi.org/10.1007/BF02650179)
   - **Importancia Teórica:** El artículo que dio origen a la computación cuántica al sugerir que solo una máquina basada en las reglas cuánticas podría simular mecánicas cuánticas sin un coste exponencial.
   - **Fondo Matemático:** Feynman examinó la probabilidad intrínseca y la no-localidad en el espacio de configuración completo de las variables, postulando un simulador universal $U(t) = e^{-iHt}$.
   - **Implicaciones Físicas:** Inició la búsqueda de hardware cuántico para superar las limitaciones de la simulación clásica en química cuántica y la física de materia condensada.

2. **Universal Quantum Simulators (S. Lloyd, 1996)**
   - **Enlace:** [https://science.sciencemag.org/content/273/5278/1073](https://science.sciencemag.org/content/273/5278/1073)
   - **Importancia Teórica:** Formaliza la intuición de Feynman, probando matemáticamente que un simulador cuántico universal puede operar eficientemente simulando sistemas locales.
   - **Fondo Matemático:** Emplea la expansión de Suzuki-Trotter para dividir el Hamiltoniano total $H = \sum_j H_j$ en pasos manejables, limitando el error de los conmutadores no nulos:

     $$

     e^{-i H t} \approx \left( \prod_j e^{-i H_j \Delta t} \right)^{t/\Delta t}

     $$

   - **Implicaciones Físicas:** Garantiza la viabilidad de la simulación molecular dinámica, reduciendo la barrera teórica de la simulación de materiales exóticos.

3. **A variational eigenvalue solver on a photonic quantum processor (Peruzzo et al., 2014)**
   - **Enlace:** [https://arxiv.org/abs/1304.3061](https://arxiv.org/abs/1304.3061)
   - **Importancia Teórica:** Introduce el Variational Quantum Eigensolver (VQE), un algoritmo híbrido cuántico-clásico, resiliente al ruido y pilar de los algoritmos NISQ actuales.
   - **Fondo Matemático:** Usa el principio variacional de Rayleigh-Ritz:

     $$

     E_0 \leq \frac{\langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle}{\langle \psi(\vec{\theta}) | \psi(\vec{\theta}) \rangle}

     $$

     donde $|\psi(\vec{\theta})\rangle$ es un ansatz parametrizado, y la CPU clásica optimiza $\vec{\theta}$ mediante gradiente descendente estocástico.
   - **Implicaciones Físicas:** Hizo realizable la química cuántica de moléculas pequeñas con el hardware ruidoso de la era contemporánea.

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
