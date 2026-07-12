# Circuitos y Corriente

El estudio de circuitos y corriente eléctrica se ocupa del movimiento macroscópico continuo de cargas eléctricas a través de conductores y componentes pasivos o activos. Es la base tecnológica de toda la electrónica moderna.

## 📜 Contexto Histórico
A finales del siglo XVIII, Luigi Galvani descubrió la "electricidad animal" en patas de rana, lo cual inspiró a Alessandro Volta a inventar en 1800 la primera pila eléctrica (pila voltaica), proporcionando una fuente de corriente continua y estable. En 1827, el físico alemán Georg Simon Ohm publicó su famosa ley que relaciona voltaje y corriente, basándose en analogías con el flujo de calor de Fourier. En 1845, Gustav Kirchhoff generalizó el análisis de topologías de circuitos complejos al deducir sus famosas leyes (Leyes de Kirchhoff) basadas en la conservación de carga y energía. 

---

## 🧮 Desarrollo Teórico Profundo

El estudio analítico de los circuitos eléctricos requiere una inmersión profunda en la teoría de transporte de carga y la conservación de la energía en medios materiales. A diferencia del vacío, los medios conductores están repletos de portadores de carga que interactúan térmicamente con la red cristalina.

### 1. Ecuación de Continuidad y Conservación de la Carga
La piedra angular de toda la teoría de circuitos es la conservación de la carga eléctrica, expresada localmente mediante la ecuación de continuidad. Consideremos un volumen arbitrario $V$ delimitado por una superficie cerrada $S$. La tasa de disminución de la carga neta $Q$ en este volumen debe ser exactamente igual al flujo de carga que atraviesa $S$:
$$ \oint_S \vec{J} \cdot d\vec{A} = -\frac{d}{dt} \int_V \rho_e \, dV $$
Aplicando el Teorema de la Divergencia de Gauss al lado izquierdo:
$$ \int_V (\nabla \cdot \vec{J}) \, dV = \int_V \left( -\frac{\partial \rho_e}{\partial t} \right) \, dV $$
Dado que esto se cumple para cualquier volumen $V$, obtenemos la **Ecuación de Continuidad Diferencial**:
$$ \nabla \cdot \vec{J} + \frac{\partial \rho_e}{\partial t} = 0 $$
En condiciones estacionarias (corriente continua, DC), la densidad de carga no varía con el tiempo ($\partial \rho_e / \partial t = 0$), lo que implica que el campo vectorial de la densidad de corriente es solenoidal:
$$ \nabla \cdot \vec{J} = 0 $$

### 2. Modelo de Drude para la Conducción Eléctrica
El flujo de corriente macroscópico está intrínsecamente ligado al movimiento microscópico de los electrones. El modelo clásico de Drude asume un "gas de electrones" libres que sufren colisiones inelásticas con la red de iones positivos. 

La ecuación de movimiento para un electrón promedio, sometido a un campo eléctrico externo $\vec{E}$ y sujeto a una fuerza de fricción visco-elástica debida a colisiones (caracterizada por un tiempo medio entre colisiones $\tau$), es:
$$ m_e \frac{d\vec{v}_d}{dt} = -e\vec{E} - \frac{m_e \vec{v}_d}{\tau} $$
En régimen estacionario ($d\vec{v}_d/dt = 0$), la velocidad de deriva $\vec{v}_d$ alcanza un valor terminal:
$$ \vec{v}_d = -\frac{e \tau}{m_e} \vec{E} $$
La densidad de corriente está dada por $\vec{J} = -n e \vec{v}_d$, donde $n$ es la densidad numérica de electrones de conducción. Sustituyendo $\vec{v}_d$:
$$ \vec{J} = \left( \frac{n e^2 \tau}{m_e} \right) \vec{E} $$
Definimos la **conductividad eléctrica** $\sigma$ como:
$$ \sigma = \frac{n e^2 \tau}{m_e} $$
Lo cual nos lleva a la forma microscópica de la Ley de Ohm:
$$ \vec{J} = \sigma \vec{E} $$

### 3. Condiciones de Contorno en Conductores
Para resolver problemas complejos de circuitos distribuidos, debemos aplicar condiciones de contorno en las interfaces entre dos materiales de conductividades $\sigma_1$ y $\sigma_2$. 

