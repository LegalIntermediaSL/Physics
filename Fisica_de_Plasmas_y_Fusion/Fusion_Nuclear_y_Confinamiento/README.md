# Fusión Nuclear y Confinamiento

La fusión nuclear es el proceso mediante el cual dos núcleos atómicos ligeros se combinan para formar uno más pesado, liberando inmensas cantidades de energía. Replicar este proceso de forma controlada requiere confinar plasmas a condiciones extremas.

## 📜 Contexto Histórico

La teoría de que el sol brilla debido a la fusión nuclear fue propuesta por Arthur Eddington en los años 20 y detallada por Hans Bethe en 1939. En 1950, los científicos soviéticos Andrei Sakharov e Igor Tamm propusieron el diseño del "Tokamak" (cámara toroidal con bobinas magnéticas), que sigue siendo el enfoque líder para la fusión magnética en proyectos como ITER (International Thermonuclear Experimental Reactor).

## 🧮 Desarrollo Teórico Profundo

El desafío de la fusión termonuclear controlada reside en reproducir las condiciones estelares en un entorno de laboratorio. La reacción más accesible debido a su sección eficaz máxima a temperaturas "moderadas" es la de Deuterio y Tritio:

$$ ^2_1\text{D} + ^3_1\text{T} \rightarrow ^4_2\text{He} (3.52 \, \text{MeV}) + ^1_0\text{n} (14.06 \, \text{MeV}) $$

La energía total liberada es $Q = 17.58 \, \text{MeV}$. Los neutrones escapan del confinamiento magnético para depositar su energía cinética en el manto reproductor, mientras que las partículas alfa ($^4_2\text{He}$) quedan confinadas y calientan el plasma.

### 1. Balance de Energía y el Criterio de Lawson

Consideremos un volumen unitario de plasma D-T. La tasa de reacciones de fusión por unidad de volumen está dada por:

$$ R_{DT} = n_D n_T \langle \sigma v \rangle $$

donde $\langle \sigma v \rangle$ es el promedio Maxwelliano de la sección eficaz $\sigma(v)$ por la velocidad relativa $v$. Si asumimos una mezcla óptima 50:50, $n_D = n_T = n/2$, por lo que $R_{DT} = \frac{1}{4} n^2 \langle \sigma v \rangle$.

La potencia de calentamiento alfa $P_\alpha$ (potencia depositada intrínsecamente en el plasma) es:

$$ P_\alpha = \frac{1}{4} n^2 \langle \sigma v \rangle E_\alpha $$

donde $E_\alpha = 3.52 \, \text{MeV}$.

Las pérdidas de energía en el plasma se deben fundamentalmente a dos mecanismos: transporte (fuga térmica y de partículas) y radiación térmica (Bremsstrahlung).
La densidad de energía térmica del plasma es $W = 3 n k_B T$ (considerando electrones e iones a la misma temperatura $T$).
Definimos el **tiempo de confinamiento de energía**, $\tau_E$, mediante la tasa de pérdida de energía por transporte $P_{trans} = W / \tau_E$.
La pérdida por radiación Bremsstrahlung es $P_{br} = C_B n^2 \sqrt{T}$.

La ecuación de balance de energía del plasma en estado estacionario, con un aporte de potencia externa $P_{ext}$, es:

$$ P_{ext} + P_\alpha = P_{trans} + P_{br} $$

$$ P_{ext} + \frac{1}{4} n^2 \langle \sigma v \rangle E_\alpha = \frac{3 n k_B T}{\tau_E} + C_B n^2 \sqrt{T} $$

#### La Condición de Ignición
El objetivo último de un reactor comercial es la **ignición**, donde el calentamiento alfa es suficiente para sostener la temperatura contra las pérdidas, permitiendo apagar el calentamiento externo ($P_{ext} = 0$).

$$ \frac{1}{4} n^2 \langle \sigma v \rangle E_\alpha \geq \frac{3 n k_B T}{\tau_E} + C_B n^2 \sqrt{T} $$

Despejando el producto $n \tau_E$:

$$ n \tau_E \geq \frac{12 k_B T}{\langle \sigma v \rangle E_\alpha - 4 C_B \sqrt{T}} $$

Esta es la forma rigurosa del **Criterio de Lawson**. En el régimen de temperaturas óptimas de operación (alrededor de $T \approx 15 \, \text{keV}$), el Bremsstrahlung es pequeño comparado con el transporte, lo que permite simplificar la expresión a la condición de **Producto Triple**:

