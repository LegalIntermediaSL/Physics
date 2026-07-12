# Acústica y Sonido
La acústica es la disciplina que trata la propagación de ondas mecánicas en gases, líquidos y sólidos, incluyendo fenómenos como la vibración, el sonido, el ultrasonido y el infrasonido.

## 📜 Contexto Histórico
Pitágoras (siglo VI a.C.) fue uno de los primeros en investigar las propiedades musicales del sonido mediante cuerdas vibrantes. Posteriormente, en el siglo XVII, Marin Mersenne determinó empíricamente la velocidad del sonido en el aire y relacionó la frecuencia de una cuerda con su tensión y densidad. La teoría moderna del sonido se consolidó con la publicación de *The Theory of Sound* por Lord Rayleigh en 1877.

## 🧮 Desarrollo Teórico Profundo
Las ondas sonoras en un fluido son ondas longitudinales de presión y desplazamiento.

**Ecuación de Onda Acústica (Presión):**
$$ \nabla^2 p - \frac{1}{c^2} \frac{\partial^2 p}{\partial t^2} = 0 $$
donde $ p $ es la presión acústica y $ c $ es la velocidad del sonido.

**Velocidad del Sonido:**
En un gas ideal, $ c = \sqrt{\frac{\gamma R T}{M}} $, donde $ \gamma $ es el coeficiente de dilatación adiabática, $ R $ es la constante de los gases, $ T $ es la temperatura absoluta y $ M $ es la masa molar.
A $ 20^\circ \text{C} $ en el aire, $ c \approx 343 \text{ m/s} $.

**Nivel de Intensidad Sonora (Decibelios):**
$$ \beta = 10 \log_{10} \left(\frac{I}{I_0}\right) \text{ dB} $$
donde $ I $ es la intensidad de la onda ($ \text{W/m}^2 $) y $ I_0 = 10^{-12} \text{ W/m}^2 $ es el umbral de audición.

**Efecto Doppler:**
Para fuente ($ v_s $) y observador ($ v_o $) moviéndose en línea recta:
$$ f' = f \left( \frac{c \pm v_o}{c \mp v_s} \right) $$
(El signo superior se usa cuando se acercan, el inferior cuando se alejan).

## 🛠 Ejemplo Práctico
**Problema:** Una sirena de ambulancia emite un sonido con frecuencia de $ 800 \text{ Hz} $. La ambulancia se acerca a un observador estacionario a una velocidad de $ 30 \text{ m/s} $. Si la velocidad del sonido en el aire es de $ 340 \text{ m/s} $, ¿cuál es la frecuencia que escucha el observador? ¿Y cuál es la longitud de onda del sonido frente a la ambulancia?

**Solución paso a paso:**
1. Frecuencia percibida (Efecto Doppler): $ v_o = 0 $, fuente acercándose (restamos en el denominador).
   $$ f' = f \left( \frac{c}{c - v_s} \right) $$
2. Sustituimos los valores:
   $ f' = 800 \left( \frac{340}{340 - 30} \right) = 800 \left( \frac{340}{310} \right) = 800 \times 1.0968 = 877.4 \text{ Hz} $.
3. Longitud de onda frente a la ambulancia: La onda "se comprime" por el movimiento de la fuente.
   $ \lambda' = \frac{c - v_s}{f} = \frac{340 - 30}{800} = \frac{310}{800} = 0.3875 \text{ m} $.

## 📚 Recursos Específicos
### Cursos
1. ["Acoustics: Basic Physics" - Coursera (UNSW Sydney)](https://www.coursera.org/learn/acoustics)
2. ["Fundamentals of Audio and Music Engineering" - Coursera (University of Rochester)](https://www.coursera.org/learn/audio-engineering)
3. ["Introduction to Acoustics" - edX (TU Delft)](https://www.edx.org/course/introduction-to-acoustics)
4. ["Architectural Acoustics" - NPTEL (IIT Kharagpur)](https://nptel.ac.in/courses/105105152)
5. ["Vibrations and Waves" - MIT OCW](https://ocw.mit.edu/courses/8-03-physics-iii-vibrations-and-waves-fall-2004/)
6. ["Sound and Waves" - Khan Academy](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound)

### Artículos y Simulaciones
1. ["Sound" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/sound)
2. ["Wave on a String" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/wave-on-a-string)
3. ["Normal Modes" - PhET Interactive Simulations](https://phet.colorado.edu/en/simulations/normal-modes)
4. ["Online Tone Generator" - Szynalski](https://www.szynalski.com/tone-generator/)
5. ["Ripple Tank" - Falstad](http://www.falstad.com/ripple/)
6. ["Doppler Effect Simulation" - oPhysics](https://ophysics.com/w11.html)
7. ["Standing Waves Simulation" - oPhysics](https://ophysics.com/w8.html)
8. ["Beat Frequency Simulation" - oPhysics](https://ophysics.com/w10.html)
9. ["Physics of Musical Instruments" - UNSW](https://newt.phys.unsw.edu.au/jw/basics.html)

### 📖 Referencias Útiles y Bibliografía
1. [*Fundamentals of Acoustics* por Lawrence E. Kinsler et al.](https://www.wiley.com/en-us/Fundamentals+of+Acoustics%2C+4th+Edition-p-9780471847892)
2. [*The Theory of Sound* por Lord Rayleigh](https://archive.org/details/theoryofsound01rayl)
3. [*Acoustics* por Leo L. Beranek](https://asa.scitation.org/doi/book/10.1121/1.4920216)
4. [*Vibrations and Waves* por A.P. French](https://www.routledge.com/Vibrations-and-Waves/French/p/book/9780393099362)
