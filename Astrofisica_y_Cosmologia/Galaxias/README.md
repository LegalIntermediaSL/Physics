# Galaxias

El estudio de las Galaxias comprende la dinámica, formación, evolución y morfología de las estructuras masivas unidas gravitacionalmente que contienen estrellas, gas estelar, polvo cósmico y materia oscura.

## 📜 Contexto Histórico

Hasta principios del siglo XX, muchos astrónomos creían que la Vía Láctea constituía la totalidad del universo, y que las "nebulosas espirales" observadas eran sistemas solares en formación dentro de nuestra galaxia. Este debate culminó en 1920 con el "Gran Debate" entre Harlow Shapley y Heber Curtis.

En 1924, Edwin Hubble resolvió el debate al utilizar estrellas variables Cefeidas en la galaxia de Andrómeda para medir su distancia. Hubble demostró que Andrómeda estaba mucho más allá de los límites de la Vía Láctea, probando que el universo contiene múltiples "universos islas" o galaxias. En 1926, Hubble creó el sistema de **Clasificación Morfológica de Galaxias** (el "Diapasón de Hubble"), clasificándolas en Elípticas, Espirales y Lenticulares.

Posteriormente, en la década de 1970, Vera Rubin observó las curvas de rotación de las galaxias espirales. Encontró que las estrellas en los bordes de la galaxia se movían demasiado rápido para ser contenidas por la masa visible, proporcionando una de las evidencias más fuertes de la existencia del **Halo de Materia Oscura**.

---

## 🧮 Desarrollo Teórico Profundo

**Dinámica Galáctica y Curvas de Rotación:**
En una galaxia espiral, si asumimos órbitas circulares para las estrellas en el disco, la velocidad de rotación orbital $v(r)$ a una distancia $r$ del centro se deriva igualando la fuerza centrípeta y la gravitacional:

$$\frac{mv^2}{r} = \frac{GM(r)m}{r^2}$$
$$v(r) = \sqrt{\frac{GM(r)}{r}}$$

Donde $M(r)$ es la masa encerrada en un radio $r$. Si toda la masa de la galaxia estuviera concentrada en el bulto central visible (como en el Sistema Solar), esperaríamos que, en las regiones externas, $M(r) \approx M_{total}$ sea constante, y por tanto la velocidad disminuya como un perfil kepleriano: $v(r) \propto 1/\sqrt{r}$.

Sin embargo, las observaciones muestran que $v(r)$ permanece constante (curva plana) para valores muy grandes de $r$. Para que $v(r)$ sea constante ($v(r) = V_c$), debe ocurrir que:
$$M(r) = \frac{V_c^2 r}{G} \implies M(r) \propto r$$
Si la masa encerrada crece linealmente con el radio, la densidad del halo de materia oscura debe ser de la forma:
$$\rho(r) = \frac{1}{4\pi r^2} \frac{dM}{dr} = \frac{V_c^2}{4\pi G r^2}$$
Esto implica un halo esférico de materia oscura con un perfil de densidad de la "esfera isoterma singular" que se extiende mucho más allá del disco visible.

**Teorema de Relajación Violenta (Donald Lynden-Bell, 1967):**
Explica por qué las galaxias elípticas tienen una distribución regular a pesar de formarse a partir de colapsos asimétricos y fusiones, mediante una termalización del gas sin necesidad de colisiones cuerpo a cuerpo de estrellas.

---

## 🛠 Ejemplo Práctico

**Problema:** Una galaxia espiral exhibe una velocidad de rotación plana de $v = 220$ km/s. Calcula la masa de la galaxia encerrada en un radio de $r = 20$ kpc (kiloparsecs). (Considera $1 \text{ kpc} \approx 3.086 \times 10^{19} \text{ m}$).

**Solución paso a paso:**
1. Datos conocidos:
   - $v = 220 \text{ km/s} = 2.2 \times 10^5 \text{ m/s}$
   - $r = 20 \text{ kpc} = 20 \times 3.086 \times 10^{19} \text{ m} = 6.172 \times 10^{20} \text{ m}$
   - $G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$
2. Utilizamos la fórmula de velocidad orbital derivada del equilibrio gravitacional:
   $$v = \sqrt{\frac{GM}{r}} \implies M = \frac{v^2 r}{G}$$
3. Sustituimos valores:
   $$M = \frac{(2.2 \times 10^5)^2 \times (6.172 \times 10^{20})}{6.674 \times 10^{-11}}$$
   $$M = \frac{(4.84 \times 10^{10}) \times (6.172 \times 10^{20})}{6.674 \times 10^{-11}}$$
   $$M = \frac{29.87 \times 10^{30}}{6.674 \times 10^{-11}} \approx 4.47 \times 10^{41} \text{ kg}$$
4. Convertimos a masas solares ($1 M_\odot \approx 1.989 \times 10^{30} \text{ kg}$):
   $$M \approx \frac{4.47 \times 10^{41}}{1.989 \times 10^{30}} \approx 2.25 \times 10^{11} M_\odot$$
