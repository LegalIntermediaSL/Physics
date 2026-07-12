# Física Molecular

La física molecular se centra en el estudio de las propiedades físicas de las moléculas, los enlaces químicos, y la dinámica de los núcleos y electrones que conforman estas estructuras poliatómicas.

## 📜 Contexto Histórico

La teoría del enlace químico y la física molecular nacieron formalmente tras la publicación en 1927 del artículo de Walter Heitler y Fritz London aplicando la mecánica cuántica a la molécula de $H_2$. Poco después, Born y Oppenheimer introdujeron su famosa aproximación, que permite separar el movimiento rápido de los electrones del movimiento lento de los núcleos masivos.

## 🧮 Desarrollo Teórico Profundo

**Aproximación de Born-Oppenheimer:**
Dado que las masas nucleares ($M$) son mucho mayores que la masa electrónica ($m_e$), los electrones se ajustan casi instantáneamente a las posiciones nucleares. El Hamiltoniano molecular total se separa y la función de onda se expresa como:

$$ \Psi_{\text{mol}}(\mathbf{R}, \mathbf{r}) = \psi_{\text{elec}}(\mathbf{r}; \mathbf{R}) \chi_{\text{nuc}}(\mathbf{R}) $$

donde $\mathbf{R}$ representa las coordenadas nucleares y $\mathbf{r}$ las electrónicas. La energía electrónica calculada para diferentes posiciones nucleares forma la **Curva de Energía Potencial** $V(\mathbf{R})$ bajo la cual vibran los núcleos.

**Niveles de Energía de una Molécula Diatómica:**
La energía total de una molécula se puede aproximar como la suma de las energías electrónica, vibracional y rotacional:

$$ E = E_{\text{elec}} + E_{\text{vib}} + E_{\text{rot}} $$

1. **Energía Vibracional (Aproximación Armónica):**
   Cerca del mínimo del pozo de potencial, la molécula se comporta como un oscilador armónico cuántico:
   $$ E_{\text{vib}} = \hbar \omega \left( v + \frac{1}{2} \right), \quad v = 0, 1, 2, ... $$
   Donde $\omega = \sqrt{\frac{k}{\mu_{\text{mol}}}}$ es la frecuencia de oscilación, $k$ es la constante de fuerza del enlace y $\mu_{\text{mol}}$ es la masa reducida de los núcleos.

2. **Energía Rotacional (Modelo de Rotor Rígido):**
   $$ E_{\text{rot}} = \frac{\hbar^2}{2I} J(J+1) = B J(J+1), \quad J = 0, 1, 2, ... $$
   Donde $I = \mu_{\text{mol}} R_0^2$ es el momento de inercia, $R_0$ es la longitud de enlace de equilibrio, y $B = \frac{\hbar^2}{2I}$ es la constante rotacional.

## 🛠 Ejemplo Práctico

**Problema:** El espectro de rotación pura de la molécula de monóxido de carbono $^{12}\text{C}^{16}\text{O}$ presenta líneas de absorción adyacentes separadas por una frecuencia de $\Delta \nu = 115.27 \, \text{GHz}$. Calcular la longitud de enlace $R_0$ del CO.

**Solución paso a paso:**

1. **Condición de Transición Rotacional:**
   Las reglas de selección para absorción rotacional son $\Delta J = +1$. La energía absorbida es:
   $$ \Delta E = E_{J+1} - E_J = B(J+1)(J+2) - BJ(J+1) = 2B(J+1) $$
   La separación en energía (frecuencia) entre líneas adyacentes (p.ej. de $J\rightarrow J+1$ y de $J+1\rightarrow J+2$) es $\Delta(\Delta E) = 2B$. Por lo tanto, en términos de frecuencia $h \Delta \nu = 2B$.

2. **Calcular la Constante Rotacional $B$:**
   $$ B = \frac{h \Delta \nu}{2} = \frac{(6.626 \times 10^{-34} \, \text{J s})(115.27 \times 10^9 \, \text{Hz})}{2} = 3.818 \times 10^{-23} \, \text{J} $$

3. **Calcular el Momento de Inercia $I$:**
   $$ B = \frac{\hbar^2}{2I} \implies I = \frac{\hbar^2}{2B} = \frac{(1.054 \times 10^{-34})^2}{2(3.818 \times 10^{-23})} \approx 1.455 \times 10^{-46} \, \text{kg m}^2 $$

4. **Calcular la Masa Reducida $\mu_{\text{mol}}$:**
   Masas molares: C = 12.00 g/mol, O = 15.99 g/mol.
   Masa atómica: $m_C \approx 1.992 \times 10^{-26} \, \text{kg}$, $m_O \approx 2.656 \times 10^{-26} \, \text{kg}$.
   $$ \mu_{\text{mol}} = \frac{m_C m_O}{m_C + m_O} = \frac{(1.992)(2.656)}{1.992 + 2.656} \times 10^{-26} \approx 1.139 \times 10^{-26} \, \text{kg} $$

5. **Calcular la Longitud de Enlace $R_0$:**
   $$ I = \mu_{\text{mol}} R_0^2 \implies R_0 = \sqrt{\frac{I}{\mu_{\text{mol}}}} = \sqrt{\frac{1.455 \times 10^{-46}}{1.139 \times 10^{-26}}} \approx \sqrt{1.277 \times 10^{-20}} $$
   $$ R_0 \approx 1.13 \times 10^{-10} \, \text{m} = 0.113 \, \text{nm} \, (1.13 \, \text{Å}) $$

## 📚 Recursos Específicos

### Cursos Específicos
1. [Molecular Physics - University of Manchester (Coursera)](https://www.coursera.org/)
2. [Introduction to Molecular Spectroscopy - NPTEL](https://nptel.ac.in)
3. [Physical Chemistry: Molecular Structure - MIT OCW](https://ocw.mit.edu)

### Artículos y Simulaciones
1. Born, M., & Oppenheimer, R. (1927). *Zur Quantentheorie der Molekeln*. Annalen der Physik.
2. Heitler, W., & London, F. (1927). *Wechselwirkung neutraler Atome und homöopolare Bindung nach der Quantenmechanik*.
3. [PhET Simulation: Molecule Shapes](https://phet.colorado.edu/en/simulations/molecule-shapes)
4. [NIST Chemistry WebBook](https://webbook.nist.gov/chemistry/) - Datos espectroscópicos moleculares.
