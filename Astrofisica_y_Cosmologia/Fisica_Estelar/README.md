# Física Estelar

La Física Estelar es la rama de la astrofísica que estudia la formación, evolución, estructura interna y muerte de las estrellas, aplicando los principios de la mecánica cuántica, la termodinámica, el electromagnetismo y la relatividad.

## 📜 Contexto Histórico

La comprensión moderna de las estrellas comenzó a finales del siglo XIX y principios del XX. Cecilia Payne-Gaposchkin (1925) demostró que el Sol y las estrellas están compuestas principalmente de hidrógeno y helio, refutando la creencia previa de que su composición era similar a la de la Tierra. 

Hans Bethe (1939) describió los procesos de fusión nuclear (la cadena protón-protón y el ciclo CNO) que proporcionan la energía que hace brillar a las estrellas. Subrahmanyan Chandrasekhar (1930) dedujo el límite máximo de masa para una enana blanca (Límite de Chandrasekhar, $\sim 1.4 M_\odot$), estableciendo que estrellas más masivas debían colapsar en estrellas de neutrones o agujeros negros. El desarrollo del **Diagrama de Hertzsprung-Russell** (HR) por Ejnar Hertzsprung y Henry Norris Russell en 1910 permitió a los astrónomos clasificar las estrellas y entender su ciclo vital visualmente.

---

## 🧮 Desarrollo Teórico Profundo

El interior de una estrella en equilibrio hidrostático y térmico se describe mediante **cuatro ecuaciones diferenciales fundamentales de la estructura estelar**:

1. **Equilibrio Hidrostático:** (La gravedad se equilibra con el gradiente de presión).
   $$\frac{dP}{dr} = -\frac{GM_r \rho}{r^2}$$
   Donde $P$ es la presión, $r$ es el radio, $M_r$ es la masa encerrada en el radio $r$, y $\rho$ es la densidad local.

2. **Continuidad de Masa:**
   $$\frac{dM_r}{dr} = 4\pi r^2 \rho$$

3. **Generación de Energía:**
   $$\frac{dL_r}{dr} = 4\pi r^2 \rho \epsilon$$
   Donde $L_r$ es la luminosidad en $r$ y $\epsilon$ es la tasa de producción de energía por unidad de masa.

4. **Transporte de Energía (Radiativo o Convectivo):** 
   Para el transporte radiativo (fotones):
   $$\frac{dT}{dr} = -\frac{3\kappa \rho L_r}{16\pi a c T^3 r^2}$$
   Donde $T$ es la temperatura, $\kappa$ es la opacidad, $a$ es la constante de radiación.

**Luminosidad y Fusión:**
Durante la secuencia principal, el Sol fusiona hidrógeno en helio principalmente mediante la cadena protón-protón (p-p). La energía liberada ($Q$) por la fusión de 4 protones en un núcleo de $^4He$ es dada por:
$$\Delta E = (\Sigma m_i - m_f)c^2 \approx 26.73 \text{ MeV}$$

---

## 🛠 Ejemplo Práctico

**Problema:** Estimación de la presión central del Sol asumiendo una densidad constante.

**Solución paso a paso:**
Para un modelo de densidad constante, $\rho(r) = \rho_0 = \frac{M}{(4/3)\pi R^3}$.
1. La ecuación de equilibrio hidrostático es: $\frac{dP}{dr} = -\frac{G M_r \rho_0}{r^2}$.
2. La masa encerrada $M_r$ en un radio $r$ es $M_r = \frac{4}{3}\pi r^3 \rho_0$.
3. Sustituimos $M_r$:
   $$\frac{dP}{dr} = -\frac{G (\frac{4}{3}\pi r^3 \rho_0) \rho_0}{r^2} = -\frac{4\pi}{3} G \rho_0^2 r$$
4. Integramos desde el centro ($r=0, P=P_c$) hasta la superficie ($r=R, P=0$):
   $$\int_{P_c}^{0} dP = -\frac{4\pi}{3} G \rho_0^2 \int_{0}^{R} r \, dr$$
   $$0 - P_c = -\frac{4\pi}{3} G \rho_0^2 \left[ \frac{r^2}{2} \right]_0^R = -\frac{2\pi}{3} G \rho_0^2 R^2$$
   $$P_c = \frac{2\pi}{3} G \rho_0^2 R^2$$
5. Sustituyendo $\rho_0 = \frac{3M}{4\pi R^3}$:
   $$P_c = \frac{2\pi}{3} G \left( \frac{3M}{4\pi R^3} \right)^2 R^2 = \frac{3GM^2}{8\pi R^4}$$
6. Si ponemos los valores del Sol ($M \approx 2 \times 10^{30}$ kg, $R \approx 7 \times 10^8$ m):
   $$P_c \sim 10^{14} \text{ Pa}$$