$$ n T \tau_E \geq \frac{12 k_B T^2}{E_\alpha \langle \sigma v \rangle} $$

Dado que el término $\langle \sigma v \rangle / T^2$ alcanza un máximo cerca de los $15 \, \text{keV}$, el valor mínimo requerido para el producto triple es aproximadamente:

$$ n T \tau_E \approx 3 \times 10^{21} \, \text{m}^{-3} \cdot \text{keV} \cdot \text{s} $$

### 2. Ganancia de Fusión ($Q$)

Se define el factor de ganancia de energía de fusión $Q$ como la relación entre la potencia total de fusión generada ($P_{fus} = P_\alpha + P_{neutrones} = 5 P_\alpha$) y la potencia externa suministrada para calentar el plasma:

$$ Q = \frac{P_{fus}}{P_{ext}} = \frac{5 P_\alpha}{P_{ext}} $$

Utilizando la ecuación de balance $P_{ext} = P_{trans} + P_{br} - P_\alpha$:

$$ Q = \frac{5 P_\alpha}{P_{trans} + P_{br} - P_\alpha} $$

Se distinguen dos hitos históricos:
- **Break-even Científico ($Q=1$):** La potencia de fusión iguala al calentamiento externo. Sin embargo, el reactor aún pierde energía porque los neutrones se escapan.
- **Ignición ($Q = \infty$):** $P_{ext} = 0$. Todo el calentamiento es proporcionado por las partículas alfa ($P_\alpha = P_{trans} + P_{br}$).

### Diagrama: Cadena de Fusión y Balance Térmico

```mermaid
graph TD
    A[Potencia Externa P_ext<br>RF, NBI] -->|Calentamiento| B(Plasma D-T en Equilibrio Térmico)
    C[Calentamiento Alfa P_&alpha;] -->|Autocalentamiento| B
    B -->|Reacciones Termonucleares| D{Fusión}
    D -->|3.5 MeV (20%)| C
    D -->|14.1 MeV (80%)| E[Potencia de Neutrones P_n]
    B -->|Difusión/Transporte| F[Pérdidas de Calor W / &tau;_E]
    B -->|Radiación (Bremsstrahlung)| G[Pérdidas Radiativas P_br]
    
    style B fill:#d90429,stroke:#fff,color:#fff
    style D fill:#fb8500,stroke:#fff,color:#fff
    style E fill:#023047,stroke:#fff,color:#fff
```

## 🛠 Ejemplo Práctico

**Problema:** Un diseño de reactor Tokamak D-T tiene como objetivo la ignición ($Q=\infty$). Planea operar a una temperatura óptima de $T = 15 \, \text{keV}$. Sabiendo que el límite de densidad de Greenwald dicta una densidad máxima operativa de $n = 10^{20} \, \text{m}^{-3}$, determine el tiempo de confinamiento de energía $\tau_E$ necesario para la ignición. Además, si el tiempo de confinamiento real predicho por la escala empírica de ITER (IPB98) resulta ser $\tau_{E, real} = 1.8 \, \text{s}$, calcule el factor $Q$ que alcanzará el reactor asumiendo que el Bremsstrahlung es despreciable respecto al transporte.

**Solución paso a paso:**

1. **Tiempo de confinamiento para ignición ($\tau_{E, ign}$):**
   Utilizando la condición del Producto Triple de Lawson para ignición:
   $$ n T \tau_{E, ign} \approx 3 \times 10^{21} \, \text{m}^{-3} \cdot \text{keV} \cdot \text{s} $$
   Despejando $\tau_{E, ign}$:
   $$ \tau_{E, ign} = \frac{3 \times 10^{21}}{n T} $$
   $$ \tau_{E, ign} = \frac{3 \times 10^{21}}{(10^{20}) (15)} = \frac{3 \times 10^{21}}{1.5 \times 10^{21}} = 2.0 \, \text{s} $$
   Para lograr la ignición autónoma, el calor debe retenerse en promedio durante 2.0 segundos.

