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
