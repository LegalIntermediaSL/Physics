# Superconductividad y Magnetismo

Estos fenómenos muestran cómo las interacciones microscópicas pueden producir orden colectivo macroscópico. Son ejemplos privilegiados de transición de fase y ruptura espontánea de simetría en sistemas de muchos cuerpos.

## 🧮 Desarrollo Teórico Profundo

La superconductividad y el ferromagnetismo son, en su esencia más destilada, fenómenos diametralmente excluyentes y ferozmente competitivos en la física de materia condensada. Mientras que el magnetismo busca alinear los espines electrónicos colinealmente para ganar energía de intercambio, la superconductividad BCS estándar sobrevive uniendo electrones de espines opuestos (singletes $\uparrow\downarrow$). Esta incompatibilidad engendra ricas transiciones de fase y fenómenos topológicos cuando ambos intentan coexistir microscópicamente en un material (como en los superconductores magnéticos $ErRh_4B_4$ o $UGe_2$).

### 1. Competencia y Destrucción del Estado Superconductor

Existen dos mecanismos teóricos principales por los cuales el magnetismo aniquila a la superconductividad singlete estándar:

**El Efecto Orbital (Límite Meissner):**
Un campo magnético externo ($\mathbf{H}$) interacciona geométricamente con los momentos orbitales de los electrones mediante las fuerzas de Lorentz. El superconductor gasta energía en mantener corrientes superficiales de apantallamiento para cancelar $\mathbf{B}$ en su interior ($\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M}) = 0 \implies \mathbf{M} = -\mathbf{H}$).
La termodinámica requiere que el aumento de la energía libre magnética no supere a la energía de condensación estabilizadora del estado BCS. Cuando el campo aplicado $H$ supera un límite termodinámico crítico, se vuelve energéticamente favorable abortar la fase Meissner, romper los pares y que el material reingrese al estado normal permeable.
$$ \Delta G_{mag} = \frac{1}{2} \mu_0 H_c^2 \equiv E_{condensacion} \implies H_c = \sqrt{\frac{2 \mu_0}{V_c} E_{cond}} $$
Para superconductores Tipo II, las ecuaciones de Ginzburg-Landau demuestran que en lugar de destruirse uniformemente, el material permite la penetración parcial y cuantizada del campo a través de la formación de una Red de Vórtices de Abrikosov, sobreviviendo así hasta campos formidables $H_{c2}$.

**El Efecto Paramagnético de Pauli (Límite de Clogston-Chandrasekhar):**
Este mecanismo microscópico no concierne al movimiento orbital, sino estrictamente a la energía Zeeman de los espines. Un campo magnético penetrante interactúa de manera desigual con los espines del par de Cooper ($\uparrow$ y $\downarrow$).
La energía del estado antiparalelo no se altera promedialmente, pero en el estado normal, los electrones pueden polarizarse todos "spin-up" para ganar energía Zeeman ($\Delta E_{Z} = \mu_B B$). Si la ganancia de energía Zeeman térmica de los electrones normales iguala o supera la brecha atractiva emparejadora $\Delta_0$ (gap superconductor a T=0), el par se rompe catastróficamente por desalineación de momentos.
El campo crítico superior estricto impuesto por la ruptura de par de Pauli es:
$$ \mu_B B_p = \frac{\Delta_0}{\sqrt{2}} \implies B_p(T=0) \approx 1.84 \, T_c \, [\text{Tesla/Kelvin}] $$

### 2. Parámetro de Orden de Ginzburg-Landau Acoplado

Para modelar matemáticamente los dominios donde el ferromagnetismo y la superconductividad chocan, el fenomenalismo de Landau se expande introduciendo dos parámetros de orden coexistentes: $\Psi(\mathbf{r})$ (la densidad coherente de pares de Cooper) y $\mathbf{M}(\mathbf{r})$ (el vector de magnetización local).
El funcional de Energía Libre $F[\Psi, \mathbf{M}]$ añade las contribuciones individuales y un término heurístico de interacción magnetoestática e intercambio:

$$ F = \int d^3r \Big[ \alpha_\Psi |\Psi|^2 + \frac{\beta_\Psi}{2}|\Psi|^4 + \frac{1}{2m^*} |(\nabla - i \frac{2e}{\hbar c}\mathbf{A})\Psi|^2 + \alpha_M M^2 + \frac{\beta_M}{2}M^4 + \gamma (\nabla \mathbf{M})^2 + \eta |\Psi|^2 M^2 \Big] $$