2. **Cálculo del Factor $Q$ con el tiempo real:**
   Dado $\tau_{E, real} = 1.8 \, \text{s} < 2.0 \, \text{s}$, el reactor no alcanza la ignición ($Q < \infty$). Necesitará calentamiento externo $P_{ext}$ constante.
   Sabemos que:
   $$ Q = \frac{5 P_\alpha}{P_{trans} - P_\alpha} $$  (despreciando Bremsstrahlung)
   
   Dividimos numerador y denominador por $P_{trans}$:
   $$ Q = \frac{5 (P_\alpha / P_{trans})}{1 - (P_\alpha / P_{trans})} $$
   
   La relación $(P_\alpha / P_{trans})$ depende linealmente del tiempo de confinamiento si $n$ y $T$ son constantes. Como sabemos que a $\tau_E = 2.0 \, \text{s}$ la potencia alfa iguala exactamente a la potencia perdida por transporte (ignición, $P_\alpha = P_{trans}$), entonces:
   $$ \frac{P_\alpha}{P_{trans}} = \frac{\tau_{E, real}}{\tau_{E, ign}} = \frac{1.8}{2.0} = 0.9 $$
   
   Es decir, las partículas alfa proveen el 90% del calentamiento necesario, y el $P_{ext}$ debe aportar el 10% restante.

3. **Obtención del valor final de $Q$:**
   $$ Q = \frac{5 (0.9)}{1 - 0.9} = \frac{4.5}{0.1} = 45 $$

**Conclusión:** El reactor no se autosostendrá completamente, pero generará 45 veces más energía térmica de fusión que la energía inyectada para mantener el plasma caliente. Este es un reactor de muy alto rendimiento, muy superior al break-even ($Q=1$), y comparable al objetivo de diseño base de ITER ($Q \ge 10$).

## 📚 Recursos Específicos

### Cursos Específicos
1. [Nuclear Energy - MIT OpenCourseWare](https://ocw.mit.edu)
2. [Introduction to Fusion Energy - TU/e (Coursera)](https://www.coursera.org)
3. [Fusion Materials - NPTEL](https://nptel.ac.in)
4. [ITER E-Learning Courses](https://www.iter.org/)
5. [Inertial Confinement Fusion - LLNL Short Courses](https://lasers.llnl.gov)
6. [Thermonuclear Reactor Design - Tokyo Institute of Technology](https://www.titech.ac.jp)

### Artículos y Simulaciones
1. [Lawson, J. D. (1957). *Some Criteria for a Power Producing Thermonuclear Reactor*. Proc. Phys. Soc.](https://doi.org/10.1088/0370-1301/70/1/303)
2. [Nuckolls, J., Wood, L., Thiessen, A., & Zimmerman, G. (1972). *Laser Compression of Matter to Super-High Densities*. Nature.](https://www.nature.com/articles/239139a0)
3. [Hurricane, O. A., et al. (2014). *Fuel gain exceeding unity in an inertially confined fusion implosion*. Nature.](https://www.nature.com/articles/nature13008)
4. [Rebut, P. H. (1995). *ITER: The first experimental fusion reactor*. Fusion Engineering and Design.](https://doi.org/10.1016/0920-3796(95)90103-5)
5. [Abu-Shumays, I. K., et al. (1999). *Simulations for ICF Experiments*.](https://doi.org/10.1109/99.757313)
6. [ITER - The Way to New Energy (Sitio oficial)](https://www.iter.org/)
7. [National Ignition Facility (NIF) - Confinamiento Inercial](https://lasers.llnl.gov/)
8. [HELIOS](https://www.prism-cs.com/Software/Helios/Helios.html) - 1D Radiation Magnetohydrodynamics Code for ICF.
9. [FLASH](https://flash.rochester.edu/) - Multiphysics code for laser fusion.

### 📖 Referencias Útiles y Bibliografía
1. [Atzeni, S., & Meyer-ter-Vehn, J. (2004). *The Physics of Inertial Fusion*. Oxford University Press.](https://global.oup.com/academic/product/the-physics-of-inertial-fusion-9780198562641)
2. [Wesson, J. (2011). *Tokamaks* (Vol. 149). Oxford University Press.](https://global.oup.com/academic/product/tokamaks-9780199592234)
3. [McCracken, G., & Stott, P. (2012). *Fusion: The Energy of the Universe*. Academic Press.](https://www.sciencedirect.com/book/9780123846563/fusion)
4. [Stacey, W. M. (2010). *Fusion Plasma Physics*. Wiley-VCH.](https://www.wiley.com/en-us/Fusion+Plasma+Physics%2C+2nd+Edition-p-9783527409679)
