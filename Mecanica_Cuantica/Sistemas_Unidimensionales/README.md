# Sistemas Unidimensionales

El estudio de los sistemas unidimensionales permite resolver de forma exacta la ecuación de Schrödinger y comprender fenómenos cuánticos puramente no clásicos, como la cuantización de la energía, la penetración en regiones clásicamente prohibidas y el efecto túnel.

## 📜 Contexto Histórico
* Tras el establecimiento de la ecuación de Schrödinger en 1926, los físicos aplicaron la teoría a los "modelos de juguete" más simples para ver sus consecuencias.
* **George Gamow (1928):** Aplicó el concepto de efecto túnel a través de barreras unidimensionales para explicar la desintegración alfa de los núcleos radiactivos.
* Las soluciones exactas de pozos de potencial y osciladores armónicos sentaron las bases para modelos más complejos en la física del estado sólido y la química cuántica.

---

## 🧮 Desarrollo Teórico Profundo

Resolver la ecuación de Schrödinger en una dimensión permite aislar y examinar el corazón matemático de la mecánica cuántica sin la complejidad del momento angular de las soluciones en 3D. Esto revela directamente la naturaleza de las restricciones impuestas por las condiciones de contorno y la aparición de energías cuantizadas.

### El Pozo Cuadrado Infinito (Partícula en una Caja)

Supongamos una partícula de masa $m$ en un potencial $V(x)$:
$$ V(x) = \begin{cases} 0 & \text{si } 0 < x < L \\ \infty & \text{en el exterior} \end{cases} $$
Fuera de la caja, la probabilidad de encontrar la partícula es nula debido al potencial infinito; por ende, $\psi(x) = 0$ para $x \le 0$ y $x \ge L$. 

En el interior de la caja, el Hamiltoniano es el de una partícula libre, y la ecuación de Schrödinger independiente del tiempo se reduce a:
$$ -\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} = E \psi(x) \implies \frac{d^2\psi}{dx^2} + k^2\psi = 0 \quad \text{donde } k = \frac{\sqrt{2mE}}{\hbar} $$
Esta es una ecuación diferencial ordinaria de segundo orden con coeficientes constantes. La solución general es una combinación lineal de ondas planas:
$$ \psi(x) = A\sin(kx) + B\cos(kx) $$

**Imposición de Condiciones de Contorno:**
1. $\psi(0) = 0 \implies A\sin(0) + B\cos(0) = B = 0$. La solución se reduce a $\psi(x) = A\sin(kx)$.
2. $\psi(L) = 0 \implies A\sin(kL) = 0$. Dado que $A \neq 0$ (la solución trivial no es normalizable), la función seno debe anularse, lo que implica que su argumento es un múltiplo entero de $\pi$:
$$ kL = n\pi \implies k_n = \frac{n\pi}{L}, \quad \text{con } n = 1, 2, 3, \dots $$

Al sustituir el valor cuantizado de $k_n$ en la definición de energía, descubrimos la **cuantización de la energía**:
$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2mL^2} $$
Es crucial destacar que la energía más baja posible no es cero ($E_1 > 0$). Este es el llamado nivel de punto cero, una manifestación del Principio de Incertidumbre: confinar la partícula reduce drásticamente su incertidumbre espacial $\Delta x$, lo que fuerza un aumento en la incertidumbre del momento $\Delta p$ y, en consecuencia, en la energía cinética promedio.

Aplicando la condición de normalización $\int_0^L |A\sin(n\pi x / L)|^2 dx = 1$, encontramos la amplitud $A = \sqrt{2/L}$. Las autofunciones resultan:
$$ \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) $$

```mermaid
graph LR
    A[Potencial Confinante: V=inf en los bordes] --> B(Ecuación de Onda Libre Interna)
    B --> C{Condiciones de Contorno psi=0}
    C -->|B=0| D[Soluciones Senoidales]
    C -->|kL = n*pi| E[k cuantizado]
    E --> F[Energía Cuantizada En]
    D --> G[Autofunciones con Nodos n-1]
    F --> H[Nivel Mínimo E1 > 0]
```