El término de acoplamiento biquadrático $\eta |\Psi|^2 M^2$ (con $\eta > 0$ por la fuerte repulsión repulsiva entre estados) dicta que es energéticamente prohibitivo que ambos parámetros de orden sean simultáneamente grandes en el mismo espacio. Las ecuaciones de minimización ($\delta F = 0$) derivan en complejas soluciones oscilatorias, previendo estados intermedios estriados donde el material intercala espontáneamente dominios nanométricos magnéticos y superconductores (Fase Criptomagnética).

### Diagrama: Efectos Antagónicos y Exotismo Topológico

```mermaid
graph TD
    A{Electrones en el <br> Mar de Fermi} -->|Atracción por Fonones| B[Singlete de Pares Cooper<br>Superconductividad]
    A -->|Interacción de Intercambio| C[Alineación Colineal<br>Ferromagnetismo]
    
    B -->|Genera Efecto Meissner| D(Expulsa H_interno)
    C -->|Genera Magnetización| E(Crea H_interno)
    D -. Choque Físico Directo .-> E
    
    E -->|1. Ruptura de Pauli<br>Zeeman Spin Splitting| B
    E -->|2. Ruptura Orbital<br>Fuerza de Lorentz| B
    
    B -. Materiales Exóticos <br> p-wave / Triplete .-> F[Superconductividad Ferromagnética<br>Pares Cooper con Espín S=1]
    
    style B fill:#219ebc,stroke:#fff,color:#fff
    style C fill:#d62828,stroke:#fff,color:#fff
    style F fill:#9d4edd,stroke:#fff,color:#fff
```

## 🛠 Ejemplo Práctico

**Problema:** Un nuevo superconductor candidato de baja temperatura (Nb-X) tiene una temperatura crítica puramente medida de $T_c = 4.2 \, \text{K}$. Al fabricar películas ultradelgadas donde el campo magnético puede ser puramente paralelo a la película (minimizando el efecto Meissner orbital), los experimentalistas logran observar la destrucción de la fase superconductora dictada enteramente por el límite paramagnético de Pauli a $0\,K$.
Utilice la ley de Clogston-Chandrasekhar para calcular teóricamente la intensidad del campo magnético crítico de Pauli $B_p$ requerido para destruir los pares singlete. Si el material estuviese dopado con átomos magnéticos de forma que produzcan internamente un campo microscópico efectivo de intercambio equivalente a $2.5 \, \text{T}$, ¿sobreviviría la superconductividad a temperaturas por debajo de $T_c$?

**Solución paso a paso:**

1. **Estimación del Gap de BCS:**
   Para calcular el límite teórico, primero determinamos la brecha de energía superconductora en el cero absoluto ($\Delta_0$). Empleamos la universalidad BCS para un acoplamiento débil de electrones-fonones:
   $$ 2\Delta_0 = 3.52 k_B T_c \implies \Delta_0 = 1.76 k_B T_c $$
   Usando $k_B \approx 8.617 \times 10^{-5} \, \text{eV/K}$:
   $$ \Delta_0 = 1.76 \times (8.617 \times 10^{-5}) \times 4.2 \approx 6.37 \times 10^{-4} \, \text{eV} = 0.637 \, \text{meV} $$

2. **Cálculo del Límite Paramagnético Crítico (Pauli-Clogston):**
   La condición física establece que la superconductividad se extingue cuando la ganancia energética de orientar un espín electrón al campo (Energía Zeeman $\mu_B B$) iguala a la energía necesaria para quebrar el par estabilizado por la brecha de energía, ajustado por la termodinámica de la superficie de Fermi normal ($1/\sqrt{2}$ de diferencia en energías libres):
   $$ \mu_B B_p = \frac{\Delta_0}{\sqrt{2}} $$
   Con el magnetón de Bohr $\mu_B \approx 5.788 \times 10^{-5} \, \text{eV/T}$ y $\sqrt{2} \approx 1.414$:
   $$ B_p = \frac{6.37 \times 10^{-4} \, \text{eV}}{\sqrt{2} \times 5.788 \times 10^{-5} \, \text{eV/T}} \approx \frac{6.37}{1.414 \times 0.5788} \approx \frac{6.37}{0.818} \approx 7.78 \, \text{Tesla} $$
   *(Alternativamente, la fórmula empírica directa establece $B_p \approx 1.84 \, T_c = 1.84 \times 4.2 \approx 7.73 \, \text{T}$, muy concordante dadas las diferencias de redondeo).*

