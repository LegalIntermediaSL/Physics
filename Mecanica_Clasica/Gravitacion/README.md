# Gravitación

La fuerza que mantiene unida la estructura del cosmos a gran escala. Históricamente, fue la primera fuerza fundamental en ser matematizada y sigue siendo un campo de intensa investigación moderna.

## 📜 Contexto Histórico
Las **Leyes de Kepler** (1609-1619) describían empíricamente cómo se movían los planetas en elipses a diferentes velocidades, basadas en los increíbles datos observacionales de Tycho Brahe. Décadas después, **Isaac Newton** (1687) revolucionó la ciencia al formular su *Ley de Gravitación Universal*, demostrando matemáticamente que la *misma* fuerza invisible que hacía caer las manzanas de los árboles era la responsable de atar la Luna en su órbita terrestre y validar con total precisión cada una de las empíricas leyes de Kepler.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Ley de Gravitación Universal de Newton
Entre cualquier par de masas puntuales $m_1$ y $m_2$ separadas por una distancia $r$, existe una fuerza de atracción mutua:
$ \vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{r} $
Donde $G = 6.6743 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$. El signo negativo indica que la fuerza es atractiva. 

### 2. Campo Gravitatorio ($\vec{g}$)
El campo generado por una masa $M$ en su entorno. Es la fuerza por unidad de masa de prueba:
$ \vec{g} = \frac{\vec{F}_g}{m} = -G \frac{M}{r^2} \hat{r} $
En la superficie de la Tierra ($M_T, R_T$), $g \approx 9.81 \text{ m/s}^2$.

### 3. Energía Potencial Gravitacional ($U$)
Para una fuerza conservativa que depende de $1/r^2$, la energía potencial (tomando el nivel cero en $r=\infty$) se calcula integrando:
$ U(r) = - \int_{\infty}^{r} \left(-G \frac{m_1 m_2}{r^2}\right) dr = -G \frac{m_1 m_2}{r} $
Esta es la energía de "enlace". Es negativa porque debemos suministrar energía (hacer trabajo positivo) para separar las masas hasta el infinito.

### 4. Leyes de Kepler Derivadas
Con el cálculo de Newton, la tercera ley de Kepler se deriva fácilmente para órbitas circulares igualando la fuerza centrípeta y la gravitacional:
$ \frac{m v^2}{r} = G \frac{M m}{r^2} \implies v^2 = \frac{GM}{r} $
Dado que la velocidad orbital es $v = \frac{2\pi r}{T}$ (donde $T$ es el periodo orbital):
$ \left(\frac{2\pi r}{T}\right)^2 = \frac{GM}{r} \implies \frac{4\pi^2 r^2}{T^2} = \frac{GM}{r} \implies \mathbf{T^2 = \left(\frac{4\pi^2}{GM}\right) r^3} $
*(El cuadrado del periodo es proporcional al cubo de la distancia orbital).*

---

## 🛠 Ejemplo Práctico: Velocidad de Escape
¿A qué velocidad $v_{esc}$ debes disparar un proyectil de masa $m$ desde la superficie terrestre ($M$, $R$) para que nunca vuelva a caer, escapando hasta el infinito?

**Solución**:
1. Usamos la conservación de la energía mecánica $E_i = E_f$.
2. En la superficie: $E_i = K_i + U_i = \frac{1}{2}m v_{esc}^2 - G \frac{mM}{R}$.
3. Para apenas escapar, su velocidad al llegar al infinito ($r \to \infty$) será exactamente cero: $E_f = K_f + U_f = 0 + 0 = 0$.
4. Igualamos:
   $ \frac{1}{2}m v_{esc}^2 - G \frac{mM}{R} = 0 $
5. Despejando $v_{esc}$ (nota que no depende de la masa $m$ del cohete):
   $ \mathbf{v_{esc} = \sqrt{\frac{2GM}{R}}} $
   Para la Tierra, esto equivale a unos espectaculares $11.2 \text{ km/s}$.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. [MIT 8.01 - Universal Gravity (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-10-rotational-energy/): Cubre las Leyes de Kepler y el concepto de energía en el espacio profundo.
2. [Yale PHYS 200 - Lecture 7: Universal Gravitation](https://oyc.yale.edu/physics/phys-200/lecture-7): Deducción formal del cálculo orbital y masas reducidas.
3. [Khan Academy - Gravitación](https://es.khanacademy.org/science/physics/centripetal-force-and-gravitation): Excelente guía de paso a paso.

### 📝 Artículos e Interactivos Interesantes
1. **Artículo Histórico**: [Kepler's Discovery of the Laws of Planetary Motion (Scholarpedia)](http://www.scholarpedia.org/article/Kepler%27s_laws_of_planetary_motion).
2. **Artículo (Cavendish)**: [El Experimento de Cavendish (Wikipedia)](https://es.wikipedia.org/wiki/Experimento_de_Cavendish) - Cómo la humanidad "pesó" la Tierra por primera vez usando una balanza de torsión para calcular $G$.
3. **Simulador**: [PhET - Laboratorio de Gravedad](https://phet.colorado.edu/es/simulations/gravity-and-orbits) - Construye tu propio sistema solar y observa cómo las masas y distancias alteran las trayectorias parabólicas, hiperbólicas o elípticas.
4. **Juego Físico**: [Kerbal Space Program](https://www.kerbalspaceprogram.com/) - El mejor "simulador" lúdico del mundo para entender la mecánica orbital y las leyes de Kepler por intuición pura.
