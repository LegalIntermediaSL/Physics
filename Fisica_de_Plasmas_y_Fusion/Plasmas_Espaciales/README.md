# Plasmas Espaciales

La mayor parte de la materia visible del universo está en estado de plasma. El viento solar, la corona solar, las magnetosferas planetarias y muchos chorros astrofísicos son ejemplos donde la física del plasma es imprescindible.

## 🧮 Desarrollo Teórico Profundo

Los plasmas espaciales difieren fundamentalmente de los plasmas de laboratorio en su escala colosal y su densidad increíblemente baja. Al no poseer bordes materiales sólidos, su dinámica está dictada enteramente por la interacción mutua entre el viento estelar, los campos magnéticos intrínsecos de los planetas y el campo magnético interplanetario.

### 1. El Viento Solar: Expansión de Parker

En 1958, Eugene Parker demostró matemáticamente que la corona solar no podía estar en equilibrio estático termodinámico con el medio interestelar, lo que llevaba inevitablemente a la existencia de un flujo de plasma supersónico y constante: el Viento Solar.

Partiendo de la ecuación de momento de fluido isotérmico estacionario esféricamente simétrica para protones bajo la gravedad solar (masa $M_\odot$, radio r):

$$ m_p u \frac{du}{dr} = -\frac{1}{n} \frac{dp}{dr} - \frac{G M_\odot m_p}{r^2} $$

Utilizando la ecuación de estado $p = 2 n k_B T$ y la conservación de masa $\nabla \cdot (n \mathbf{u}) = 0 \implies 4\pi r^2 n u = \text{cte}$, podemos relacionar el gradiente de densidad con el gradiente de velocidad:

$$ \frac{1}{n} \frac{dn}{dr} = - \left( \frac{1}{u} \frac{du}{dr} + \frac{2}{r} \right) $$

Sustituyendo esto en la ecuación de momento, obtenemos la **Ecuación del Viento de Parker**:

$$ \left( u - \frac{2 k_B T}{m_p u} \right) \frac{du}{dr} = \frac{4 k_B T}{m_p r} - \frac{G M_\odot}{r^2} $$

Definiendo la velocidad del sonido isotérmica $c_s = \sqrt{2 k_B T / m_p}$, la ecuación se factoriza:

$$ \frac{u^2 - c_s^2}{u} \frac{du}{dr} = \frac{2 c_s^2}{r} - \frac{G M_\odot}{r^2} $$

Esta ecuación diferencial ordinaria presenta un punto crítico en $r_c = \frac{G M_\odot}{2 c_s^2}$. 
Para $r < r_c$, el lado derecho es negativo; para $r > r_c$, es positivo.
La única solución física que empieza con velocidades subsónicas ($u \approx 0$) en la superficie del Sol ($r = R_\odot$) y logra que la presión se desvanezca en el infinito ($r \to \infty$) es la **solución supersónica de Parker**. En esta, la velocidad del viento aumenta suavemente y cruza la barrera del sonido ($u = c_s$) exactamente en $r = r_c$, acelerándose asintóticamente a velocidades supersónicas del orden de $400 - 800$ km/s.

### 2. Formación de la Magnetosfera (Presión Dinámica)

Cuando el flujo supersónico del viento solar golpea el campo magnético dipolo de la Tierra, se forma una onda de choque en arco (*Bow Shock*). El plasma se frena y se desvía alrededor de la magnetosfera protectora, creando un límite definido conocido como **Magnetopausa**.

La posición de la magnetopausa frontal (punto de estancamiento subsolar) se determina por el balance entre la presión dinámica del viento solar entrante y la presión magnética del dipolo terrestre. 

Presión Dinámica del Viento Solar: $p_{dyn} = \rho u^2$
Presión Magnética del Campo Terrestre: $p_{mag} = \frac{B_{mp}^2}{2\mu_0}$

