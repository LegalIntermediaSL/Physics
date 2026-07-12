# Momento Lineal y Colisiones

El momento lineal y el impulso son conceptos fundamentales derivados de la segunda ley de Newton que nos permiten analizar sistemas de múltiples partículas y eventos bruscos, como choques y explosiones, sin necesidad de conocer los intrincados detalles de las fuerzas instantáneas.

## 📜 Contexto Histórico
El concepto fue introducido formalmente por **René Descartes** como *quantitas motus* (cantidad de movimiento), argumentando que esta cantidad se conservaba en el universo. **John Wallis** y **Christopher Wren**, contemporáneos de Newton, formularon las primeras reglas precisas de las colisiones elásticas e inelásticas, demostrando empíricamente la conservación del momento antes de que Newton la derivara rigurosamente de su Tercera Ley.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Momento Lineal e Impulso
El momento lineal $\vec{p}$ de una partícula se define como:
$$ \vec{p} = m \vec{v} $$

La Segunda Ley de Newton, en su forma original más pura, es la derivada del momento:
$$ \sum \vec{F} = \frac{d\vec{p}}{dt} $$

Si multiplicamos por $dt$ e integramos durante un intervalo de tiempo $\Delta t$, obtenemos el **Teorema del Impulso y el Momento Lineal**. El impulso $\vec{J}$ es la fuerza acumulada en el tiempo:
$$ \vec{J} = \int_{t_i}^{t_f} \vec{F} dt = \Delta\vec{p} = \vec{p}_f - \vec{p}_i $$

### 2. Conservación del Momento Lineal
Para un sistema de partículas interactuando entre sí (y sin fuerzas externas netas):
$$ \sum \vec{F}_{ext} = 0 \implies \frac{d\vec{P}_{sis}}{dt} = 0 \implies \vec{P}_{sis} = \text{constante} $$
$$ m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f} $$

### 3. Tipos de Colisiones
- **Elásticas**: Se conserva tanto el momento lineal $\vec{P}$ como la energía cinética total $K$. Las partículas rebotan perfectamente.
- **Inelásticas**: Se conserva el momento lineal, pero $K$ disminuye (se disipa en calor, sonido, o deformación plástica).
- **Completamente inelásticas**: Se conserva el momento lineal, $K$ disminuye drásticamente y, de hecho, los cuerpos quedan unidos tras el choque, moviéndose con una velocidad común $\vec{v}_f$.

### 4. Centro de Masa ($\vec{r}_{CM}$)
El punto geométrico que se mueve como si toda la masa del sistema y todas las fuerzas externas estuvieran aplicadas a él.
$$ \vec{r}_{CM} = \frac{1}{M_{tot}} \sum_{i} m_i \vec{r}_i = \frac{1}{M_{tot}} \int \vec{r} \, dm $$
La velocidad del centro de masa $\vec{v}_{CM}$ es directamente proporcional al momento total del sistema: $\vec{P}_{sis} = M_{tot} \vec{v}_{CM}$.

---

## 🛠 Ejemplo Práctico: El Péndulo Balístico
Un bloque de madera de masa $M$ cuelga de dos cuerdas. Una bala de masa $m$ que viaja horizontalmente a velocidad $v_0$ se incrusta en el bloque. El conjunto se balancea hasta una altura máxima $h$. ¿Cuál era la velocidad inicial de la bala $v_0$?

**Solución**:
Este clásico problema se divide en dos fases distintas:
1. **Fase de Colisión (Completamente inelástica)**: 
   Las fuerzas impulsivas internas son inmensas, pero la fuerza externa neta horizontal es 0. Conservamos el momento, *pero no* la energía.
   $$ m v_0 = (m + M) V_{final} \implies V_{final} = \frac{m}{m+M} v_0 $$
2. **Fase de Balanceo (Conservación de Energía)**:
   La tensión de las cuerdas no hace trabajo. La única fuerza conservativa es la gravedad. Aquí se conserva la energía mecánica, *pero no* el momento (la gravedad actúa).
   Energía inicial de esta fase: $K = \frac{1}{2}(m+M)V_{final}^2$. Energía final: $U = (m+M)gh$.
   $$ \frac{1}{2}(m+M)V_{final}^2 = (m+M)gh \implies V_{final} = \sqrt{2gh} $$
3. **Igualando ecuaciones**:
   $$ \frac{m}{m+M} v_0 = \sqrt{2gh} \implies \mathbf{v_0 = \left(\frac{m+M}{m}\right) \sqrt{2gh}} $$

---

## 📚 Recursos Específicos de Momento y Colisiones

