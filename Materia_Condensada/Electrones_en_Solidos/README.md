# Electrones en Sólidos

En un sólido, los electrones no se comportan como partículas aisladas. La periodicidad del cristal y las interacciones colectivas modifican drásticamente su dinámica y originan fenómenos como conducción, aislación, magnetismo y efectos cuánticos colectivos.

## 🧮 Desarrollo Teórico Profundo

El comportamiento de los electrones en un sólido define si un material es metálico, semiconductor, aislante o superconductor. El avance teórico en el siglo XX pasó de tratar a los electrones como un gas clásico (Drude), a un gas cuántico (Sommerfeld), y finalmente a partículas en potenciales periódicos que dan lugar a las bandas de energía (Bloch).

### 1. El Gas de Electrones Libres de Sommerfeld

En un metal, los electrones de valencia se deslocalizan formando un "gas" cuántico de fermiones confinados en una caja de volumen $V=L^3$, ignorando el potencial iónico local periódico.

Debido al principio de exclusión de Pauli y a las condiciones de contorno periódicas de Born-von Karman ($\psi(x+L, y, z) = \psi(x, y, z)$), los estados permitidos de los vectores de onda $\mathbf{k}$ están cuantizados:

$$ \mathbf{k} = \left( \frac{2\pi n_x}{L}, \frac{2\pi n_y}{L}, \frac{2\pi n_z}{L} \right) \quad \text{con } n_i \in \mathbb{Z} $$

Cada estado $\mathbf{k}$ ocupa un volumen $(2\pi/L)^3 = 8\pi^3/V$ en el espacio recíproco. A $T=0$, los electrones llenan los estados de menor energía (desde $k=0$) hasta un momento máximo $k_F$, formando una esfera en el espacio $\mathbf{k}$ conocida como **Esfera de Fermi**.
El número total de electrones $N$ (teniendo en cuenta la degeneración de espín de 2) es el volumen de la esfera dividido por el volumen por estado:

$$ N = 2 \frac{\frac{4}{3}\pi k_F^3}{8\pi^3/V} = \frac{V}{3\pi^2} k_F^3 $$

De aquí derivamos el vector de onda de Fermi $k_F$ en función de la densidad electrónica $n = N/V$:

$$ k_F = (3\pi^2 n)^{1/3} $$

La **Energía de Fermi** (energía cinética máxima a temperatura cero) es inmensa en los metales típicos (del orden de electronvoltios, equivalentes a decenas de miles de Kelvin):

$$ E_F = \frac{\hbar^2 k_F^2}{2m_e} = \frac{\hbar^2}{2m_e} (3\pi^2 n)^{2/3} $$

### 2. Potenciales Periódicos y el Teorema de Bloch

La aproximación del gas libre no puede explicar por qué el diamante (carbono) es un aislante transparente mientras que el grafito (carbono) es conductor opaco. Para resolver esto, debemos incluir la interacción de los electrones con la red periódica de iones.

El Hamiltoniano de un solo electrón es $H = \frac{p^2}{2m} + U(\mathbf{r})$, donde $U(\mathbf{r}) = U(\mathbf{r} + \mathbf{R})$ para cualquier vector de la red de Bravais $\mathbf{R}$.
El **Teorema de Bloch** garantiza que las soluciones $\psi(\mathbf{r})$ pueden elegirse con la forma de una onda plana modulada por la periodicidad de la red:

$$ \psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}) $$

donde $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{n\mathbf{k}}(\mathbf{r})$.
La consecuencia más revolucionaria es que si un electrón se encuentra en un estado de Bloch, el potencial periódico de los iones *no causa dispersión* (scattering) en absoluto. Un electrón en un cristal perfecto sin defectos ni vibraciones (fonones a $T=0$) tiene un camino libre medio infinito: la resistividad residual se debe únicamente a las imperfecciones cristalinas.

### 3. Modelo de Electrón Casi Libre y Origen de la Brecha de Banda