El campo dipolar a lo largo del ecuador disminuye con el radio cúbico:
$$ B(r) = B_0 \left( \frac{R_E}{r} \right)^3 $$
donde $B_0 \approx 31,000$ nT es el campo magnético en el ecuador terrestre y $R_E$ es el radio de la Tierra. Asumiendo una compresión del campo en la frontera por las corrientes de magnetopausa inducidas de un factor de $\approx 2$:

$$ B_{mp} \approx 2 B_0 \left( \frac{R_E}{r} \right)^3 $$

Igualando la presión dinámica (asumiendo pérdida total de momento normal) con la presión magnética:

$$ n_w m_p u_w^2 \approx \frac{1}{2\mu_0} \left( 2 B_0 \left( \frac{R_E}{r} \right)^3 \right)^2 = \frac{2 B_0^2}{\mu_0} \left( \frac{R_E}{r} \right)^6 $$

Despejando la distancia de equilibrio radial de la magnetopausa, la **Distancia de Chapman-Ferraro** ($R_{mp}$):

$$ R_{mp} \approx R_E \left( \frac{2 B_0^2}{\mu_0 n_w m_p u_w^2} \right)^{1/6} $$

### Diagrama: Interacción Viento Solar - Magnetosfera

```mermaid
graph LR
    A(Sol) -->|Viento Solar<br>Supersónico| B[Bow Shock]
    B -->|Plasma Frenado<br>y Calentado| C(Magnetosheath)
    C --> D{Magnetopausa}
    D -- Flujo Externo --> E[Lóbulos de la Cola]
    D -- Equilibrio --> F((Tierra))
    E -->|Reconexión Magnética en la Cola| G[Flujo de Retorno Plasma Sheet]
    G -->|Precipitación| H(Auroras / Tormentas Magnéticas)
    
    style A fill:#fb8500,stroke:#fff,color:#fff
    style D fill:#8ecae6,stroke:#fff,color:#000
    style H fill:#9d4edd,stroke:#fff,color:#fff
```

### 3. Reconexión Magnética Espacial

En plasmas espaciales casi colisionales, el Teorema de Alfvén ($d\Phi/dt = 0$) es casi exacto a macroescala. Sin embargo, en capas donde el campo magnético cambia abruptamente de dirección (hojas de corriente neutras, como el lado diurno de la magnetopausa cuando el campo magnético interplanetario apunta al sur), los gradientes espaciales se vuelven tan masivos que rompen las aproximaciones ideales.

En la capa de difusión disipativa a escala electrónica, la ecuación generalizada de Ohm incluye términos antes despreciados (como el término de Hall y el gradiente de presión de electrones). Este proceso local microscópico permite el "corte" y "reconexión" topológica de las líneas de campo del Sol con las de la Tierra (modelo de Dungey). Esto actúa como una válvula que transfiere impulsivamente momento, plasma y enormes cantidades de energía almacenada en el lóbulo de la cola hacia la ionosfera, originando las tormentas aurorales y los eventos drásticos del **Clima Espacial**.

## 🛠 Ejemplo Práctico

**Problema:** Una fulguración solar masiva emite una ráfaga de viento solar rápido. Los satélites de alerta temprana en L1 miden que el viento solar impactante tiene una densidad $n_w = 50 \, \text{cm}^{-3}$ ($5 \times 10^7 \, \text{m}^{-3}$) y viaja a $u_w = 900 \, \text{km/s}$. Calcule la nueva posición comprimida de la magnetopausa terrestre y compárela con su posición nominal en tiempo de calma ($R_{mp} \approx 10 \, R_E$). ¿Estarían en peligro inminente los satélites geoestacionarios orbitando a $r_{GEO} \approx 6.6 \, R_E$?

**Solución paso a paso:**

1. **Datos:**
   - Densidad de viento: $n_w = 5 \times 10^7 \, \text{m}^{-3}$
   - Velocidad: $u_w = 9 \times 10^5 \, \text{m/s}$
   - Masa protón: $m_p = 1.67 \times 10^{-27} \, \text{kg}$
   - Campo ecuatorial $B_0 = 3.1 \times 10^{-5} \, \text{T}$
   - Permeabilidad $\mu_0 = 4\pi \times 10^{-7} \, \text{T}\cdot\text{m/A}$