*(Nota: Un modelo solar real arroja $\sim 10^{16}$ Pa, porque el núcleo es mucho más denso que la media, pero esta estimación básica ilustra el principio).*

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **[Yale Courses: ASTR 160 Frontiers and Controversies in Astrophysics](https://oyc.yale.edu/astronomy/astr-160)** - Profundización impartida por Charles Bailyn, cubriendo evolución estelar, agujeros negros y exoplanetas.
2. **[Ohio State University: Astronomy 1144 / 871 (Richard Pogge)](http://www.astronomy.ohio-state.edu/~pogge/Ast871/)** - Notas de clase excepcionales que detallan de manera accesible pero rigurosa la estructura y vida estelar.
3. **[Coursera: Astronomy: Exploring Time and Space](https://www.coursera.org/learn/astro)** - (Universidad de Arizona) El módulo dedicado a estrellas y su clasificación es altamente ilustrativo.
4. **[MIT 8.284 Modern Astrophysics](https://ocw.mit.edu/courses/8-284-modern-astrophysics-spring-2006/)** - Clases y materiales disponibles vía OCW que cubren las ecuaciones de equilibrio hidrostático y transporte radiativo.
5. **[ANU - Astrophysics: Cosmology & Astrophysics (edX)](https://www.edx.org/micromasters/anu-astrophysics)** - Impartido por Paul Francis y Brian Schmidt, con énfasis en supernovas, remanentes estelares y métodos observacionales.

### 📝 Artículos e Interactivos Interesantes
1. [Naap Labs: Hertzsprung-Russell Diagram Explorer](https://astro.unl.edu/naap/hr/hr_background1.html) - Magnífico simulador interactivo de la Universidad de Nebraska para entender cómo varían luminosidad, temperatura y radio a lo largo de la evolución.
2. [Naap Labs: Eclipsing Binary Simulator](https://astro.unl.edu/naap/ebs/ebs.html) - Herramienta interactiva para entender cómo se miden empíricamente las masas estelares.
3. [Artículo original de Hans Bethe (1939)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.55.434) - "Energy Production in Stars", la publicación histórica que desentrañó la fusión nuclear (ciclo CNO y p-p).
4. [Scholarpedia: Stellar Evolution](http://www.scholarpedia.org/article/Stellar_evolution) - Resumen detallado sobre las diferentes etapas vitales (secuencia principal, gigantes rojas, nebulosas planetarias).
5. [The MESA Project (Modules for Experiments in Stellar Astrophysics)](https://docs.mesastar.org/) - Código open-source de uso profesional para simular la evolución estelar; incluye excelentes tutoriales.
6. [Chandra X-ray Observatory: Supernovas & Supernova Remnants](https://chandra.harvard.edu/xray_sources/supernovas.html) - Galería, datos y artículos sobre las espectaculares muertes de estrellas masivas.
7. [Hubble Site: Stars](https://hubblesite.org/science/stars-and-nebulas) - Artículos y observaciones directas de discos protoplanetarios y enanas blancas.
8. [Wikipedia: Stellar nucleosynthesis](https://en.wikipedia.org/wiki/Stellar_nucleosynthesis) - Cómo los elementos de la tabla periódica se forjan dentro de los núcleos estelares.

### 📖 Referencias Útiles y Bibliografía
- **["An Introduction to Modern Astrophysics" - Bradley W. Carroll y Dale A. Ostlie (El "BOB")](https://www.cambridge.org/highereducation/books/an-introduction-to-modern-astrophysics/8C2B3C2B3A6C5B3E6B4A6C8D8E9F6B5C)**: El texto estándar definitivo de astrofísica a nivel universitario. Tiene un extenso volumen dedicado a física estelar.
- **["Stellar Structure and Evolution" - Rudolf Kippenhahn, Alfred Weigert, y Achim Weiss](https://link.springer.com/book/10.1007/978-3-642-30304-3)**: El clásico absoluto para la teoría avanzada de interiores estelares y el modelado computacional.
- **["Black Holes, White Dwarfs, and Neutron Stars" - Stuart L. Shapiro y Saul A. Teukolsky](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617661)**: La biblia de la física de objetos compactos y los remanentes finales del colapso estelar.
- **["Evolution of Stars and Stellar Populations" - Maurizio Salaris y Santi Cassisi](https://onlinelibrary.wiley.com/doi/book/10.1002/047009219X)**: Excelente recurso para entender tanto estrellas individuales como cúmulos estelares.
- **["Astrophysics in a Nutshell" - Dan Maoz](https://press.princeton.edu/books/hardcover/9780691164793/astrophysics-in-a-nutshell)**: Excelente para repasar rápidamente de manera concisa pero profunda los principios físicos clave detrás del funcionamiento del sol y otras estrellas.
