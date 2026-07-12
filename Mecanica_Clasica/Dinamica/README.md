# Dinámica

La dinámica es la parte de la mecánica clásica que estudia la relación entre el movimiento de un cuerpo y las causas que lo producen (las fuerzas y momentos). Es el "por qué" las cosas se mueven.

## 📜 Contexto Histórico
Culminando con la publicación de su obra maestra *Philosophiæ Naturalis Principia Mathematica* en 1687, **Sir Isaac Newton** unificó el comportamiento mecánico del cielo y de la Tierra. Antes de él, Aristóteles afirmaba que el estado natural de un objeto era el reposo (y que se requería una fuerza continua para moverlo). Newton demostró que el estado natural es el movimiento rectilíneo uniforme, estableciendo las leyes fundamentales que gobernaron la física durante más de 200 años hasta la llegada de la relatividad.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Las Tres Leyes de Newton

1. **Primera Ley (Ley de la Inercia)**:
   *Todo cuerpo persevera en su estado de reposo o movimiento uniforme y rectilíneo a no ser que sea obligado a cambiar su estado por fuerzas impresas sobre él.*
   Esto define empíricamente lo que es un **Sistema de Referencia Inercial**: un sistema donde la Primera Ley se cumple.
   $$ \sum \vec{F} = 0 \implies \frac{d\vec{v}}{dt} = 0 $$

2. **Segunda Ley (Ley Fundamental de la Dinámica)**:
   *El cambio de movimiento es directamente proporcional a la fuerza motriz impresa y ocurre según la línea recta a lo largo de la cual aquella fuerza se imprime.*
   Originalmente Newton la formuló en términos del momento lineal ($\vec{p} = m\vec{v}$):
   $$ \sum \vec{F} = \frac{d\vec{p}}{dt} $$
   Para masa $m$ constante, esto se convierte en la célebre ecuación:
   $$ \sum \vec{F} = m\vec{a} $$
   Esta es una ecuación diferencial vectorial de segundo orden: $\vec{F}(\vec{r}, \vec{v}, t) = m\frac{d^2\vec{r}}{dt^2}$.

3. **Tercera Ley (Acción y Reacción)**:
   *Con toda acción ocurre siempre una reacción igual y contraria.*
   Si el objeto $A$ ejerce una fuerza sobre el objeto $B$, el objeto $B$ ejerce una fuerza de igual magnitud pero dirección opuesta sobre $A$. Estas fuerzas nunca se cancelan entre sí porque actúan sobre **cuerpos diferentes**.
   $$ \vec{F}_{A \to B} = -\vec{F}_{B \to A} $$

### 2. Fuerzas Comunes en Dinámica

- **Peso ($\vec{W}$)**: La fuerza de gravedad cerca de la superficie terrestre. $\vec{W} = m\vec{g}$.
- **Fuerza Normal ($\vec{N}$)**: Fuerza de reacción perpendicular que ejerce una superficie. 
- **Fuerza de Fricción ($\vec{f}$)**: Oposición al movimiento.
  - Estática (impide el inicio del movimiento): $f_s \le \mu_s N$
  - Cinética (durante el movimiento): $f_k = \mu_k N$
- **Tensión ($\vec{T}$)**: Fuerza transmitida a lo largo de una cuerda inextensible.
- **Fuerza Elástica (Ley de Hooke)**: Fuerza restauradora de un resorte. $\vec{F}_s = -k\vec{x}$.

---

## 🛠 Ejemplo Práctico: Plano Inclinado con Fricción
Un bloque de masa $m$ se desliza hacia abajo por un plano inclinado con ángulo $\theta$ respecto a la horizontal. El coeficiente de fricción cinética es $\mu_k$. Calcular la aceleración del bloque.

**Solución**:
1. Establecemos los ejes de coordenadas: el eje $x$ paralelo al plano (hacia abajo positivo) y el eje $y$ perpendicular al plano (hacia arriba positivo).
2. Descomponemos el peso $mg$ en estos ejes:
   - $W_x = mg \sin\theta$
   - $W_y = -mg \cos\theta$
3. Aplicamos la Segunda Ley de Newton en el eje $y$ (no hay movimiento en $y$):
   $$ \sum F_y = N - mg \cos\theta = 0 \implies N = mg \cos\theta $$
4. Aplicamos la Segunda Ley de Newton en el eje $x$:
   $$ \sum F_x = mg \sin\theta - f_k = ma $$
   Como $f_k = \mu_k N = \mu_k (mg \cos\theta)$:
   $$ mg \sin\theta - \mu_k mg \cos\theta = ma $$
