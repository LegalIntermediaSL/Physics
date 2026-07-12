# Cosmología del Big Bang

La Cosmología del Big Bang es el modelo estándar sobre el origen y evolución del universo, que postula que este comenzó en un estado extremadamente caliente y denso hace unos 13.800 millones de años, y ha estado expandiéndose y enfriándose desde entonces.

## 📜 Contexto Histórico

En la década de 1920, las soluciones a las ecuaciones de la Relatividad General de Einstein por parte de Alexander Friedmann (1922) y Georges Lemaître (1927) sugerían que el universo no era estático, sino dinámico (pudiendo expandirse o contraerse). Einstein, prefiriendo un universo estático, introdujo la Constante Cosmológica para forzar esta quietud.

Sin embargo, en 1929, Edwin Hubble descubrió la **Ley de Hubble-Lemaître**: las galaxias se alejan de nosotros con una velocidad proporcional a su distancia, la primera prueba empírica de la expansión del universo. Lemaître propuso la teoría del "Átomo Primigenio", sugiriendo que si hoy el universo se expande, en el pasado debió estar concentrado en un punto.

El modelo rival de Estado Estacionario (Fred Hoyle, 1948) perdió apoyo definitivamente cuando en 1964 Arno Penzias y Robert Wilson descubrieron accidentalmente el **Fondo Cósmico de Microondas (CMB)**, el remanente térmico previsto por la teoría del Big Bang. En los 90s, el estudio de supernovas tipo Ia reveló que esta expansión está acelerada debido a la llamada **Energía Oscura**.

---

## 🧮 Desarrollo Teórico Profundo

El universo a gran escala se asume homogéneo e isótropo (Principio Cosmológico). La geometría del espacio-tiempo está descrita por la **Métrica de Friedmann-Lemaître-Robertson-Walker (FLRW)**:

$$ds^2 = c^2 dt^2 - a(t)^2 \left[ \frac{dr^2}{1 - kr^2} + r^2(d\theta^2 + \sin^2\theta d\phi^2) \right]$$

Donde:
- $a(t)$ es el **factor de escala cosmológico** (describe cómo crece el espacio).
- $k$ es el parámetro de curvatura espacial ($k=0$ plano, $k=1$ cerrado, $k=-1$ abierto).

Sustituyendo esta métrica en las Ecuaciones de Einstein, se obtienen las **Ecuaciones de Friedmann**:

1. **Primera Ecuación de Friedmann (Evolución de la expansión):**
   $$H^2 = \left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}$$
   Donde $H(t) \equiv \dot{a}/a$ es el **Parámetro de Hubble**.

2. **Segunda Ecuación de Friedmann (Ecuación de Aceleración):**
   $$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3} \left( \rho + \frac{3P}{c^2} \right) + \frac{\Lambda c^2}{3}$$
   Donde $\rho$ es la densidad de energía y $P$ la presión.

**Densidad Crítica:**
Si tomamos $k=0$ y $\Lambda=0$, el universo es plano. La densidad requerida para esto es la densidad crítica:
$$\rho_c = \frac{3H^2}{8\pi G}$$

**Desplazamiento al Rojo (Redshift):**
La expansión estira la longitud de onda de la luz:
$$1 + z = \frac{\lambda_{\text{observada}}}{\lambda_{\text{emitida}}} = \frac{a(t_0)}{a(t_e)}$$
Donde $t_0$ es el tiempo actual y $t_e$ el tiempo de emisión.

---

## 🛠 Ejemplo Práctico

**Problema:** Suponiendo que el universo actual está dominado por materia no relativista, ¿cómo escala el factor de escala $a(t)$ con el tiempo?

**Solución paso a paso:**
1. Para la materia (polvo), la ecuación de continuidad hidrodinámica cósmica dice que la densidad disminuye con el volumen: 
   $$\rho_m \propto a^{-3} \implies \rho_m = \frac{\rho_0}{a^3}$$
   (Asumiendo $a(t_0) = 1$).
2. Partimos de la primera Ecuación de Friedmann para un universo plano ($k=0$) sin constante cosmológica ($\Lambda=0$):
   $$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \rho_m$$
3. Sustituyendo $\rho_m$:
   $$\frac{\dot{a}^2}{a^2} = \frac{8\pi G \rho_0}{3 a^3} \implies \dot{a}^2 = \frac{8\pi G \rho_0}{3 a}$$
4. Por lo tanto, $\dot{a} \propto a^{-1/2}$. Tomemos una constante de proporcionalidad $C$:
   $$\frac{da}{dt} = C a^{-1/2}$$
5. Integramos por separación de variables:
   $$\int a^{1/2} da = \int C dt$$
   $$\frac{2}{3} a^{3/2} = C t \implies a^{3/2} \propto t$$
