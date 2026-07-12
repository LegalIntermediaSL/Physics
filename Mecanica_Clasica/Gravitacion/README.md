# Gravitación

La fuerza que mantiene unida la estructura del cosmos a gran escala. Históricamente, fue la primera fuerza fundamental en ser matematizada y sigue siendo un campo de intensa investigación moderna.

## 📜 Contexto Histórico
Las **Leyes de Kepler** (1609-1619) describían empíricamente cómo se movían los planetas en elipses a diferentes velocidades, basadas en los increíbles datos observacionales de Tycho Brahe. Décadas después, **Isaac Newton** (1687) revolucionó la ciencia al formular su *Ley de Gravitación Universal*, demostrando matemáticamente que la *misma* fuerza invisible que hacía caer las manzanas de los árboles era la responsable de atar la Luna en su órbita terrestre y validar con total precisión cada una de las empíricas leyes de Kepler.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Ley de Gravitación Universal de Newton
Entre cualquier par de masas puntuales $m_1$ y $m_2$ separadas por una distancia $r$, existe una fuerza de atracción mutua:
$$ \vec{F}_g = -G \frac{m_1 m_2}{r^2} \hat{r} $$
Donde $G = 6.6743 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$. El signo negativo indica que la fuerza es atractiva. 

### 2. Campo Gravitatorio ($\vec{g}$)
El campo generado por una masa $M$ en su entorno. Es la fuerza por unidad de masa de prueba:
$$ \vec{g} = \frac{\vec{F}_g}{m} = -G \frac{M}{r^2} \hat{r} $$
En la superficie de la Tierra ($M_T, R_T$), $g \approx 9.81 \text{ m/s}^2$.

### 3. Energía Potencial Gravitacional ($U$)
Para una fuerza conservativa que depende de $1/r^2$, la energía potencial (tomando el nivel cero en $r=\infty$) se calcula integrando:
$$ U(r) = - \int_{\infty}^{r} \left(-G \frac{m_1 m_2}{r^2}\right) dr = -G \frac{m_1 m_2}{r} $$
Esta es la energía de "enlace". Es negativa porque debemos suministrar energía (hacer trabajo positivo) para separar las masas hasta el infinito.

### 4. Leyes de Kepler Derivadas
Con el cálculo de Newton, la tercera ley de Kepler se deriva fácilmente para órbitas circulares igualando la fuerza centrípeta y la gravitacional:
$$ \frac{m v^2}{r} = G \frac{M m}{r^2} \implies v^2 = \frac{GM}{r} $$
Dado que la velocidad orbital es $v = \frac{2\pi r}{T}$ (donde $T$ es el periodo orbital):
$$ \left(\frac{2\pi r}{T}\right)^2 = \frac{GM}{r} \implies \frac{4\pi^2 r^2}{T^2} = \frac{GM}{r} \implies \mathbf{T^2 = \left(\frac{4\pi^2}{GM}\right) r^3} $$
*(El cuadrado del periodo es proporcional al cubo de la distancia orbital).*

---

## 🛠 Ejemplo Práctico: Velocidad de Escape
¿A qué velocidad $v_{esc}$ debes disparar un proyectil de masa $m$ desde la superficie terrestre ($M$, $R$) para que nunca vuelva a caer, escapando hasta el infinito?

**Solución**:
1. Usamos la conservación de la energía mecánica $E_i = E_f$.
2. En la superficie: $E_i = K_i + U_i = \frac{1}{2}m v_{esc}^2 - G \frac{mM}{R}$.
3. Para apenas escapar, su velocidad al llegar al infinito ($r \to \infty$) será exactamente cero: $E_f = K_f + U_f = 0 + 0 = 0$.
4. Igualamos:
   $$ \frac{1}{2}m v_{esc}^2 - G \frac{mM}{R} = 0 $$
5. Despejando $v_{esc}$ (nota que no depende de la masa $m$ del cohete):
   $$ \mathbf{v_{esc} = \sqrt{\frac{2GM}{R}}} $$
   Para la Tierra, esto equivale a unos espectaculares $11.2 \text{ km/s}$.

---

## 📚 Recursos Específicos de Gravitación