5. La masa encerrada en esos 20 kpc es aproximadamente 225 mil millones de masas solares (lo cual incluye mucha materia oscura).

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **[UC Irvine: Physics 20B Cosmology (James Bullock)](https://www.youtube.com/playlist?list=PLqOZ6FD_RQ7nwb-mX-Z6G5fFv9yO-F18i)** - Aborda profundamente halos de materia oscura, rotación galáctica y modelos de formación jerárquica.
2. **[MIT 8.286 The Early Universe](https://ocw.mit.edu/courses/8-286-the-early-universe-fall-2013/)** - Incluye aspectos de la estructura a gran escala del universo y cómo las fluctuaciones primordiales dieron lugar a las galaxias.
3. **[Canal de YouTube Dr. Becky](https://www.youtube.com/c/DrBecky)** - Becky Smethurst es una destacada investigadora de galaxias y agujeros negros supermasivos que explica fenomenalmente la evolución galáctica en video.
4. **[Caltech - Ay 127: Cosmology and Galaxy Formation](http://www.astro.caltech.edu/~george/ay127/)** - Material avanzado (a menudo disponible de forma gratuita por profesores) sobre los detalles finos del medio intergaláctico y simulaciones N-body.
5. **[Coursera: Galaxies and Cosmology (Caltech / varios)](https://www.coursera.org/learn/astro)** - Módulos introductorios que explican las formas galácticas, el grupo local, colisiones y la historia temprana del universo galáctico.

### 📝 Artículos e Interactivos Interesantes
1. [Galaxy Zoo (Zooniverse)](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/) - Un proyecto de ciencia ciudadana famosísimo donde puedes ayudar a astrónomos a clasificar millones de galaxias según su morfología.
2. [Sloan Digital Sky Survey (SDSS)](https://www.sdss.org/) - Una de las cartografías digitales más grandes del cielo nocturno. Permite explorar la estructura a gran escala, agrupaciones y el espectro de millones de galaxias.
3. [Vera Rubin's 1970 Paper en The Astrophysical Journal](https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R/abstract) - Artículo original donde establece de forma robusta las curvas de rotación de galaxias espirales (Andrómeda).
4. [Illustris Project / IllustrisTNG](https://www.illustris-project.org/) - Simulaciones computacionales masivas de formación galáctica desde el Big Bang hasta hoy. Tienen espectaculares visualizaciones y videos.
5. [Hubble Ultra Deep Field (NASA)](https://esahubble.org/images/heic0611b/) - La histórica imagen que capturó miles de galaxias muy lejanas en un parche aparentemente vacío del cielo.
6. [Scholarpedia: Galaxy Formation](http://www.scholarpedia.org/article/Galaxy_formation) - Explicaciones detalladas de la disipación de gas, halos de materia oscura y retroalimentación de supernovas/agujeros negros.
7. [NASA/IPAC Extragalactic Database (NED)](https://ned.ipac.caltech.edu/) - La base de datos definitiva de objetos extragalácticos para investigadores y aficionados serios.
8. [Space Telescope Science Institute: Galaxies](https://www.stsci.edu/) - Investigaciones recientes impulsadas por el James Webb Space Telescope (JWST) sobre las primeras galaxias del universo.

### 📖 Referencias Útiles y Bibliografía
- **["Galactic Dynamics" - James Binney y Scott Tremaine](https://press.princeton.edu/books/paperback/9780691130279/galactic-dynamics)**: El tratado definitivo y avanzado (nivel de posgrado) sobre cómo se mueven las estrellas y el gas dentro del campo gravitacional galáctico.
- **["Galaxies in the Universe: An Introduction" - Linda S. Sparke y John S. Gallagher III](https://www.cambridge.org/highereducation/books/galaxies-in-the-universe/6F045A9524584288C00F7A598F6B928E)**: Un texto excepcional para niveles de pregrado y posgrado temprano, que conecta observaciones con las teorías físicas.
- **["Extragalactic Astronomy and Cosmology: An Introduction" - Peter Schneider](https://link.springer.com/book/10.1007/978-3-642-54083-7)**: Cubre todo lo que está más allá de la Vía Láctea, incluyendo núcleos galácticos activos y cuásares.
- **["Galaxy Formation and Evolution" - Houjun Mo, Frank van den Bosch, y Simon White](https://www.cambridge.org/highereducation/books/galaxy-formation-and-evolution/8C4A731F75B26E9528D8E9F6A24D3D52)**: Una referencia moderna monumental para entender la física completa (gas, enfriamiento, fusión) que forma el zoológico galáctico.
- **["An Introduction to Modern Astrophysics" - B. Carroll y D. Ostlie](https://www.cambridge.org/highereducation/books/an-introduction-to-modern-astrophysics/8C2B3C2B3A6C5B3E6B4A6C8D8E9F6B5C)**: También provee capítulos robustos en su sección extragaláctica, ideales como primer encuentro formal con las ecuaciones de galaxias espirales y elípticas.