Si el potencial periódico $U(\mathbf{r})$ es débil, podemos aplicar la teoría de perturbaciones cuántica. Expandimos $U(\mathbf{r})$ en la red recíproca:

$$ U(\mathbf{r}) = \sum_{\mathbf{G}} U_{\mathbf{G}} e^{i\mathbf{G}\cdot\mathbf{r}} $$

Para un estado con vector de onda $\mathbf{k}$, la teoría de perturbaciones no degenerada establece que las correcciones a la energía $E^{(0)}(\mathbf{k}) = \hbar^2 k^2/2m$ de la partícula libre provienen del acoplamiento con estados desplazados en un vector recíproco $\mathbf{k} - \mathbf{G}$.
Cuando la energía de los estados acoplados coincide, es decir, $E^{(0)}(\mathbf{k}) \approx E^{(0)}(\mathbf{k} - \mathbf{G})$, la teoría no degenerada falla. Esto sucede exactamente en los planos que bisecan los vectores $\mathbf{G}$, formando las **Zonas de Brillouin**.

En los límites de la Zona de Brillouin ($|\mathbf{k}| = |\mathbf{k} - \mathbf{G}|$, que equivale a $\mathbf{k} \cdot \mathbf{G} = G^2/2$), ocurre difracción de Bragg interna. Las ondas viajeras $e^{i\mathbf{k}\cdot\mathbf{r}}$ y $e^{i(\mathbf{k}-\mathbf{G})\cdot\mathbf{r}}$ se acoplan fuertemente creando ondas estacionarias.
Existen dos superposiciones lineales posibles: $\psi_+ \propto \cos(\pi x / a)$ y $\psi_- \propto \sin(\pi x / a)$. 
La onda coseno acumula densidad electrónica $| \psi_+ |^2$ sobre los núcleos atómicos (donde el potencial atractivo de los iones es fuerte, bajando la energía). La onda seno tiene nodos sobre los átomos, acumulando densidad en el espacio intersticial (subiendo la energía).

Esta diferencia de energía de interacción es la que "rompe" la parábola continua del electrón libre, abriendo una **Brecha de Banda (Band Gap)** de magnitud $E_g = 2|U_{\mathbf{G}}|$. Ningún estado electrónico puede existir con energías dentro del gap en el bulto del cristal.

### Diagrama: Brechas de Energía

```mermaid
graph TD
    A[Potencial Periódico Débil] --> B{Teoría Perturbativa}
    B -->|Lejos frontera Brillouin| C[Fermiones Libres<br>E ~ k^2]
    B -->|Borde de Zona de Brillouin<br>k = &pi;/a| D[Difracción de Bragg<br>Ondas Estacionarias]
    D --> E[Banda de Valencia<br>Menor Energía, Nodos Intersticiales]
    D --> F[Banda de Conducción<br>Mayor Energía, Nodos sobre Iones]
    E -.->|Gap de Energía E_g = 2|U_G|| F
    
    style C fill:#457b9d,stroke:#fff,color:#fff
    style E fill:#2a9d8f,stroke:#fff,color:#fff
    style F fill:#e76f51,stroke:#fff,color:#fff
```

## 🛠 Ejemplo Práctico

**Problema:** Calcule la Energía de Fermi $E_F$ y la temperatura de Fermi $T_F$ del Cobre metálico, asumiendo el modelo de gas de electrones libres. Sabiendo que el cobre cristaliza en una red FCC con un parámetro de red $a = 3.61 \, \text{Å}$ y proporciona un electrón de valencia por átomo a la banda de conducción.

**Solución paso a paso:**

1. **Cálculo de la Densidad Electrónica ($n$):**
   Una celda unitaria de la red FCC contiene exactamente 4 átomos.
   Puesto que cada átomo aporta un electrón libre de conducción ($Z=1$), el número de electrones de conducción por celda unitaria es 4.
   El volumen de la celda unitaria es $V_c = a^3$.
   $$ n = \frac{\text{electrones}}{\text{volumen}} = \frac{4}{a^3} $$
   Convirtiendo el parámetro de red a metros: $a = 3.61 \times 10^{-10} \, \text{m}$.
   $$ n = \frac{4}{(3.61 \times 10^{-10})^3} \approx \frac{4}{4.704 \times 10^{-29}} \approx 8.50 \times 10^{28} \, \text{m}^{-3} $$

