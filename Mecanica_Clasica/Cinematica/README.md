# Cinemática

La cinemática (del griego $\kappa\iota\nu\eta\mu\alpha$, kinema, "movimiento") es la rama de la mecánica clásica que describe el movimiento de puntos, cuerpos y sistemas de cuerpos sin considerar las fuerzas que provocan dicho movimiento. Mientras que la dinámica explica el "por qué" se mueven los objetos, la cinemática se centra estrictamente en el "cómo".

## 📜 Contexto Histórico
El estudio formal de la cinemática moderna comenzó con **Galileo Galilei** a principios del siglo XVII. Galileo rompió con la tradición aristotélica al demostrar empíricamente (lanzando esferas por planos inclinados) que en ausencia de resistencia del aire, todos los objetos caen con la misma aceleración, independientemente de su masa. Introdujo el concepto de que el movimiento de los proyectiles es parabólico y sentó las bases para que, décadas más tarde, Isaac Newton desarrollara el cálculo y las leyes del movimiento.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Vectores Fundamentales del Movimiento
Todo el movimiento clásico tridimensional se describe usando vectores que dependen del tiempo $t$.

- **Posición ($\vec{r}(t)$)**: Vector que indica la ubicación de un objeto respecto al origen de un sistema de coordenadas. 
  $$ \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k} $$
- **Desplazamiento ($\Delta\vec{r}$)**: El cambio neto en la posición. Es independiente de la trayectoria.
  $$ \Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1) $$
- **Velocidad ($\vec{v}(t)$)**: La derivada de la posición respecto al tiempo. Representa la tasa de cambio de la posición.
  $$ \vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k} $$
- **Aceleración ($\vec{a}(t)$)**: La derivada de la velocidad respecto al tiempo. Representa cómo cambia la velocidad (su magnitud o su dirección).
  $$ \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2} $$

### 2. Derivación de las Ecuaciones del MRUA
Cuando la aceleración es constante ($\vec{a}(t) = \vec{a}_0$), podemos integrar las ecuaciones diferenciales fundamentales para obtener la cinemática estándar de 1 dimensión:

1. **Velocidad en función del tiempo**:
   Sabemos que $a = \frac{dv}{dt}$. Integrando ambos lados con respecto al tiempo:
   $$ \int_{v_0}^{v(t)} dv = \int_{0}^{t} a \, dt \implies v(t) - v_0 = at \implies \mathbf{v(t) = v_0 + at} $$

2. **Posición en función del tiempo**:
   Sabemos que $v = \frac{dx}{dt}$. Usando la ecuación anterior:
   $$ \int_{x_0}^{x(t)} dx = \int_{0}^{t} (v_0 + at) \, dt \implies \mathbf{x(t) = x_0 + v_0 t + \frac{1}{2} a t^2} $$

3. **Ecuación de Torricelli (Sin tiempo explícito)**:
   Si usamos la regla de la cadena $a = \frac{dv}{dt} = \frac{dv}{dx} \frac{dx}{dt} = v \frac{dv}{dx}$ y separamos variables:
   $$ a \int_{x_0}^{x} dx = \int_{v_0}^{v} v \, dv \implies a(x - x_0) = \frac{1}{2}v^2 - \frac{1}{2}v_0^2 \implies \mathbf{v^2 = v_0^2 + 2a\Delta x} $$

### 3. Movimiento de Proyectiles (Tiro Parabólico)
El movimiento en 2D bajo la influencia de una gravedad constante $g$ hacia abajo ($\hat{j}$). Los ejes son independientes (Principio de Superposición de Galileo).

- Eje $x$ (MRU): $x(t) = (v_0 \cos\theta) t$
- Eje $y$ (MRUA): $y(t) = (v_0 \sin\theta) t - \frac{1}{2} g t^2$

---

## 🛠 Ejemplo Práctico: Altura Máxima y Alcance
Un cañón dispara un proyectil con velocidad $v_0$ a un ángulo $\theta$. ¿Cuál es la altura máxima ($H$) y el alcance máximo ($R$)?

**Solución**:
1. **Altura Máxima ($H$)**: Ocurre cuando la velocidad vertical es cero ($v_y = 0$).
   Usando $v_y = v_0 \sin\theta - gt = 0 \implies t_{subida} = \frac{v_0 \sin\theta}{g}$.
   Sustituyendo en $y(t)$:
   $$ H = (v_0 \sin\theta)\left(\frac{v_0 \sin\theta}{g}\right) - \frac{1}{2}g\left(\frac{v_0 \sin\theta}{g}\right)^2 = \mathbf{\frac{v_0^2 \sin^2\theta}{2g}} $$

