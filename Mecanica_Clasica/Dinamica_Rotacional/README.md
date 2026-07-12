# Dinámica Rotacional

Para entender el movimiento completo de los objetos reales (no solo de partículas puntuales ideales), debemos incorporar la rotación. Para casi cada concepto de la mecánica traslacional (masa, velocidad, fuerza) existe una contraparte análoga en el mundo rotacional.

## 📜 Contexto Histórico
El estudio de los sólidos rígidos, y en particular la introducción de los momentos de inercia y los ejes principales, se debe abrumadoramente a **Leonhard Euler** en el siglo XVIII. Sus *Ecuaciones de Euler* describen la rotación de cuerpos tridimensionales sin necesidad de reducirlos a puntos individuales, revolucionando campos como la ingeniería mecánica, la giroscopía y la astronomía.

---

## 🧮 Desarrollo Teórico Profundo

### 1. Variables Cinemáticas Angulares
Si un objeto gira alrededor de un eje a una distancia $r$, un arco de longitud $s = r \theta$. Derivando:
- Posición Angular: $\theta$ (rad)
- Velocidad Angular: $\omega = \frac{d\theta}{dt} = \frac{v_t}{r}$ (rad/s)
- Aceleración Angular: $\alpha = \frac{d\omega}{dt} = \frac{a_t}{r}$ (rad/s$^2$)

### 2. Momento de Inercia ($I$)
Es el equivalente rotacional de la masa; mide la resistencia de un objeto a cambiar su estado de rotación. No solo depende de la masa total, sino de *cómo está distribuida* esa masa respecto al eje.
$$ I = \sum m_i r_i^2 \quad \text{o en continuo} \quad I = \int r^2 \, dm $$
- Ejemplos: Un anillo ($I = MR^2$), un disco sólido ($I = \frac{1}{2}MR^2$), una esfera sólida ($I = \frac{2}{5}MR^2$).

### 3. Torque ($\vec{\tau}$)
El equivalente de la fuerza. Es la capacidad de una fuerza para producir rotación. 
$$ \vec{\tau} = \vec{r} \times \vec{F} \quad \implies \quad |\tau| = r F \sin\theta $$
Donde $\vec{r}$ es el vector posición desde el eje de rotación hasta el punto de aplicación de la fuerza.

### 4. Segunda Ley de Newton Rotacional
Para un eje fijo:
$$ \sum \tau = I \alpha $$

### 5. Momento Angular ($\vec{L}$) y Energía
- **Momento Angular**: El ímpetu de rotación. $\vec{L} = \vec{r} \times \vec{p}$. Para un sólido rígido girando en un eje de simetría: $L = I \omega$.
- **Conservación**: Si el torque externo neto es cero ($\sum \tau_{ext} = 0$), el momento angular $\vec{L}$ se conserva. (Un patinador que acerca sus brazos disminuye $I$, y por tanto debe aumentar $\omega$ para que $L$ se mantenga).
- **Energía Cinética Rotacional**: $K_{rot} = \frac{1}{2} I \omega^2$.

---

## 🛠 Ejemplo Práctico: Descenso por un plano inclinado
Imagina que soltamos simultáneamente un aro hueco ($I = MR^2$), un cilindro macizo ($I = \frac{1}{2}MR^2$) y una esfera sólida ($I = \frac{2}{5}MR^2$) por una rampa. Todos tienen masa $M$ y radio $R$. Ruedan sin resbalar. ¿Cuál llega primero al final de la rampa (altura $h$)?

**Solución por Energía**:
1. Conservación de energía para todos. $U_i = Mgh$, $K_i = 0$.
2. Al pie de la rampa, la energía cinética es traslacional más rotacional:
   $$ E_f = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2 = Mgh $$
3. Como ruedan sin deslizar, $v = \omega R \implies \omega = v/R$.
4. Sustituyendo $I = c MR^2$ (donde $c=1$ aro, $c=1/2$ cilindro, $c=2/5$ esfera):
   $$ \frac{1}{2} M v^2 + \frac{1}{2} (c MR^2) \left(\frac{v^2}{R^2}\right) = Mgh $$
   $$ \frac{1}{2} v^2 (1 + c) = gh \implies \mathbf{v = \sqrt{\frac{2gh}{1 + c}}} $$
5. Como $v$ es mayor para el coeficiente $c$ más pequeño, el objeto con la masa más concentrada en el centro ganará. 
   **Ganador**: La esfera ($c=0.4$). **Perdedor**: El aro ($c=1$).

---

