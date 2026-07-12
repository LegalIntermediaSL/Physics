# Electrostática

La electrostática es la rama de la física que estudia los efectos mutuos que se producen entre los cuerpos como consecuencia de sus cargas eléctricas en reposo. Constituye la base fundamental del electromagnetismo y describe cómo las cargas interactúan mediante fuerzas a distancia, creando campos eléctricos y acumulando energía potencial.

## 📜 Contexto Histórico
El estudio de la electrostática se remonta a la antigüedad clásica, cuando Tales de Mileto observó que frotar ámbar (cuyo nombre en griego es *elektron*) atraía objetos ligeros. Sin embargo, el estudio formal comenzó en el siglo XVIII. Benjamin Franklin propuso el principio de conservación de la carga y acuñó los términos positivo y negativo. En 1785, Charles-Augustin de Coulomb formuló la ley de la fuerza electrostática mediante experimentos con una balanza de torsión. Posteriormente, Michael Faraday introdujo el concepto revolucionario de "campo eléctrico", transformando la física de la acción a distancia en una teoría de campos locales, y Carl Friedrich Gauss formuló el teorema de flujo eléctrico, estableciendo un pilar matemático esencial.

---

## 🧮 Desarrollo Teórico Profundo

El tratamiento riguroso de la electrostática se basa en el análisis de campos vectoriales en reposo macroscópico. A nivel universitario superior, superamos la simple evaluación de cargas puntuales para integrar formulaciones continuas, ecuaciones diferenciales en derivadas parciales y series armónicas complejas.

### 1. El Campo Vectorial y El Teorema de Helmholtz
El teorema de Helmholtz establece que cualquier campo vectorial suave y de decaimiento rápido se determina completamente si conocemos su divergencia y su rotacional. En electrostática, las cargas están en reposo ($\partial \rho/\partial t = 0$, $\vec{J} = \vec{0}$). Postulamos fundamentalmente:
1. **Irrotacionalidad:** $\nabla \times \vec{E} = \vec{0}$.
2. **Fuentes (Ley de Gauss diferencial):** $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$.

Como el rotacional de todo gradiente es idénticamente nulo, la primera condición asegura la existencia de un potencial escalar unívoco (hasta una constante) $V$:
$$ \vec{E} = -\nabla V $$
El trabajo realizado para mover una carga $q$ entre dos puntos $\vec{a}$ y $\vec{b}$ es independiente de la trayectoria:
$$ W = -q \int_{\vec{a}}^{\vec{b}} \vec{E} \cdot d\vec{l} = q[V(\vec{b}) - V(\vec{a})] $$

### 2. Ecuaciones de Poisson y Laplace
Sustituyendo $\vec{E} = -\nabla V$ en la ecuación diferencial de Gauss, obtenemos la **Ecuación de Poisson**:
$$ \nabla \cdot (-\nabla V) = \frac{\rho}{\varepsilon_0} \implies \nabla^2 V = -\frac{\rho}{\varepsilon_0} $$
donde $\nabla^2$ es el operador Laplaciano. Esta es la ecuación fundamental de la electrostática para resolver el potencial en presencia de una distribución de carga conocida. 

En las regiones libres de carga ($\rho = 0$), esto se reduce a la **Ecuación de Laplace**:
$$ \nabla^2 V = 0 $$
Las soluciones a la ecuación de Laplace (funciones armónicas) no admiten máximos ni mínimos locales en el interior del dominio, sólo en sus fronteras (Teorema del Máximo). La unicidad de la solución para un conjunto de condiciones de contorno (Dirichlet o Neumann) está garantizada por el **Teorema de Unicidad**.

