# El Modelo Estándar de Partículas
El Modelo Estándar es la teoría fundamental que describe las partículas elementales que componen la materia y las tres fuerzas fundamentales (electromagnética, débil y fuerte) que interactúan entre ellas, excluyendo la gravedad.

## 📜 Contexto Histórico
El desarrollo del Modelo Estándar comenzó en la década de 1960. Murray Gell-Mann y George Zweig propusieron de manera independiente el modelo de los quarks en 1964 para explicar la vasta "fauna" de hadrones. Sheldon Glashow, Abdus Salam y Steven Weinberg unificaron el electromagnetismo y la fuerza débil (teoría electrodébil) a finales de la década de 1960. En 1964, se propuso el mecanismo de Brout-Englert-Higgs para explicar cómo las partículas adquieren masa, lo que culminó con el descubrimiento del bosón de Higgs en el CERN en 2012.

## 🧮 Desarrollo Teórico Profundo
El Modelo Estándar es una teoría cuántica de campos basada en la simetría de gauge local:
$ SU(3)_C \times SU(2)_L \times U(1)_Y $
- $ SU(3)_C $: Describe la cromodinámica cuántica (QCD), la fuerza fuerte mediada por 8 gluones que interactúan con el color.
- $ SU(2)_L \times U(1)_Y $: Teoría electrodébil mediada por los bosones $ W^\pm, Z^0 $ (débil) y el fotón $ \gamma $ (electromagnetismo).

El lagrangiano del Modelo Estándar se puede escribir simbólicamente en cuatro partes principales:
$ \mathcal{L}_{SM} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + i\bar{\psi}\not\!\!D\psi + |D_\mu \phi|^2 - V(\phi) + \mathcal{L}_{Yukawa} $
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
   $ J_p = 1/2 $
   $ J_n = 1/2 $
   *(El estado $ J=3/2 $ corresponde a las resonancias bariónicas $\Delta$).*

## 📚 Recursos Específicos
### Cursos
- "Particle Physics" (MIT OCW)
- "The Discovery of the Higgs Boson" (Coursera - University of Edinburgh)
- "Quantum Field Theory" (Stanford University / edX)

### Artículos y Simulaciones
- CERN Document Server y Open Data Portal
- PDG (Particle Data Group): The Review of Particle Physics
- "A Model of Leptons" (S. Weinberg, 1967)
- "Broken Symmetries and the Masses of Gauge Bosons" (P. W. Higgs, 1964)
