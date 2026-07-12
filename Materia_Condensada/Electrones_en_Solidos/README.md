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

## 📚 Recursos Específicos

### Cursos
1. **[Electrons in Crystals (MIT OCW)](https://ocw.mit.edu):** Análisis profundo del teorema de Bloch.
2. **[Quantum Physics of Materials (Coursera)](https://www.coursera.org):** Introducción al gas de electrones libres.
3. **[NPTEL Electron Theory of Solids](https://nptel.ac.in):** Detalles sobre el modelo de Kronig-Penney y bandas.
4. **[Condensed Matter Theory (Stanford)](https://online.stanford.edu):** Correlaciones electrónicas avanzadas.
5. **[Many-Body Physics (Cambridge)](https://www.cam.ac.uk):** Tratamiento de sistemas interactuantes y efectos colectivos.

### Artículos y Simulaciones
1. **[nanoHUB Band Structure Lab](https://nanohub.org):** Simulador de estructuras de bandas unidimensionales y 3D.
2. **["The Free Electron Model of Metals" (Sommerfeld, original overview)](https://archive.org):** Perspectiva histórica del modelo de Drude-Sommerfeld.
3. **[Fermi Surface Viewer](http://www.xcrysden.org/):** Herramientas online (como XCrySDen) para visualizar superficies de Fermi.
4. **["Electrons in artificial lattices" (Nature)](https://www.nature.com):** Artículo sobre electrones en superredes y materiales 2D.
5. **[Quantum Espresso / PySCF Tutorials](https://www.quantum-espresso.org/):** Guías para simular electrones en cristales desde primeros principios.
6. **["Topological Band Theory" (Review of Modern Physics)](https://journals.aps.org/rmp/):** Para ir más allá del teorema de Bloch clásico.
7. **[PhET: Conductivity](https://phet.colorado.edu):** Simulación educativa sobre bandas y conductividad.
8. **[ARPES Database](https://arxiv.org):** Repositorios que muestran estructuras de bandas experimentales reales medidas con ARPES.

### 📖 Referencias Útiles y Bibliografía
1. [Ashcroft, N. W., & Mermin, N. D. *Solid State Physics*](https://archive.org) (Capítulos sobre gas de electrones y bandas).
2. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org).
3. [Simon, S. H. *The Oxford Solid State Basics*](https://global.oup.com).
4. [Marder, M. P. *Condensed Matter Physics*](https://www.wiley.com).
