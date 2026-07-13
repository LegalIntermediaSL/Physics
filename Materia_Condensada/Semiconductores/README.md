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

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Concentración Intrínseca de Portadores $n_i$
A partir de las densidades efectivas de estados en las bandas de conducción ($N_c$) y valencia ($N_v$), derive la expresión para la concentración intrínseca de portadores $n_i$ en un semiconductor en equilibrio térmico y demuestre su dependencia exponencial con la temperatura.

**Solución paso a paso:**
En equilibrio térmico, la concentración de electrones $n$ en la banda de conducción y de huecos $p$ en la banda de valencia, usando estadística de Maxwell-Boltzmann (válida si el nivel de Fermi está al menos a $3k_B T$ del borde de banda), son:
$$ n = N_c e^{-(E_c - E_F)/k_B T} $$
$$ p = N_v e^{-(E_F - E_v)/k_B T} $$
donde $N_c = 2(m_e^* k_B T / 2\pi\hbar^2)^{3/2}$ y $N_v = 2(m_h^* k_B T / 2\pi\hbar^2)^{3/2}$.
El producto de estas concentraciones nos da la ley de acción de masas para semiconductores:
$$ np = N_c N_v e^{-(E_c - E_v)/k_B T} $$
La diferencia $E_c - E_v$ es precisamente la energía del gap prohibido $E_g$.
Para un semiconductor intrínseco (sin dopar), por conservación de carga se debe cumplir que $n = p = n_i$.
Entonces $n_i^2 = n p = N_c N_v e^{-E_g/k_B T}$.
Tomando la raíz cuadrada:
$$ n_i = \sqrt{N_c N_v} e^{-E_g / 2k_B T} $$
Dado que $N_c, N_v \propto T^{3/2}$, la concentración intrínseca varía como $T^{3/2} e^{-E_g / 2k_B T}$.
Esta fuerte dependencia exponencial domina, por lo que una pequeña variación de $T$ produce cambios de órdenes de magnitud en el número de portadores intrínsecos.

### Problema 2: Energía de Ionización de Impurezas Donadoras
Estime la energía de ionización de una impureza donadora (como fósforo) en silicio utilizando el modelo del átomo de hidrógeno de Bohr modificado para medios sólidos. ($m_e^* \approx 0.26 m_e$, $\epsilon_r \approx 11.7$).

**Solución paso a paso:**
En el modelo hidrogenoide, el electrón donado orbita alrededor del ión donador positivo incrustado en el cristal.
Utilizamos los resultados del modelo de Bohr para la energía del estado fundamental, reemplazando la masa del electrón por la masa efectiva $m_e^*$ y la permitividad del vacío $\epsilon_0$ por la permitividad del material $\epsilon = \epsilon_r \epsilon_0$.
La energía de ionización del átomo de hidrógeno en el vacío es:
$$ E_H = \frac{m_e e^4}{8 \epsilon_0^2 h^2} = 13.6 \text{ eV} $$
Para la impureza en el cristal, la energía de ionización será:
$$ E_d = \frac{m_e^* e^4}{8 (\epsilon_r \epsilon_0)^2 h^2} = E_H \left( \frac{m_e^*}{m_e} \right) \left( \frac{1}{\epsilon_r^2} \right) $$
Sustituyendo los valores para el Silicio:
$$ E_d = 13.6 \text{ eV} \times (0.26) \times \left( \frac{1}{11.7^2} \right) $$
$$ E_d = 13.6 \times 0.26 \times 0.0073 \approx 0.0258 \text{ eV} \approx 25.8 \text{ meV} $$
Esta energía ($~25$ meV) es muy cercana a la energía térmica a temperatura ambiente ($k_B T \approx 26$ meV). Por esta razón, a temperatura ambiente, casi todos los donadores en silicio están completamente ionizados, aportando un electrón libre a la banda de conducción.

### Problema 3: Potencial de Contacto en una Unión p-n
Calcule el potencial de contacto $V_0$ (built-in potential) de una unión p-n abrupta de silicio a $T = 300$ K dopada con $N_A = 10^{16} \text{ cm}^{-3}$ y $N_D = 10^{15} \text{ cm}^{-3}$. Asuma $n_i \approx 10^{10} \text{ cm}^{-3}$ y $V_T = k_B T / q \approx 25.9$ mV.

**Solución paso a paso:**
Lejos de la región de agotamiento (en las zonas neutras), las concentraciones mayoritarias son aproximadamente $p_p \approx N_A$ y $n_n \approx N_D$.
En el equilibrio, el nivel de Fermi debe ser constante en toda la estructura.
En el lado p:
$$ p_p = n_i e^{(E_i - E_{Fp}) / k_B T} \implies E_i^{(p)} - E_F = k_B T \ln\left(\frac{N_A}{n_i}\right) $$
En el lado n:
$$ n_n = n_i e^{(E_{Fn} - E_i) / k_B T} \implies E_F - E_i^{(n)} = k_B T \ln\left(\frac{N_D}{n_i}\right) $$
El potencial de contacto surge de la diferencia entre el nivel intrínseco $E_i$ en los dos lados. Puesto que la energía potencial es $-q V(x) = E_i(x)$, la diferencia de potencial electrostático es $V_0 = \frac{1}{q} [E_i^{(p)} - E_i^{(n)}]$.
Sumando las ecuaciones:
$$ E_i^{(p)} - E_i^{(n)} = k_B T \ln\left(\frac{N_A}{n_i}\right) + k_B T \ln\left(\frac{N_D}{n_i}\right) = k_B T \ln\left(\frac{N_A N_D}{n_i^2}\right) $$
Entonces el potencial de contacto en voltios es:
$$ V_0 = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right) $$
Sustituyendo los valores:
$$ V_0 = 0.0259 \ln\left(\frac{10^{16} \times 10^{15}}{(10^{10})^2}\right) = 0.0259 \ln(10^{11}) $$
Sabiendo que $\ln(10) \approx 2.303$:
$$ V_0 = 0.0259 \times 11 \times 2.303 \approx 0.656 \text{ V} $$
El potencial de contacto es de aproximadamente 0.66 V.

## 💻 Simulaciones Computacionales

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_intrinsic_carrier_concentration():
    T = np.linspace(200, 600, 400)
    k_B = 8.617e-5 # eV/K
    
    # Parametros para Si y Ge
    Eg_Si = 1.12 # eV
    Eg_Ge = 0.66 # eV
    
    # N_c * N_v proportional to T^3
    # n_i ~ T^(3/2) * exp(-Eg / 2kT)
    
    ni_Si = (T**1.5) * np.exp(-Eg_Si / (2 * k_B * T))
    ni_Ge = (T**1.5) * np.exp(-Eg_Ge / (2 * k_B * T))
    
    plt.figure(figsize=(9, 6))
    plt.semilogy(1000/T, ni_Si, label='Silicio ($E_g = 1.12$ eV)')
    plt.semilogy(1000/T, ni_Ge, label='Germanio ($E_g = 0.66$ eV)')
    
    plt.xlabel('$1000 / T$ ($K^{-1}$)')
    plt.ylabel('Concentración de Portadores Intrínseca (Unidades Arb.)')
    plt.title('Simulación: Dependencia de $n_i$ con la Temperatura')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == '__main__':
    plot_intrinsic_carrier_concentration()
```

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
