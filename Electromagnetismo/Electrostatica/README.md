# Electrostática

La electrostática es la rama de la física que estudia los efectos mutuos que se producen entre los cuerpos como consecuencia de sus cargas eléctricas en reposo. Constituye la base fundamental del electromagnetismo y describe cómo las cargas interactúan mediante fuerzas a distancia, creando campos eléctricos y acumulando energía potencial.

## 📜 Contexto Histórico
El estudio de la electrostática se remonta a la antigüedad clásica, cuando Tales de Mileto observó que frotar ámbar (cuyo nombre en griego es *elektron*) atraía objetos ligeros. Sin embargo, el estudio formal comenzó en el siglo XVIII. Benjamin Franklin propuso el principio de conservación de la carga y acuñó los términos positivo y negativo. En 1785, Charles-Augustin de Coulomb formuló la ley de la fuerza electrostática mediante experimentos con una balanza de torsión. Posteriormente, Michael Faraday introdujo el concepto revolucionario de "campo eléctrico", transformando la física de la acción a distancia en una teoría de campos locales, y Carl Friedrich Gauss formuló el teorema de flujo eléctrico, estableciendo un pilar matemático esencial.

---

## 🧮 Desarrollo Teórico Profundo

### Ley de Coulomb
La fuerza $\vec{F}$ entre dos cargas puntuales $q_1$ y $q_2$ separadas por una distancia $r$ en el vacío está dada por:
$$ \vec{F} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2} \hat{r} $$
donde $\varepsilon_0 \approx 8.854 \times 10^{-12} \, \text{C}^2/(\text{N}\cdot\text{m}^2)$ es la permitividad del vacío.

### Campo Eléctrico
El campo eléctrico $\vec{E}$ se define como la fuerza por unidad de carga que experimentaría una carga de prueba $q_0$:
$$ \vec{E} = \frac{\vec{F}}{q_0} $$
Para una carga puntual $q$, el campo generado a una distancia $r$ es:
$$ \vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r} $$
El principio de superposición establece que el campo total creado por una distribución de cargas es la suma vectorial de los campos individuales: $\vec{E} = \sum \vec{E}_i$.

### Ley de Gauss
La Ley de Gauss relaciona el flujo eléctrico $\Phi_E$ a través de una superficie cerrada $S$ con la carga neta $Q_{\text{enc}}$ encerrada por dicha superficie:
$$ \oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} $$
Esta ley es extremadamente poderosa para calcular campos eléctricos en sistemas con alta simetría (esférica, cilíndrica o plana).

### Potencial Eléctrico
Dado que la fuerza electrostática es conservativa ($\nabla \times \vec{E} = 0$), el campo eléctrico puede expresarse como el gradiente negativo de un potencial escalar $V$:
$$ \vec{E} = -\nabla V $$
La diferencia de potencial entre dos puntos $A$ y $B$ es el trabajo por unidad de carga necesario para mover la carga:
$$ V_B - V_A = -\int_A^B \vec{E} \cdot d\vec{l} $$

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular el campo eléctrico a una distancia $r$ del centro de una esfera aislante de radio $R$ que tiene una carga total $Q$ distribuida uniformemente en todo su volumen.

**Solución paso a paso:**
1. **Identificar la simetría:** La distribución tiene simetría esférica. Por tanto, el campo eléctrico debe ser radial: $\vec{E} = E(r)\hat{r}$.
2. **Definir la densidad de carga:** La densidad volumétrica de carga es $\rho = \frac{Q}{\frac{4}{3}\pi R^3}$.
3. **Aplicar la Ley de Gauss en el interior ($r < R$):**
   Consideramos una superficie gaussiana esférica de radio $r$.
   $$ \oint_S \vec{E} \cdot d\vec{A} = E(4\pi r^2) $$
   La carga encerrada es $Q_{\text{enc}} = \rho (\frac{4}{3}\pi r^3) = Q \frac{r^3}{R^3}$.
   $$ E(4\pi r^2) = \frac{Q}{\varepsilon_0} \frac{r^3}{R^3} \implies \vec{E}_{\text{int}} = \frac{Q}{4\pi\varepsilon_0 R^3} r \, \hat{r} $$
