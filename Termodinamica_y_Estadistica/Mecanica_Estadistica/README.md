# Mecánica Estadística

La mecánica estadística es la formulación matemática que deduce todas las leyes de la termodinámica clásica partiendo del estudio probabilístico de los incontables microestados (configuraciones atómicas o cuánticas) compatibles con un macroestado dado (como energía, volumen y temperatura fijas).

## 📜 Contexto Histórico
A finales del siglo XIX, Ludwig Boltzmann y Josiah Willard Gibbs sentaron las bases fundacionales de esta disciplina. Boltzmann propuso que la entropía es una medida del número de microestados disponibles (expresado en su famosa lápida $S = k \log W$). Gibbs, por su parte, desarrolló la noción de los "colectivos" o "ensembles" (microcanónico, canónico, macrocanónico). Con el advenimiento de la mecánica cuántica, Albert Einstein, Satyendra Nath Bose, Enrico Fermi y Paul Dirac ampliaron la teoría a los bosones y fermiones en la década de 1920, lo que permitió explicar fenómenos que escapaban a la física clásica (como el cuerpo negro, la conducción en metales y la superfluidez).

---

## 🧮 Desarrollo Teórico Profundo

### Colectivo Microcanónico (Sistema Aislado)
Describe un sistema aislado con número de partículas $N$, volumen $V$, y energía total $E$ fijos. El postulado fundamental afirma que todos los microestados accesibles $\Omega(N,V,E)$ son igualmente probables.
La entropía $S$ se define como:
$$ S = k_B \ln \Omega $$

### Colectivo Canónico (Sistema en Contacto Térmico)
Describe un sistema con $N$ y $V$ fijos, pero que puede intercambiar energía con un baño térmico inmenso a temperatura constante $T$. La probabilidad de encontrar al sistema en un microestado $r$ con energía $E_r$ está dada por la distribución de Boltzmann:
$$ P_r = \frac{e^{-\beta E_r}}{Z} $$
donde $\beta = \frac{1}{k_B T}$ y $Z$ es la **función de partición canónica**:
$$ Z(N,V,T) = \sum_r e^{-\beta E_r} $$
A partir de $Z$ se deducen todas las variables termodinámicas. Por ejemplo, la Energía Libre de Helmholtz $F$ es:
$$ F = -k_B T \ln Z $$
Y la energía interna media $U$:
$$ U = \langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} $$

### Estadísticas Cuánticas
A bajas temperaturas o altas densidades, la naturaleza indistinguible de las partículas cuánticas es crucial.
* **Estadística de Bose-Einstein (Bosones):** Partículas de espín entero, sin restricción de ocupación. El número de ocupación medio por estado de energía $\epsilon_i$ es:
  $$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$
* **Estadística de Fermi-Dirac (Fermiones):** Partículas de espín semientero (e.g., electrones), sujetas al principio de exclusión de Pauli (a lo sumo 1 partícula por estado):
  $$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} + 1} $$
donde $\mu$ es el potencial químico.

---

## 🛠 Ejemplo Práctico
**Problema:** Calcular la energía interna promedio y la capacidad calorífica de un paramagneto de espín $1/2$ que consta de $N$ átomos fijos y no interactuantes, en presencia de un campo magnético externo $B$, a temperatura $T$.

**Solución paso a paso:**
1. **Identificar los microestados de un átomo:**
   Cada espín puede apuntar "arriba" (energía $\epsilon_{\uparrow} = -\mu_B B$) o "abajo" (energía $\epsilon_{\downarrow} = +\mu_B B$), donde $\mu_B$ es el magnetón de Bohr.
2. **Calcular la función de partición de una sola partícula ($z$):**
   $$ z = e^{-\beta(-\mu_B B)} + e^{-\beta(+\mu_B B)} = e^{\beta \mu_B B} + e^{-\beta \mu_B B} = 2 \cosh(\beta \mu_B B) $$
3. **Calcular la función de partición total ($Z$):**
   Como las partículas son distinguibles por estar fijas en la red cristalina:
   $$ Z = z^N = \left[ 2 \cosh(\beta \mu_B B) \right]^N $$
4. **Calcular la energía interna ($U$):**
   $$ U = -\frac{\partial \ln Z}{\partial \beta} = -N \frac{\partial}{\partial \beta} \ln[2 \cosh(\beta \mu_B B)] $$
   $$ U = -N \frac{2 \mu_B B \sinh(\beta \mu_B B)}{2 \cosh(\beta \mu_B B)} = -N \mu_B B \tanh(\beta \mu_B B) $$