5. Cancelando la masa $m$, obtenemos la aceleración (independiente de la masa):
   $$ \mathbf{a = g (\sin\theta - \mu_k \cos\theta)} $$

---

## 📚 Recursos Específicos de Dinámica

### 🎓 Cursos y Clases Recomendadas (5-7)
1. **[MIT 8.01 - Newton's Laws of Motion (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-2-newtons-laws-of-motion/)**: Semanas 2 y 3 dedicadas exclusivamente a resolver problemas clásicos de dinámica.
2. **[Yale PHYS 200 - Lecture 3: Newton's Laws of Motion](https://oyc.yale.edu/physics/phys-200/lecture-3)**: Un análisis riguroso de qué son realmente la masa y la inercia.
3. **[Khan Academy - Fuerzas y Leyes de Newton](https://es.khanacademy.org/science/physics/forces-newtons-laws)**: Diagramas de cuerpo libre paso a paso y fuerzas interactivas.
4. **[Coursera - Engineering Mechanics: Statics & Dynamics (Georgia Tech)](https://www.coursera.org/learn/engineering-mechanics-statics)**: Un enfoque muy práctico sobre fuerzas en estructuras y aceleración de componentes mecánicos.
5. **[NPTEL - Engineering Mechanics (IIT)](https://nptel.ac.in/courses/122/104/122104015/)**: Excelente curso centrado en problemas de dinámica rigurosa con un enfoque ingenieril avanzado.

### 📝 Artículos, Simulaciones e Interactivos (8-10)
1. **Artículo Histórico**: [Principia Mathematica en español](http://www.cervantesvirtual.com/obra/principios-matematicos-de-la-filosofia-natural--0/) - Leer las propias palabras de Newton al definir la inercia y fuerza.
2. **Artículo (Stanford)**: [Newton's Philosophiae Naturalis Principia Mathematica](https://plato.stanford.edu/entries/newton-principia/) - Análisis filosófico detallado de sus leyes axiomáticas.
3. **Simulador**: [PhET - Fuerzas y Movimiento (Conceptos básicos)](https://phet.colorado.edu/es/simulations/forces-and-motion-basics) - Excelente para visualizar empujones, tirones y fuerzas de fricción.
4. **Simulador**: [PhET - Rampa, Fuerzas y Movimiento](https://phet.colorado.edu/es/simulations/ramp-forces-and-motion) - Ajusta el coeficiente de fricción de un plano inclinado y observa diagramas de cuerpo libre cambiantes.
5. **Video Analítico**: [Veritasium - Why Gravity is NOT a Force](https://www.youtube.com/watch?v=XRr1kaXKBsU) - Interesante contraste entre la dinámica newtoniana y relativista.
6. **Artículo**: [Friction and Drag (HyperPhysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/frict.html) - Conceptos básicos sobre rozamiento aerodinámico y fuerzas disipativas.
7. **Simulador**: [GeoGebra - Diagramas de Cuerpo Libre](https://www.geogebra.org/m/J2K6D3x5) - Applets para practicar la suma vectorial de fuerzas con polígonos.
8. **Video Experimental**: [SmarterEveryDay - Fluid Dynamics and Drag](https://www.youtube.com/watch?v=3u_R4yqHqA8) - Impacto visual de las fuerzas de arrastre fluidas que complican la ley de Newton.

### 📖 Referencias Útiles y Bibliografía
- **[Classical Dynamics of Particles and Systems (Marion & Thornton)](https://www.cengage.com/c/classical-dynamics-of-particles-and-systems-5e-thornton/9780534408961/)**: Clave para ir un paso más allá de la física de primer año, abordando fuerzas centrales y acopladas.
- **[Classical Mechanics (John R. Taylor)](https://uscibooks.aip.org/books/classical-mechanics/)**: Su tratamiento sobre fuerzas con resistencia del aire (drag) y fuerzas restauradoras es magnífico.
- **[Classical Mechanics (Goldstein)](https://en.wikipedia.org/wiki/Classical_Mechanics_(Goldstein_book))**: Aborda la dinámica desde el principio de D'Alembert, esencial para la formulación lagrangiana de sistemas restringidos.
- **[Física Universitaria (Sears & Zemansky)](https://www.pearson.com/en-us/subject-catalog/p/university-physics-with-modern-physics/P200000003295/9780135159552)**: Extenso banco de ejercicios sobre tensiones, resortes, planos inclinados y máquinas de Atwood.
- **[Introduction to Classical Mechanics (David Morin)](https://www.cambridge.org/highereducation/books/introduction-to-classical-mechanics/31CB8B93623D3F14E1EE98B223D1DE47)**: Lleno de problemas retadores de dinámica, famoso por su rigor matemático intuitivo y sus limericks.