6. Despejando $a(t)$:
   $$a(t) \propto t^{2/3}$$
**Conclusión:** En un universo plano y dominado por materia (como fue gran parte de la historia del universo antes de la dominación de la energía oscura), el factor de escala crece como $t^{2/3}$.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **[Stanford University: Cosmology (Leonard Susskind)](https://theoreticalminimum.com/courses/cosmology/2013/winter)** - Parte del "Theoretical Minimum", explica en detalle las métricas y ecuaciones de Friedmann usando la relatividad general.
2. **[MIT 8.286 The Early Universe](https://ocw.mit.edu/courses/8-286-the-early-universe-fall-2013/)** - Curso completo por Alan Guth, el creador de la teoría de la inflación cósmica, disponible en MIT OpenCourseWare.
3. **[Perimeter Institute Seminars](https://pirsa.org/)** - Grabaciones gratuitas de conferencias avanzadas debatiendo el estado actual del modelo estándar cosmológico.
4. **[Coursera: From the Big Bang to Dark Energy](https://www.coursera.org/learn/big-bang)** - Curso de la Universidad de Tokio (Hitoshi Murayama) que cubre la formación de estructuras, inflación y energía oscura.
5. **[UC Irvine - Physics 20B: Cosmology (James Bullock)](https://www.youtube.com/playlist?list=PLqOZ6FD_RQ7nwb-mX-Z6G5fFv9yO-F18i)** - Clases fundamentales de pregrado que enseñan la historia térmica del universo y materia oscura.

### 📝 Artículos e Interactivos Interesantes
1. [Planck Legacy Archive (ESA)](http://pla.esac.esa.int/) - Acceso a los mapas e imágenes reales del fondo cósmico de microondas obtenidos por la misión Planck.
2. [Ned Wright's Cosmology Tutorial & Calculator](http://www.astro.ucla.edu/~wright/CosmoCalc.html) - Herramienta clave e interactiva para calcular tiempos, distancias y escalas según el corrimiento al rojo ($z$).
3. [Wikipedia: Timeline of the early universe](https://en.wikipedia.org/wiki/Timeline_of_the_early_universe) - Un repaso cronológico profundo y detallado de las primeras fracciones de segundo.
4. [NASA WMAP Science](https://map.gsfc.nasa.gov/universe/) - Recurso educativo sobre la misión WMAP que estableció de forma precisa la edad del universo (13.77 mil millones de años).
5. [The Dark Energy Survey (DES)](https://www.darkenergysurvey.org/) - Página oficial con los hallazgos y metodologías para trazar la historia de expansión cósmica.
6. [Scholarpedia: Inflationary Cosmology](http://www.scholarpedia.org/article/Cosmic_inflation) - Un análisis riguroso escrito por expertos sobre cómo la inflación resuelve los problemas del Big Bang clásico.
7. [Cosmic Microwave Background Simulator](http://lambda.gsfc.nasa.gov/) - Herramientas de simulación y bases de datos del LAMBDA (Legacy Archive for Microwave Background Data Analysis).
8. [Supernova Cosmology Project](http://scp.berkeley.edu/) - Datos históricos y explicaciones sobre el descubrimiento de la energía oscura usando supernovas Tipo Ia.

### 📖 Referencias Útiles y Bibliografía
- **["Cosmology" - Steven Weinberg](https://global.oup.com/academic/product/cosmology-9780198526827)**: Un texto fundamental y riguroso; es el estándar de oro en cursos de posgrado.
- **["Introduction to Cosmology" - Barbara Ryden](https://www.cambridge.org/highereducation/books/introduction-to-cosmology/A7080DA9D6A9C5D089E4670DAB5259B2)**: Posiblemente el libro de introducción a la cosmología más claro y accesible para nivel de pregrado, excelente para entender la Ecuación de Friedmann.
- **["The First Three Minutes" - Steven Weinberg](https://www.basicbooks.com/titles/steven-weinberg/the-first-three-minutes/9780465024377/)**: Un clásico de divulgación que explica de manera brillante la termodinámica del universo temprano.
- **["Modern Cosmology" - Scott Dodelson](https://shop.elsevier.com/books/modern-cosmology/dodelson/978-0-12-815948-4)**: Texto avanzado muy utilizado que se enfoca en las perturbaciones cosmológicas y el análisis del CMB.
- **["An Introduction to Modern Cosmology" - Andrew Liddle](https://www.wiley.com/en-us/An+Introduction+to+Modern+Cosmology%2C+3rd+Edition-p-9781118502143)**: Otra opción fenomenal, un poco más breve que Ryden, para cursos introductorios universitarios.
