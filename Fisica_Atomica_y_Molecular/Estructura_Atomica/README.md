# Estructura Atómica

La estructura atómica se ocupa de la organización de electrones, protones y neutrones dentro del átomo, utilizando la mecánica cuántica como herramienta principal para describir el comportamiento electrónico.

## 📜 Contexto Histórico

Desde el modelo planetario de Rutherford (1911) hasta la cuantización propuesta por Niels Bohr (1913), la estructura atómica revolucionó la física. En 1925-1926, Heisenberg y Schrödinger formularon la mecánica cuántica moderna. Posteriormente, Dirac introdujo la relatividad en 1928, prediciendo la existencia del espín del electrón y la antimateria.

## 🧮 Desarrollo Teórico Profundo

El átomo de hidrógeno es el sistema fundamental en la física atómica. La ecuación de Schrödinger independiente del tiempo para el electrón en un potencial central de Coulomb $V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$ es:

$$ \left( -\frac{\hbar^2}{2\mu} \nabla^2 - \frac{e^2}{4\pi\epsilon_0 r} \right) \psi(r, \theta, \phi) = E \psi(r, \theta, \phi) $$

Donde $\mu$ es la masa reducida del sistema. Al separar variables, la función de onda se expresa como:

$$ \psi_{nlm}(r, \theta, \phi) = R_{nl}(r) Y_{l}^{m}(\theta, \phi) $$

Los niveles de energía cuantizados (sin considerar la estructura fina) dependen únicamente del número cuántico principal $n$:

$$ E_n = - \frac{\mu e^4}{8\epsilon_0^2 h^2} \frac{1}{n^2} = -\frac{13.6 \, \text{eV}}{n^2} $$

Para átomos multielectrónicos, el Hamiltoniano incluye la repulsión interelectrónica:

$$ \hat{H} = \sum_{i=1}^{Z} \left( -\frac{\hbar^2}{2m} \nabla_i^2 - \frac{Z e^2}{4\pi\epsilon_0 r_i} \right) + \sum_{i<j} \frac{e^2}{4\pi\epsilon_0 | \mathbf{r}_i - \mathbf{r}_j |} $$

Debido al término de repulsión, esta ecuación no tiene solución analítica exacta, requiriendo métodos de aproximación como el **Método de Hartree-Fock** o la Teoría de Perturbaciones. El estado cuántico global debe ser antisimétrico respecto al intercambio de fermiones (Principio de exclusión de Pauli).

## 🛠 Ejemplo Práctico

**Problema:** Calcular la longitud de onda de un fotón emitido cuando un electrón en un átomo de hidrógeno transita del estado $n=3$ al estado $n=2$ (Serie de Balmer - $H_\alpha$).

**Solución paso a paso:**

1. **Energía inicial ($n_i = 3$):**
   $$ E_3 = -\frac{13.6 \, \text{eV}}{3^2} = -\frac{13.6}{9} \approx -1.511 \, \text{eV} $$

2. **Energía final ($n_f = 2$):**
   $$ E_2 = -\frac{13.6 \, \text{eV}}{2^2} = -\frac{13.6}{4} = -3.400 \, \text{eV} $$

3. **Energía del fotón emitido ($\Delta E$):**
   $$ \Delta E = E_3 - E_2 = -1.511 - (-3.400) = 1.889 \, \text{eV} $$

4. **Conversión a Joules:**
   $$ \Delta E = 1.889 \times 1.602 \times 10^{-19} \, \text{J} = 3.026 \times 10^{-19} \, \text{J} $$

5. **Longitud de onda ($\lambda$):**
   Usando $E = \frac{hc}{\lambda}$:
   $$ \lambda = \frac{hc}{\Delta E} = \frac{(6.626 \times 10^{-34}) (3 \times 10^8)}{3.026 \times 10^{-19}} $$
   $$ \lambda = \frac{1.988 \times 10^{-25}}{3.026 \times 10^{-19}} \approx 6.57 \times 10^{-7} \, \text{m} = 657 \, \text{nm} $$

(El valor exacto experimental de $H_\alpha$ es $656.3 \, \text{nm}$, usando la masa reducida $\mu$).

## 📚 Recursos Específicos

### Cursos Específicos
1. [Atomic Structure - MIT OCW](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/)
2. [Quantum Mechanics - Stanford (YouTube)](https://www.youtube.com/playlist?list=PL84C10A9CB1D13841)
3. [Physical Chemistry - NPTEL](https://nptel.ac.in/courses/104104085)
4. [Quantum Mechanics and Atomic Physics - MIT (OCW)](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/)
5. [Exploring Quantum Physics - Coursera](https://www.coursera.org/learn/quantum-physics)

### Artículos y Simulaciones
1. [Bohr, N. (1913). *On the Constitution of Atoms and Molecules*. Phil. Mag.](https://www.tandfonline.com/doi/abs/10.1080/14786441308634955)
2. [PhET Simulation: Build an Atom](https://phet.colorado.edu/en/simulations/build-an-atom)
3. [PhET Simulation: Hydrogen Atom Models](https://phet.colorado.edu/en/simulations/hydrogen-atom)
4. [Hartree, D. R. (1928). *The Wave Mechanics of an Atom with a Non-Coulomb Central Field*.](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/wave-mechanics-of-an-atom-with-a-noncoulomb-central-field/564BEEA1EB919DE476DA06BE7B2E7852)
5. [Schrödinger, E. (1926). *An Undulatory Theory of the Mechanics of Atoms and Molecules*. Phys. Rev.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.28.1049)
6. [Pauli, W. (1925). *On the Connexion between the Completion of Electron Groups in an Atom with the Complex Structure of Spectra*.](https://link.springer.com/article/10.1007/BF02980631)
7. [PhET Simulation: Rutherford Scattering](https://phet.colorado.edu/en/simulations/rutherford-scattering)
8. [PhET Simulation: Neon Lights & Other Discharge Lamps](https://phet.colorado.edu/en/simulations/neon-lights-and-other-discharge-lamps)
9. [Dirac, P. A. M. (1928). *The Quantum Theory of the Electron*. Proc. R. Soc. Lond.](https://royalsocietypublishing.org/doi/10.1098/rspa.1928.0023)
10. [Slater, J. C. (1929). *The Theory of Complex Spectra*. Phys. Rev.](https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.1293)

### 📖 Referencias Útiles y Bibliografía
- [Foot, C. J. (2005). *Atomic Physics*. Oxford University Press.](https://global.oup.com/academic/product/atomic-physics-9780198506966)
- [Bransden, B. H., & Joachain, C. J. (2003). *Physics of Atoms and Molecules*. Pearson Education.](https://www.pearson.com/en-us/subject-catalog/p/physics-of-atoms-and-molecules/P200000005739)
- [Woodgate, G. K. (1980). *Elementary Atomic Structure*. Oxford University Press.](https://global.oup.com/academic/product/elementary-atomic-structure-9780198511564)
- [Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California Press.](https://www.ucpress.edu/book/9780520038219/the-theory-of-atomic-structure-and-spectra)
