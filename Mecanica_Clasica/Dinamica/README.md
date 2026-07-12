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
   $ \sum \vec{F} = 0 \implies \frac{d\vec{v}}{dt} = 0 $

2. **Segunda Ley (Ley Fundamental de la Dinámica)**:
   *El cambio de movimiento es directamente proporcional a la fuerza motriz impresa y ocurre según la línea recta a lo largo de la cual aquella fuerza se imprime.*
   Originalmente Newton la formuló en términos del momento lineal ($\vec{p} = m\vec{v}$):
   $ \sum \vec{F} = \frac{d\vec{p}}{dt} $
   Para masa $m$ constante, esto se convierte en la célebre ecuación:
   $ \sum \vec{F} = m\vec{a} $
   Esta es una ecuación diferencial vectorial de segundo orden: $\vec{F}(\vec{r}, \vec{v}, t) = m\frac{d^2\vec{r}}{dt^2}$.

3. **Tercera Ley (Acción y Reacción)**:
   *Con toda acción ocurre siempre una reacción igual y contraria.*
   Si el objeto $A$ ejerce una fuerza sobre el objeto $B$, el objeto $B$ ejerce una fuerza de igual magnitud pero dirección opuesta sobre $A$. Estas fuerzas nunca se cancelan entre sí porque actúan sobre **cuerpos diferentes**.
   $ \vec{F}_{A \to B} = -\vec{F}_{B \to A} $

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
   $ \sum F_y = N - mg \cos\theta = 0 \implies N = mg \cos\theta $
4. Aplicamos la Segunda Ley de Newton en el eje $x$:
   $ \sum F_x = mg \sin\theta - f_k = ma $
   Como $f_k = \mu_k N = \mu_k (mg \cos\theta)$:
   $ mg \sin\theta - \mu_k mg \cos\theta = ma $
5. Cancelando la masa $m$, obtenemos la aceleración (independiente de la masa):
   $ \mathbf{a = g (\sin\theta - \mu_k \cos\theta)} $

---

## 📚 Recursos Específicos de Dinámica

### 🎓 Cursos y Clases Recomendadas
1. [MIT 8.01 - Newton's Laws of Motion (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-2-newtons-laws-of-motion/): Semanas 2 y 3 dedicadas exclusivamente a resolver problemas de dinámica.
2. [Yale PHYS 200 - Lecture 3: Newton's Laws of Motion](https://oyc.yale.edu/physics/phys-200/lecture-3): Un análisis riguroso de qué son realmente la masa y la inercia.
3. [Khan Academy - Fuerzas y Leyes de Newton](https://es.khanacademy.org/science/physics/forces-newtons-laws): Diagramas de cuerpo libre paso a paso.

### 📝 Artículos e Interactivos Interesantes
1. **Artículo Histórico**: [Principia Mathematica en español](http://www.cervantesvirtual.com/obra-visor/principios-matematicos-de-la-filosofia-natural--0/html/) - Leer las propias palabras de Newton al definir la masa.
2. **Artículo (Stanford)**: [Newton's Philosophiae Naturalis Principia Mathematica](https://plato.stanford.edu/entries/newton-principia/) - Análisis filosófico de sus leyes.
3. **Simulador**: [PhET - Fuerzas y Movimiento (Conceptos básicos)](https://phet.colorado.edu/es/simulations/forces-and-motion-basics) - Excelente para visualizar empujones y fricción.
4. **Simulador**: [PhET - Rampa, Fuerzas y Movimiento](https://phet.colorado.edu/es/simulations/ramp-forces-and-motion) - Ajusta el coeficiente de fricción de un plano inclinado y observa los diagramas de cuerpo libre.
5. **Video Analítico**: [Veritasium - Why Gravity is NOT a Force](https://www.youtube.com/watch?v=XRr1kaXKBsU) - Interesante contraste entre la dinámica newtoniana (donde la gravedad es una fuerza real) y la relatividad general (donde es producto de sistemas no inerciales).