### El Oscilador Armónico Cuántico: Enfoque Algebraico

El potencial armónico clásico $V(x) = \frac{1}{2}m\omega^2 x^2$ es fundamental, ya que aproxima el comportamiento de cualquier potencial cerca de un punto de equilibrio estable (expansión de Taylor).
El Hamiltoniano cuántico es:
$$ \hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 $$
En lugar de resolver la complicada ecuación diferencial que involucra polinomios de Hermite, Paul Dirac introdujo el método algebraico de operadores de creación y aniquilación (u operadores escalera). Definimos operadores adimensionales, no hermitianos:
$$ \hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left( \hat{x} + \frac{i}{m\omega}\hat{p} \right), \quad \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left( \hat{x} - \frac{i}{m\omega}\hat{p} \right) $$
Se puede demostrar, a partir del conmutador fundamental $[\hat{x}, \hat{p}] = i\hbar$, que:
$$ [\hat{a}, \hat{a}^\dagger] = 1 $$
Reescribiendo el Hamiltoniano en términos de estos operadores:
$$ \hat{H} = \hbar\omega \left( \hat{a}^\dagger\hat{a} + \frac{1}{2} \right) $$
Si actuamos con $\hat{H}$ sobre el estado modificado $\hat{a}|n\rangle$, se comprueba que disminuye la energía en $\hbar\omega$; por eso $\hat{a}$ es el **operador de aniquilación** o descenso. De manera análoga, $\hat{a}^\dagger$ la aumenta, siendo el **operador de creación**. 

Para evitar un colapso hacia energías negativas infinitas (lo cual violaría la positividad del espectro), debe existir un estado fundamental mínimo $|0\rangle$ tal que la aplicación de $\hat{a}$ lo anule: $\hat{a}|0\rangle = 0$.
A partir de aquí, la energía del estado fundamental es:
$$ \hat{H}|0\rangle = \hbar\omega \left( 0 + \frac{1}{2} \right)|0\rangle = \frac{1}{2}\hbar\omega |0\rangle \implies E_0 = \frac{1}{2}\hbar\omega $$
Los autoestados excitados superiores se obtienen aplicando iterativamente el operador escalera de subida:
$$ E_n = \hbar\omega \left( n + \frac{1}{2} \right), \quad n=0, 1, 2, \dots $$
Este espectro está igualmente espaciado.

### Efecto Túnel Cuántico

Una característica contraria a la intuición surge cuando resolvemos la ecuación de Schrödinger para una barrera de potencial de altura $V_0$ y ancho $a$, sobre la cual incide una partícula con energía $E < V_0$. Clásicamente, la partícula rebotaría con un 100% de certeza en el punto de retorno.

Cuantitativamente, la ecuación en la zona prohibida (dentro de la barrera $0 \le x \le a$) es:
$$ \frac{d^2\psi}{dx^2} = \frac{2m(V_0 - E)}{\hbar^2} \psi = \kappa^2 \psi $$
Donde $\kappa$ es una constante real. La solución no oscila, sino que decrece exponencialmente:
$$ \psi(x) = C e^{-\kappa x} + D e^{+\kappa x} $$
Empalmando las funciones de onda y sus primeras derivadas (condiciones de continuidad) en las fronteras de la barrera $x=0$ y $x=a$, se descubre que la amplitud de la onda en la región más allá de la barrera ($x > a$) no es cero. La partícula tiene una probabilidad de "hacer un túnel".
El coeficiente de transmisión $T$ para una barrera ancha y alta decae exponencialmente de la forma:
$$ T \approx e^{-2\kappa a} = \exp\left( -2a \frac{\sqrt{2m(V_0 - E)}}{\hbar} \right) $$
Este fenómeno explica procesos tan diversos como la desintegración radiactiva alfa, el funcionamiento de microscopios de efecto túnel (STM) y las fusiones nucleares en los centros estelares, que ocurren a temperaturas "demasiado frías" para superar clásicamente las barreras de repulsión de Coulomb.