2. **Cálculo de la Presión Dinámica del Viento Solar:**
   $$ p_{dyn} = n_w m_p u_w^2 = (5 \times 10^7) (1.67 \times 10^{-27}) (9 \times 10^5)^2 $$
   $$ p_{dyn} = (8.35 \times 10^{-20}) (8.1 \times 10^{11}) \approx 6.76 \times 10^{-8} \, \text{Pa} $$
   *(Para dar contexto, en tiempo de calma el viento es $\approx 5 \, \text{cm}^{-3}$ y $400 \, \text{km/s}$, con $p_{dyn} \approx 1.3 \times 10^{-9} \, \text{Pa}$. ¡Esta es una compresión de 50 veces!)*

3. **Cálculo de la constante magnética del numerador:**
   $$ \frac{2 B_0^2}{\mu_0} = \frac{2 (3.1 \times 10^{-5})^2}{4\pi \times 10^{-7}} = \frac{1.922 \times 10^{-9}}{1.256 \times 10^{-6}} \approx 1.53 \times 10^{-3} \, \text{Pa} $$

4. **Despeje de $R_{mp}$ usando la Distancia de Chapman-Ferraro:**
   $$ \frac{R_{mp}}{R_E} = \left( \frac{2 B_0^2 / \mu_0}{p_{dyn}} \right)^{1/6} $$
   $$ \frac{R_{mp}}{R_E} = \left( \frac{1.53 \times 10^{-3}}{6.76 \times 10^{-8}} \right)^{1/6} = (22633)^{1/6} $$
   $$ \frac{R_{mp}}{R_E} \approx 5.3 $$

**Conclusión:** La magnetopausa ha sido comprimida violentamente desde sus $10 \, R_E$ nominales hasta $R_{mp} \approx 5.3 \, R_E$.
Dado que los satélites geoestacionarios (comunicaciones, clima) orbitan a $6.6 \, R_E$, este evento de súper tormenta dejaría a los satélites **fuera del escudo magnético terrestre**, sumergiéndolos directamente en la turbulenta y radioactiva "Magnetosheath", poniéndolos en severo peligro de fallos electrónicos inducidos.

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Modelo del Espiral Magnético de Parker
Asumiendo un Sol en rotación con velocidad angular $\Omega_\odot$ y un viento solar de velocidad constante $u_w$ estrictamente radial lejos de la superficie, derive la forma geométrica de las líneas de campo magnético interplanetario (IMF) en el plano ecuatorial. Demuestre que forman la espiral de Arquímedes y calcule el "ángulo de espiral" en la órbita de la Tierra (1 AU).

