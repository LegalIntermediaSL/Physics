# Magnetismo

El magnetismo es la rama de la física que describe los fenómenos magnéticos, que surgen como resultado del movimiento de cargas eléctricas (corrientes) y de momentos magnéticos intrínsecos de las partículas elementales (espín).

## 📜 Contexto Histórico
Durante milenios, el magnetismo se consideró un fenómeno misterioso asociado a la magnetita. En 1820, Hans Christian Ørsted descubrió de forma accidental que una brújula se desviaba cerca de un cable con corriente, estableciendo la primera conexión entre electricidad y magnetismo. Poco después, Jean-Baptiste Biot y Félix Savart formularon la ley empírica que describe el campo generado por un segmento de corriente. André-Marie Ampère extendió estos trabajos y demostró que las corrientes se atraen o repelen de forma análoga a los imanes, fundando la electrodinámica. Finalmente, Hendrik Lorentz formalizó la fuerza que experimenta una carga móvil dentro de un campo electromagnético.

---

## 🧮 Desarrollo Teórico Profundo

### Fuerza Magnética y Fuerza de Lorentz
Una carga $q$ que se mueve con velocidad $\vec{v}$ en presencia de un campo magnético $\vec{B}$ experimenta una fuerza dada por:
$$ \vec{F}_m = q (\vec{v} \times \vec{B}) $$
Si además existe un campo eléctrico $\vec{E}$, la fuerza total es la Fuerza de Lorentz:
$$ \vec{F} = q(\vec{E} + \vec{v} \times \vec{B}) $$

### Ley de Biot-Savart
El campo magnético $d\vec{B}$ creado en un punto en el espacio por un elemento diferencial de corriente $Id\vec{l}$ viene dado por:
$$ d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \, d\vec{l} \times \hat{r}}{r^2} $$
donde $\mu_0 = 4\pi \times 10^{-7} \, \text{T}\cdot\text{m}/\text{A}$ es la permeabilidad magnética del vacío, y $\vec{r}$ es el vector que va desde el elemento al punto.

### Ley de Ampère
La Ley de Ampère es el equivalente magnético de la Ley de Gauss para situaciones de alta simetría. Relaciona la circulación del campo magnético a lo largo de una curva cerrada $C$ con la corriente total $I_{\text{enc}}$ que la atraviesa:
$$ \oint_C \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}} $$
En forma diferencial: $\nabla \times \vec{B} = \mu_0 \vec{J}$.

### Flujo Magnético y Ausencia de Monopolos
A diferencia de las cargas eléctricas, no existen fuentes aisladas (monopolos) de campo magnético. Por tanto, las líneas de campo magnético siempre son cerradas. Matemáticamente, el flujo a través de cualquier superficie cerrada es nulo (Ley de Gauss para el magnetismo):
$$ \oint_S \vec{B} \cdot d\vec{A} = 0 \quad \implies \quad \nabla \cdot \vec{B} = 0 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular el campo magnético $\vec{B}$ a una distancia $r$ de un hilo recto e infinito que transporta una corriente constante $I$.

**Solución paso a paso:**
1. **Identificar la simetría:** El sistema tiene simetría cilíndrica. Las líneas de campo magnético formarán círculos concéntricos alrededor del hilo.
2. **Aplicar la Ley de Ampère:** 
   Seleccionamos un bucle amperiano circular de radio $r$ centrado en el hilo. Por simetría, la magnitud de $\vec{B}$ es constante a lo largo de este bucle, y el vector $\vec{B}$ es tangente a la curva en cada punto.
3. **Calcular la circulación:**
   $$ \oint \vec{B} \cdot d\vec{l} = B \oint dl = B (2\pi r) $$
4. **Relacionar con la corriente:**
   La corriente encerrada por el bucle es $I$. Por lo tanto:
   $$ B (2\pi r) = \mu_0 I $$
5. **Resultado final:**
   $$ B = \frac{\mu_0 I}{2\pi r} $$
   La dirección se obtiene usando la regla de la mano derecha.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. [MIT 8.02 - Electricity and Magnetism](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/): Clases icónicas con demostraciones sobre el campo magnético generado por corrientes, fuerzas de espiras magnéticas e inducción.
