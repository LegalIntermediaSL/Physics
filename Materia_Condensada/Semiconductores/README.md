# Semiconductores

Los semiconductores ocupan un lugar intermedio entre conductores y aislantes. Su enorme importancia tecnológica se debe a que su conductividad puede controlarse con dopaje, temperatura, campos eléctricos y luz.

## 🧮 Desarrollo Teórico Profundo

Los semiconductores son aislantes a $T=0\,K$ con un bandgap ($E_g$) lo suficientemente estrecho (generalmente $E_g < 3 \, \text{eV}$) como para que las fluctuaciones térmicas a temperatura ambiente logren promover electrones desde la banda de valencia a la banda de conducción.

### 1. Estadística de Portadores Intrínsecos

A temperatura $T$, la probabilidad de que un estado cuántico con energía $E$ esté ocupado por un electrón viene dictada por la **Distribución de Fermi-Dirac**:

$$
f(E) = \frac{1}{e^{(E - E_F)/k_B T} + 1}
$$

donde $E_F$ es el Nivel de Fermi (el potencial químico electrónico). 
La densidad de electrones en la banda de conducción $n_c$ y de huecos en la banda de valencia $p_v$ se calcula integrando la distribución de Fermi multiplicada por la densidad de estados $D(E)$:

$$
n_c = \int_{E_c}^\infty D_c(E) f(E) dE \quad \text{y} \quad p_v = \int_{-\infty}^{E_v} D_v(E) [1 - f(E)] dE
$$

Para un semiconductor no degenerado, donde $E_c - E_F \gg k_B T$ y $E_F - E_v \gg k_B T$, la distribución de Fermi se reduce a la de Boltzmann. Asumiendo bandas parabólicas isotrópicas con masas efectivas $m_e^*$ (electrones) y $m_h^*$ (huecos):

$$
n_c = N_c e^{-(E_c - E_F)/k_B T} \quad \text{y} \quad p_v = N_v e^{-(E_F - E_v)/k_B T}
$$

donde las densidades efectivas de estados de banda son:

$$
N_c = 2 \left( \frac{m_e^* k_B T}{2\pi \hbar^2} \right)^{3/2} \quad \text{y} \quad N_v = 2 \left( \frac{m_h^* k_B T}{2\pi \hbar^2} \right)^{3/2}
$$

El producto empírico de las densidades es la **Ley de Acción de Masas** para semiconductores, siendo independiente del nivel de Fermi y por tanto inalterable ante el dopaje:

$$
n_c p_v = n_i^2 = N_c N_v e^{-E_g / k_B T}
$$

donde $E_g = E_c - E_v$ es el bandgap. En un semiconductor intrínseco (puro), $n = p = n_i$.

### 2. Semiconductores Extrínsecos: Teoría del Dopaje Hidrogenoide

Para controlar la conductividad y manipular $E_F$, introducimos impurezas atómicas (dopaje). 
Si sustituimos un átomo de Silicio (Grupo IV) por un átomo de Fósforo (Grupo V), este aporta un electrón extra. 
El electrón extra no participa en los enlaces covalentes y queda débilmente ligado al ión $P^+$ mediante atracción Coulombiana protegida por la permitividad dieléctrica del medio $\epsilon_r$.

Este sistema se modela matemáticamente como un **Átomo de Hidrógeno Modificado** (Aproximación de Masa Efectiva). La energía de ligadura de este electrón "Donador" es:

$$
E_d = \frac{13.6 \, \text{eV}}{\epsilon_r^2} \left( \frac{m_e^*}{m_e} \right)
$$

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

   

$$
p \approx N_A = 10^{16} \, \text{cm}^{-3}
$$

2. **Cálculo de Portadores Minoritarios:**
   Utilizamos la fundamental Ley de Acción de Masas para semiconductores en equilibrio térmico:

   

$$
n \cdot p = n_i^2
$$

   Despejando la concentración de electrones (minoritarios):

   

$$
n = \frac{n_i^2}{p} = \frac{(10^{10} \, \text{cm}^{-3})^2}{10^{16} \, \text{cm}^{-3}} = \frac{10^{20}}{10^{16}} = 10^4 \, \text{cm}^{-3}
$$

   El dopaje ha suprimido a los electrones por un factor de un millón (de $10^{10}$ a $10^4$).

