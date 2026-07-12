# Circuitos y Corriente

El estudio de circuitos y corriente eléctrica se ocupa del movimiento macroscópico continuo de cargas eléctricas a través de conductores y componentes pasivos o activos. Es la base tecnológica de toda la electrónica moderna.

## 📜 Contexto Histórico
A finales del siglo XVIII, Luigi Galvani descubrió la "electricidad animal" en patas de rana, lo cual inspiró a Alessandro Volta a inventar en 1800 la primera pila eléctrica (pila voltaica), proporcionando una fuente de corriente continua y estable. En 1827, el físico alemán Georg Simon Ohm publicó su famosa ley que relaciona voltaje y corriente, basándose en analogías con el flujo de calor de Fourier. En 1845, Gustav Kirchhoff generalizó el análisis de topologías de circuitos complejos al deducir sus famosas leyes (Leyes de Kirchhoff) basadas en la conservación de carga y energía. 

---

## 🧮 Desarrollo Teórico Profundo

### Corriente y Densidad de Corriente
La corriente eléctrica $I$ es la tasa de flujo de carga neta que cruza un área transversal en un tiempo $dt$:
$$ I = \frac{dq}{dt} $$
Microscópicamente, se define mediante el vector densidad de corriente $\vec{J}$:
$$ I = \int_S \vec{J} \cdot d\vec{A} $$
donde $\vec{J} = n q \vec{v}_d$, siendo $n$ la densidad de portadores, $q$ la carga de cada portador y $\vec{v}_d$ la velocidad de deriva.

### Ley de Ohm
En muchos materiales, la densidad de corriente es proporcional al campo eléctrico local:
$$ \vec{J} = \sigma \vec{E} $$
donde $\sigma$ es la conductividad. En forma macroscópica para un hilo conductor uniforme de longitud $L$, área $A$ y resistividad $\rho = 1/\sigma$, esto se convierte en la Ley de Ohm:
$$ V = I R $$
con la resistencia definida como $R = \rho \frac{L}{A}$.

### Potencia Eléctrica
La tasa a la que la energía eléctrica es transferida por un circuito es:
$$ P = V I $$
Para una resistencia óhmica, esto resulta en calentamiento por efecto Joule:
$$ P = I^2 R = \frac{V^2}{R} $$

### Leyes de Kirchhoff
Las leyes de Kirchhoff permiten resolver redes eléctricas complejas:
1. **Ley de Nodos (KCL - Conservación de la carga):** La suma algebraica de las corrientes que entran y salen de un nodo es cero:
   $$ \sum_{k} I_k = 0 $$
2. **Ley de Mallas (KVL - Conservación de la energía):** La suma algebraica de las diferencias de potencial en un camino cerrado es cero:
   $$ \sum_{k} \Delta V_k = 0 $$

---

## 🛠 Ejemplo Práctico
**Problema:** Un circuito RC en serie consta de una fuente de voltaje continuo $\mathcal{E}$, una resistencia $R$, y un condensador de capacitancia $C$, inicialmente descargado. El circuito se cierra mediante un interruptor en $t=0$. Encontrar la carga del condensador $q(t)$ como función del tiempo.

**Solución paso a paso:**
1. **Aplicar la Ley de Mallas de Kirchhoff:**
   Al recorrer el circuito, tenemos el aumento de la fuente, la caída en el resistor y la caída en el condensador:
   $$ \mathcal{E} - I R - \frac{q}{C} = 0 $$
2. **Expresar la corriente:** Sabemos que $I = \frac{dq}{dt}$, luego:
   $$ R \frac{dq}{dt} + \frac{q}{C} = \mathcal{E} $$
3. **Resolver la ecuación diferencial:**
   Esta es una ecuación diferencial lineal de primer orden separable:
   $$ \frac{dq}{dt} = \frac{\mathcal{E} C - q}{R C} \implies \frac{dq}{q - \mathcal{E} C} = -\frac{dt}{R C} $$
   Integrando desde $t=0$ (con $q(0)=0$) hasta $t$:
   $$ \ln \left( \frac{q(t) - \mathcal{E} C}{-\mathcal{E} C} \right) = -\frac{t}{R C} $$
4. **Despejar $q(t)$:**
   $$ q(t) - \mathcal{E} C = -\mathcal{E} C e^{-t/(RC)} $$
   $$ q(t) = C \mathcal{E} \left( 1 - e^{-t/\tau} \right) $$
   Donde $\tau = R C$ es la constante de tiempo del circuito. La carga crece asintóticamente hasta el valor máximo $Q_{\max} = C \mathcal{E}$.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. [MIT 6.002 - Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/): Clásico y excelente curso para dominar el análisis de circuitos a nivel universitario y en diseño de ingeniería.
