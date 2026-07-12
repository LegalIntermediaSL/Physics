# Propiedades Electrónicas y Bandas

La teoría de bandas de los sólidos es el modelo cuántico que explica el comportamiento de los electrones en la materia condensada. Al someter a los electrones a un potencial periódico creado por la red cristalina, sus niveles de energía permitidos se agrupan en "bandas" continuas separadas por "brechas" (bandgaps) de energías prohibidas. Esta teoría es la piedra angular para entender por qué existen metales, aislantes y semiconductores.

## 📜 Contexto Histórico

El modelo del electrón libre fue propuesto inicialmente por Paul Drude (1900) y mejorado con la estadística cuántica por Arnold Sommerfeld (1927). Sin embargo, este modelo no podía explicar la existencia de aislantes o semiconductores. En 1928, Felix Bloch desarrolló el teorema que lleva su nombre, aplicando la mecánica cuántica a partículas en potenciales periódicos. Poco después, A.H. Wilson formuló la teoría moderna de semiconductores en 1931, basándose en la idea de que los materiales con bandas totalmente llenas y un gran bandgap actúan como aislantes, mientras que aquellos con bandas parcialmente llenas son conductores.

## 🧮 Desarrollo Teórico Profundo

El movimiento de un electrón en un cristal está gobernado por la ecuación de Schrödinger con un potencial periódico $U(\mathbf{r}) = U(\mathbf{r} + \mathbf{R})$, donde $\mathbf{R}$ es un vector de la red de Bravais.
$$ \left[ -\frac{\hbar^2}{2m} \nabla^2 + U(\mathbf{r}) \right] \psi(\mathbf{r}) = E \psi(\mathbf{r}) $$

El **Teorema de Bloch** establece que los autoestados de este Hamiltoniano tienen la forma de una onda plana modulada por una función que comparte la periodicidad de la red:
$$ \psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}) $$
donde $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{n\mathbf{k}}(\mathbf{r})$, $n$ es el índice de banda y $\mathbf{k}$ es el vector de onda en la primera zona de Brillouin.

El **Modelo de Kronig-Penney** ofrece una solución analítica para un potencial periódico unidimensional compuesto por barreras delta de Dirac. La condición para los valores permitidos de $k$ resulta en:
$$ P \frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a) = \cos(ka) $$
donde $P$ es proporcional a la "fuerza" de la barrera de potencial y $\alpha = \sqrt{2mE}/\hbar$. Como la función del lado izquierdo debe estar en el intervalo $[-1, 1]$ para que haya soluciones reales de $k$, se producen rangos de energía $E$ permitidos (bandas) y prohibidos (bandgaps).

## 🛠 Ejemplo Práctico

**Problema:** Derivar la masa efectiva $m^*$ de un electrón cerca del mínimo de una banda de conducción, asumiendo una relación de dispersión parabólica.

**Solución paso a paso:**
1. Cerca del mínimo de una banda (digamos en $\mathbf{k} = 0$), la energía $E(\mathbf{k})$ se puede expandir en serie de Taylor:
   $$ E(\mathbf{k}) \approx E(0) + \nabla_{\mathbf{k}} E \cdot \mathbf{k} + \frac{1}{2} \sum_{i,j} k_i \frac{\partial^2 E}{\partial k_i \partial k_j} k_j $$
2. En el mínimo de la banda, el término de la primera derivada es cero ($\nabla_{\mathbf{k}} E = 0$). Asumiendo isotropía, la matriz de segundas derivadas (el tensor de masa efectiva) se simplifica y podemos escribir:
   $$ E(\mathbf{k}) \approx E_c + \frac{1}{2} \frac{\partial^2 E}{\partial k^2} k^2 $$
3. Para una partícula libre, la energía clásica y cuántica es $E = \frac{p^2}{2m} = \frac{\hbar^2 k^2}{2m}$.
4. Comparando ambas expresiones, definimos la **masa efectiva** $m^*$ del electrón en el cristal de modo que la relación de dispersión recupere la forma de la partícula libre:
   $$ \frac{\hbar^2}{2m^*} = \frac{1}{2} \frac{\partial^2 E}{\partial k^2} \implies m^* = \hbar^2 \left( \frac{\partial^2 E}{\partial k^2} \right)^{-1} $$
**Conclusión:** La inercia del electrón frente a fuerzas externas dentro del cristal está determinada por la curvatura de la banda de energía. Una banda muy plana resulta en una masa efectiva muy grande (electrón "pesado").

## 📚 Recursos Específicos

### Cursos
1. **[Semiconductor Devices (Coursera / Purdue)](https://www.coursera.org):** Excelente introducción a cómo las bandas definen la funcionalidad de los dispositivos.
2. **[Quantum Theory of Materials (Oxford)](https://www.ox.ac.uk):** Teoría rigurosa sobre el comportamiento de electrones en redes periódicas.
3. **[Electronic Structure of Solids (MIT OCW)](https://ocw.mit.edu):** Enfocado en modelos de enlace fuerte (tight-binding) y ondas planas.
4. **[NPTEL Electronic Materials](https://nptel.ac.in):** Estudio detallado de materiales semiconductores y metales.
5. **[Band Theory of Solids (edX)](https://www.edx.org):** Ideal para estudiantes que recién se introducen al espacio k y zonas de Brillouin.

### Artículos y Simulaciones
1. **[nanoHUB "Band Structure"](https://nanohub.org):** Simulador online interactivo para calcular estructuras de bandas.
2. **["Energy Bands in Solids" (Bloch's original concepts)](https://archive.org):** Notas sobre la formulación original del teorema de Bloch.
3. **[Wannier90 (Software)](http://www.wannier.org/):** Herramienta clave para construir orbitales localizados a partir de bandas (simulaciones avanzadas).
4. **["Graphene: Status and Prospects" (Geim, Science)](https://www.science.org):** Artículo sobre el modelo de bandas más famoso y de cono de Dirac.
5. **[Tight-Binding Studio](https://tight-binding.com/):** Aplicación para generar bandas de energía con modelos tight-binding fenomenológicos.
6. **[VASP / Quantum Espresso examples](https://www.quantum-espresso.org/):** Simulaciones DFT para obtener bandas de materiales reales.
7. **["The physics of bandgaps" (Review paper)](https://journals.aps.org):** Lectura fundamental sobre por qué se abren los bandgaps.
8. **[ARPES simulators](https://arxiv.org):** Para entender cómo se miden las bandas experimentalmente con fotoemisión.
9. **[PhET Semiconductors](https://phet.colorado.edu):** Muestra conceptos básicos de bandas de valencia y conducción interactivos.

### 📖 Referencias Útiles y Bibliografía
1. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://archive.org) (Particularmente caps. 8-10).
2. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org).
3. [Sutton, A. P. *Electronic Structure of Materials*](https://global.oup.com). Oxford University Press.
4. [Sze, S. M. *Physics of Semiconductor Devices*](https://www.wiley.com). Wiley.