---

## 🛠 Ejemplo Práctico
**Problema:** Una partícula se encuentra en el estado fundamental de un pozo infinito de potencial unidimensional de anchura $L$. ¿Cuál es la probabilidad de encontrar a la partícula en el tercio central de la caja, es decir, entre $x = L/3$ y $x = 2L/3$?

**Solución paso a paso:**
1. La función de onda del estado fundamental ($n=1$) es:
$$ \psi_1(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{\pi x}{L}\right) $$
2. La densidad de probabilidad es $P(x) = |\psi_1(x)|^2 = \frac{2}{L} \sin^2\left(\frac{\pi x}{L}\right)$.
3. Calculamos la integral de probabilidad en el intervalo pedido:
$$ P = \int_{L/3}^{2L/3} \frac{2}{L} \sin^2\left(\frac{\pi x}{L}\right) dx $$
4. Usamos la identidad trigonométrica $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$:
$$ P = \frac{2}{L} \int_{L/3}^{2L/3} \frac{1 - \cos\left(\frac{2\pi x}{L}\right)}{2} dx = \frac{1}{L} \left[ x - \frac{L}{2\pi}\sin\left(\frac{2\pi x}{L}\right) \right]_{L/3}^{2L/3} $$
5. Evaluamos en los límites:
$$ P = \frac{1}{L} \left[ \left( \frac{2L}{3} - \frac{L}{2\pi}\sin\left(\frac{4\pi}{3}\right) \right) - \left( \frac{L}{3} - \frac{L}{2\pi}\sin\left(\frac{2\pi}{3}\right) \right) \right] $$
Sabiendo que $\sin(4\pi/3) = -\sqrt{3}/2$ y $\sin(2\pi/3) = \sqrt{3}/2$:
$$ P = \frac{1}{L} \left[ \frac{L}{3} - \frac{L}{2\pi}\left(-\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2}\right) \right] = \frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 0.333 + 0.276 = 0.609 $$
La probabilidad es del 60.9%, mucho mayor al 33.3% clásico esperado, debido a que la onda de probabilidad "se abulta" en el centro.

---

## 📝 Guía de Ejercicios Resueltos

**Problema 1: Potencial Delta Atractivo de Dirac**
Encuentra el estado ligado y su energía para una partícula de masa $m$ bajo la influencia de un potencial de pozo de la forma $V(x) = -\alpha \delta(x)$ con $\alpha > 0$.
**Solución paso a paso:**
1. La ecuación de Schrödinger es $-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} - \alpha \delta(x)\psi = E\psi$.
2. Para $x \neq 0$, $V=0$. Las soluciones acotadas para estados ligados ($E < 0$) son ondas evanescentes: $\psi(x) = A e^{-\kappa x}$ (para $x>0$) y $\psi(x) = A e^{+\kappa x}$ (para $x<0$), donde $\kappa = \sqrt{-2mE}/\hbar$. Podemos escribir $\psi(x) = A e^{-\kappa |x|}$.
3. Integramos la ecuación de Schrödinger en un intervalo $[-\epsilon, +\epsilon]$ alrededor del origen y tomamos el límite $\epsilon \to 0$:
$$ -\frac{\hbar^2}{2m} \left( \left. \frac{d\psi}{dx} \right|_{0^+} - \left. \frac{d\psi}{dx} \right|_{0^-} \right) - \alpha \psi(0) = 0 $$
4. Calculamos los saltos de las derivadas en $x=0$:
$$ \left. \frac{d\psi}{dx} \right|_{0^+} = -A\kappa, \quad \left. \frac{d\psi}{dx} \right|_{0^-} = +A\kappa $$
5. Sustituimos en la condición de discontinuidad: $-\frac{\hbar^2}{2m} (-2A\kappa) = \alpha A$.
6. Simplificando obtenemos $\frac{\hbar^2 \kappa}{m} = \alpha \implies \kappa = \frac{m\alpha}{\hbar^2}$.
7. Recordando que $E = -\frac{\hbar^2 \kappa^2}{2m}$, la energía del único estado ligado es $E_0 = -\frac{m\alpha^2}{2\hbar^2}$.