3. **Análisis de Coexistencia del Dopaje:**
   El campo destructivo molecular interno aportado por las impurezas magnéticas es $B_{int} = 2.5 \, \text{T}$.
   Comparamos este campo con la tenacidad magnética del material calculada ($B_p \approx 7.78 \, \text{T}$).
   Como $B_{int} = 2.5 \, \text{T} < B_p = 7.78 \, \text{T}$, el campo efectivo de la magnetización no es lo suficientemente potente como para reventar todos los pares de Cooper mediante Zeeman splitting.

**Conclusión Física:** El material Nb-X ultradelgado sí **sostendrá la fase de superconductividad coexistente** a pesar del entorno fuertemente magnético que lo permea en el bulk. Este es el principio rector para diseñar ciertos "superconductores de aleación pesada" que soportan simultáneamente flujos de intercambio ferromagnéticos y supercorrientes bosónicas a muy bajas temperaturas.

## 📚 Recursos Específicos

### Cursos
1. **[Interplay of Magnetism and Superconductivity (NPTEL advanced)](https://nptel.ac.in):** Análisis de cómo el magnetismo normalmente destruye la superconductividad y excepciones notables.
2. **[Strongly Correlated Electron Systems (MIT OCW)](https://ocw.mit.edu):** Curso avanzado sobre fermiones pesados donde coexisten ambas fases.
3. **[Quantum Phase Transitions (Coursera / edX)](https://www.coursera.org):** Teoría de transiciones cuánticas en el cero absoluto entre estados magnéticos y superconductores.
4. **[Advanced Solid State Physics (Cambridge)](https://www.cam.ac.uk):** Discusión sobre simetrías rotas.
5. **[Unconventional Superconductors (Oxford lectures)](https://www.ox.ac.uk):** Estudio de casos donde las fluctuaciones magnéticas median los pares de Cooper.

### Artículos y Simulaciones
1. **["Coexistence of superconductivity and magnetism" (Review of Modern Physics)](https://journals.aps.org/rmp/):** Artículo comprensivo sobre sistemas donde ambos fenómenos ocurren simultáneamente.
2. **["Magnetic Fluctuations in High-Tc Cuprates" (Nature Physics)](https://www.nature.com):** Sobre el origen magnético de los superconductores de alta temperatura.
3. **[MuSR (Muon Spin Rotation) virtual labs](https://www.psi.ch/en/lmu):** Técnicas experimentales para detectar magnetismo en materiales superconductores.
4. **["Ferromagnetic Superconductors" (UGe2, URhGe, etc.)](https://arxiv.org):** Literatura sobre materiales muy peculiares que combinan ambos mundos de forma cooperativa.
5. **[SQUIDs simulators (Falstad / Python)](https://www.falstad.com/circuit/):** Interacción práctica entre un dispositivo superconductor y flujos magnéticos muy débiles.
6. **["Majorana Fermions in Condensed Matter" (Alicea, ROP)](https://arxiv.org):** Sobre cómo la combinación de un campo magnético y un superconductor (con acoplamiento espín-órbita) da lugar a estos estados exóticos.
7. **[Simulación de vórtices magnéticos en superconductores](https://github.com):** Herramientas GL para ver campos penetrando en forma de líneas de flujo (vórtices de Abrikosov).
8. **["Spin-Triplet Superconductivity" (Physics Today)](https://physicstoday.scitation.org):** Cuando los pares de Cooper se forman con espines paralelos.

### 📖 Referencias Útiles y Bibliografía
1. [Tinkham, M. *Introduction to Superconductivity*](https://store.doverpublications.com).
2. [Blundell, S. *Magnetism in Condensed Matter*](https://global.oup.com).
3. [Annett, J. F. *Superconductivity, Superfluids and Condensates*](https://global.oup.com). Oxford University Press.
4. [Kittel, C. *Introduction to Solid State Physics*](https://archive.org).
5. [Sachdev, S. *Quantum Phase Transitions*](https://www.cambridge.org). Cambridge University Press.
