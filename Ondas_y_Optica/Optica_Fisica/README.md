# Óptica Física
La óptica física (u óptica ondulatoria) considera la naturaleza electromagnética y ondulatoria de la luz para explicar fenómenos que la óptica geométrica no puede, tales como la interferencia, la difracción y la polarización.

## 📜 Contexto Histórico
El modelo ondulatorio de la luz fue propuesto inicialmente por Christiaan Huygens en 1678. Sin embargo, no fue hasta 1801, con el famoso experimento de la doble rendija de Thomas Young, que la naturaleza ondulatoria de la luz se demostró concluyentemente a través del fenómeno de interferencia. James Clerk Maxwell unificó más tarde la óptica con el electromagnetismo en la década de 1860.

## 🧮 Desarrollo Teórico Profundo
**Interferencia de Doble Rendija (Experimento de Young):**
La diferencia de camino óptico $ \Delta r $ entre dos ondas provenientes de rendijas separadas por una distancia $ d $ hacia un punto en una pantalla con ángulo $ \theta $ es:
$$ \Delta r = d \sin(\theta) $$
- Condición de máximo constructivo: $ d \sin(\theta) = m\lambda $ donde $ m = 0, \pm 1, \pm 2, \dots $
- Condición de mínimo destructivo: $ d \sin(\theta) = \left(m + \frac{1}{2}\right)\lambda $

**Difracción por una Sola Rendija:**
La intensidad en un patrón de difracción de Fraunhofer para una rendija de ancho $ a $ está dada por:
$$ I(\theta) = I_0 \text{sinc}^2\left( \frac{\pi a \sin(\theta)}{\lambda} \right) = I_0 \left( \frac{\sin(\beta)}{\beta} \right)^2 $$
donde $ \beta = \frac{\pi a \sin(\theta)}{\lambda} $.
Los mínimos de intensidad ocurren cuando $ a \sin(\theta) = m\lambda $ (para $ m = \pm 1, \pm 2, \dots $).

**Ley de Malus (Polarización):**
Si luz polarizada con intensidad $ I_0 $ pasa por un polarizador cuyo eje de transmisión forma un ángulo $ \theta $ con el plano de polarización inicial:
$$ I = I_0 \cos^2(\theta) $$

## 🛠 Ejemplo Práctico
**Problema:** Luz láser roja ($ \lambda = 632.8 \text{ nm} $) incide sobre dos rendijas estrechas separadas por $ 0.2 \text{ mm} $. Una pantalla se coloca a $ 2.5 \text{ m} $ de las rendijas. ¿A qué distancia del centro (máximo central) se encuentra el tercer máximo brillante de interferencia?

**Solución paso a paso:**
1. Identificamos variables: $ \lambda = 632.8 \times 10^{-9} \text{ m} $, $ d = 0.2 \times 10^{-3} \text{ m} $, $ L = 2.5 \text{ m} $, y orden $ m = 3 $.
2. Condición de máximo: $ d \sin(\theta) = m\lambda $.
3. Ya que el ángulo $ \theta $ es pequeño, usamos la aproximación de ángulo pequeño: $ \sin(\theta) \approx \tan(\theta) = \frac{y}{L} $.
4. Sustituyendo en la condición: $ d \frac{y}{L} = m\lambda \implies y = \frac{m \lambda L}{d} $.
5. Calculamos la distancia $ y $:
   $$ y = \frac{3 \cdot (632.8 \times 10^{-9}) \cdot 2.5}{0.2 \times 10^{-3}} = \frac{4746 \times 10^{-9}}{0.2 \times 10^{-3}} = 23730 \times 10^{-6} \text{ m} $$
   $$ y = 23.73 \text{ mm} $$

## 📚 Recursos Específicos
### Cursos
1. ["Physics III: Vibrations and Waves" - MIT OCW](https://ocw.mit.edu/courses/8-03-physics-iii-vibrations-and-waves-fall-2004/)
2. ["Exploring Quantum Optics" - Coursera (École Polytechnique)](https://www.coursera.org/learn/quantum-optics)
3. ["Waves and Optics" - edX (Rice University)](https://www.edx.org/course/waves-and-optics)
4. ["Light and Optics" - Khan Academy](https://www.khanacademy.org/science/physics/light-waves)
5. ["Optics" - NPTEL (IIT Kharagpur)](https://nptel.ac.in/courses/115105099)
6. ["Understanding Optics" - Coursera (University of Central Florida)](https://www.coursera.org/learn/optics)

### Artículos y Simulaciones
1. ["Wave Interference" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/wave-interference)
2. ["Quantum Wave Interference" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/quantum-wave-interference)
3. ["Single Slit Diffraction" - oPhysics](https://ophysics.com/l5.html)
4. ["Double Slit Interference" - oPhysics](https://ophysics.com/l4.html)
5. ["Polarization of Light" - oPhysics](https://ophysics.com/l3.html)
6. ["Michelson Interferometer Simulation" - Amrita O-labs](http://vlab.amrita.edu/?sub=1&brch=189&sim=1106&cnt=1)
7. ["Diffraction Grating Simulation" - oPhysics](https://ophysics.com/l6.html)
8. ["Thin Film Interference" - oPhysics](https://ophysics.com/l7.html)
9. ["Faraday Effect and Polarization" - HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/faraday.html)

### 📖 Referencias Útiles y Bibliografía
1. [*Principles of Optics* por Max Born y Emil Wolf](https://www.cambridge.org/core/books/principles-of-optics/1B445037E90B051D57457FBD56A1F6E2)
2. [*Introduction to Electrodynamics* por David J. Griffiths](https://www.cambridge.org/highereducation/books/introduction-to-electrodynamics/9781108420419)
3. [*Optics* por Eugene Hecht](https://www.pearson.com/en-us/subject-catalog/p/optics/P200000006793/9780133977226)
4. ["On the Theory of Light and Colors" por Thomas Young](https://royalsocietypublishing.org/doi/10.1098/rstl.1802.0004)