### 🎓 Cursos y Clases Recomendadas (5-7)
1. **[MIT 8.01 - Momentum and Collisions (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-5-momentum-and-impulse/)**: Impresionantes demostraciones de choques en rieles de aire sin fricción y conservación vectorial.
2. **[Yale PHYS 200 - Lecture 11: Conservation of Momentum](https://oyc.yale.edu/physics/phys-200/lecture-11)**: Profundo vínculo entre la simetría traslacional del espacio y el teorema de Noether.
3. **[Khan Academy - Momento Lineal e Impulso](https://es.khanacademy.org/science/physics/linear-momentum)**: Ejercicios para interiorizar cálculos 1D y 2D en colisiones elásticas e inelásticas.
4. **[Coursera - Physics 101 - Forces and Kinematics (Rice University)](https://www.coursera.org/learn/physics-101-forces-kinematics)**: Buena sección dedicada al impulso, coeficientes de restitución y conservación de sistemas cerrados.
5. **[edX - Momentum and Energy (MITx)](https://www.edx.org/course/mechanics-momentum-and-energy)**: Desafíos matemáticos y problemas prácticos analizando la energía perdida en las explosiones y choques inelásticos.

### 📝 Artículos, Simulaciones e Interactivos (8-10)
1. **Artículo**: [Conservation of Momentum (HyperPhysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/conser.html) - Mapas conceptuales excelentes con desgloses de ecuaciones para colisiones.
2. **Simulador**: [PhET - Laboratorio de Colisiones](https://phet.colorado.edu/es/simulations/collision-lab) - Crea colisiones 1D y 2D elásticas e inelásticas, midiendo los vectores $p$ y $K$ en tiempo real.
3. **Video Educativo**: [SmarterEveryDay - Ver balas impactar a cámara superlenta](https://www.youtube.com/watch?v=QfDoQwIAaXg) - Un acercamiento fenomenal muy visual y tangible a las colisiones puramente inelásticas.
4. **Artículo**: [Centro de Masas (Wikipedia)](https://es.wikipedia.org/wiki/Centro_de_masas) - Repaso matemático sobre los cálculos continuos (integrales) de distribuciones asimétricas.
5. **Simulador**: [Walter Fendt - Choque Elástico e Inelástico](https://www.walter-fendt.de/html5/phes/collision_es.htm) - Un applet clásico para probar fórmulas de coeficientes de restitución.
6. **Artículo**: [Rocket Equation of Tsiolkovsky (Scholarpedia)](http://www.scholarpedia.org/article/Tsiolkovsky_rocket_equation) - Estudio riguroso de cómo el momento lineal permite el viaje espacial arrojando masa hacia atrás.
7. **Video Analítico**: [Veritasium - The Bizarre Behavior of Rotating Bodies](https://www.youtube.com/watch?v=1n-HMSCDYtM) - Aunque mezcla momento angular, muestra la importancia crítica del centro de masa en colisiones excéntricas.
8. **Simulador**: [GeoGebra - Péndulo Balístico](https://www.geogebra.org/m/eUDBxK8B) - Explora las dos fases de este histórico sistema y cómo la energía se disipa.

### 📖 Referencias Útiles y Bibliografía
- **[Classical Dynamics of Particles and Systems (Marion & Thornton)](https://www.cengage.com/c/classical-dynamics-of-particles-and-systems-5e-thornton/9780534408961/)**: Contiene uno de los mejores capítulos para dominar el paso del referencial de Laboratorio al referencial del Centro de Masa.
- **[Classical Mechanics (John R. Taylor)](https://uscibooks.aip.org/books/classical-mechanics/)**: Excepcional explicación intuitiva y formal del uso del centro de masa, así como de sistemas de masa variable (cohetes y cadenas cayendo).
- **[Introduction to Classical Mechanics (David Morin)](https://www.cambridge.org/highereducation/books/introduction-to-classical-mechanics/31CB8B93623D3F14E1EE98B223D1DE47)**: Tiene decenas de problemas endiablados sobre colisiones en 2D e interacciones relativas que destrozan la intuición básica.
- **[Física Universitaria (Sears & Zemansky)](https://www.pearson.com/en-us/subject-catalog/p/university-physics-with-modern-physics/P200000003295/9780135159552)**: Extenso banco de ejercicios estándar de choques de billar, balas y bloques pendulares de obligada resolución para estudiantes.
- **[The Feynman Lectures on Physics (Vol 1)](https://www.feynmanlectures.caltech.edu/I_toc.html)**: Feynman ahonda en cómo la simetría y las leyes de conservación de colisiones son más fundamentales que el propio concepto de "fuerza".
