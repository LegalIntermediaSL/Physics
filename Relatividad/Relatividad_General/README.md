# Relatividad General

La Relatividad General es la teoría métrica de la gravitación publicada por Albert Einstein en 1915, que describe la gravedad no como una fuerza, sino como una curvatura del espacio-tiempo causada por la masa y la energía.

## 📜 Contexto Histórico

Tras formular la Relatividad Especial en 1905, Einstein se dio cuenta de que esta teoría no era compatible con la ley de la gravitación universal de Newton, la cual implicaba una acción a distancia instantánea, violando el límite de la velocidad de la luz. 

Durante una década de intensa investigación y colaboración matemática con Marcel Grossmann, Einstein formuló el **Principio de Equivalencia** (1907), que postula que la gravedad y la aceleración son localmente indistinguibles. Usando la geometría diferencial de Riemann, Einstein concluyó que la presencia de masa o energía curva el espacio-tiempo. En noviembre de 1915, presentó las Ecuaciones de Campo de Einstein a la Academia Prusiana de las Ciencias. La teoría fue confirmada dramáticamente en 1919 por Arthur Eddington durante un eclipse solar al medir la deflexión de la luz de las estrellas, consolidando la fama mundial de Einstein.

---

## 🧮 Desarrollo Teórico Profundo

El núcleo de la Relatividad General son las **Ecuaciones de Campo de Einstein** (EFE). Son un conjunto de 10 ecuaciones diferenciales parciales no lineales (escritas como una única ecuación tensorial) que relacionan la geometría del espacio-tiempo con la distribución de materia y energía.

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Donde:
- $R_{\mu\nu}$: Tensor de curvatura de Ricci.
- $R$: Escalar de Ricci (curvatura escalar).
- $g_{\mu\nu}$: Tensor métrico (describe la métrica del espacio-tiempo).
- $\Lambda$: Constante cosmológica.
- $G$: Constante de gravitación universal.
- $c$: Velocidad de la luz.
- $T_{\mu\nu}$: Tensor de energía-impulso (densidad y flujo de energía y momento).

El lado izquierdo representa la **curvatura del espacio-tiempo**, y el lado derecho representa el **contenido de materia y energía**. En palabras de John Archibald Wheeler: *"El espacio-tiempo le dice a la materia cómo moverse; la materia le dice al espacio-tiempo cómo curvarse."*

**La Métrica de Schwarzschild:**
La primera solución exacta a estas ecuaciones fue encontrada por Karl Schwarzschild (1916) para una masa esférica y no rotatoria en el vacío. La métrica es:

$$ds^2 = \left(1 - \frac{r_s}{r}\right)c^2 dt^2 - \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 - r^2(d\theta^2 + \sin^2\theta d\phi^2)$$

Donde $r_s = \frac{2GM}{c^2}$ es el **Radio de Schwarzschild**. Si un objeto colapsa por debajo de este radio, se forma un agujero negro, de donde ni siquiera la luz puede escapar.

---

## 🛠 Ejemplo Práctico

**Problema:** Calcula el radio de Schwarzschild para el Sol ($M = 1.989 \times 10^{30}$ kg). Si el Sol colapsara a un agujero negro sin perder masa, ¿cuál sería el radio de su horizonte de sucesos?

**Solución paso a paso:**
1. Datos conocidos:
   - $G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$
   - $M = 1.989 \times 10^{30} \text{ kg}$
   - $c = 3 \times 10^8 \text{ m/s}$
2. Aplicamos la fórmula del radio de Schwarzschild:
   $$r_s = \frac{2GM}{c^2}$$
3. Sustituimos los valores:
   $$r_s = \frac{2 \times (6.674 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3 \times 10^8)^2}$$
4. Realizamos los cálculos:
   - Numerador: $2 \times 6.674 \times 1.989 \times 10^{19} \approx 26.549 \times 10^{19}$
   - Denominador: $9 \times 10^{16}$
   $$r_s = \frac{26.549 \times 10^{19}}{9 \times 10^{16}} \approx 2.95 \times 10^3 \text{ metros}$$
