# Semiconductores

Los semiconductores ocupan un lugar intermedio entre conductores y aislantes. Su enorme importancia tecnológica se debe a que su conductividad puede controlarse con dopaje, temperatura, campos eléctricos y luz.

## 🧮 Desarrollo Teórico Profundo

Los semiconductores son aislantes a $T=0\,K$ con un bandgap ($E_g$) lo suficientemente estrecho (generalmente $E_g < 3 \, \text{eV}$) como para que las fluctuaciones térmicas a temperatura ambiente logren promover electrones desde la banda de valencia a la banda de conducción.

### 1. Estadística de Portadores Intrínsecos

A temperatura $T$, la probabilidad de que un estado cuántico con energía $E$ esté ocupado por un electrón viene dictada por la **Distribución de Fermi-Dirac**:

$$ f(E) = \frac{1}{e^{(E - E_F)/k_B T} + 1} $$

donde $E_F$ es el Nivel de Fermi (el potencial químico electrónico). 
La densidad de electrones en la banda de conducción $n_c$ y de huecos en la banda de valencia $p_v$ se calcula integrando la distribución de Fermi multiplicada por la densidad de estados $D(E)$:

$$ n_c = \int_{E_c}^\infty D_c(E) f(E) dE \quad \text{y} \quad p_v = \int_{-\infty}^{E_v} D_v(E) [1 - f(E)] dE $$

Para un semiconductor no degenerado, donde $E_c - E_F \gg k_B T$ y $E_F - E_v \gg k_B T$, la distribución de Fermi se reduce a la de Boltzmann. Asumiendo bandas parabólicas isotrópicas con masas efectivas $m_e^*$ (electrones) y $m_h^*$ (huecos):

$$ n_c = N_c e^{-(E_c - E_F)/k_B T} \quad \text{y} \quad p_v = N_v e^{-(E_F - E_v)/k_B T} $$

donde las densidades efectivas de estados de banda son:
$$ N_c = 2 \left( \frac{m_e^* k_B T}{2\pi \hbar^2} \right)^{3/2} \quad \text{y} \quad N_v = 2 \left( \frac{m_h^* k_B T}{2\pi \hbar^2} \right)^{3/2} $$

El producto empírico de las densidades es la **Ley de Acción de Masas** para semiconductores, siendo independiente del nivel de Fermi y por tanto inalterable ante el dopaje:

$$ n_c p_v = n_i^2 = N_c N_v e^{-E_g / k_B T} $$
donde $E_g = E_c - E_v$ es el bandgap. En un semiconductor intrínseco (puro), $n = p = n_i$.

### 2. Semiconductores Extrínsecos: Teoría del Dopaje Hidrogenoide

Para controlar la conductividad y manipular $E_F$, introducimos impurezas atómicas (dopaje). 
Si sustituimos un átomo de Silicio (Grupo IV) por un átomo de Fósforo (Grupo V), este aporta un electrón extra. 
El electrón extra no participa en los enlaces covalentes y queda débilmente ligado al ión $P^+$ mediante atracción Coulombiana protegida por la permitividad dieléctrica del medio $\epsilon_r$.

Este sistema se modela matemáticamente como un **Átomo de Hidrógeno Modificado** (Aproximación de Masa Efectiva). La energía de ligadura de este electrón "Donador" es:

$$ E_d = \frac{13.6 \, \text{eV}}{\epsilon_r^2} \left( \frac{m_e^*}{m_e} \right) $$

Para el Silicio ($\epsilon_r = 11.9$, $m_e^* \approx 0.2 m_e$), la energía de ionización es de apenas $\sim 20-30 \, \text{meV}$, comparable con la energía térmica a temperatura ambiente ($k_B T \approx 26 \, \text{meV}$). Por consiguiente, a temperatura ambiente prácticamente todos los átomos donadores estarán ionizados térmicamente, liberando sus electrones en la banda de conducción. 

