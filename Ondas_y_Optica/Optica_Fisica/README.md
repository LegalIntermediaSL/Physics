# Óptica Física
La óptica física (u óptica ondulatoria) considera la naturaleza electromagnética y ondulatoria de la luz para explicar fenómenos que la óptica geométrica no puede, tales como la interferencia, la difracción y la polarización.

## 📜 Contexto Histórico
El modelo ondulatorio de la luz fue propuesto inicialmente por Christiaan Huygens en 1678. Sin embargo, no fue hasta 1801, con el famoso experimento de la doble rendija de Thomas Young, que la naturaleza ondulatoria de la luz se demostró concluyentemente a través del fenómeno de interferencia. James Clerk Maxwell unificó más tarde la óptica con el electromagnetismo en la década de 1860.

## 🧮 Desarrollo Teórico Profundo
**Interferencia de Doble Rendija (Experimento de Young):**
La diferencia de camino óptico $ \Delta r $ entre dos ondas provenientes de rendijas separadas por una distancia $ d $ hacia un punto en una pantalla con ángulo $ \theta $ es:
$ \Delta r = d \sin(\theta) $
- Condición de máximo constructivo: $ d \sin(\theta) = m\lambda $ donde $ m = 0, \pm 1, \pm 2, \dots $
- Condición de mínimo destructivo: $ d \sin(\theta) = \left(m + \frac{1}{2}\right)\lambda $

**Difracción por una Sola Rendija:**
La intensidad en un patrón de difracción de Fraunhofer para una rendija de ancho $ a $ está dada por:
$ I(\theta) = I_0 \text{sinc}^2\left( \frac{\pi a \sin(\theta)}{\lambda} \right) = I_0 \left( \frac{\sin(\beta)}{\beta} \right)^2 $
donde $ \beta = \frac{\pi a \sin(\theta)}{\lambda} $.
Los mínimos de intensidad ocurren cuando $ a \sin(\theta) = m\lambda $ (para $ m = \pm 1, \pm 2, \dots $).

**Ley de Malus (Polarización):**
Si luz polarizada con intensidad $ I_0 $ pasa por un polarizador cuyo eje de transmisión forma un ángulo $ \theta $ con el plano de polarización inicial:
$ I = I_0 \cos^2(\theta) $

## 🛠 Ejemplo Práctico
**Problema:** Luz láser roja ($ \lambda = 632.8 \text{ nm} $) incide sobre dos rendijas estrechas separadas por $ 0.2 \text{ mm} $. Una pantalla se coloca a $ 2.5 \text{ m} $ de las rendijas. ¿A qué distancia del centro (máximo central) se encuentra el tercer máximo brillante de interferencia?

**Solución paso a paso:**
1. Identificamos variables: $ \lambda = 632.8 \times 10^{-9} \text{ m} $, $ d = 0.2 \times 10^{-3} \text{ m} $, $ L = 2.5 \text{ m} $, y orden $ m = 3 $.
2. Condición de máximo: $ d \sin(\theta) = m\lambda $.
3. Ya que el ángulo $ \theta $ es pequeño, usamos la aproximación de ángulo pequeño: $ \sin(\theta) \approx \tan(\theta) = \frac{y}{L} $.
4. Sustituyendo en la condición: $ d \frac{y}{L} = m\lambda \implies y = \frac{m \lambda L}{d} $.
5. Calculamos la distancia $ y $:
   $ y = \frac{3 \cdot (632.8 \times 10^{-9}) \cdot 2.5}{0.2 \times 10^{-3}} = \frac{4746 \times 10^{-9}}{0.2 \times 10^{-3}} = 23730 \times 10^{-6} \text{ m} $
   $ y = 23.73 \text{ mm} $

## 📚 Recursos Específicos
- **Cursos:** "Waves and Optics" (MIT OCW), "Quantum Optics" (École Polytechnique).
- **Artículos/Textos:** *Principles of Optics* (Born & Wolf), *Introduction to Electrodynamics* (Griffiths - Ondas EM).
- **Simulaciones:** "Wave Interference" y "Quantum Wave Interference" (PhET Interactive Simulations).