**Problema 2: Barrera de Potencial y Aproximación WKB**
Estima el coeficiente de transmisión $T$ para una barrera de potencial parabólica invertida $V(x) = V_0 - \frac{1}{2}kx^2$ usando la aproximación WKB para un electrón de energía $E < V_0$.
**Solución paso a paso:**
1. La aproximación WKB para el coeficiente de transmisión es $T \approx \exp\left( -2 \int_{x_1}^{x_2} \kappa(x) dx \right)$, donde $\kappa(x) = \frac{\sqrt{2m(V(x) - E)}}{\hbar}$.
2. Encontramos los puntos de retorno $x_1, x_2$ igualando $E = V(x)$:
$$ E = V_0 - \frac{1}{2}kx^2 \implies x_{1,2} = \pm \sqrt{\frac{2(V_0 - E)}{k}} $$
3. Evaluamos la integral $I = \int_{-x_0}^{x_0} \sqrt{2m \left( V_0 - E - \frac{1}{2}kx^2 \right)} dx$, donde $x_0 = \sqrt{\frac{2(V_0 - E)}{k}}$.
4. Esta integral tiene la forma del área de un semi-círculo/elipse. Sea $V_0 - E = \Delta E$:
$$ I = \sqrt{mk} \int_{-x_0}^{x_0} \sqrt{x_0^2 - x^2} dx $$
5. La integral matemática $\int_{-a}^a \sqrt{a^2-x^2} dx = \frac{\pi}{2}a^2$.
6. Así, $I = \sqrt{mk} \frac{\pi}{2} x_0^2 = \sqrt{mk} \frac{\pi}{2} \frac{2\Delta E}{k} = \pi \Delta E \sqrt{\frac{m}{k}}$.
7. Notando que la frecuencia natural del oscilador parabólico es $\omega = \sqrt{k/m}$, $I = \frac{\pi \Delta E}{\omega}$.
8. Sustituyendo en $T$: $T \approx \exp\left( -2 \frac{I}{\hbar} \right) = \exp\left( -\frac{2\pi(V_0 - E)}{\hbar\omega} \right)$.

**Problema 3: Base del Oscilador Armónico e Incertidumbre**
Para el estado fundamental $|0\rangle$ del oscilador armónico cuántico, demuestra explícitamente usando los operadores de creación y aniquilación que se minimiza el principio de incertidumbre de Heisenberg ($\Delta x \Delta p = \hbar / 2$).
**Solución paso a paso:**
1. Definimos $\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger)$ y $\hat{p} = -i\sqrt{\frac{m\hbar\omega}{2}}(\hat{a} - \hat{a}^\dagger)$.
2. En el estado base, $\langle 0 | \hat{x} | 0 \rangle = 0$ y $\langle 0 | \hat{p} | 0 \rangle = 0$ debido a la simetría de paridad y las propiedades de $\hat{a}|0\rangle = 0$.
3. Calculamos $\langle \hat{x}^2 \rangle = \frac{\hbar}{2m\omega} \langle 0 | (\hat{a} + \hat{a}^\dagger)^2 | 0 \rangle$.
Al expandir: $\hat{a}^2 + \hat{a}\hat{a}^\dagger + \hat{a}^\dagger\hat{a} + (\hat{a}^\dagger)^2$. Los términos $\hat{a}^2$ y $(\hat{a}^\dagger)^2$ cambian el estado en $\pm 2$ cuantos, dando un producto interno cero con $|0\rangle$.
4. Usamos el conmutador $[\hat{a}, \hat{a}^\dagger] = 1 \implies \hat{a}\hat{a}^\dagger = 1 + \hat{a}^\dagger\hat{a}$.
Así, $\langle 0 | \hat{a}\hat{a}^\dagger | 0 \rangle = 1 + \langle 0|\hat{a}^\dagger\hat{a}|0\rangle = 1 + 0 = 1$.
5. Por lo tanto, $(\Delta x)^2 = \langle \hat{x}^2 \rangle = \frac{\hbar}{2m\omega}$.
6. Del mismo modo para $\langle \hat{p}^2 \rangle = -\frac{m\hbar\omega}{2} \langle 0 | (\hat{a} - \hat{a}^\dagger)^2 | 0 \rangle$.
Expansión arroja un término útil $-\hat{a}\hat{a}^\dagger$, que aporta $-1$.
7. $(\Delta p)^2 = \langle \hat{p}^2 \rangle = \frac{m\hbar\omega}{2}$.
8. Multiplicando las varianzas: $(\Delta x)^2(\Delta p)^2 = \left( \frac{\hbar}{2m\omega} \right) \left( \frac{m\hbar\omega}{2} \right) = \frac{\hbar^2}{4}$.
Tomando la raíz cuadrada, obtenemos $\Delta x \Delta p = \hbar / 2$, el límite inferior exacto.