2. [Yale PHYS 201 - Fundamentals of Physics II](https://oyc.yale.edu/physics/phys-201): Las magistrales lecciones del Prof. Ramamurti Shankar explorando a detalle la Fuerza de Lorentz, ciclotrones y el tensor electromagnético.
3. [Feynman Lectures on Physics - Vol II, Ch 13: Magnetostatics](https://www.feynmanlectures.caltech.edu/II_13.html): Analiza el comportamiento estacionario de las corrientes y delinea conceptualmente el rotacional del vector magnético.
4. [Khan Academy - Campos Magnéticos](https://es.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields): Una extensa serie de resoluciones en formato de "pizarra virtual", explicando la regla de la mano derecha con pericia.
5. [Coursera - Magnetic Fields and Forces](https://www.coursera.org/learn/physics-102): Ideal para el manejo y cálculo detallado del vector de Ampère y la ley integral de flujo de Biot-Savart en 3D.
6. [edX - E&M: Magnetism and Induction](https://www.edx.org/course/electricity-and-magnetism-part-2): Curso sólido que detalla cómo un flujo magnético variable en una espira origina un campo eléctrico turbillonario no conservativo.

### 📝 Artículos e Interactivos Interesantes
1. [PhET - Laboratorio Electromagnético de Faraday](https://phet.colorado.edu/en/simulations/faradays-law): Genial emulador web interactivo donde se experimenta en tiempo real con un imán de barra, un osciloscopio virtual, un voltímetro, y bobinas de distinto espirado.
2. [HyperPhysics - Magnetism](http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/magcon.html): Recorrido extenso e íntegro sobre la fuerza magnética en cables, momentos magnéticos de espiras, magnetización, ferromagnetismo e histéresis.
3. [Wikipedia: Fuerza de Lorentz](https://es.wikipedia.org/wiki/Fuerza_de_Lorentz): Exposición a fondo de la ecuación del movimiento para partículas cargadas en aceleradores de partículas de altas energías, plasmas y tubos de rayos catódicos.
4. [Wikipedia: Experimento de Ørsted](https://es.wikipedia.org/wiki/Experimento_de_Oersted): Revisión del crucial descubrimiento experimental de 1820 de la interdependencia simbiótica entre espiras de conducción eléctrica y brújulas con aguja imantada.
5. [Física Práctica - Fuerza Magnética](https://www.fisicapractica.com/fuerza-magnetica.php): Breves extractos orientados a resolver las fuerzas transversales ejercidas entre alambres conductores paralelos en direcciones idénticas o contrapuestas.
6. [FísicaLab - El Campo Magnético y el Movimiento](https://www.fisicalab.com/tema/campo-magnetico): Decenas de problemas, explicaciones geométricas e ideas centrales para comprender la trayectoria en espiral que genera un ciclotrón o un espectrómetro de masa.
7. [National MagLab - Magnet Academy](https://nationalmaglab.org/education/magnet-academy): Gran portal educativo (financiado y mantenido por el National High Magnetic Field Laboratory de EEUU) que compila demostraciones maravillosas de diamagnetismo y superconducción a baja temperatura.
8. [LibreTexts - Magnetic Forces and Fields](https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/11%3A_Magnetic_Forces_and_Fields): La bibliografía libre para los cursos básicos de magnetostática de todos los capítulos que conciernen el flujo continuo no esférico magnético.

### 📖 Referencias Útiles y Bibliografía
1. [Introduction to Electrodynamics - David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-electrodynamics/971275E590D0DE07E9CD0DB4F2C2FA04): El texto de referencia por excelencia (estándar de oro) para estudiantes de pregrado en física, claro y didáctico.
2. [Classical Electrodynamics - John David Jackson](https://www.wiley.com/en-us/Classical+Electrodynamics%2C+3rd+Edition-p-9780471309321): Obra matemática y avanzada requerida en todos los posgrados y doctorados del mundo físico.
3. [Electricity and Magnetism - Edward M. Purcell & David J. Morin](https://www.cambridge.org/highereducation/books/electricity-and-magnetism/C16C976ADCD2F4A96DD8DD3DDAB303CE): Magnífico abordaje donde el magnetismo emerge naturalmente como consecuencia de la relatividad especial.
4. [Física Universitaria (Vol. 2) - Sears y Zemansky](https://www.pearson.com/store/p/fisica-universitaria-vol-2/P200000000305/9786073244404): Gran manual estándar ampliamente adoptado por miles de universidades para enseñar fuerza motriz magnética.
5. [Foundations of Electromagnetic Theory - Reitz, Milford & Christy](https://www.pearson.com/store/p/foundations-of-electromagnetic-theory/P200000003666): Libro con abordajes únicos, extremadamente riguroso, especialmente profundo al examinar las propiedades magnéticas de medios magnetizados macroscópicos.