2. **Cálculo del Vector de Onda de Fermi ($k_F$):**
   $$ k_F = (3 \pi^2 n)^{1/3} $$
   $$ k_F = (3 \pi^2 \times 8.50 \times 10^{28})^{1/3} = (2.518 \times 10^{30})^{1/3} \approx 1.36 \times 10^{10} \, \text{m}^{-1} $$

3. **Cálculo de la Energía de Fermi ($E_F$):**
   Usando la masa del electrón en reposo $m_e = 9.11 \times 10^{-31} \, \text{kg}$ y $\hbar = 1.055 \times 10^{-34} \, \text{J}\cdot\text{s}$:
   $$ E_F = \frac{\hbar^2 k_F^2}{2 m_e} = \frac{(1.055 \times 10^{-34})^2 (1.36 \times 10^{10})^2}{2 \times 9.11 \times 10^{-31}} $$
   $$ E_F = \frac{(1.11 \times 10^{-68}) (1.85 \times 10^{20})}{1.822 \times 10^{-30}} \approx \frac{2.05 \times 10^{-48}}{1.822 \times 10^{-30}} \approx 1.125 \times 10^{-18} \, \text{J} $$
   Convirtiendo a electrón-voltios ($1 \, \text{eV} = 1.602 \times 10^{-19} \, \text{J}$):
   $$ E_F (\text{eV}) = \frac{1.125 \times 10^{-18}}{1.602 \times 10^{-19}} \approx 7.02 \, \text{eV} $$

4. **Cálculo de la Temperatura de Fermi ($T_F$):**
   La temperatura equivalente es aquella donde la energía térmica iguala a la energía de Fermi:
   $$ T_F = \frac{E_F}{k_B} = \frac{1.125 \times 10^{-18}}{1.38 \times 10^{-23}} \approx 81,500 \, \text{K} $$

**Conclusión:** La Energía de Fermi en el Cobre es de 7.02 eV, lo cual corresponde a una colosal temperatura termodinámica de más de ochenta mil grados Kelvin. Debido a que a temperatura ambiente ($T \sim 300 \, \text{K}$) se cumple que $T \ll T_F$, el gas electrónico en metales es un gas de fermiones altamente degenerado cuánticamente. Las excitaciones térmicas apenas afectan a los electrones en la base de la banda; sólo los electrones cercanos a la superficie de Fermi pueden absorber calor o conducir electricidad.

## 📝 Guía de Ejercicios Resueltos

### Problema 1: Energía de Fermi para un Gas de Electrones Libres en 3D
Determine la expresión analítica para la energía de Fermi $E_F$ de un gas tridimensional de $N$ electrones libres confinados en un volumen $V$. 

**Solución paso a paso:**
La densidad de estados en el espacio de momento (espacio k) para un volumen tridimensional es constante, dada por $\frac{V}{(2\pi)^3}$.
El número total de estados permitidos dentro de una esfera de radio $k_F$ (vector de onda de Fermi) considerando la degeneración de espín (2 electrones por estado k) es:
$$ N = 2 \frac{V}{(2\pi)^3} \int_0^{k_F} 4\pi k^2 dk = \frac{V}{\pi^2} \frac{k_F^3}{3} $$
Despejando $k_F$ en función de la densidad electrónica $n = N/V$:
$$ k_F = (3\pi^2 n)^{1/3} $$
La energía de Fermi es la energía cinética correspondiente a $k_F$:
$$ E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3} $$
Esta es la energía máxima ocupada a temperatura $T=0$ K, un resultado puramente cuántico que surge del Principio de Exclusión de Pauli.

