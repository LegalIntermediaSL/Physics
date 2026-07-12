# Óptica Geométrica
La óptica geométrica es la rama de la física que estudia la propagación de la luz asumiendo que viaja en líneas rectas (rayos). Es una aproximación válida cuando la longitud de onda de la luz es mucho menor que el tamaño de los objetos con los que interactúa.

## 📜 Contexto Histórico
El estudio de la óptica geométrica data de la antigüedad, con Euclides escribiendo "Óptica" alrededor del año 300 a.C. En el siglo XI, Ibn al-Haytham (Alhazen) hizo contribuciones fundamentales en su "Libro de Óptica". La ley de refracción fue descubierta empíricamente por Willebrord Snellius en 1621 y deducida a partir del principio del tiempo mínimo por Pierre de Fermat.

## 🧮 Desarrollo Teórico Profundo
La óptica geométrica se basa en dos principios fundamentales al interactuar con fronteras entre medios:

**Ley de Reflexión:**
El ángulo de incidencia es igual al ángulo de reflexión respecto a la normal.
$$ \theta_i = \theta_r $$

**Ley de Snell (Refracción):**
Relaciona los índices de refracción de dos medios ($ n_1, n_2 $) con los ángulos de los rayos.
$$ n_1 \sin(\theta_1) = n_2 \sin(\theta_2) $$

**Ecuación de los Fabricantes de Lentes (Lentes Delgadas):**
Para una lente delgada en el aire, con radios de curvatura $ R_1 $ y $ R_2 $, la distancia focal $ f $ es:
$$ \frac{1}{f} = (n - 1) \left( \frac{1}{R_1} - \frac{1}{R_2} \right) $$

**Ecuación de las Lentes y Espejos:**
$$ \frac{1}{s} + \frac{1}{s'} = \frac{1}{f} $$
Donde $ s $ es la distancia al objeto y $ s' $ la distancia a la imagen. El aumento lateral es $ m = -\frac{s'}{s} $.

## 🛠 Ejemplo Práctico
**Problema:** Un objeto de $ 5 \text{ cm} $ de altura se coloca a $ 30 \text{ cm} $ de una lente convergente que tiene una distancia focal de $ 10 \text{ cm} $. Determina la posición de la imagen, su aumento y su tamaño.

**Solución paso a paso:**
1. Usamos la ecuación de lentes delgadas: $ \frac{1}{s} + \frac{1}{s'} = \frac{1}{f} $.
2. Sustituimos valores ($ s = 30 \text{ cm}, f = 10 \text{ cm} $):
   $$ \frac{1}{30} + \frac{1}{s'} = \frac{1}{10} $$
3. Despejamos $ s' $:
   $$ \frac{1}{s'} = \frac{1}{10} - \frac{1}{30} = \frac{3 - 1}{30} = \frac{2}{30} = \frac{1}{15} $$
   $ s' = 15 \text{ cm} $ (Imagen real y detrás de la lente).
4. Calculamos el aumento lateral $ m $:
   $ m = -\frac{s'}{s} = -\frac{15}{30} = -0.5 $ (Imagen invertida y reducida a la mitad).
5. Tamaño de la imagen $ y' $:
   $ y' = m \cdot y = -0.5 \cdot 5 \text{ cm} = -2.5 \text{ cm} $.

## 📚 Recursos Específicos
### Cursos
1. ["Optics" - Coursera (University of Rochester)](https://www.coursera.org/learn/optics)
2. ["Introduction to Light" - edX](https://www.edx.org/course/introduction-to-light)
3. ["Geometric Optics" - Khan Academy](https://www.khanacademy.org/science/physics/geometric-optics)
4. ["Physics III: Waves and Optics" - MIT OCW](https://ocw.mit.edu/courses/8-03-physics-iii-vibrations-and-waves-fall-2004/)
5. ["Ray Optics" - NPTEL (IIT Bombay)](https://nptel.ac.in/courses/115101011)
6. ["Applied Optics" - Coursera](https://www.coursera.org/learn/applied-optics)

### Artículos y Simulaciones
1. ["Geometric Optics" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/geometric-optics)
2. ["Bending Light" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/bending-light)
3. ["Lens and Mirror Simulator" - oPhysics](https://ophysics.com/l12.html)
4. ["Refraction and Snell's Law" - oPhysics](https://ophysics.com/l8.html)
5. ["Total Internal Reflection" - oPhysics](https://ophysics.com/l9.html)
6. ["Prism Simulator" - oPhysics](https://ophysics.com/l11.html)
7. ["Ray Tracing Tool" - Ricktu288](https://ricktu288.github.io/ray-optics/)
8. ["Optics Bench" - Amrita O-labs](http://vlab.amrita.edu/?sub=1&brch=281&sim=1509&cnt=1)
9. ["Interactive Ray Tracing" - PhET](https://phet.colorado.edu/en/simulations/geometric-optics-basics)

### 📖 Referencias Útiles y Bibliografía
1. [*Optics* por Eugene Hecht](https://www.pearson.com/en-us/subject-catalog/p/optics/P200000006793/9780133977226)
2. [*Fundamentals of Physics* (Capítulos de Óptica) por Halliday & Resnick](https://www.wiley.com/en-us/Fundamentals+of+Physics%2C+12th+Edition-p-9781119773511)
3. ["Book of Optics" - Alhazen (Contexto Histórico)](https://archive.org/details/AlhazenBookOfOptics)
4. [*Principles of Optics* por Max Born y Emil Wolf](https://www.cambridge.org/core/books/principles-of-optics/1B445037E90B051D57457FBD56A1F6E2)