**Solución paso a paso:**
Consideremos el marco de referencia en corrotación con el Sol. En este marco (sistema ideal estacionario), la ley de congelamiento de flujo dicta que la velocidad del fluido es estrictamente paralela al campo magnético: $\mathbf{u}' \parallel \mathbf{B}$.
En el marco sidéreo inercial, la velocidad del plasma cuenta con una componente de rotación arrastrada desde el origen $\mathbf{v}_\phi = \Omega_\odot r$, de manera que la velocidad corrotante aparente del viento visto desde el Sol rígidamente giratorio es:
$$ \mathbf{u}' = u_w \hat{r} - \Omega_\odot r \hat{\phi} $$
Como $\mathbf{B}$ es paralelo a $\mathbf{u}'$, las componentes de $\mathbf{B} = (B_r, B_\phi, 0)$ satisfacen:
$$ \frac{B_\phi}{B_r} = \frac{- \Omega_\odot r}{u_w} $$
En coordenadas polares $(r, \phi)$, la ecuación diferencial de una línea de campo geométricamente es $r d\phi / dr = B_\phi / B_r$.
$$ \frac{r d\phi}{dr} = -\frac{\Omega_\odot r}{u_w} \implies d\phi = -\frac{\Omega_\odot}{u_w} dr $$
Integrando desde la superficie fuente $r_0$ hasta $r$:
$$ \phi(r) - \phi_0 = -\frac{\Omega_\odot}{u_w} (r - r_0) $$
Esta es matemáticamente la ecuación de la Espiral de Arquímedes.
Para la Tierra, la distancia $r \approx 1 \, \text{AU} = 1.5 \times 10^{11} \, \text{m}$, y el periodo de rotación ecuatorial solar es unos $25.4$ días, $\Omega_\odot = \frac{2\pi}{25.4 \times 86400} \approx 2.86 \times 10^{-6} \, \text{rad/s}$. Si tomamos $u_w \approx 400 \, \text{km/s} = 4 \times 10^5 \, \text{m/s}$:
El ángulo de espiral del IMF (el ángulo entre la dirección radial y el campo), está dado por:
$$ \tan \theta_P = \left| \frac{B_\phi}{B_r} \right| = \frac{\Omega_\odot r}{u_w} = \frac{(2.86 \times 10^{-6}) (1.5 \times 10^{11})}{4 \times 10^5} \approx \frac{429}{400} \approx 1.07 $$
$$ \theta_P = \arctan(1.07) \approx 47^\circ $$
Esto indica que el campo magnético del sol no nos alcanza radialmente, sino que intercepta la Tierra con un ángulo de unos 45 grados de desviación matutina.

### Problema 2: Presión Magnética en la Cola de la Magnetosfera (Magnetotail)
Asuma que el lóbulo magnético en la cola oscura de la Tierra es modelable geométricamente como un cilindro largo de radio $R_T$ que transporta el campo magnético $\mathbf{B}_L$ estrictamente paralelo al cilindro. El exterior está bañado por la vaina (magnetosheath) con plasma a presión $p_s$ y densidad $n_s$. Despreciando el campo magnético externo, determine el campo magnético en el lóbulo $B_L$.

**Solución paso a paso:**
En la transición de las fronteras magnetosféricas estacionarias largas donde la tensión tangencial magnética y la curvatura son despreciables, el equilibrio requiere estricta continuidad de la presión total (cinética + magnética) a través de la frontera de la magnetopausa externa hacia el lóbulo.
$$ \left( p + \frac{B^2}{2\mu_0} \right)_{Lóbulo} = \left( p + \frac{B^2}{2\mu_0} \right)_{Vaina} $$
El lóbulo de la cola magnética está prácticamente vacío de partículas comparado con su inmenso campo; es una estructura magnéticamente dominada, por tanto $p_{Lóbulo} \approx 0$.
En contraste, asumimos según el enunciado que en la región exterior el campo magnético tangencial dispersado es pequeño, entonces su término magnético puede subestimarse, siendo dominante la presión térmica o estática del plasma $p_s$.
Igualando:
$$ \frac{B_L^2}{2\mu_0} \approx p_s $$
$$ B_L \approx \sqrt{2\mu_0 p_s} $$
El campo geomagnético en la inmensa cola se autosustenta estrictamente equilibrando con su presión interna la presión termodinámica ejercida por el viento solar circundante fluyendo hacia el abismo exterior. 

### Problema 3: Reflexión de Ondas de Radio Cortas en la Ionosfera
La ionosfera de la Tierra presenta capas sucesivas (D, E, F1, F2) con densidades crecientes de electrones, alcanzando un pico de $N_{max} \approx 10^{12} \, \text{m}^{-3}$ en la capa F2 alrededor de 300 km de altitud. Utilizando la aproximación de un plasma sin campo magnético en este estrato local para oscilaciones de alta frecuencia, determine la "Frecuencia Crítica" máxima $f_c$ de señales de radio terrestres verticales que pueden rebotar en la ionosfera (Skip radio propagation).

