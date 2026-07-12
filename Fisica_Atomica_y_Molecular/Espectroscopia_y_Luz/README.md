# Espectroscopia y Luz

La espectroscopia es el estudio de la interacción entre la radiación electromagnética y la materia, fundamental para determinar la estructura y la dinámica de átomos y moléculas.

## 📜 Contexto Histórico

En el siglo XIX, Fraunhofer descubrió líneas oscuras en el espectro solar (Líneas de Fraunhofer). Bunsen y Kirchhoff demostraron en 1859 que cada elemento emite y absorbe luz en longitudes de onda específicas. En 1916, Albert Einstein sentó las bases para el láser mediante su teoría de los coeficientes $A$ y $B$ para emisión espontánea y estimulada.

## 🧮 Desarrollo Teórico Profundo

La interacción de un átomo con un campo electromagnético se trata comúnmente en la **Aproximación Dipolar Eléctrica**. La perturbación armónica dependiente del tiempo es:

$$ \hat{H}'(t) = - \mathbf{d} \cdot \mathbf{E}(t) = -e \mathbf{r} \cdot \mathbf{E_0} \cos(\omega t) $$

Donde $\mathbf{d} = e\mathbf{r}$ es el operador de momento dipolar eléctrico. La probabilidad de transición de un estado $|i\rangle$ a un estado $|f\rangle$ está dada por la **Regla de Oro de Fermi**:

$$ W_{i \rightarrow f} = \frac{2\pi}{\hbar} | \langle f | \hat{H}' | i \rangle |^2 \rho(E_f) $$

Las transiciones sólo están permitidas si el elemento de matriz del dipolo no es cero:
$$ \langle f | \mathbf{r} | i \rangle \neq 0 $$

Esto da lugar a las **Reglas de Selección** para transiciones dipolares eléctricas (por ejemplo, para el átomo de H):
- $\Delta l = \pm 1$ (cambio de paridad necesario).
- $\Delta m_l = 0, \pm 1$.

**Efecto Zeeman:**
En presencia de un campo magnético externo $\mathbf{B}$, los niveles de energía atómicos se desdoblan debido a la interacción del momento magnético total del átomo $\boldsymbol{\mu}$ con el campo. El hamiltoniano de perturbación es $\hat{H}_B = -\boldsymbol{\mu} \cdot \mathbf{B}$. El desplazamiento energético en el límite de campo débil es:

$$ \Delta E = \mu_B g_J m_J B $$

Donde $\mu_B$ es el magnetón de Bohr, $m_J$ es el número cuántico magnético total y $g_J$ es el factor g de Landé.

## 🛠 Ejemplo Práctico

**Problema:** Calcular el desdoblamiento de energía (efecto Zeeman normal, espín cero o estado singlete con $S=0$, por lo que $J=L$, $g_J=1$) del nivel $2p$ ($l=1$) de un átomo colocado en un campo magnético externo de $B = 1 \, \text{T}$.

**Solución paso a paso:**

1. Para $l=1$, los valores de $m_l$ (o $m_J$) son $-1, 0, +1$.
2. **Fórmula del desplazamiento de energía:**
   $$ \Delta E = \mu_B m_l B $$
3. **Datos:**
   - $\mu_B = 9.274 \times 10^{-24} \, \text{J/T}$
   - $B = 1 \, \text{T}$
4. **Cálculo de los desplazamientos:**
   - Para $m_l = +1$:
     $$ \Delta E = (9.274 \times 10^{-24}) (1) (1) = 9.274 \times 10^{-24} \, \text{J} \approx 5.79 \times 10^{-5} \, \text{eV} $$
   - Para $m_l = 0$:
     $$ \Delta E = 0 $$
   - Para $m_l = -1$:
     $$ \Delta E = -9.274 \times 10^{-24} \, \text{J} \approx -5.79 \times 10^{-5} \, \text{eV} $$

El nivel original se desdobla en 3 niveles, separados por $5.79 \times 10^{-5} \, \text{eV}$.

## 📚 Recursos Específicos

### Cursos Específicos
1. [Light and Matter - MIT OCW](https://ocw.mit.edu)
2. [Spectroscopy - Coursera](https://www.coursera.org)
3. [Atomic and Optical Physics - MIT (YouTube)](https://www.youtube.com)

### Artículos y Simulaciones
1. Einstein, A. (1916). *Strahlungs-emission und -absorption nach der Quantentheorie*.
2. [PhET Simulation: Molecules and Light](https://phet.colorado.edu/en/simulations/molecules-and-light)
3. [PhET Simulation: Lasers](https://phet.colorado.edu/en/simulations/lasers)
4. Townes, C. H., & Schawlow, A. L. (1955). *Microwave Spectroscopy*. McGraw-Hill.
