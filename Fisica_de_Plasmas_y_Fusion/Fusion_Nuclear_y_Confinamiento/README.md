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

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Tasa de Reacción y Energía de Ignición
Calcule la densidad de potencia de fusión (en $\text{MW/m}^3$) de un plasma equimolar Deuterio-Tritio con densidad total $n_e = 10^{20} \, \text{m}^{-3}$ y una reactividad $\langle \sigma v \rangle = 1.1 \times 10^{-22} \, \text{m}^3/\text{s}$ (típica para $T = 10 \, \text{keV}$). ¿Cuál es el requerimiento de tiempo de confinamiento para alcanzar el break-even ideal ($Q=1$) si sólo consideramos pérdidas por transporte?

**Solución paso a paso:**
1. **Densidad de Potencia de Fusión:**
Para una mezcla 50:50 de D-T, las densidades de combustible son $n_D = n_T = n_e / 2 = 0.5 \times 10^{20} \, \text{m}^{-3}$.
La tasa volumétrica de reacciones es:
$$ R_{DT} = n_D n_T \langle \sigma v \rangle = (0.5 \times 10^{20})^2 (1.1 \times 10^{-22}) = 2.75 \times 10^{17} \, \text{reacciones/m}^3\cdot\text{s} $$
La energía liberada por cada reacción es $E_{fus} = 17.6 \, \text{MeV} = 2.82 \times 10^{-12} \, \text{J}$.
Densidad de potencia total de fusión:
$$ P_{fus} = R_{DT} E_{fus} = (2.75 \times 10^{17}) (2.82 \times 10^{-12}) = 7.75 \times 10^5 \, \text{W/m}^3 = 0.775 \, \text{MW/m}^3 $$

2. **Requerimiento para Break-Even ($Q=1$):**
En el break-even, la potencia de fusión total generada iguala a las pérdidas de potencia (ignorando Bremsstrahlung y asumiendo $T_e = T_i = 10 \, \text{keV}$):
$$ P_{fus} = \frac{3 n k_B T}{\tau_E} $$
Despejamos $\tau_E$:
$$ \tau_E = \frac{3 n k_B T}{P_{fus}} = \frac{3 (10^{20}) (10 \times 10^3 \text{ eV}) (1.6 \times 10^{-19} \text{ J/eV})}{7.75 \times 10^5 \text{ W/m}^3} $$
$$ \tau_E = \frac{4.8 \times 10^5}{7.75 \times 10^5} \approx 0.62 \, \text{s} $$
Para que el reactor rompa el empate energético bajo estas condiciones ideales, la energía debe mantenerse por al menos $0.62$ segundos.

### Problema 2: Compresión Inercial (Confinamiento Inercial)
En fusión por confinamiento inercial (ICF), un pulso láser comprime esféricamente una cápsula de D-T sólido. Si la cápsula inicial tiene radio $r_0 = 1 \, \text{mm}$ y la densidad inicial es de $0.2 \, \text{g/cm}^3$, determine la densidad final y la masa volumétrica requerida si se quiere alcanzar un $\rho R = 3 \, \text{g/cm}^2$ para asegurar la quema eficiente del combustible.

**Solución paso a paso:**
La condición de ignición inercial requiere que la fracción de quemado sea alta, típicamente requiriendo el parámetro areal $\rho R \ge 3 \, \text{g/cm}^2$.
1. Conservación de masa:
La masa de la cápsula esférica de combustible es constante durante la implosión.
$$ M = \frac{4}{3} \pi r_0^3 \rho_0 = \frac{4}{3} \pi R^3 \rho $$
De aquí, el radio comprimido es $R = r_0 \left( \frac{\rho_0}{\rho} \right)^{1/3}$.

2. Reemplazo en el criterio de densidad areal:
$$ \rho R = \rho \left( r_0 \left( \frac{\rho_0}{\rho} \right)^{1/3} \right) = r_0 \rho_0^{1/3} \rho^{2/3} = 3 \, \text{g/cm}^2 $$