### 🎓 Cursos y Clases Recomendadas (5-7)
1. **[MIT 8.01 - Universal Gravity (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-10-rotational-energy/)**: Cubre magistralmente las Leyes de Kepler, la mecánica celeste y el concepto de energía en el espacio profundo.
2. **[Yale PHYS 200 - Lecture 7: Universal Gravitation](https://oyc.yale.edu/physics/phys-200/lecture-7)**: Deducción formal del cálculo orbital, secciones cónicas y reducción al problema de un solo cuerpo.
3. **[Khan Academy - Gravitación y Órbitas](https://es.khanacademy.org/science/physics/centripetal-force-and-gravitation)**: Excelente guía de paso a paso, abarcando peso aparente en el espacio y órbitas satelitales.
4. **[Coursera - Orbital Mechanics (University of Colorado Boulder)](https://www.coursera.org/learn/spacecraft-dynamics-kinematics)**: Un enfoque desde la ingeniería aeroespacial de las maniobras orbitales de Hohmann y las esferas de influencia gravitacional.
5. **[edX - Astrophysics: Cosmology (ANU)](https://www.edx.org/course/astrophysics-cosmology)**: Para ir más allá, conectando la gravedad de Newton con su rol fundamental en la estructura cosmológica.

### 📝 Artículos, Simulaciones e Interactivos (8-10)
1. **Artículo Histórico**: [Kepler's Discovery of the Laws of Planetary Motion (Scholarpedia)](http://www.scholarpedia.org/article/Kepler%27s_laws_of_planetary_motion) - Relato de cómo Kepler dedujo sus empíricas elipses de los datos de Tycho Brahe.
2. **Artículo (Cavendish)**: [El Experimento de Cavendish (Wikipedia)](https://es.wikipedia.org/wiki/Experimento_de_Cavendish) - Cómo la humanidad "pesó" la Tierra midiendo directamente la esquiva constante universal $G$.
3. **Simulador**: [PhET - Laboratorio de Gravedad](https://phet.colorado.edu/es/simulations/gravity-and-orbits) - Construye tu propio sistema solar y observa cómo varían las trayectorias parabólicas, hiperbólicas o elípticas.
4. **Simulador**: [PhET - Mi Sistema Solar](https://phet.colorado.edu/es/simulations/my-solar-system) - Excelente herramienta interactiva para jugar con órbitas multicuerpo inestables.
5. **Juego Educativo**: [Kerbal Space Program](https://www.kerbalspaceprogram.com/) - El mejor simulador espacial jamás creado para entender instintivamente la mecánica orbital newtoniana.
6. **Video Documental**: [Carl Sagan's Cosmos - Kepler & Newton](https://www.youtube.com/watch?v=zSzBksEbxYg) - Clips icónicos que enlazan el trabajo místico de Kepler con el genio matemático de Newton.
7. **Artículo**: [Gravity and General Relativity (HyperPhysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/Relativ/grel.html) - Sobre cómo y cuándo la aproximación clásica falla respecto a los agujeros negros.
8. **Simulador**: [Newton's Cannon on a Mountain](https://contrib.pbslearningmedia.org/WGBH/nvce/vis_cannon/vis_cannon.html) - La clásica demostración interactiva del experimento mental original de Newton para orbitar la Tierra.

### 📖 Referencias Útiles y Bibliografía
- **[Classical Mechanics (John R. Taylor)](https://uscibooks.aip.org/books/classical-mechanics/)**: Extraordinario capítulo sobre el problema de la fuerza central (two-body problem) y órbitas perturbadas.
- **[Orbital Mechanics for Engineering Students (Howard D. Curtis)](https://www.elsevier.com/books/orbital-mechanics-for-engineering-students/curtis/978-0-08-102133-0)**: La biblia moderna para los cálculos específicos que se usan hoy en día en satélites y viajes interplanetarios.
- **[Classical Dynamics of Particles and Systems (Marion & Thornton)](https://www.cengage.com/c/classical-dynamics-of-particles-and-systems-5e-thornton/9780534408961/)**: Su tratamiento de las secciones eficaces, las fuerzas tipo $1/r^2$ y el vector de Runge-Lenz es fundamental.
- **[Principia Mathematica (Isaac Newton)](https://es.wikipedia.org/wiki/Philosophi%C3%A6_naturalis_principia_mathematica)**: Aunque ilegible como texto moderno, los postulados sobre la Ley Universal y el Teorema de Cascarón Esférico provienen directamente de aquí.
- **[Gravity: An Introduction to Einstein's General Relativity (James Hartle)](https://www.cambridge.org/highereducation/books/gravity/D8B1C6BB1E413B52701198A019448AFE)**: Para aquellos que desean ver la frontera superior de la gravedad newtoniana.