5. **Calcular la capacidad calorífica ($C$):**
   $$ C = \frac{\partial U}{\partial T} = \frac{\partial U}{\partial \beta} \frac{\partial \beta}{\partial T} $$
   Como $\frac{\partial \beta}{\partial T} = -\frac{1}{k_B T^2}$:
   $$ C = N k_B (\beta \mu_B B)^2 \operatorname{sech}^2(\beta \mu_B B) $$
   Este resultado demuestra de forma teórica la "anomalía de Schottky", un pico en la capacidad calorífica a bajas temperaturas típico de sistemas de dos niveles.

---

## 📚 Recursos Específicos

### 🎓 Cursos y Clases Recomendadas
1. **Stanford - Statistical Mechanics (Leonard Susskind):** [Enlace al Curso](https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring) - Esencial, se adentra directamente en la lógica matemática subyacente y la física de la información.
2. **MIT 8.044 (Statistical Physics I):** [Página en MIT OCW](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/) - Excelente enfoque formal desde sistemas discretos a gases cuánticos.
3. **Perimeter Institute - Statistical Physics:** [PIPSI Lectures](https://pirsa.org/) - Clases de maestría con nivel avanzado, ideal para física de materia condensada.
4. **Oxford - Statistical Mechanics Lectures:** [Enlace a YouTube](https://www.youtube.com/playlist?list=PL4d5Ztf9HeEkOqE6Rndn5d3xU-X2CqJj4) - Serie de clases muy claras enfocadas en los diferentes ensambles de Gibbs.
5. **NPTEL - Statistical Mechanics:** [Curso NPTEL](https://nptel.ac.in/courses/115/103/115103113/) - Curso intensivo y muy matemático para entender derivaciones canónicas y gran canónicas.

### 📝 Artículos e Interactivos Interesantes
1. **Simulación Ising Model:** [Ising Model Simulation](https://mattbierbaum.github.io/ising.js/) - Visualizar el ferromagnetismo y las transiciones de fase críticas desde un ensamble de espines en interacción.
2. **Catástrofe Ultravioleta e Historia de Planck:** [Ultraviolet Catastrophe](https://en.wikipedia.org/wiki/Ultraviolet_catastrophe) - Leer sobre cómo el conteo estadístico de fotones inició la revolución cuántica.
3. **Bose-Einstein Condensation (PhET / Videos):** [PhET BEC](https://phet.colorado.edu/es/simulation/legacy/states-of-matter) - Animaciones y artículos detallando el fenómeno macroscópico que ocurre cuando la ocupación cuántica diverge hacia el estado fundamental.
4. **Scholarpedia - Gibbs Ensembles:** [Statistical Ensembles](http://www.scholarpedia.org/article/Ensemble_(physics)) - Artículo avanzado sobre los fundamentos de los colectivos microcanónico, canónico y gran canónico.
5. **Wikipedia - Función de partición:** [Partition Function](https://es.wikipedia.org/wiki/Funci%C3%B3n_de_partici%C3%B3n_(mec%C3%A1nica_estad%C3%ADstica)) - Explicación detallada de cómo calcular variables termodinámicas a partir de $Z$.
6. **HyperPhysics - Quantum Statistics:** [Estadísticas Cuánticas](http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/quastat.html) - Resumen de las diferencias entre las estadísticas de Maxwell-Boltzmann, Fermi-Dirac y Bose-Einstein.
7. **Stanford Encyclopedia of Philosophy:** [Philosophy of StatMech](https://plato.stanford.edu/entries/statphys-statmech/) - Filosofía de la mecánica estadística, abordando la irreversibilidad y las probabilidades.
8. **Wolfram Demonstrations - Maxwell-Boltzmann Distribution:** [Simulación](https://demonstrations.wolfram.com/MaxwellBoltzmannDistribution/) - Visualización interactiva de la distribución energética.

### 📖 Referencias Útiles y Bibliografía
* [Statistical Mechanics - Pathria, R. K.](https://www.elsevier.com/books/statistical-mechanics/pathria/978-0-12-382188-1) - Texto clásico y riguroso de nivel posgrado, excelente para el desarrollo teórico profundo de los ensambles.
* [Fundamentals of Statistical and Thermal Physics - Reif, F.](https://books.google.com/books?id=0sM4DgAAQBAJ) - Fundamental para el entendimiento detallado de la conexión micro-macro.
* [Thermal Physics - Kittel, C. & Kroemer, H.](https://www.macmillanlearning.com/college/us/product/Thermal-Physics/p/0716710889) - Un libro moderno con un enfoque estadístico desde la primera página, muy claro en conceptos cuánticos.
* [Statistical Physics, Part 1 - Landau, L. D. & Lifshitz, E. M.](https://www.elsevier.com/books/statistical-physics/landau/978-0-08-023039-9) - Parte de la legendaria serie, brillante e indispensable para los teóricos rigurosos.
* [The Principles of Statistical Mechanics - Tolman, R. C.](https://store.doverpublications.com/products/9780486638966) - Una referencia histórica inigualable sobre los fundamentos conceptuales de la teoría clásica y cuántica.