2. [Khan Academy - Ingeniería Eléctrica (Circuitos)](https://es.khanacademy.org/science/electrical-engineering): Explicaciones en video con resolución detallada de análisis nodales, leyes de Kirchhoff, Norton y Thevenin.
3. [Coursera - Linear Circuits 1: DC Analysis](https://www.coursera.org/learn/linear-circuits-d-c-analysis): Enfoque especializado sobre corrientes continuas, fuentes dependientes y simulaciones por parte del Georgia Tech.
4. [edX - Circuits and Electronics 1: Basic Circuit Analysis](https://www.edx.org/course/circuits-and-electronics-1-basic-circuit-analysis): Curso fundamental respaldado por MITx para modelar fenómenos físicos con elementos pasivos y activos.
5. [Feynman Lectures on Physics - Vol II, Ch 22: AC Circuits](https://www.feynmanlectures.caltech.edu/II_22.html): Introducción a la respuesta en frecuencia, impedancias complejas y resonancia de un modo excepcionalmente intuitivo.
6. [NPTEL - Basic Electrical Circuits](https://nptel.ac.in/courses/117106108): Explicaciones formales que cubren teoremas de redes, grafos de circuitos, y respuestas transitorias paso a paso.

### 📝 Artículos e Interactivos Interesantes
1. [PhET - Circuit Construction Kit: DC](https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc): Una herramienta magnífica y muy pedagógica para construir circuitos virtuales y medir con multímetros.
2. [PhET - Circuit Construction Kit: AC](https://phet.colorado.edu/en/simulations/circuit-construction-kit-ac): Ideal para ver cómo se comportan capacitores e inductores frente a estímulos alternos.
3. [Falstad Circuit Simulator](http://www.falstad.com/circuit/): Un emulador de topologías de circuitos en el navegador web altamente avanzado, visual, interactivo y en tiempo real.
4. [Wikipedia: Ley de Ohm](https://es.wikipedia.org/wiki/Ley_de_Ohm): Recorrido detallado de la base conceptual que rige a la conducción eléctrica en materiales.
5. [Wikipedia: Leyes de Kirchhoff](https://es.wikipedia.org/wiki/Leyes_de_Kirchhoff): Detalles formales y métodos sistemáticos de nodos y mallas, fundamentales en el diseño eléctrico.
6. [All About Circuits - Textbook](https://www.allaboutcircuits.com/textbook/): Interfaz moderna con lecciones gratuitas sobre componentes, hojas de datos y aplicaciones analógicas.
7. [Electronics Tutorials - DC Circuits](https://www.electronics-tutorials.ws/dccircuits/dcp_1.html): Artículos, guías y tutoriales bien escritos para aprender a reducir redes y utilizar puentes Wheatstone.
8. [LibreTexts - Electric Current and Circuits](https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/10%3A_Direct-Current_Circuits): Colección enorme y libre de conceptos sobre conducción, resistencia equivalente e instrumentos de medición.

### 📖 Referencias Útiles y Bibliografía
1. [Introduction to Electrodynamics - David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-electrodynamics/971275E590D0DE07E9CD0DB4F2C2FA04): El texto de referencia por excelencia (estándar de oro) para estudiantes de pregrado en física, claro y didáctico.
2. [Classical Electrodynamics - John David Jackson](https://www.wiley.com/en-us/Classical+Electrodynamics%2C+3rd+Edition-p-9780471309321): Obra matemática y avanzada requerida en todos los posgrados y doctorados del mundo físico.
3. [Electricity and Magnetism - Edward M. Purcell & David J. Morin](https://www.cambridge.org/highereducation/books/electricity-and-magnetism/C16C976ADCD2F4A96DD8DD3DDAB303CE): Magnífico abordaje donde el magnetismo emerge naturalmente como consecuencia de la relatividad especial.
4. [Física Universitaria (Vol. 2) - Sears y Zemansky](https://www.pearson.com/store/p/fisica-universitaria-vol-2/P200000000305/9786073244404): Libro fundamental de primer año que incluye un tratamiento fenomenológico completo de los circuitos.
5. [Fundamentos de Circuitos Eléctricos - Sadiku](https://www.mheducation.com/highered/product/fundamentals-electric-circuits-alexander-sadiku/M9781260226409.html): Un referente internacional fundamental que cubre cada teorema importante desde cero con problemas prácticos.