3. **Cálculo del Desplazamiento del Nivel de Fermi:**
   Para relacionar concentraciones con los niveles de energía, usamos las distribuciones de Boltzmann relativas al nivel intrínseco $E_i$ (donde $n = p = n_i$):

   

$$
p = n_i e^{(E_i - E_F) / k_B T}
$$

   Despejando $(E_i - E_F)$:

   

$$
\frac{p}{n_i} = e^{(E_i - E_F) / k_B T} \implies \ln\left(\frac{p}{n_i}\right) = \frac{E_i - E_F}{k_B T}
$$

   

$$
E_i - E_F = k_B T \ln\left(\frac{p}{n_i}\right)
$$

   Sustituyendo los valores, sabiendo que a $T=300 \, \text{K}$, la energía térmica es $k_B T \approx 0.0259 \, \text{eV}$:

   

$$
E_i - E_F = 0.0259 \times \ln\left( \frac{10^{16}}{10^{10}} \right) = 0.0259 \times \ln(10^6)
$$

   Sabiendo que $\ln(10^6) = 6 \ln(10) \approx 6 \times 2.302 = 13.81$:

   

$$
E_i - E_F = 0.0259 \times 13.81 \approx 0.358 \, \text{eV}
$$

**Conclusión:** 
La oblea dopada es manifiestamente **Tipo-p**, con $p = 10^{16} \, \text{cm}^{-3}$ y $n = 10^4 \, \text{cm}^{-3}$. 
El nivel de Fermi del cristal ha caído drásticamente en la brecha, situándose a **0.358 eV por debajo** de su posición media intrínseca, aproximándose vertiginosamente a la banda de valencia. Esta asimetría gigantesca de portadores es el cimiento estadístico indispensable para originar los campos eléctricos de agotamiento en las uniones P-N.

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Concentración Intrínseca de Portadores $n_i$
A partir de las densidades efectivas de estados en las bandas de conducción ($N_c$) y valencia ($N_v$), derive la expresión para la concentración intrínseca de portadores $n_i$ en un semiconductor en equilibrio térmico y demuestre su dependencia exponencial con la temperatura.

**Solución paso a paso:**
En equilibrio térmico, la concentración de electrones $n$ en la banda de conducción y de huecos $p$ en la banda de valencia, usando estadística de Maxwell-Boltzmann (válida si el nivel de Fermi está al menos a $3k_B T$ del borde de banda), son:

$$
n = N_c e^{-(E_c - E_F)/k_B T}
$$

$$
p = N_v e^{-(E_F - E_v)/k_B T}
$$

donde $N_c = 2(m_e^* k_B T / 2\pi\hbar^2)^{3/2}$ y $N_v = 2(m_h^* k_B T / 2\pi\hbar^2)^{3/2}$.
El producto de estas concentraciones nos da la ley de acción de masas para semiconductores:

$$
np = N_c N_v e^{-(E_c - E_v)/k_B T}
$$

La diferencia $E_c - E_v$ es precisamente la energía del gap prohibido $E_g$.
Para un semiconductor intrínseco (sin dopar), por conservación de carga se debe cumplir que $n = p = n_i$.
Entonces $n_i^2 = n p = N_c N_v e^{-E_g/k_B T}$.
Tomando la raíz cuadrada:

$$
n_i = \sqrt{N_c N_v} e^{-E_g / 2k_B T}
$$

Dado que $N_c, N_v \propto T^{3/2}$, la concentración intrínseca varía como $T^{3/2} e^{-E_g / 2k_B T}$.
Esta fuerte dependencia exponencial domina, por lo que una pequeña variación de $T$ produce cambios de órdenes de magnitud en el número de portadores intrínsecos.

### Problema 2: Energía de Ionización de Impurezas Donadoras
Estime la energía de ionización de una impureza donadora (como fósforo) en silicio utilizando el modelo del átomo de hidrógeno de Bohr modificado para medios sólidos. ($m_e^* \approx 0.26 m_e$, $\epsilon_r \approx 11.7$).