### Problema 2: Densidad de Estados (DOS) en un Gas Bidimensional (2D)
Demuestre que la densidad de estados en energía, $g(E)$, para un gas de electrones libres confinado estrictamente a dos dimensiones de área $A$ es constante respecto a la energía.

**Solución paso a paso:**
En 2D, el número total de estados con vector de onda menor que $k$ es:
$$ N(k) = 2 \times \frac{A}{(2\pi)^2} \times (\pi k^2) = \frac{A k^2}{2\pi} $$
Para electrones libres, la energía isotrópica es $E = \frac{\hbar^2 k^2}{2m}$. Despejamos $k^2$:
$$ k^2 = \frac{2m E}{\hbar^2} $$
Sustituyendo en $N(k)$ obtenemos el número de estados con energía menor que $E$:
$$ N(E) = \frac{A}{2\pi} \left( \frac{2m E}{\hbar^2} \right) = \frac{A m E}{\pi \hbar^2} $$
La densidad de estados $g(E)$ se define como la derivada del número total de estados respecto a la energía:
$$ g(E) = \frac{dN(E)}{dE} = \frac{A m}{\pi \hbar^2} $$
Como vemos, $g(E)$ es una constante independiente de $E$ (una función escalón si consideramos el fondo del pozo $E_0$).

### Problema 3: Capacidad Calorífica del Gas de Electrones Libres
En el modelo de Sommerfeld, demuestre por qué la contribución electrónica a la capacidad calorífica de un metal a bajas temperaturas es lineal respecto a $T$, es decir, $C_v \propto T$.

**Solución paso a paso:**
A temperatura $T > 0$, sólo los electrones cercanos a la energía de Fermi (dentro de una ventana térmica $\sim k_B T$) pueden ser excitados a estados vacíos superiores, porque los de menor energía están bloqueados por el principio de Pauli.
La fracción de electrones que participan en las excitaciones térmicas es proporcional a $\frac{k_B T}{E_F}$.
Cada electrón excitado aumenta su energía térmica en aproximadamente $\sim k_B T$.
Por lo tanto, la energía interna térmica adicional total del sistema de $N$ electrones es:
$$ \Delta U \approx N \left( \frac{k_B T}{E_F} \right) k_B T = \frac{N k_B^2 T^2}{E_F} $$
La capacidad calorífica electrónica a volumen constante es la derivada respecto a $T$:
$$ C_v = \frac{\partial U}{\partial T} \approx 2 \frac{N k_B^2}{E_F} T $$
Haciendo el tratamiento riguroso con la integral de Fermi-Dirac, la constante exacta es:
$$ C_v = \frac{\pi^2}{2} \frac{N k_B^2}{E_F} T \equiv \gamma T $$
Esto demuestra que el calor específico electrónico decae a cero de forma lineal con $T$ para $T \to 0$.

## 💻 Simulaciones Computacionales

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_fermi_dirac():
    E = np.linspace(0.1, 10, 500)
    E_F = 5.0 # Fermi energy in eV
    k_B = 8.617e-5 # eV/K
    
    plt.figure(figsize=(10, 6))
    for T in [0, 300, 1000, 3000]:
        if T == 0:
            f = np.where(E <= E_F, 1.0, 0.0)
        else:
            f = 1 / (np.exp((E - E_F) / (k_B * T)) + 1)
        plt.plot(E, f, label=f'T = {T} K')
        
    plt.axvline(E_F, color='k', linestyle='--', label='$E_F$')
    plt.xlabel('Energía (eV)')
    plt.ylabel('Probabilidad de Ocupación $f(E)$')
    plt.title('Simulación: Distribución de Fermi-Dirac a varias Temperaturas')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plot_fermi_dirac()