Asumiendo que no hay acumulación de carga interfacial constante en el tiempo en estado estacionario, la componente normal de $\vec{J}$ debe ser continua:
$$ J_{1n} = J_{2n} \implies \sigma_1 E_{1n} = \sigma_2 E_{2n} $$
Dado que el campo eléctrico conservativo cumple $\oint \vec{E} \cdot d\vec{l} = 0$, la componente tangencial de $\vec{E}$ también es continua:
$$ E_{1t} = E_{2t} \implies \frac{J_{1t}}{\sigma_1} = \frac{J_{2t}}{\sigma_2} $$
Estas condiciones determinan cómo las líneas de corriente se refractan al pasar de un material a otro, un fenómeno análogo a la refracción óptica, siguiendo la ley:
$$ \frac{\tan \theta_1}{\tan \theta_2} = \frac{\sigma_1}{\sigma_2} $$

### 4. Derivación Macroscópica de Resistencia y Capacidad
Considere un material conductor acotado con terminales en potenciales $V_1$ y $V_2$. La diferencia de potencial y la corriente total están dadas por:
$$ V = V_1 - V_2 = \int_1^2 \vec{E} \cdot d\vec{l} $$
$$ I = \int_S \vec{J} \cdot d\vec{A} = \int_S (\sigma \vec{E}) \cdot d\vec{A} $$
La resistencia $R$ queda definida rigurosamente como el cociente integral:
$$ R = \frac{\int_1^2 \vec{E} \cdot d\vec{l}}{\oint_S \sigma \vec{E} \cdot d\vec{A}} $$
Existe una profunda dualidad entre conductancia ($G = 1/R$) y capacitancia ($C$). Dado que para un dieléctrico de permitividad $\varepsilon$, la carga es $Q = \oint \varepsilon \vec{E} \cdot d\vec{A}$, obtenemos la relación fundamental para la misma geometría:
$$ R C = \frac{\varepsilon}{\sigma} $$

### 5. Teoremas de Redes y Topología de Circuitos
Para redes con elementos discretos (Lumped Element Model), las leyes de conservación se reducen a grafos topológicos, originando las Leyes de Kirchhoff y múltiples teoremas de simplificación.

#### A. Formalismo de Grafos de Nodos
Sea una red con $N$ nodos y $B$ ramas. Se define la matriz de incidencia reducida $\mathbf{A}$ de tamaño $(N-1) \times B$. La Ley de Corrientes de Kirchhoff (KCL) se expresa matricialmente:
$$ \mathbf{A} \mathbf{i} = \mathbf{0} $$
donde $\mathbf{i}$ es el vector columna de corrientes de rama. La relación entre voltajes de nodo $\mathbf{v}_n$ y voltajes de rama $\mathbf{v}_b$ es:
$$ \mathbf{v}_b = \mathbf{A}^T \mathbf{v}_n $$

#### B. Teorema de Tellegen
El Teorema de Tellegen es una consecuencia puramente topológica que garantiza la conservación de la potencia en cualquier circuito que obedezca KCL y KVL, independientemente de la naturaleza lineal o no lineal de los componentes:
$$ \sum_{k=1}^B v_k i_k = \mathbf{v}_b^T \mathbf{i} = (\mathbf{A}^T \mathbf{v}_n)^T \mathbf{i} = \mathbf{v}_n^T (\mathbf{A} \mathbf{i}) = 0 $$
Esto afirma que la suma de todas las potencias absorbidas o entregadas por cada elemento de una red cerrada siempre es exactamente cero.

```mermaid
graph TD
    A[Ecuaciones de Maxwell] --> B(Ecuación de Continuidad)
    B --> C[Modelo Estacionario dP/dt = 0]
    C --> D[Ley de Nodos - KCL]
    A --> E(Fuerza electromotriz y campos conservativos)
    E --> F[Aproximación de Elementos Discretos]
    F --> G[Ley de Mallas - KVL]
    D --> H((Análisis Nodal/Mallas))
    G --> H
    H --> I[Teorema de Tellegen]
    H --> J[Teoremas de Thevenin/Norton]
```

### 6. Trabajo y Termodinámica del Efecto Joule
El trabajo realizado por el campo eléctrico sobre un portador de carga $q$ que se mueve una distancia $d\vec{l}$ es $dW = q\vec{E} \cdot d\vec{l}$. La potencia volumétrica disipada $p$ (potencia por unidad de volumen) se obtiene sumando sobre todos los portadores:
$$ p = \frac{1}{dt \, dV} \sum q \vec{E} \cdot d\vec{l} = \vec{E} \cdot \left( \sum \frac{q \vec{v}_d}{dV} \right) = \vec{E} \cdot \vec{J} $$
Aplicando la Ley de Ohm local $\vec{J} = \sigma \vec{E}$:
$$ p = \sigma |\vec{E}|^2 = \frac{|\vec{J}|^2}{\sigma} $$
Esta energía se transfiere a los iones de la red cristalina a través de las colisiones descritas en el Modelo de Drude, incrementando la energía cinética vibracional de la red, lo que macroscópicamente se manifiesta como un aumento de temperatura (Efecto Joule).

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