**Solución paso a paso:**
En el modelo hidrogenoide, el electrón donado orbita alrededor del ión donador positivo incrustado en el cristal.
Utilizamos los resultados del modelo de Bohr para la energía del estado fundamental, reemplazando la masa del electrón por la masa efectiva $m_e^*$ y la permitividad del vacío $\epsilon_0$ por la permitividad del material $\epsilon = \epsilon_r \epsilon_0$.
La energía de ionización del átomo de hidrógeno en el vacío es:

$$
E_H = \frac{m_e e^4}{8 \epsilon_0^2 h^2} = 13.6 \text{ eV}
$$

Para la impureza en el cristal, la energía de ionización será:

$$
E_d = \frac{m_e^* e^4}{8 (\epsilon_r \epsilon_0)^2 h^2} = E_H \left( \frac{m_e^*}{m_e} \right) \left( \frac{1}{\epsilon_r^2} \right)
$$

Sustituyendo los valores para el Silicio:

$$
E_d = 13.6 \text{ eV} \times (0.26) \times \left( \frac{1}{11.7^2} \right)
$$

$$
E_d = 13.6 \times 0.26 \times 0.0073 \approx 0.0258 \text{ eV} \approx 25.8 \text{ meV}
$$

Esta energía ($~25$ meV) es muy cercana a la energía térmica a temperatura ambiente ($k_B T \approx 26$ meV). Por esta razón, a temperatura ambiente, casi todos los donadores en silicio están completamente ionizados, aportando un electrón libre a la banda de conducción.

### Problema 3: Potencial de Contacto en una Unión p-n
Calcule el potencial de contacto $V_0$ (built-in potential) de una unión p-n abrupta de silicio a $T = 300$ K dopada con $N_A = 10^{16} \text{ cm}^{-3}$ y $N_D = 10^{15} \text{ cm}^{-3}$. Asuma $n_i \approx 10^{10} \text{ cm}^{-3}$ y $V_T = k_B T / q \approx 25.9$ mV.

**Solución paso a paso:**
Lejos de la región de agotamiento (en las zonas neutras), las concentraciones mayoritarias son aproximadamente $p_p \approx N_A$ y $n_n \approx N_D$.
En el equilibrio, el nivel de Fermi debe ser constante en toda la estructura.
En el lado p:

$$
p_p = n_i e^{(E_i - E_{Fp}) / k_B T} \implies E_i^{(p)} - E_F = k_B T \ln\left(\frac{N_A}{n_i}\right)
$$

En el lado n:

$$
n_n = n_i e^{(E_{Fn} - E_i) / k_B T} \implies E_F - E_i^{(n)} = k_B T \ln\left(\frac{N_D}{n_i}\right)
$$

El potencial de contacto surge de la diferencia entre el nivel intrínseco $E_i$ en los dos lados. Puesto que la energía potencial es $-q V(x) = E_i(x)$, la diferencia de potencial electrostático es $V_0 = \frac{1}{q} [E_i^{(p)} - E_i^{(n)}]$.
Sumando las ecuaciones:

$$
E_i^{(p)} - E_i^{(n)} = k_B T \ln\left(\frac{N_A}{n_i}\right) + k_B T \ln\left(\frac{N_D}{n_i}\right) = k_B T \ln\left(\frac{N_A N_D}{n_i^2}\right)
$$

Entonces el potencial de contacto en voltios es:

$$
V_0 = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right)
$$

Sustituyendo los valores:

$$
V_0 = 0.0259 \ln\left(\frac{10^{16} \times 10^{15}}{(10^{10})^2}\right) = 0.0259 \ln(10^{11})
$$

Sabiendo que $\ln(10) \approx 2.303$:

$$
V_0 = 0.0259 \times 11 \times 2.303 \approx 0.656 \text{ V}
$$

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

## 🚀 Fronteras de Investigación y Problemas Abiertos

