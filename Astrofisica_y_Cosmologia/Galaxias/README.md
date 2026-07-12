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
- **UC Irvine: Physics 20B Cosmology (James Bullock)** - Aborda profundamente halos de materia oscura y formación de galaxias.
- **MIT 8.286 The Early Universe** - Alan Guth cubre aspectos de estructura a gran escala.
- **Canal de YouTube Dr. Becky** - Excelente investigadora (Becky Smethurst) que explica evolución galáctica y agujeros negros supermasivos.

### 📝 Artículos e Interactivos Interesantes
- [Galaxy Zoo (Zooniverse)](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/) - Proyecto de ciencia ciudadana para clasificar galaxias.
- [Sloan Digital Sky Survey (SDSS)](https://www.sdss.org/) - Mapas 3D del universo para explorar estructuras galácticas.
- Artículo de Vera Rubin (1970) sobre las curvas de rotación de Andrómeda.