**Solución paso a paso:**
Para ondas electromagnéticas puramente transversales no magnetizadas en propagación vertical, la relación de dispersión local es:
$$ \omega^2 = \omega_{pe}^2 + c^2 k^2 $$
La onda de radio penetrará la ionosfera conforme viaja hacia arriba, enfrentando un gradiente creciente de densidad, lo que incrementa $\omega_{pe}(z)$.
La frecuencia de la onda emitida ($\omega$) es constante. A medida que entra, su número de onda local $k(z)$ debe disminuir (la fase se ensancha) para satisfacer la relación de dispersión:
$$ c^2 k(z)^2 = \omega^2 - \omega_{pe}(z)^2 $$
La reflexión ocurre idénticamente cuando el vector de onda se anula localmente ($k(z) = 0$), en ese punto el índice de refracción es nulo y la señal se vuelve evanescente perdiéndose en el horizonte imaginario, lo cual significa que se refleja.
La condición de reflexión es: $\omega = \omega_{pe}(z_{reflejo})$.
La frecuencia de onda más alta capaz de reflejarse será la que encuentre apenas la densidad máxima absoluta antes de escapar del planeta:
$$ \omega_{max} = \omega_{pe}(N_{max}) = \sqrt{\frac{N_{max} e^2}{m_e \epsilon_0}} $$
En frecuencia lineal $f_c = \frac{\omega_{max}}{2\pi} \approx 8.98 \sqrt{N_{max}}$ (fórmula empírica práctica en Hz y $\text{m}^{-3}$).
$$ f_c \approx 8.98 \sqrt{10^{12}} = 8.98 \times 10^6 \, \text{Hz} = 8.98 \, \text{MHz} $$
**Conclusión:** Cualquier señal de comunicación vertical a la Tierra que exceda $\sim 9 \, \text{MHz}$ perforará limpiamente la ionosfera escapando al espacio profundo (vital para comunicarse con satélites). Las estaciones de radiodifusión en Onda Corta (SW) utilizan frecuencias hábilmente calculadas menores que esto pero radiadas oblicuamente, de modo que logran la refracción iónica y se rebotan en "saltos" intercontinentales transoceánicos que rebasan la curvatura terrestre.

## 💻 Simulaciones Computacionales

### Simulación: Solución del Viento Solar de Parker

Este script resuelve la topología de la ecuación diferencial del viento solar isotérmico, identificando el punto crítico y dibujando la solución física transónica que escapa de la gravedad estelar.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Normalizamos variables:
# u_norm = u / c_s (Número de Mach M)
# r_norm = r / r_c
# La ecuación de Parker normalizada es: (M - 1/M) dM/dr = 2/r - 2/r^2

r_norm = np.linspace(0.1, 10, 500)

# Ecuación algebraica implícita integral del viento solar:
# M^2 - 1 - 2*ln(M) = 4*ln(r_norm) + 4/r_norm - 3
# Definimos la función para buscar raíces:
def parker_eq(M, r):
    return M**2 - 1 - 2*np.log(M) - 4*np.log(r) - 4/r + 3

M_sup = np.zeros_like(r_norm)
M_sub = np.zeros_like(r_norm)

for i, r in enumerate(r_norm):
    # Buscamos solución supersónica (M > 1)
    # y solución subsónica (M < 1)
    if r == 1.0:
        M_sup[i] = 1.0
        M_sub[i] = 1.0
    else:
        # Adivinanzas iniciales basadas en el radio
        guess_sup = r if r > 1 else 2.0
        guess_sub = 0.5/r**2 if r > 1 else 0.5
        
        sol_sup = fsolve(parker_eq, guess_sup, args=(r,))
        sol_sub = fsolve(parker_eq, guess_sub, args=(r,))
        
        M_sup[i] = sol_sup[0]
        M_sub[i] = sol_sub[0]

# Construimos la solución física completa (Viento Solar)
# Combina rama subsónica para r < 1 y supersónica para r > 1
solar_wind = np.where(r_norm <= 1.0, M_sub, M_sup)
# Brisa solar (totalmente subsónica)
solar_breeze = M_sub