Esto nos da una densidad abrumadora de portadores tipo $n \approx N_D$ (densidad de donadores). Debido a la ley de acción de masas, los portadores minoritarios colapsan a $p \approx n_i^2 / N_D$. El nivel de Fermi $E_F$ se desplaza asimétricamente hacia arriba, ubicándose justo debajo de la banda de conducción. El dopaje con elementos del Grupo III (Boro) produce el efecto análogo con "Aceptores" y portadores tipo $p$.

### Diagrama: Bandas y Niveles de Dopaje

```mermaid
graph TD
    subgraph Aislante / Semiconductor Intrínseco
    A[Banda de Conducción <br> Vacía (Ec)] 
    B(Nivel Fermi Ei en el medio)
    C[Banda de Valencia <br> Llena (Ev)]
    A -.->|Bandgap Eg| C
    end
    
    subgraph Semiconductor Tipo N (Dopaje Donador)
    D[Banda de Conducción <br> Electrones en tránsito]
    E(Nivel Donador Ed cerca de Ec)
    F(Nivel Fermi Ef elevado)
    G[Banda de Valencia]
    D --- E
    end
    
    subgraph Semiconductor Tipo P (Dopaje Aceptor)
    H[Banda de Conducción]
    I(Nivel Fermi Ef hundido)
    J(Nivel Aceptor Ea cerca de Ev)
    K[Banda de Valencia <br> Huecos en tránsito]
    J --- K
    end
    
    style A fill:#a8dadc,stroke:#333
    style C fill:#457b9d,stroke:#333
    style D fill:#a8dadc,stroke:#333
    style E fill:#e63946,stroke:#333
    style G fill:#457b9d,stroke:#333
    style H fill:#a8dadc,stroke:#333
    style J fill:#2a9d8f,stroke:#333
    style K fill:#457b9d,stroke:#333
```

## 🛠 Ejemplo Práctico

**Problema:** Una oblea de Silicio purísimo a temperatura ambiente ($T=300 \, \text{K}$) tiene una concentración intrínseca de portadores de $n_i = 10^{10} \, \text{cm}^{-3}$. 
Se dopa con Boro (un aceptor trivalente) con una concentración homogénea de $N_A = 10^{16} \, \text{cm}^{-3}$. 
Asumiendo ionización completa:
1. Calcule las concentraciones de electrones ($n$) y de huecos ($p$) en equilibrio.
2. Determine el desplazamiento absoluto del nivel de Fermi ($E_F$) relativo a su nivel intrínseco ($E_i$).

**Solución paso a paso:**

1. **Estimación por Ionización Completa:**
   El Boro es un dopante Aceptor del Grupo III. Actuará robando electrones de la banda de valencia, creando huecos. 
   Dado que $N_A \gg n_i$ ($10^{16} \gg 10^{10}$), asumimos que la concentración de huecos (portadores mayoritarios) es igual a la concentración de dopantes a temperatura ambiente:
   $$ p \approx N_A = 10^{16} \, \text{cm}^{-3} $$

2. **Cálculo de Portadores Minoritarios:**
   Utilizamos la fundamental Ley de Acción de Masas para semiconductores en equilibrio térmico:
   $$ n \cdot p = n_i^2 $$
   Despejando la concentración de electrones (minoritarios):
   $$ n = \frac{n_i^2}{p} = \frac{(10^{10} \, \text{cm}^{-3})^2}{10^{16} \, \text{cm}^{-3}} = \frac{10^{20}}{10^{16}} = 10^4 \, \text{cm}^{-3} $$
   El dopaje ha suprimido a los electrones por un factor de un millón (de $10^{10}$ a $10^4$).

