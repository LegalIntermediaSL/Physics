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
* **MIT 8.04:** Clases dedicadas a pozos cuadrados, dispersión en escalones de potencial y el oscilador armónico.
* **Stanford (Susskind):** Oscilador armónico cuántico usando operadores escalera (algebraico).
* **NPTEL (Indian Institutes of Technology):** Quantum Mechanics I, enfoque en soluciones analíticas y matemáticas de 1D.

### 📝 Artículos e Interactivos Interesantes
* **PhET Interactive Simulations:** *Quantum Bound States* (Visualiza niveles de energía en distintos pozos de potencial).
* **PhET Interactive Simulations:** *Quantum Tunneling and Wave Packets* (Simulación en tiempo real del efecto túnel a través de barreras).
* **Wikipedia / HyperPhysics:** Artículos sobre "Partícula en una caja" y "Oscilador armónico cuántico" con tablas detalladas de los polinomios de Hermite.