plt.figure(figsize=(10, 6))
plt.plot(r_norm, solar_wind, 'r-', linewidth=3, label='Viento Solar (Transónico)')
plt.plot(r_norm, solar_breeze, 'b--', linewidth=2, label='Brisa Solar (Subsónica)')

plt.axvline(1.0, color='k', linestyle=':', label='Punto Crítico Sonico ($r_c$)')
plt.axhline(1.0, color='k', linestyle=':')

plt.title('Modelo Isotérmico del Viento Solar de Parker')
plt.xlabel('Distancia Normalizada $r / r_c$')
plt.ylabel('Velocidad Normalizada (Mach $u / c_s$)')
plt.ylim(0, 3.5)
plt.legend()
plt.grid(True)
plt.show()
```

## 📚 Recursos Específicos

### Cursos Específicos
1. [Space Plasma Physics - UCL](https://www.ucl.ac.uk)
2. [Physics of the Solar Corona - UIO](https://www.uio.no)
3. [Heliophysics Summer School - UCAR](https://cpaess.ucar.edu)
4. [Space Weather: Observation and Modeling - Coursera](https://www.coursera.org)
5. [Solar System Plasmas - University of Michigan](https://umich.edu)
6. [Magnetospheric Physics - KTH](https://www.kth.se)

### Artículos y Simulaciones
1. [Parker, E. N. (1958). *Dynamics of the Interplanetary Gas and Magnetic Fields*. The Astrophysical Journal.](https://doi.org/10.1086/146503)
2. [Dungey, J. W. (1961). *Interplanetary Magnetic Field and the Auroral Zones*. Physical Review Letters.](https://doi.org/10.1103/PhysRevLett.6.47)
3. [Vasyliunas, V. M. (1975). *Theoretical models of magnetic field line merging*. Reviews of Geophysics.](https://doi.org/10.1029/RG013i001p00303)
4. [Coroniti, F. V. (1985). *Space plasma physics*. Reviews of Geophysics.](https://doi.org/10.1029/RG023i002p00445)
5. [Kivelson, M. G., & Russell, C. T. (1995). *Introduction to Space Physics*. Cambridge.](https://www.cambridge.org/core/books/introduction-to-space-physics/DEAB3782C7C43E24E677F21F64A0B85E)
6. [CCMC - Community Coordinated Modeling Center](https://ccmc.gsfc.nasa.gov/) - Space weather models.
7. [BATS-R-US](https://csem.engin.umich.edu/tools/swmf/bats-r-us.php) - Global MHD modeling of the magnetosphere.
8. [Vlasiator](https://www.helsinki.fi/en/researchgroups/vlasiator) - Vlasov code for Earth's magnetosphere.
9. [OpenGGCM](https://unh.edu) - Open Geospace General Circulation Model.

### 📖 Referencias Útiles y Bibliografía
1. [Gurnett, D. A., & Bhattacharjee, A. (2005). *Introduction to Plasma Physics: With Space and Laboratory Applications*. Cambridge.](https://www.cambridge.org/core/books/introduction-to-plasma-physics/28DAA72AF30A4B4B9C8991206CC8C654)
2. [Kivelson, M. G., & Russell, C. T. (1995). *Introduction to Space Physics*. Cambridge University Press.](https://www.cambridge.org/core/books/introduction-to-space-physics/DEAB3782C7C43E24E677F21F64A0B85E)
3. [Baumjohann, W., & Treumann, R. A. (2012). *Basic Space Plasma Physics*. Imperial College Press.](https://www.worldscientific.com/worldscibooks/10.1142/p850)
4. [Kallenrode, M.-B. (2004). *Space Physics: An Introduction to Plasmas and Particles in the Heliosphere and Magnetospheres*. Springer.](https://link.springer.com/book/10.1007/978-3-662-09419-3)
5. [Parks, G. K. (2004). *Physics of Space Plasmas: An Introduction*. Westview Press.](https://www.taylorfrancis.com/books/mono/10.4324/9780429497534/physics-space-plasmas-george-parks)