2. **Alcance Máximo ($R$)**: El proyectil cae al suelo cuando $y=0$ (en $t = 2 t_{subida}$ por simetría).
   $$ t_{total} = \frac{2v_0 \sin\theta}{g} $$
   Sustituyendo en $x(t)$:
   $$ R = (v_0 \cos\theta)\left(\frac{2v_0 \sin\theta}{g}\right) = \frac{v_0^2 (2 \sin\theta \cos\theta)}{g} = \mathbf{\frac{v_0^2 \sin(2\theta)}{g}} $$
   *(De aquí se deduce que el alcance máximo ocurre a $\theta = 45^\circ$)*.

---

## 📚 Recursos Específicos de Cinemática

### 🎓 Cursos y Clases Recomendadas (5-7)
1. **[MIT 8.01 - Kinematics (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-1-kinematics/)**: La primera semana del famoso curso, centrada en sistemas 1D y 2D y con una claridad asombrosa.
2. **[Yale PHYS 200 - Lecture 2: Vectors in Multiple Dimensions](https://oyc.yale.edu/physics/phys-200/lecture-2)**: Tratamiento profundo de vectores en cinemática, con aplicaciones al movimiento 3D.
3. **[Khan Academy - Movimiento Unidimensional y Bidimensional](https://es.khanacademy.org/science/physics/one-dimensional-motion)**: Práctica interactiva paso a paso para dominar gráficas y ecuaciones.
4. **[Coursera - Kinematics and Dynamics (UPenn)](https://www.coursera.org/learn/robotics-kinematics)**: Curso específico sobre cómo modelar sistemas mecánicos y su movimiento espacial.
5. **[edX - Classical Mechanics (MITx)](https://www.edx.org/course/mechanics-kinematics-and-dynamics)**: Módulos interactivos enfocados a la resolución de problemas cinemáticos avanzados.
6. **[Física en Línea - Universidad de los Andes](https://fisica.uniandes.edu.co/)**: Módulos en español con simulaciones de trayectoria y problemas de encuentro de móviles.

### 📝 Artículos, Simulaciones e Interactivos (8-10)
1. **Artículo**: [Galileo's Experiments on Falling Bodies (Scholarpedia)](http://www.scholarpedia.org/article/Galileo%27s_experiments_on_falling_bodies) - Análisis histórico de los planos inclinados.
2. **Artículo**: [Ecuación de Torricelli y su deducción](https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_Torricelli) - Historia y uso de las fórmulas independientes del tiempo.
3. **Simulador**: [PhET - Movimiento de un Proyectil](https://phet.colorado.edu/es/simulations/projectile-motion) - Ajusta masa, arrastre aerodinámico y gravedad de proyectiles.
4. **Simulador**: [PhET - El Hombre Móvil](https://phet.colorado.edu/es/simulations/moving-man) - Clave para intuir gráficas de posición, velocidad y aceleración en el tiempo.
5. **Simulador**: [FísicaLab - Cinemática](https://www.fisicalab.com/tema/cinematica-conceptos) - Problemas interactivos y animaciones de movimientos MRU/MRUA.
6. **Video**: [The Physics of Bullet Drop (YouTube)](https://www.youtube.com/watch?v=cxvsHNRXLjw) - La independencia de ejes visualizada en situaciones de alcance extremo.
7. **Artículo**: [Kinematics of Mechanisms (HyperPhysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/kinm.html) - Cinemática aplicada al mundo real (engranajes, levas, poleas).
8. **Simulador**: [GeoGebra - Tiro Parabólico Interactivo](https://www.geogebra.org/m/eDkG6vG9) - Applets de la comunidad para ver los vectores de velocidad variando su componente en Y.

### 📖 Referencias Útiles y Bibliografía
- **[Classical Mechanics por Herbert Goldstein](https://en.wikipedia.org/wiki/Classical_Mechanics_(Goldstein_book))**: Obra fundamental; aunque se enfoca en mecánica analítica, los capítulos iniciales asientan bases formales.
- **[Classical Mechanics por John R. Taylor](https://uscibooks.aip.org/books/classical-mechanics/)**: Excelente texto para transición entre física general y teórica. Muy claro en cinemática polar y 3D.
- **[Classical Dynamics of Particles and Systems por Stephen T. Thornton y Jerry B. Marion](https://www.cengage.com/c/classical-dynamics-of-particles-and-systems-5e-thornton/9780534408961/)**: Conocido como el "Marion", incluye un tratamiento excepcionalmente claro sobre sistemas de partículas.
- **[Física Universitaria por Sears y Zemansky](https://www.pearson.com/en-us/subject-catalog/p/university-physics-with-modern-physics/P200000003295/9780135159552)**: El libro base estándar con cientos de problemas propuestos de cinemática de nivel básico a intermedio.
- **[The Feynman Lectures on Physics (Vol 1)](https://www.feynmanlectures.caltech.edu/I_toc.html)**: Para una discusión filosófica e intuitiva sobre el tiempo, el espacio y la relatividad de Galileo.