3. Despeje de la densidad comprimida requerida $\rho$:
$$ \rho^{2/3} = \frac{\rho R}{r_0 \rho_0^{1/3}} $$
En unidades CGS: $r_0 = 0.1 \, \text{cm}$, $\rho_0 = 0.2 \, \text{g/cm}^3$.
$$ \rho^{2/3} = \frac{3}{(0.1) (0.2)^{1/3}} = \frac{3}{(0.1) (0.585)} = \frac{3}{0.0585} = 51.3 $$
$$ \rho = (51.3)^{3/2} \approx 367 \, \text{g/cm}^3 $$

**Conclusión:** El plasma inercial debe ser comprimido a una densidad más de 1000 veces mayor que la sólida para frenar intrínsecamente las partículas alfa generadas y lograr la retroalimentación térmica estallante.

### Problema 3: Factor de Reproducción de Tritio (TBR) en la Envoltura
El tritio no existe de forma natural; debe ser reproducido (bred) en el "blanket" del reactor bombardeando Litio con los neutrones de la reacción D-T. Si el núcleo del reactor genera $N_0$ reacciones D-T, se liberan $N_0$ neutrones. Suponga que la probabilidad de que un neutrón produzca Tritio es $1.15$ debido a multiplicadores neutrónicos como Berilio. Sin embargo, hay una eficiencia de extracción del $90\%$ y el sistema se detiene el $5\%$ del tiempo por mantenimiento. ¿Cuál es la Tasa Efectiva de Reproducción (TBR efectivo)?

**Solución paso a paso:**
1. TBR Ideal:
El sistema generará teóricamente $N_{bred} = 1.15 N_0$ átomos de Tritio en el interior del manto. El TBR ideal es de $1.15$.

2. Pérdidas de Sistema:
La eficiencia de recolección, confinamiento y purificación en la planta de tritio es $\eta_{ext} = 0.90$.
Además, el decaimiento radiactivo del Tritio (vida media $\approx 12.3$ años) y las interrupciones imponen la disponibilidad del reactor. Si está desconectado $f_{down} = 0.05$, operará el $95\%$ del tiempo. (Para simplificar, tomamos directamente el factor de disponibilidad como penalización de tiempo de reacción, aunque rigurosamente afecta a la acumulación global).
Tritio recuperado neto y disponible como combustible:
$$ TBR_{net} = TBR_{ideal} \times \eta_{ext} \times (1 - f_{down}) $$
$$ TBR_{net} = 1.15 \times 0.90 \times 0.95 = 0.983 $$

**Conclusión:** Como el $TBR_{net} < 1.0$, el reactor consumirá más tritio del que logra reemplazar en el ciclo. Se necesita mejorar los multiplicadores neutrónicos o minimizar las pérdidas de recolección química en el manto para que el reactor sea autosostenible en combustible.

## 💻 Simulaciones Computacionales

### Simulación: Tasa de Reacción D-T y Criterio de Lawson

Este código calcula y grafica la sección eficaz parametrizada de la reacción de fusión D-T y la curva ideal de ignición de Lawson (Producto Triple) asumiendo pérdida dominante por Bremsstrahlung a bajas temperaturas.

```python
import numpy as np
import matplotlib.pyplot as plt

# Temperaturas en keV
T = np.logspace(0, 2, 500)

# Usaremos un modelo más simple analítico para <sigma v> de D-T (en m^3/s)
def get_sigmav_DT(T_keV):
    # Ajuste fenomenológico válido entre 1 y 100 keV
    return 3.68e-18 / (T_keV**(2/3)) * np.exp(-19.94 / T_keV**(1/3))

sigmav_DT = get_sigmav_DT(T)

# Producto triple n T tau_E (keV s / m^3) para ignición ideal
# n T tau = 12 kT^2 / (E_alpha * <sigma v>)
E_alpha_J = 3.52e6 * 1.602e-19
k_B = 1.602e-16 # J / keV
nTtau = (12 * k_B * T**2) / (E_alpha_J * sigmav_DT)

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Temperatura (keV)')
ax1.set_ylabel(r'Reactividad $\langle \sigma v \rangle$ (m$^3$/s)', color=color)
ax1.loglog(T, sigmav_DT, color=color, linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(1e-26, 1e-21)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel(r'Producto Triple Requerido $n T \tau_E$ (m$^{-3}$ keV s)', color=color)
ax2.loglog(T, nTtau, color=color, linestyle='--', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(1e21, 1e24)

plt.title('Fusión D-T: Reactividad y Condición de Ignición')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()
```

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