## 💻 Simulaciones Computacionales

A continuación se presenta un script que calcula y grafica numéricamente las funciones de onda (eigenestados) y los niveles de energía del oscilador armónico cuántico resolviendo el problema de autovalores del Hamiltoniano mediante un esquema de diferencias finitas de matriz dispersa.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

# Parámetros del espacio y del oscilador
N = 1000        # Puntos de la malla
L = 10.0        # Dimensión de la caja
x = np.linspace(-L/2, L/2, N)
dx = x[1] - x[0]

# Constantes físicas (unidades naturales: m=1, hbar=1)
m = 1.0
hbar = 1.0
omega = 1.0

# Potencial del oscilador armónico V(x) = (1/2)*m*omega^2*x^2
V = 0.5 * m * omega**2 * x**2

# Construcción del Hamiltoniano H = T + V usando diferencias finitas
# Derivada segunda: d^2/dx^2 f_i approx (f_{i+1} - 2f_i + f_{i-1}) / dx^2
t_coeff = -hbar**2 / (2.0 * m * dx**2)

main_diag = -2.0 * t_coeff * np.ones(N) + V
off_diag = t_coeff * np.ones(N-1)

H = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csc')

# Resolviendo para los primeros 5 autoestados
num_eigenstates = 5
eigenvalues, eigenvectors = eigsh(H, k=num_eigenstates, which='SM')

# Graficando
plt.figure(figsize=(10, 7))
plt.plot(x, V, color='black', linewidth=2, label='Potencial Armónico $V(x)$')

# Escala para la visualización de las funciones de onda
scale = 2.0 

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i in range(num_eigenstates):
    E = eigenvalues[i]
    psi = eigenvectors[:, i]
    # Aseguramos un signo consistente para los gráficos
    if psi[np.argmax(np.abs(psi))] < 0:
        psi = -psi
    
    # Dibujamos el nivel de energía
    plt.axhline(E, color=colors[i], linestyle='--', alpha=0.5)
    
    # Dibujamos la función de onda desplazada al nivel de energía correspondiente
    plt.plot(x, E + scale * psi, color=colors[i], 
             label=f'n={i}, $E_{i}$={E:.2f} $\hbar\omega$')