La física de semiconductores, pilar de la tecnología actual, sigue expandiéndose hacia nuevos regímenes de interacción de luz y materia y nanoestructuración.
- **Valletrónica y Espintrónica en Semiconductores 2D:** Dicalcogenuros de Metales de Transición (TMDs) como el MoS$_2$ monocapa, donde es posible manipular cuánticamente el momento angular (spin) y el momento del valle (extremos locales en las bandas) acoplándolos mediante espín-órbita.
- **Dispositivos Optoelectrónicos de Alta Eficiencia (Perovskitas):** Entender la física de recombinación de pares electrón-hueco y el rol de los polarones grandes en semiconductores híbridos de perovskitas halógenas, buscando la celda solar "perfecta" y económica.
- **Puntos Cuánticos (Quantum Dots) para Qubits de Espín:** Atrapar electrones o huecos individuales en heteroestructuras semiconductoras a bajas temperaturas, donde las interacciones hiperfinas con los espines nucleares del semiconductor son el principal mecanismo de decoherencia (y un desafío activo a superar para lograr la computación cuántica).

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

Cuando los semiconductores se miniaturizan a la escala nanométrica y operan fuera del equilibrio, la ecuación semiclásica de Boltzmann falla.

**Formalismo de Keldysh para el No-Equilibrio Cuántico:**
Para describir transporte cuántico a través de uniones túnel o puntos cuánticos, es indispensable utilizar las Funciones de Green de No Equilibrio (NEGF). En el formalismo de Keldysh, la evolución temporal requiere un contorno de integración cerrado $\mathcal{C}$ (desde $t=-\infty$ hasta $t=\infty$ y viceversa).
Las funciones de Green matriciales se organizan en la matriz de Keldysh:

$$
\mathbf{G}(1,2) = \begin{pmatrix} G^R(1,2) & G^K(1,2) \\ 0 & G^A(1,2) \end{pmatrix}
$$

Donde $G^R$ (Retardada) contiene información del espectro y la estructura de bandas, mientras que $G^K$ (Cinética/Keldysh) contiene información sobre la ocupación (función de distribución cuántica).

La corriente $I$ eléctrica estacionaria a través de una región semiconductora interactuante entre contactos $L$ y $R$ se calcula exactamante mediante la fórmula de Landauer generalizada (Fórmula de Meir-Wingreen):

$$
I = \frac{ie}{h} \int dE \, \text{Tr}\left[ \Gamma_L(E) f_L(E) - \Gamma_R(E) f_R(E) \right] \{ G^R(E) - G^A(E) \} + \text{Tr} \left[ \Gamma_L(E) G^<(E) + \text{...} \right]
$$

## 📚 Recursos Específicos

