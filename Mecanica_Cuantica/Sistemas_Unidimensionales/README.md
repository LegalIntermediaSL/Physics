# Sistemas Unidimensionales

El estudio de los sistemas unidimensionales permite resolver de forma exacta la ecuación de Schrödinger y comprender fenómenos cuánticos puramente no clásicos, como la cuantización de la energía, la penetración en regiones clásicamente prohibidas y el efecto túnel.

## 📜 Contexto Histórico
* Tras el establecimiento de la ecuación de Schrödinger en 1926, los físicos aplicaron la teoría a los "modelos de juguete" más simples para ver sus consecuencias.
* **George Gamow (1928):** Aplicó el concepto de efecto túnel a través de barreras unidimensionales para explicar la desintegración alfa de los núcleos radiactivos.
* Las soluciones exactas de pozos de potencial y osciladores armónicos sentaron las bases para modelos más complejos en la física del estado sólido y la química cuántica.

---

## 🧮 Desarrollo Teórico Profundo

### La Partícula en una Caja (Pozo Infinito)
Consideremos un potencial:
$$ V(x) = \begin{cases} 0 & \text{si } 0 < x < L \\ \infty & \text{en cualquier otro lugar} \end{cases} $$
Dentro de la caja, la ecuación es $-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} = E\psi$. La solución general es $\psi(x) = A\sin(kx) + B\cos(kx)$, con $k = \sqrt{2mE}/\hbar$.
Condiciones de contorno: $\psi(0) = \psi(L) = 0$.
Esto fuerza $B=0$ y $kL = n\pi$ para $n=1,2,3,\dots$.
Energías cuantizadas:
$$ E_n = \frac{n^2\pi^2\hbar^2}{2mL^2} $$
Funciones de onda normalizadas:
$$ \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) $$

### Oscilador Armónico Cuántico
El potencial es $V(x) = \frac{1}{2}m\omega^2 x^2$. La solución a la ecuación de Schrödinger lleva a polinomios de Hermite. Sin embargo, usando operadores de creación ($\hat{a}^\dagger$) y aniquilación ($\hat{a}$), encontramos que las energías están discretizadas e igualmente espaciadas:
$$ E_n = \hbar\omega \left( n + \frac{1}{2} \right), \quad n=0,1,2,\dots $$
La energía del punto cero es $E_0 = \hbar\omega/2$, una consecuencia directa del principio de incertidumbre.

### Barreras de Potencial y Efecto Túnel
Cuando una partícula de energía $E$ encuentra una barrera de altura $V_0 > E$ y anchura $a$, clásicamente debería rebotar. Cuánticamente, la función de onda en la región de la barrera es una exponencial decreciente $\sim e^{-\kappa x}$ con $\kappa = \sqrt{2m(V_0-E)}/\hbar$. Si la barrera es lo suficientemente delgada, hay una probabilidad no nula de que la partícula atraviese (coeficiente de transmisión $T > 0$).

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
