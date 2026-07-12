# Teoría Cinética de los Gases

La teoría cinética de los gases proporciona una descripción microscópica y mecánica del comportamiento macroscópico de los gases. Sustituye la visión continua de la termodinámica por un modelo estadístico de un número inmenso de partículas diminutas en movimiento constante y aleatorio.

## 📜 Contexto Histórico
La idea atómica de la materia se originó en la Antigua Grecia, pero Daniel Bernoulli (1738) fue el primero en derivar la ley de Boyle a partir de colisiones de partículas. En la segunda mitad del siglo XIX, James Clerk Maxwell y Ludwig Boltzmann desarrollaron esta idea formalmente, creando la distribución de velocidades de Maxwell-Boltzmann. Ellos establecieron cómo la temperatura macroscópica se correlaciona con la energía cinética microscópica. Posteriormente, el trabajo de Albert Einstein en 1905 sobre el movimiento browniano proporcionó la confirmación definitiva de la realidad física de átomos y moléculas.

---

## 🧮 Desarrollo Teórico Profundo

### Hipótesis del Gas Ideal
El modelo asume:
1. El gas consta de moléculas idénticas de tamaño insignificante en comparación con la distancia promedio entre ellas.
2. Las moléculas no interactúan excepto durante las colisiones.
3. Las colisiones con las paredes son perfectamente elásticas.

### Derivación de la Presión
Si una partícula de masa $m$ se mueve con velocidad $v_x$ hacia una pared de área $A$, en un choque elástico el cambio de momento es $\Delta p_x = 2mv_x$.
El tiempo entre choques contra la misma pared en una caja de longitud $L$ es $\Delta t = \frac{2L}{v_x}$.
La fuerza promediada por una partícula es $F_1 = \frac{\Delta p_x}{\Delta t} = \frac{m v_x^2}{L}$.
Para $N$ partículas, la presión $P = F_{\text{total}}/A$ resulta:
$$ P = \frac{N m \langle v_x^2 \rangle}{A L} = \frac{N m \langle v_x^2 \rangle}{V} $$
Por isotropía espacial, $\langle v_x^2 \rangle = \frac{1}{3} \langle v^2 \rangle$, entonces:
$$ P = \frac{1}{3} \frac{N m \langle v^2 \rangle}{V} $$

### Temperatura y Energía Cinética Promedio
Igualando la expresión anterior con la ecuación macroscópica de los gases ideales ($PV = N k_B T$):
$$ N k_B T = \frac{1}{3} N m \langle v^2 \rangle $$
$$ \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T $$
Esto demuestra que la energía cinética traslacional media de una molécula es directamente proporcional a la temperatura absoluta.

### Teorema de Equipartición de la Energía
Establece que, en equilibrio térmico, cada grado de libertad cuadrático (como posiciones o momentos) contribuye en promedio con $\frac{1}{2} k_B T$ a la energía del sistema.
Para un gas ideal con $f$ grados de libertad (traslacionales, rotacionales, vibracionales):
$$ U = N \frac{f}{2} k_B T $$
Lo cual determina la capacidad calorífica $C_V = \frac{f}{2} N k_B$.

---

## 🛠 Ejemplo Práctico
**Problema:** Determinar la velocidad cuadrática media ($v_{\text{rms}}$) de las moléculas de gas oxígeno (O$_2$) a una temperatura de $T = 300\text{ K}$.

**Solución paso a paso:**
1. **Identificar la masa molar del oxígeno:** La molécula diatómica O$_2$ tiene una masa molar aproximada de $M = 32\text{ g/mol} = 0.032\text{ kg/mol}$.
2. **Relacionar $k_B$ y la masa molecular con $R$ y la masa molar:**
   La constante de Boltzmann es $k_B = R/N_A$, y la masa molecular es $m = M/N_A$.
3. **Aplicar la fórmula de $v_{\text{rms}}$:**
   Por definición, $v_{\text{rms}} = \sqrt{\langle v^2 \rangle}$. De la teoría cinética:
   $$ \langle v^2 \rangle = \frac{3 k_B T}{m} = \frac{3 R T}{M} $$
4. **Sustituir los valores:**
   Usamos $R \approx 8.314\text{ J/(mol}\cdot\text{K)}$:
   $$ v_{\text{rms}} = \sqrt{\frac{3 \times 8.314 \times 300}{0.032}} $$
   $$ v_{\text{rms}} = \sqrt{233831.25} \approx 483.5\text{ m/s} $$
   A temperatura ambiente, ¡las moléculas de oxígeno viajan a casi $500\text{ m/s}$ (más de $1700\text{ km/h}$)!

---

## 📚 Recursos Específicos
### 🎓 Cursos y Clases Recomendadas
* **Feynman Lectures on Physics:** Vol I, Capítulos 39 (Teoría cinética de los gases) y 40 (Mecánica estadística).
* **MIT 8.044 (Statistical Physics I):** Primeras sesiones centradas en la derivación de Maxwell.
* **Stanford - Mecánica Estadística (Susskind):** Conferencias sobre el significado físico de la equipartición.

### 📝 Artículos e Interactivos Interesantes
* **PhET - Gases Intro:** Una simulación increíble para medir presiones, temperaturas y ver colisiones de partículas.
* **Artículo de Einstein de 1905 sobre el Movimiento Browniano:** Un pilar histórico para probar la teoría cinética de la materia.
* **Maxwell-Boltzmann Distribution Calculator (Hyperphysics):** Para explorar la distribución de velocidades de diferentes gases a distintas temperaturas.