### 3. Desarrollo Multipolar
A menudo necesitamos evaluar el potencial o el campo eléctrico generado por una distribución de carga localizada compleja en un punto lejano $|\vec{r}| \gg |\vec{r}'|$. Utilizamos una expansión en serie de Taylor del término $1/|\vec{r} - \vec{r}'|$ (empleando polinomios de Legendre), obteniendo el **Desarrollo Multipolar**:
$$ V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int (r')^n P_n(\cos\theta') \rho(\vec{r}') \, d\tau' $$
Los primeros términos son:
1. **Monopolar ($n=0$):** $V_{\text{mono}}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r}$, donde $Q = \int \rho \, d\tau$ es la carga neta.
2. **Dipolar ($n=1$):** $V_{\text{dip}}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \frac{\vec{p} \cdot \hat{r}}{r^2}$, donde $\vec{p} = \int \vec{r}' \rho(\vec{r}') \, d\tau'$ es el momento dipolar eléctrico.
3. **Cuadrupolar ($n=2$):** $V_{\text{cuad}}(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \frac{1}{2 r^3} \sum_{i,j} \hat{r}_i \hat{r}_j Q_{ij}$, donde $Q_{ij}$ es el tensor momento cuadrupolar nulo en traza.

### 4. Energía Electroestática y Tensión de Maxwell
La energía requerida para ensamblar una distribución discreta de cargas desde el infinito es:
$$ U = \frac{1}{2} \sum_{i \neq j} \frac{1}{4\pi\varepsilon_0} \frac{q_i q_j}{|\vec{r}_i - \vec{r}_j|} = \frac{1}{2} \sum_i q_i V(\vec{r}_i) $$
Pasando al límite continuo, la energía electrostática total almacenada en todo el espacio es:
$$ U = \frac{1}{2} \int \rho V \, d\tau $$
Podemos reescribir esto enteramente en función del campo eléctrico. Sustituyendo $\rho = \varepsilon_0 \nabla \cdot \vec{E}$ e integrando por partes, asumiendo que el campo decae suficientemente rápido en el infinito:
$$ U = \frac{\varepsilon_0}{2} \int |\vec{E}|^2 \, d\tau $$
Esto nos dice que la energía electrostática está almacenada *en el propio campo*, con una densidad de energía $u = \frac{\varepsilon_0}{2} |\vec{E}|^2$. 
Las fuerzas sobre los conductores pueden calcularse de forma elegante utilizando el **Tensor de Esfuerzos de Maxwell** $T_{ij}$:
$$ T_{ij} = \varepsilon_0 \left( E_i E_j - \frac{1}{2} \delta_{ij} |\vec{E}|^2 \right) $$
Donde la fuerza neta sobre un volumen $V$ contenido en una superficie $S$ es simplemente la integral del flujo de la tensión a través de la superficie:
$$ \vec{F} = \oint_S \mathbf{T} \cdot d\vec{A} $$

```mermaid
flowchart TD
    A[Carga en reposo \rho] -->|Ley de Coulomb| B(Campo Vectorial E)
    A -->|Ecuación de Poisson| C(Potencial Escalar V)
    B -->|Gradiente E = -\nabla V| C
    C -->|Integral de Camino V = -\int E \cdot dl| B
    B -->|Integral de Superficie \epsilon_0/2 |E|^2| D{Energía Electrostática U}
    C -->|Integral de Volumen 1/2 \int \rho V| D
    B -->|Expansión en el infinito| E[Desarrollo Multipolar]
```

### 5. Problemas de Frontera: Método de Imágenes
Un problema clásico es calcular el potencial en la vecindad de conductores perfectos sometidos a cargas externas. Dado que la superficie de un conductor ideal es equipotencial, la Ecuación de Poisson y el Teorema de Unicidad nos permiten sustituir las superficies conductoras por "cargas imagen" virtuales ubicadas fuera de nuestra región de interés. 
Por ejemplo, para una carga puntual $q$ a distancia $d$ de un plano conductor infinito a tierra ($V=0$), la solución se obtiene idénticamente colocando una carga imagen $-q$ a una distancia $d$ detrás del plano (como en un espejo). El potencial total válido para $z > 0$ es la superposición del potencial de ambas cargas puntuales, sin resolver explícitamente ecuaciones diferenciales de frontera.

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