3. **Cálculo del Desplazamiento del Nivel de Fermi:**
   Para relacionar concentraciones con los niveles de energía, usamos las distribuciones de Boltzmann relativas al nivel intrínseco $E_i$ (donde $n = p = n_i$):
   $$ p = n_i e^{(E_i - E_F) / k_B T} $$
   Despejando $(E_i - E_F)$:
   $$ \frac{p}{n_i} = e^{(E_i - E_F) / k_B T} \implies \ln\left(\frac{p}{n_i}\right) = \frac{E_i - E_F}{k_B T} $$
   $$ E_i - E_F = k_B T \ln\left(\frac{p}{n_i}\right) $$
   Sustituyendo los valores, sabiendo que a $T=300 \, \text{K}$, la energía térmica es $k_B T \approx 0.0259 \, \text{eV}$:
   $$ E_i - E_F = 0.0259 \times \ln\left( \frac{10^{16}}{10^{10}} \right) = 0.0259 \times \ln(10^6) $$
   Sabiendo que $\ln(10^6) = 6 \ln(10) \approx 6 \times 2.302 = 13.81$:
   $$ E_i - E_F = 0.0259 \times 13.81 \approx 0.358 \, \text{eV} $$

**Conclusión:** 
La oblea dopada es manifiestamente **Tipo-p**, con $p = 10^{16} \, \text{cm}^{-3}$ y $n = 10^4 \, \text{cm}^{-3}$. 
El nivel de Fermi del cristal ha caído drásticamente en la brecha, situándose a **0.358 eV por debajo** de su posición media intrínseca, aproximándose vertiginosamente a la banda de valencia. Esta asimetría gigantesca de portadores es el cimiento estadístico indispensable para originar los campos eléctricos de agotamiento en las uniones P-N.

## 📚 Recursos Específicos

### Cursos
1. **[Semiconductor Devices (Coursera / NCKU)](https://www.coursera.org):** Fundamentos físicos de diodos y transistores.
2. **[Physics of Semiconductors (NPTEL)](https://nptel.ac.in):** Teoría rigurosa del transporte y óptica en semiconductores.
3. **[Nanoelectronics (MIT OCW)](https://ocw.mit.edu):** Semiconductores en la escala nanométrica.
4. **[Solid State Devices (edX)](https://www.edx.org):** Aplicaciones prácticas de los principios de dopaje y uniones p-n.
5. **[Optoelectronics (Stanford)](https://online.stanford.edu):** Interacción de semiconductores con la luz (LEDs y láseres).

### Artículos y Simulaciones
1. **[nanoHUB PN Junction Lab](https://nanohub.org):** Simulador fenomenal para ver perfiles de bandas, campos eléctricos y corrientes en uniones p-n.
2. **[PhET - Semiconductors](https://phet.colorado.edu):** Excelente simulación para visualizar dopaje tipo $p$ y tipo $n$ y el movimiento de portadores.
3. **["The Transistor: 60 Years Later" (IEEE Spectrum)](https://spectrum.ieee.org):** Artículo histórico sobre el impacto de la física de semiconductores.
4. **[TCAD Sentaurus / Silvaco](https://www.synopsys.com):** (Menciones de software profesional) Herramientas estándar de la industria para simular dispositivos.
5. **["Moore's Law and the Future of Semiconductors" (Nature)](https://www.nature.com):** Reflexión sobre los límites de los dispositivos actuales.
6. **[Bandgap Engineering (Capasso, Science)](https://www.science.org):** Cómo diseñar materiales modificando sus bandas.
7. **[BJT / MOSFET Simulators (Falstad)](https://www.falstad.com/circuit/):** Circuitos y uniones simuladas en tiempo real.
8. **["Two-dimensional semiconductors" (Nature Nanotechnology)](https://www.nature.com):** Introducción a los semiconductores basados en TMDs (MoS2, etc.).

### 📖 Referencias Útiles y Bibliografía
1. [Sze, S. M. *Physics of Semiconductor Devices*](https://www.wiley.com). Wiley (El estándar de la industria).
2. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org) (Capítulo 8).
3. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://archive.org) (Capítulo 28).
4. [Streetman, B. G., & Banerjee, S. K. *Solid State Electronic Devices*](https://www.pearson.com). Pearson.
5. [Pierret, R. F. *Semiconductor Device Fundamentals*](https://archive.org). Addison-Wesley.