5. Conclusión: El radio de Schwarzschild del Sol es aproximadamente 2.95 km (o $\approx 3$ km).

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas (5-7 Recomendados)
1. **[Stanford University: General Relativity (Leonard Susskind)](https://theoreticalminimum.com/courses/general-relativity/2012/fall)** - Excelente punto de partida para aprender sobre la geometría riemanniana, métricas y las ecuaciones de campo de Einstein de forma accesible.
2. **[MIT OpenCourseWare: 8.962 General Relativity (Scott Hughes)](https://ocw.mit.edu/courses/8-962-general-relativity-spring-2020/)** - Curso integral de posgrado que cubre a fondo tensores, métricas de Schwarzschild, ondas gravitacionales y cosmología.
3. **[Perimeter Institute: General Relativity Courses](https://perimeterinstitute.ca/training/perimeter-scholars-international/psi-lectures)** - Múltiples cursos ofrecidos por investigadores de primer nivel sobre la estructura causal, horizontes de eventos y gravedad cuántica.
4. **[International Centre for Theoretical Sciences (ICTS): General Relativity](https://www.youtube.com/playlist?list=PL04QVxpjcnjjB7Qx7xJtd9Y7X8iYx5n0z)** - Clases en video de alta calidad sobre la formulación geométrica de la gravedad.
5. **[Coursera: Astrophysics and General Relativity](https://www.coursera.org/learn/general-relativity)** - Variedad de cursos modulares impartidos por diferentes universidades explorando los aspectos astrofísicos.
6. **[PBS Space Time (YouTube)](https://www.youtube.com/playlist?list=PLsPUh22kYmNBl4h0i4mC51829e_jT-0c1)** - Serie exhaustiva sobre el espacio-tiempo, la métrica y cómo los objetos verdaderamente caen en un campo gravitatorio curvo.
7. **[Date un Vlog / Javier Santaolalla (YouTube)](https://www.youtube.com/c/DateunVlog)** - Para construir intuición física fundamental sobre por qué la gravedad no es una fuerza, previo a introducir las matemáticas pesadas.

### 📝 Artículos y Simulaciones Interesantes (8-10 Recomendados)
1. **Simulador**: [Black Hole Simulator / Ray Tracing](http://sirxemic.github.io/Interstellar/) - Visualización interactiva del trazado de rayos alrededor de un agujero negro de Schwarzschild y de Kerr.
2. **Simulador**: [Gravity Simulator (Test of Relativity)](https://testofrelativity.com/) - Herramientas para visualizar cómo las masas deforman el espacio en un modelo bidimensional (análogo elástico).
3. **Simulador**: [LIGO Gravitational Wave Observatory](https://www.ligo.org/) - Datos interactivos, audios de los "chirps" y animaciones de la fusión de agujeros negros.
4. **Living Reviews in Relativity**: [Journal](https://link.springer.com/journal/41114) - La revista de mayor impacto con revisiones detalladas y gratuitas de expertos mundiales en diversas áreas de relatividad general.
5. **Wikipedia**: [Ecuaciones del Campo de Einstein](https://es.wikipedia.org/wiki/Ecuaciones_del_campo_de_Einstein) - Desglose detallado componente por componente de la ecuación fundamental.
6. **Wikipedia**: [Métrica de Schwarzschild](https://es.wikipedia.org/wiki/M%C3%A9trica_de_Schwarzschild) - La primera solución exacta a las Ecuaciones de Einstein y la base para estudiar agujeros negros no rotatorios.
7. **Scholarpedia**: [General Relativity](http://www.scholarpedia.org/article/General_relativity) - Enciclopedia curada por expertos sobre los cimientos matemáticos de la teoría.
8. **Artículo Histórico**: [The Foundation of the General Theory of Relativity (1916)](https://einsteinpapers.press.princeton.edu/) - Traducción de la obra maestra fundacional de Albert Einstein.
9. **Quanta Magazine**: [Black Holes & General Relativity](https://www.quantamagazine.org/physics/) - Reportajes actualizados sobre la frontera del conocimiento (paradoja de la información, entrelazamiento y ER=EPR).
10. **Stanford Encyclopedia of Philosophy**: [Hole Argument (El Argumento del Agujero)](https://plato.stanford.edu/entries/spacetime-holearg/) - Un fascinante problema histórico-filosófico con el que luchó Einstein al desarrollar las ecuaciones covariantes.

### 📖 Referencias Útiles y Bibliografía
1. **[Bernard F. Schutz - A First Course in General Relativity](https://www.cambridge.org/highereducation/books/a-first-course-in-general-relativity/94B2E0D6528A32A17EFB738C2ACAEFDE)** - Ampliamente considerado como el mejor libro introductorio para estudiantes de pregrado; muy claro en el desarrollo matemático y cálculo tensorial.
2. **[James B. Hartle - Gravity: An Introduction to Einstein's General Relativity](https://www.pearson.com/en-us/subject-catalog/p/gravity-an-introduction-to-einsteins-general-relativity/P200000004543/9780805386622)** - Adopta un enfoque "physics first", enseñando aplicaciones físicas (agujeros negros, cosmología) utilizando métricas dadas antes de sumergirse en la geometría diferencial pesada.
3. **[Sean M. Carroll - Spacetime and Geometry: An Introduction to General Relativity](https://www.cambridge.org/highereducation/books/spacetime-and-geometry/1F2F2D1F6E20700B025C6BE60037BD62)** - Un excelente texto puente entre el pregrado y el posgrado, moderno, intuitivo y riguroso.
4. **[Robert M. Wald - General Relativity](https://press.uchicago.edu/ucp/books/book/chicago/G/bo5952261.html)** - El estándar de oro para los cursos de posgrado. Altamente matemático, riguroso y abstracto, utilizando la notación moderna libre de índices y formas diferenciales.
5. **[Charles W. Misner, Kip S. Thorne, John Archibald Wheeler - Gravitation (MTW)](https://press.princeton.edu/books/hardcover/9780691177793/gravitation)** - El libro enciclopédico de referencia de 1973 (apodado "la guía telefónica" por su tamaño). Profundo, poético, con abundantes diagramas y un enfoque geométrico inigualable.