### Cursos
1. **[MIT OCW: 6.012 Microelectronic Devices and Circuits](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/)**: Excelente aproximación a la física de uniones p-n y al comportamiento del transistor MOS y bipolar, enfocada fuertemente a las ecuaciones de transporte y dopaje.
2. **[nanoHUB/Purdue: Semiconductor Devices I & II](https://nanohub.org/courses/sd1)**: Un análisis moderno, fenomenalmente animado sobre la estadística de portadores y las ecuaciones de deriva-difusión.
3. **[Stanford Online: Nanoelectronics](https://online.stanford.edu/courses/soe-yeeqn-nanoelectronics)**: Para extender la teoría del semiconductor hacia los regímenes de transporte balístico a nanoescala.

### Artículos y Simulaciones
1. **["Electron-Hole Drops in Semiconductors" por T. M. Rice (1977)](https://www.sciencedirect.com/science/article/pii/0038109877913349)**
   - **Importancia Teórica:** Describe el fenómeno de condensación en el cual, bajo alta excitación óptica y muy bajas temperaturas, el gas libre de excitones (pares electrón-hueco unidos coulombianamente) sufre una transición de fase termodinámica para formar un "líquido metálico" macroscópico análogo a gotas de agua.
   - **Fondo Matemático:** El Hamiltoniano interactuante del plasma de electrones y huecos es sometido a un análisis termodinámico. El sistema tiene una fase gas aislante a baja densidad $\rho$ y una fase líquida metálica a alta densidad $\rho_c$. La energía de la gota por par e-h se parametriza minimizando la energía en función del parámetro de densidad de radio de Wigner-Seitz $r_s$:

     

$$
E(r_s) = E_{kin}(r_s) + E_{exch}(r_s) + E_{corr}(r_s) = \frac{a}{r_s^2} - \frac{b}{r_s} + E_{corr}(r_s)
$$

     donde $E_{exch}$ es la energía de intercambio de Hartree-Fock atractiva, y $E_{corr}$ incluye correlaciones complejas (como RPA).
   - **Implicaciones Físicas:** Demuestra cómo un semiconductor puede experimentar transiciones de fase puramente gobernadas por interacciones correlacionadas electrón-electrón impulsadas ópticamente, de forma similar al modelo gas-líquido de Van der Waals.

2. **["Shockley-Queisser Limit on the Efficiency of a P-N Junction Solar Cell" (1961)](https://aip.scitation.org/doi/10.1063/1.1736034)**
   - **Importancia Teórica:** Establece el límite termodinámico máximo insuperable de eficiencia para la conversión de luz solar a electricidad utilizando una unión P-N de banda prohibida simple.
   - **Fondo Matemático:** El cálculo impone un balance detallado (equilibrio termodinámico de radiación) asumiendo el espectro de Planck $I(E, T_s)$ emitido por el Sol ($T_s \approx 6000\text{ K}$). Para un semiconductor de bandgap $E_g$, los fotones con $E < E_g$ se pierden transparentemente, y los fotones con $E > E_g$ desperdician el exceso térmicamente (termalización) bajando hasta $E_g$. La corriente máxima extraíble, suponiendo 1 electrón por fotón, es:

     

$$
J_{sc} = q \int_{E_g}^{\infty} \frac{I(E, T_s)}{E} dE
$$

     La potencia saliente, penalizada por la recombinación radiativa fundamental en el balance térmico de la celda a $T_c \approx 300\text{ K}$, genera una eficiencia termodinámica final $\eta(E_g)$:

     

$$
\eta(E_g) = \frac{V_{oc} \cdot J_{sc} \cdot FF}{P_{in}}
$$

     donde la eficiencia pico matemática arroja matemáticamente un $\approx 33.7\%$ óptimo para un semiconductor con $E_g \approx 1.34\text{ eV}$ (afortunadamente, el GaAs y el Silicio caen muy cerca de este pico radiativo).
   - **Implicaciones Físicas:** Condiciona todo el esfuerzo de ingeniería en dispositivos fotovoltaicos. Es el motivo por el cual hoy en día se buscan tecnologías multi-unión (tándem) o perovskitas superpuestas con silicio para superar este límite estricto de banda única.

3. **[nanoHUB: PN Junction Lab](https://nanohub.org/resources/pnjunction)**: Potentísimo simulador numérico que resuelve en tiempo real y tridimensionalmente las ecuaciones no lineales de Poisson acopladas a deriva-difusión (Drift-Diffusion) para obtener perfiles de bandas e intensidades de campo en interfaces.

### 📖 Referencias Útiles y Bibliografía
1. [Sze, S. M., & Ng, K. K. *Physics of Semiconductor Devices*](https://www.wiley.com/en-us/Physics+of+Semiconductor+Devices%2C+3rd+Edition-p-9780471143239) - El libro definitivo y más referenciado globalmente de la industria semiconductora.
2. [Pierret, R. F. *Semiconductor Device Fundamentals*](https://www.pearson.com/en-us/subject-catalog/p/semiconductor-device-fundamentals/P200000006764) - Texto pedagógico introductorio ideal para estadistica de portadores.

## 🌐 Seminarios Avanzados y Literatura de Frontera

- [Stanford SystemX Alliance Seminars](https://systemx.stanford.edu/) - El futuro de la tecnología de semiconductores, empaquetado 3D y materiales 2D.
- [IMEC Technology Forums](https://www.imec-int.com/en) - Charlas sobre miniaturización en los límites de litografía EUV y más allá de los transistores FinFET.
- [MIT Microsystems Technology Laboratories](https://www.mtl.mit.edu/) - Nuevos paradigmas en la física de dispositivos semiconductores nanométricos.

- [Nature: "Two-dimensional transition metal dichalcogenides for next-generation electronics"](https://www.nature.com/) - Uso de TMDs monocapa como semiconductores límite-escalado.
- [Science: "Silicon spin qubits for quantum computation"](https://www.science.org/) - Semiconductores clásicos adaptados para aislar electrones individuales como qubits.
- [Physical Review Letters: "Exciton condensation in semiconductor heterostructures"](https://journals.aps.org/prl/) - Formación de fluidos cuánticos bosónicos a partir de excitones semiconductores.