plt.xlim(-5, 5)
plt.ylim(0, max(eigenvalues) + 1)
plt.xlabel('Posición (x)')
plt.ylabel('Energía / Amplitud de Onda')
plt.title('Estados Ligados del Oscilador Armónico Cuántico (1D)')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
# plt.show() # Descomentar para visualizar
```

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. [MIT 8.04 Quantum Physics I (Allan Adams)](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/): Serie de clases meticulosamente dedicadas a pozos cuadrados, pozos finitos, dispersión en escalones de potencial y funciones de onda atadas.
2. [Stanford - Quantum Mechanics (Leonard Susskind)](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtWCAh1E_yT1eF82k7bFepf): Lecciones que resuelven el oscilador armónico cuántico de manera puramente algebraica usando operadores de creación y destrucción.
3. [NPTEL Quantum Mechanics I (IIT Madras)](https://nptel.ac.in/courses/115106066): Enfoque analítico riguroso en las soluciones matemáticas de sistemas 1D, ideal para quienes buscan derivaciones paso a paso de las ecuaciones diferenciales.
4. [MIT 8.05 Quantum Physics II (Barton Zwiebach)](https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/): Repaso profundo de los potenciales en una dimensión haciendo énfasis en los teoremas generales de degeneración y nodos de la función de onda.
5. [Coursera - Quantum Mechanics (University of Colorado)](https://www.coursera.org/learn/quantum-mechanics): Análisis visual de las barreras de potencial y cálculo detallado del coeficiente de transmisión de túnel.

### 📝 Artículos e Interactivos Interesantes
1. **PhET Interactive Simulations:** [Quantum Bound States](https://phet.colorado.edu/en/simulations/bound-states) - Magnífica simulación para construir potenciales arbitrarios y visualizar los niveles de energía discretos.
2. **PhET Interactive Simulations:** [Quantum Tunneling and Wave Packets](https://phet.colorado.edu/en/simulations/quantum-tunneling) - Simulador en tiempo real que permite mandar paquetes de ondas Gaussianos hacia barreras y ver las ondas transmitidas y reflejadas.
3. **Falstad Quantum 1D Applet:** [QM 1D](http://www.falstad.com/qm1d/) - (Imprescindible) Visualiza fasores, funciones de onda, valores esperados y evolución temporal para el oscilador armónico y otras geometrías 1D.
4. **HyperPhysics:** [Particle in a Box](http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/schr.html#c3) - Descripción concisa con calculadora interactiva de energías según la anchura y masa.
5. **HyperPhysics:** [Quantum Harmonic Oscillator](http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hosc.html) - Resume maravillosamente las energías y grafica las distribuciones probabilísticas contra el caso clásico.
6. **Wikipedia:** [Oscilador Armónico Cuántico](https://es.wikipedia.org/wiki/Oscilador_arm%C3%B3nico_cu%C3%A1ntico) - Artículo completo, incluye tablas con las formas explícitas de los polinomios de Hermite.
7. **Wikipedia:** [Efecto Túnel](https://es.wikipedia.org/wiki/Efecto_t%C3%BAnel) - Artículo teórico sobre el cálculo matemático, la aproximación WKB y aplicaciones.
8. **Wolfram Demonstrations Project:** [Harmonic Oscillator Wavefunctions](https://demonstrations.wolfram.com/HarmonicOscillatorWavefunctions/) - Manipula los parámetros $n$ y $\omega$ para visualizar la probabilidad cuántica y su límite clásico.

### 📖 Referencias Útiles y Bibliografía
1. **Libro**: [Introduction to Quantum Mechanics - David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-quantum-mechanics/990799252758F46C8765A2C3946C342C) (Capítulo 2). El estándar de oro. Todo el capítulo está dedicado a problemas en 1D: pozo infinito, oscilador, partícula libre y barrera de potencial.
2. **Libro**: [Quantum Mechanics - Claude Cohen-Tannoudji](https://www.wiley.com/en-us/Quantum+Mechanics%2C+Volume+1%3A+Basic+Concepts%2C+Tools%2C+and+Applications%2C+2nd+Edition-p-9783527345533) (Vol. 1). Aborda en detalle los complementos matemáticos y soluciones hipergeométricas para potenciales en una dimensión.
3. **Libro**: [Principles of Quantum Mechanics - R. Shankar](https://link.springer.com/book/10.1007/978-1-4615-7675-4) (Capítulos 5 y 7). Su resolución analítica y algebraica del oscilador armónico unidimensional es insuperable.
4. **Libro**: [Feynman Lectures on Physics - Richard Feynman](https://www.feynmanlectures.caltech.edu/III_toc.html) (Vol. III). Aporta una perspectiva única sobre los estados base en el amoníaco y cómo modelos simples 1D explican moléculas complejas.