## 📚 Recursos Específicos de Dinámica Rotacional

### 🎓 Cursos y Clases Recomendadas (5-7)
1. **[MIT 8.01 - Torque and Angular Momentum (Walter Lewin)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-9-rotational-dynamics/)**: Uno de los bloques más famosos de Lewin, con demostraciones legendarias de giroscopios y patinadores.
2. **[Yale PHYS 200 - Lecture 9: Rotations](https://oyc.yale.edu/physics/phys-200/lecture-9)**: Descripción matricial y vectorial rigurosa de las transformaciones rotacionales.
3. **[Khan Academy - Torque y Momento Angular](https://es.khanacademy.org/science/physics/torque-angular-momentum)**: Explicaciones muy amigables sobre rotaciones, momentos de inercia y equilibrio estático.
4. **[Coursera - Advanced Engineering Mechanics (Various)](https://www.coursera.org/learn/advanced-engineering-systems-in-motion-dynamics-of-three-dimensional-3d-motion)**: Ideal para ver aplicaciones de las ecuaciones de Euler a la ingeniería aeroespacial o robótica.
5. **[edX - Rotational Dynamics (MITx)](https://www.edx.org/course/mechanics-rotational-dynamics)**: Problemas interactivos centrados en la conservación del momento angular y choques rotacionales.

### 📝 Artículos, Simulaciones e Interactivos (8-10)
1. **Artículo**: [Conservation of Angular Momentum (HyperPhysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/amom.html) - Desglose de fórmulas sobre precesión y momentos.
2. **Artículo**: [Euler's equations for rigid body dynamics](https://en.wikipedia.org/wiki/Euler%27s_equations_(rigid_body_dynamics)) - Para un enfoque tensorial más avanzado de las rotaciones 3D.
3. **Simulador**: [PhET - Ladybug Revolution](https://phet.colorado.edu/es/simulations/rotation) - Explora posición, velocidad y aceleración angular con una mariquita en un plato giratorio.
4. **Simulador**: [PhET - Balancing Act](https://phet.colorado.edu/es/simulations/balancing-act) - Aprende el principio de las palancas y la igualación de torques.
5. **Video Experimental**: [Veritasium - Bullet Block Experiment](https://www.youtube.com/watch?v=vVQzgrKExF4) - Experimento espectacular que involucra momento angular e inercia en una colisión.
6. **Artículo**: [Tensor de Inercia (Scholarpedia)](http://www.scholarpedia.org/article/Moment_of_inertia) - Definición profunda de los ejes principales de rotación para objetos asimétricos.
7. **Video Analítico**: [SmarterEveryDay - Gyroscopic Precession](https://www.youtube.com/watch?v=cquvA_IpEsA) - Explicación clara y visual del contra-intuitivo fenómeno de la precesión de los giroscopios.
8. **Simulador**: [GeoGebra - Momento de Inercia](https://www.geogebra.org/m/XfN6sZRb) - Herramienta para integrar virtualmente el momento de inercia de perfiles 2D de masa constante.

### 📖 Referencias Útiles y Bibliografía
- **[Classical Mechanics (Herbert Goldstein)](https://en.wikipedia.org/wiki/Classical_Mechanics_(Goldstein_book))**: Famoso por su detalladísimo estudio matemático sobre la cinemática de los cuerpos rígidos, los ángulos de Euler y el tensor de inercia.
- **[Classical Dynamics of Particles and Systems (Marion & Thornton)](https://www.cengage.com/c/classical-dynamics-of-particles-and-systems-5e-thornton/9780534408961/)**: Aporta un equilibrio perfecto, tratando el cuerpo rígido usando la formulación newtoniana clásica y matrices.
- **[Classical Mechanics (John R. Taylor)](https://uscibooks.aip.org/books/classical-mechanics/)**: Incluye un capítulo soberbio sobre dinámica de cuerpos rígidos, rotaciones 3D de la Tierra (efecto Coriolis y péndulo de Foucault).
- **[Introduction to Classical Mechanics (David Morin)](https://www.cambridge.org/highereducation/books/introduction-to-classical-mechanics/31CB8B93623D3F14E1EE98B223D1DE47)**: Tiene una colección brutal de problemas avanzados y contra-intuitivos de trompos, aros y cilindros rodantes.
- **[Feynman Lectures on Physics (Vol 1)](https://www.feynmanlectures.caltech.edu/I_toc.html)**: Feynman ilumina los conceptos de rotación, con especial énfasis en la analogía matemática profunda con la traslación.