```

## 🚀 Fronteras de Investigación y Problemas Abiertos

El estudio de los electrones en sólidos ha derivado hacia el estudio de sistemas altamente correlacionados, donde la aproximación de electrones independientes falla catastróficamente.
- **Materiales de Moiré y Twistrónica:** Al apilar capas de grafeno (o dicalcogenuros de metales de transición) con un "ángulo mágico", los electrones experimentan bandas casi planas. El origen exacto de la superconductividad y de los estados aislantes correlacionados en estos sistemas es una de las fronteras más ardientes de la física cuántica actual.
- **Líquidos No-Fermi:** En ciertos materiales, como los fermiones pesados o cupratos en la fase "strange metal", la descripción de los electrones como cuasipartículas del líquido de Fermi de Landau colapsa. La resistividad escala linealmente con la temperatura ($\rho \propto T$), y encontrar una teoría general para estos líquidos no-Fermi, posiblemente vinculada a la dualidad holográfica (AdS/CFT), es un problema abierto.
- **Fases Topológicas Fuertemente Correlacionadas:** Más allá de los aislantes topológicos no interactuantes, la física de hoy busca comprender fases como los Aislantes Topológicos Fraccionarios y sistemas con excitaciones anyónicas que podrían servir para computación cuántica topológica.

## 📐 Formalismo Matemático Avanzado (Nivel Posgrado/Doctorado)

En regímenes de fuerte correlación, el formalismo hamiltoniano estándar se reemplaza a menudo por teorías cuánticas de campos y formulaciones de integral de camino.

**Integrales de Camino y Funciones de Green (Teoría de Muchos Cuerpos):**
La función de partición gran canónica de un gas de electrones interactuantes se expresa como una integral funcional sobre campos de Grassmann $\psi, \bar{\psi}$:
$$ \mathcal{Z} = \int \mathcal{D}[\bar{\psi}, \psi] \exp\left( -S[\bar{\psi}, \psi] \right) $$
Donde la acción de Matsubara en tiempo imaginario $\tau = it$ (con $\beta = 1/k_B T$) es:
$$ S = \int_0^\beta d\tau \int d^3x \left[ \bar{\psi}_\sigma \left( \partial_\tau - \frac{\nabla^2}{2m} - \mu \right) \psi_\sigma + \frac{1}{2} \int d^3x' \, V(|\mathbf{x} - \mathbf{x}'|) \bar{\psi}_\sigma(\mathbf{x}) \bar{\psi}_{\sigma'}(\mathbf{x}') \psi_{\sigma'}(\mathbf{x}') \psi_\sigma(\mathbf{x}) \right] $$

Para tratar el "Líquido No-Fermi", se hace uso de teorías de campo gauge efectivas acopladas a la materia, donde las cuasipartículas fermiónicas se acoplan a bosones mediadores (p. ej., fluctuaciones magnéticas) con un acoplamiento singular. La función de Green vestida $G(k, \omega)$ diverge de su polo cuasiparticular estándar, teniendo la forma:
$$ G^{-1}(\mathbf{k}, \omega) = \omega - v_F(k - k_F) - \Sigma(\mathbf{k}, \omega) $$
Donde la autoenergía (self-energy) $\Sigma \sim -i |\omega|^\alpha$ (con $\alpha < 1$) destruye el concepto de cuasipartícula.

## 📚 Recursos Específicos

### Cursos
1. **[MIT OCW: 8.231 Physics of Solids I](https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/)**: Aborda de manera analítica la teoría de Sommerfeld, el teorema de Bloch y el origen de las estructuras de bandas de energía en sólidos periódicos.
2. **[Stanford Online: Quantum Mechanics for Scientists and Engineers](https://online.stanford.edu/courses/soe-yeeqm-quantum-mechanics-scientists-and-engineers)**: Proporciona las bases fundamentales de mecánica cuántica necesarias para comprender los estados de los electrones en potenciales periódicos.
3. **[NPTEL: Solid State Physics](https://nptel.ac.in/courses/115105099)**: Detalles exhaustivos sobre el modelo de Kronig-Penney y dinámica de electrones casi libres.

### Artículos y Simulaciones
1. **["The Band Theory of Graphite" por P. R. Wallace (1947)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.71.622)**
   - **Importancia Teórica:** Fue el primer cálculo teórico de la estructura de bandas del grafeno y grafito utilizando el método de enlace fuerte (tight-binding). Es fundamental por haber predicho los puntos de Dirac 60 años antes del aislamiento experimental del grafeno.
   - **Fondo Matemático:** El Hamiltoniano de amarre fuerte considerando vecinos más cercanos sobre la red de panal de abeja (que contiene dos subredes, A y B) se formula como una matriz $2 \times 2$. Los valores propios de energía para los electrones $\pi$ están dados por:
     $$ E(\mathbf{k}) = \pm \gamma_0 \sqrt{1 + 4\cos\left(\frac{\sqrt{3} k_x a}{2}\right)\cos\left(\frac{k_y a}{2}\right) + 4\cos^2\left(\frac{k_y a}{2}\right)} $$
     En las esquinas de la zona de Brillouin (los puntos $K$ y $K'$), la dispersión de energía se vuelve lineal respecto al momento cristalino $\mathbf{q} = \mathbf{k} - \mathbf{K}$:
     $$ E(\mathbf{q}) \approx \pm \hbar v_F |\mathbf{q}| $$
     donde $v_F$ es la velocidad de Fermi (aproximadamente $10^6 \text{ m/s}$).
   - **Implicaciones Físicas:** Demostró que los electrones en el grafeno obedecen la ecuación relativista de Dirac en lugar de la ecuación de Schrödinger no relativista, actuando como fermiones de Dirac sin masa. Esto tiene profundas implicaciones en la conductividad balística del material.

2. **["Colloquium: Topological insulators" por M. Z. Hasan y C. L. Kane (2010)](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.82.3045)**
   - **Importancia Teórica:** Artículo fundacional que unifica la topología con la teoría de bandas clásica. Introduce los materiales aislantes topológicos que son aislantes en su interior pero conductores perfectos en su superficie.
   - **Fondo Matemático:** La estructura topológica se caracteriza por el invariante topológico de Chern (para el efecto Hall cuántico) o el invariante $\mathbb{Z}_2$ (para sistemas con simetría de inversión temporal). La curvatura de Berry $\mathbf{\Omega}(\mathbf{k})$ de una banda de Bloch $|u_{n\mathbf{k}}\rangle$ se define como:
     $$ \mathbf{\Omega}_n(\mathbf{k}) = i \langle \nabla_{\mathbf{k}} u_{n\mathbf{k}} | \times | \nabla_{\mathbf{k}} u_{n\mathbf{k}} \rangle $$
     El número de Chern $C_n$, que debe ser un entero invariante, se obtiene integrando sobre toda la primera zona de Brillouin (BZ):
     $$ C_n = \frac{1}{2\pi} \int_{\text{BZ}} d^2k \, \Omega_{n,z}(\mathbf{k}) $$
   - **Implicaciones Físicas:** Concluye que la presencia de estados de superficie metálicos (y fuertemente polarizados en espín) está topológicamente protegida contra el desorden, las impurezas y las perturbaciones suaves, ofreciendo una ruta hacia una espintrónica robusta y la computación cuántica tolerante a fallos.

3. **[nanoHUB: Band Structure Lab](https://nanohub.org/resources/bandstr)**: Herramienta de simulación de alta calidad que permite visualizar y calcular estructuras de bandas electrónicas en sólidos utilizando diferentes modelos de masa y potenciales periódicos.

### 📖 Referencias Útiles y Bibliografía
1. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://www.cengage.com/c/solid-state-physics-1e-ashcroft/9780030839931/) - Un tratamiento insuperable para la fenomenología del gas de electrones.
2. [Kittel, C. *Introduction to Solid State Physics* (8va ed.)](https://www.wiley.com/en-us/Introduction+to+Solid+State+Physics%2C+8th+Edition-p-9780471415268) - Excelente abordaje introductorio al modelo de Kronig-Penney.