4. **Aplicar la Ley de Gauss en el exterior ($r \ge R$):**
   La carga encerrada es total, $Q_{\text{enc}} = Q$.
   $$ E(4\pi r^2) = \frac{Q}{\varepsilon_0} \implies \vec{E}_{\text{ext}} = \frac{Q}{4\pi\varepsilon_0 r^2} \hat{r} $$

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. [MIT 8.02 - Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/): Las inigualables e icónicas clases de Walter Lewin. Las primeras semanas desarrollan la estática de manera insuperable.
2. [Khan Academy - Electrostática](https://es.khanacademy.org/science/physics/electric-charge-electric-force-and-voltage): Una fantástica secuencia de videos que enseña paso a paso a utilizar vectores y sumas algebraicas de campo puntual.
3. [Feynman Lectures on Physics - Vol II, Ch 4: Electrostatics](https://www.feynmanlectures.caltech.edu/II_04.html): Lectura fundacional; ofrece la distinción elegante entre los enfoques integrales y la ecuación de Poisson y Laplace.
4. [Coursera - Physics 102: Electric Charges and Fields](https://www.coursera.org/learn/physics-102): Orientado a establecer un dominio firme de la constante de Coulomb y el principio de superposición.
5. [edX - E&M: Fields and Potentials](https://www.edx.org/course/electricity-and-magnetism-part-1): Una mirada detallada provista por el MIT sobre el mapeo topológico del potencial conservativo frente a su gradiente vectorial.

### 📝 Artículos e Interactivos Interesantes
1. [PhET - Charges and Fields](https://phet.colorado.edu/en/simulations/charges-and-fields): Simulador fascinante para componer configuraciones arbitrarias y observar en vivo el campo vectorial y las superficies equipotenciales.
2. [PhET - Balloons and Static Electricity](https://phet.colorado.edu/en/simulations/balloons-and-static-electricity): Ayuda visual que explica fenómenos de frotación, carga por inducción, y polarización superficial de dieléctricos microscópicos.
3. [Wikipedia: Ley de Coulomb](https://es.wikipedia.org/wiki/Ley_de_Coulomb): El artículo madre que revisa la historia, formalismos en diversos sistemas de coordenadas y la constante electrostática del vacío.
4. [Wikipedia: Balanza de torsión de Coulomb](https://es.wikipedia.org/wiki/Balanza_de_torsión): Repaso al exquisito experimento de 1785 que brindó validez cuantitativa y geométrica a la ley de la inversa del cuadrado.
5. [HyperPhysics - Electrostatics](http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elefie.html): Árbol explicativo indispensable que conecta fuerzas, campos energéticos, capacitancia y el trabajo mecánico asociado.
6. [FísicaLab - El Campo Eléctrico](https://www.fisicalab.com/tema/campo-electrico): Artículos repletos de problemas paso a paso resueltos sobre la influencia de esferas, anillos y líneas de carga continua.
7. [Física Práctica - Ley de Gauss](https://www.fisicapractica.com/gauss.php): Trata a fondo la poderosa utilidad del teorema de la divergencia, el flujo eléctrico y su enorme poder simplificador ante simetrías.
8. [LibreTexts - Electrostatics and Capacitance](https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/07%3A_Electric_Potential): Libro abierto completo que disecciona la relación geométrica para capacitores cilíndricos, esféricos y de placas.

### 📖 Referencias Útiles y Bibliografía
1. [Introduction to Electrodynamics - David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-electrodynamics/971275E590D0DE07E9CD0DB4F2C2FA04): El texto de referencia por excelencia (estándar de oro) para estudiantes de pregrado en física, claro y didáctico.
2. [Classical Electrodynamics - John David Jackson](https://www.wiley.com/en-us/Classical+Electrodynamics%2C+3rd+Edition-p-9780471309321): Obra matemática y avanzada requerida en todos los posgrados y doctorados del mundo físico.
3. [Electricity and Magnetism - Edward M. Purcell & David J. Morin](https://www.cambridge.org/highereducation/books/electricity-and-magnetism/C16C976ADCD2F4A96DD8DD3DDAB303CE): Magnífico abordaje donde el magnetismo emerge naturalmente como consecuencia de la relatividad especial.
4. [Física Universitaria (Vol. 2) - Sears y Zemansky](https://www.pearson.com/store/p/fisica-universitaria-vol-2/P200000000305/9786073244404): Gran obra introductoria clásica que contiene ejemplos sobresalientes de aplicaciones de la ley de Gauss en medios continuos.
5. [Electromagnetic Fields and Waves - Paul Lorrain & Dale Corson](https://www.goodreads.com/book/show/2885994-electromagnetic-fields-and-waves): Un pilar a nivel intermedio, famoso por la claridad de sus capítulos iniciales sobre desarrollo multipolar electrostático.
