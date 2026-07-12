# El Modelo Estándar de Partículas
El Modelo Estándar es la teoría fundamental que describe las partículas elementales que componen la materia y las tres fuerzas fundamentales (electromagnética, débil y fuerte) que interactúan entre ellas, excluyendo la gravedad.

## 📜 Contexto Histórico
El desarrollo del Modelo Estándar comenzó en la década de 1960. Murray Gell-Mann y George Zweig propusieron de manera independiente el modelo de los quarks en 1964 para explicar la vasta "fauna" de hadrones. Sheldon Glashow, Abdus Salam y Steven Weinberg unificaron el electromagnetismo y la fuerza débil (teoría electrodébil) a finales de la década de 1960. En 1964, se propuso el mecanismo de Brout-Englert-Higgs para explicar cómo las partículas adquieren masa, lo que culminó con el descubrimiento del bosón de Higgs en el CERN en 2012.

## 🧮 Desarrollo Teórico Profundo
El Modelo Estándar es una teoría cuántica de campos basada en la simetría de gauge local:
$$ SU(3)_C \times SU(2)_L \times U(1)_Y $$
- $ SU(3)_C $: Describe la cromodinámica cuántica (QCD), la fuerza fuerte mediada por 8 gluones que interactúan con el color.
- $ SU(2)_L \times U(1)_Y $: Teoría electrodébil mediada por los bosones $ W^\pm, Z^0 $ (débil) y el fotón $ \gamma $ (electromagnetismo).

El lagrangiano del Modelo Estándar se puede escribir simbólicamente en cuatro partes principales:
$$ \mathcal{L}_{SM} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + i\bar{\psi}\not\!\!D\psi + |D_\mu \phi|^2 - V(\phi) + \mathcal{L}_{Yukawa} $$
- Términos cinéticos de los bosones de gauge (esfuerzo del campo $ F_{\mu\nu} $).
- Términos fermiónicos $ i\bar{\psi}\not\!\!D\psi $ describen cómo la materia interacciona con las fuerzas (derivada covariante $ D $).
- El campo de Higgs $ \phi $ y su potencial $ V(\phi) = \mu^2 \phi^\dagger \phi + \lambda (\phi^\dagger \phi)^2 $ (donde $ \mu^2 < 0 $) causa la ruptura espontánea de simetría.
- El acoplamiento de Yukawa genera la masa de los fermiones interactuando con el vacío de Higgs.

## 🛠 Ejemplo Práctico
**Problema:** Determina los números cuánticos (carga eléctrica, spin) de un protón y un neutrón basados en su composición de quarks, sabiendo que el quark up (u) tiene carga +2/3 y el down (d) tiene carga -1/3.

**Solución paso a paso:**
1. **Composición de Quarks:**
   El protón es un barión compuesto por 3 quarks: $ uud $ (dos quarks up y un quark down).
   El neutrón es un barión compuesto por: $ udd $ (un quark up y dos quarks down).
2. **Cálculo de la Carga Eléctrica ($ Q $):**
   - Protón: $ Q_p = Q_u + Q_u + Q_d = (+2/3) + (+2/3) + (-1/3) = +3/3 = +1 e $
   - Neutrón: $ Q_n = Q_u + Q_d + Q_d = (+2/3) + (-1/3) + (-1/3) = 0 e $
3. **Cálculo del Spin ($ J $):**
   Tanto los quarks up como down son fermiones de spin 1/2.
   Al combinar tres partículas de spin 1/2 en el estado fundamental (momento angular orbital $ L=0 $), los espines se acoplan a $ J = 1/2 $ o $ J = 3/2 $.
   Los nucleones fundamentales (protón y neutrón) corresponden al multiplete de isospín más bajo y tienen spin:
   $$ J_p = 1/2 $$
   $$ J_n = 1/2 $$
   *(El estado $ J=3/2 $ corresponde a las resonancias bariónicas $\Delta$).*

## 📚 Recursos Específicos

### Cursos Online
1. "[Particle Physics](https://ocw.mit.edu/courses/physics/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/)" (MIT OCW)
2. "[The Discovery of the Higgs Boson](https://www.coursera.org/learn/higgs-boson)" (Coursera - University of Edinburgh)
3. "[Quantum Field Theory](https://online.stanford.edu/courses/physics330-quantum-field-theory)" (Stanford University / edX)
4. "[The Standard Model of Particle Physics](https://online.stanford.edu/)" (Stanford Online)
5. "[Symmetries, Particles and Fields](https://www.maths.cam.ac.uk/undergrad/course/symmetries-particles-and-fields)" (University of Cambridge)
6. "[Introduction to String Theory](https://ocw.mit.edu/courses/physics/8-821-string-theory-fall-2008/)" (MIT OCW)

### Artículos y Simulaciones
1. "[CERN Document Server y Open Data Portal](https://opendata.cern.ch/)"
2. "[PDG (Particle Data Group): The Review of Particle Physics](https://pdg.lbl.gov/)"
3. "[A Model of Leptons](https://doi.org/10.1103/PhysRevLett.19.1264)" (S. Weinberg, 1967)
4. "[Broken Symmetries and the Masses of Gauge Bosons](https://doi.org/10.1103/PhysRevLett.13.508)" (P. W. Higgs, 1964)
5. "[A Schematic Model of Baryons and Mesons](https://doi.org/10.1016/S0031-9163(64)92001-3)" (M. Gell-Mann, 1964)
6. "[Observation of a new particle in the search for the Standard Model Higgs boson](https://doi.org/10.1016/j.physletb.2012.08.020)" (ATLAS Collaboration, 2012)
7. "[Observation of a new boson at a mass of 125 GeV](https://doi.org/10.1016/j.physletb.2012.08.021)" (CMS Collaboration, 2012)
8. "[Partial-symmetries of weak interactions](https://doi.org/10.1016/0029-5582(61)90469-2)" (S. L. Glashow, 1961)
9. "[Quarks and Leptons Simulation](https://phet.colorado.edu/)" (PhET)

### 📖 Referencias Útiles y Bibliografía
- Halzen, F., & Martin, A. D. (1984). *[Quarks and Leptons: An Introductory Course in Modern Particle Physics](https://www.wiley.com/en-us/Quarks+and+Leptons%3A+An+Introductory+Course+in+Modern+Particle+Physics-p-9780471887416)*. John Wiley & Sons.
- Griffiths, D. J. (2008). *[Introduction to Elementary Particles](https://www.wiley.com/en-us/Introduction+to+Elementary+Particles%2C+2nd%2C+Revised+Edition-p-9783527406012)*. Wiley-VCH.
- Thomson, M. (2013). *[Modern Particle Physics](https://doi.org/10.1017/CBO9781139525367)*. Cambridge University Press.
- Perkins, D. H. (2000). *[Introduction to High Energy Physics](https://doi.org/10.1017/CBO9780511809040)*. Cambridge University Press.
